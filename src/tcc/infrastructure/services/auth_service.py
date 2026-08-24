from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from tcc.core.auth_security import extract_supabase_error_message, extract_supabase_session, extract_supabase_user, normalize_email, supabase_user_id, verify_supabase_token
from tcc.infrastructure.connection import supabase
from tcc.infrastructure.models.users_model import UserModel
from tcc.repository.user_repository import UserRepository
from tcc.api.schemas.user_schemas import LoginRequest, RefreshRequest, RegisterRequest, RegisterResponse, UserResponse, TokenResponse


class AuthService:
    def __init__(self, db: Session) -> None:
        self.repository = UserRepository(db)


    def register(self, data: RegisterRequest) -> RegisterResponse:
        email = normalize_email(str(data.email))
        nome = data.nome.strip()

        existing_profile = self.repository.get_by_email(email)
        if existing_profile:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um usuário com este e-mail.",
            )

        try:
            response = supabase.auth.sign_up(
                {
                    "email": email,
                    "password": data.senha,
                    "options": {
                        "data": {
                            "nome": nome,
                        }
                    },
                }
            )
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=extract_supabase_error_message(exc),
            ) from exc

        supabase_user = extract_supabase_user(response)
        if supabase_user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O Supabase não retornou o usuário criado.",
            )

        user_id = supabase_user_id(supabase_user)
        user_email = normalize_email(str(getattr(supabase_user, "email", email) or email))

        try:
            profile = self.repository.upsert_profile(
                user_id=user_id,
                nome=nome,
                email=user_email,
            )
        except IntegrityError:
            self._rollback_safely()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Não foi possível criar o perfil local do usuário.",
            ) from None

        session = extract_supabase_session(response)
        session_created = session is not None

        message = (
            "Usuário criado e autenticado."
            if session_created
            else "Usuário criado. Verifique o e-mail para confirmar a conta antes de entrar."
        )

        return RegisterResponse(
            user=UserResponse.model_validate(profile),
            session_created=session_created,
            message=message,
        )


    def login(self, data: LoginRequest) -> TokenResponse:
        email = normalize_email(str(data.email))

        try:
            response = supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": data.senha,
                }
            )
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="E-mail ou senha inválidos.",
                headers={"WWW-Authenticate": "Bearer"},
            ) from exc

        session = extract_supabase_session(response)
        supabase_user = extract_supabase_user(response)

        if session is None or supabase_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Não foi possível criar a sessão.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user_id = supabase_user_id(supabase_user)
        user_email = normalize_email(str(getattr(supabase_user, "email", email) or email))
        nome = self._get_user_name(supabase_user, fallback=user_email)

        try:
            profile = self.repository.upsert_profile(
                user_id=user_id,
                nome=nome,
                email=user_email,
            )
        except IntegrityError:
            self._rollback_safely()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Não foi possível sincronizar o perfil local do usuário.",
            ) from None

        return TokenResponse(
            access_token=str(session.access_token),
            refresh_token=str(session.refresh_token),
            token_type=str(getattr(session, "token_type", "bearer")),
            expires_in=int(session.expires_in) if session.expires_in is not None else None,
            user=UserResponse.model_validate(profile),
        )


    def refresh(self, data: RefreshRequest) -> TokenResponse:
        try:
            response = supabase.auth.refresh_session(data.refresh_token)
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token inválido ou expirado.",
                headers={"WWW-Authenticate": "Bearer"},
            ) from exc

        session = extract_supabase_session(response)
        supabase_user = extract_supabase_user(response)

        if session is None or supabase_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Não foi possível renovar a sessão.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user_id = supabase_user_id(supabase_user)
        user_email = normalize_email(str(getattr(supabase_user, "email", "") or ""))
        nome = self._get_user_name(supabase_user, fallback=user_email)

        profile = self.repository.upsert_profile(
            user_id=user_id,
            nome=nome,
            email=user_email,
        )

        return TokenResponse(
            access_token=str(session.access_token),
            refresh_token=str(session.refresh_token),
            token_type=str(getattr(session, "token_type", "bearer")),
            expires_in=int(session.expires_in) if session.expires_in is not None else None,
            user=UserResponse.model_validate(profile),
        )


    def get_current_user(self, token: str) -> UserModel:
        supabase_user = verify_supabase_token(token)
        user_id = supabase_user_id(supabase_user)
        user_email = normalize_email(str(getattr(supabase_user, "email", "") or ""))
        nome = self._get_user_name(supabase_user, fallback=user_email)

        user = self.repository.upsert_profile(
            user_id=user_id,
            nome=nome,
            email=user_email,
        )

        if not user.ativo:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuário desativado.",
            )

        return user


    @staticmethod
    def _get_user_name(user, *, fallback: str) -> str:
        metadata = getattr(user, "user_metadata", None) or {}
        name = metadata.get("nome") or metadata.get("name") or metadata.get("full_name")
        if name:
            return str(name).strip()[:120]
        return fallback[:120]


    def _rollback_safely(self) -> None:
        self.repository.db.rollback()