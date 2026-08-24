from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from tcc.infrastructure.connection import get_session
from tcc.api.schemas.user_schemas import LoginRequest, RefreshRequest, RegisterRequest, RegisterResponse, TokenResponse, UserResponse 
from tcc.infrastructure.services.auth_service import AuthService