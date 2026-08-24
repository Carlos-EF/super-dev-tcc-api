from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from tcc.infrastructure.connection import get_session
from tcc.api.schemas.user_schemas import LoginRequest, RefreshRequest, RegisterRequest, RegisterResponse, TokenResponse, UserResponse 
from tcc.infrastructure.services.auth_service import AuthService
from tcc.api.dependencies import CurrentUser


router = APIRouter(prefix="/auth", tags=["Autenticação"])
DBSession = Annotated[Session, Depends(get_session)]


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar usuário no Supabase Auth",
)
def register(data: RegisterRequest, db: DBSession) -> RegisterResponse:
    return AuthService(db).register(data)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Entrar usando Supabase Auth",
)
def login(data: LoginRequest, db: DBSession) -> TokenResponse:
    return AuthService(db).login(data)


@router.post(
    "/refresh",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Renovar sessão do Supabase",
)
def refresh(data: RefreshRequest, db: DBSession) -> TokenResponse:
    return AuthService(db).refresh(data)


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Obter usuário autenticado",
)
def me(current_user: CurrentUser) -> UserResponse:
    return UserResponse.model_validate(current_user)
