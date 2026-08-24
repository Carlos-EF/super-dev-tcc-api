from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from tcc.infrastructure.connection import get_session
from tcc.infrastructure.models.users_model import UserModel
from tcc.infrastructure.services.auth_service import AuthService


bearer_scheme = HTTPBearer(auto_error=False)
DBSession = Annotated[Session, Depends(get_session)]


def get_current_user(
    db: DBSession,
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
) -> UserModel:
    if credentials is None or credentials.scheme.lower() != "bearer":
        from fastapi import HTTPException, status

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Bearer não informado.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return AuthService(db).get_current_user(credentials.credentials)


CurrentUser = Annotated[UserModel, Depends(get_current_user)]