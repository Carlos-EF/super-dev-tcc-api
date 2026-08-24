from uuid import UUID
from fastapi import HTTPException, status
from tcc.infrastructure.connection import supabase


def normalize_email(email: str) -> str:
    return email.strip().lower()


def extract_supabase_user(response):
    data = getattr(response, "data", None)
    return getattr(data, "user", None) or getattr(response, "user", None)


def extract_supabase_session(response):
    data = getattr(response, "data", None)
    return getattr(data, "session", None) or getattr(response, "session", None)


def extract_supabase_error_message(error: Exception) -> str:
    message = str(error).strip()
    return message or "Falha na autenticação com o Supabase."


def verify_supabase_token(token: str):
    try:
        response = supabase.auth.get_user(token)
        user = getattr(response, "user", None)
        if user is None:
            data = getattr(response, "data", None)
            user = getattr(data, "user", None)
        if user is None:
            raise ValueError("Usuário não encontrado no Supabase.")
        return user
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token do Supabase inválido ou expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def supabase_user_id(user) -> UUID:
    try:
        return UUID(str(user.id))
    except (AttributeError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identidade Supabase inválida.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
