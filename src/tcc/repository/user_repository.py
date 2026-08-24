from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from tcc.infrastructure.models.users_model import UserModel


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, *, user_id: UUID, nome: str, email: str) -> UserModel:
        user = UserModel(
            id=user_id,
            nome=nome,
            email=email,
            ativo=True,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    

    def get_by_id(self, user_id: UUID) -> UserModel | None:
        return self.db.get(UserModel, user_id)
    

    def get_by_email(self, email: str) -> UserModel | None:
        return self.db.scalar(
            select(UserModel).where(UserModel.email == email)
        )
    

    def upsert_profile(self, *, user_id: UUID, nome: str, email: str) -> UserModel:
        user = self.get_by_id(user_id)

        if user is None:
            user = self.create(user_id=user_id, nome=nome, email=email)
            return user

        changed = False
        if user.nome != nome:
            user.nome = nome
            changed = True
        if user.email != email:
            user.email = email
            changed = True

        if changed:
            self.db.commit()
            self.db.refresh(user)

        return user
