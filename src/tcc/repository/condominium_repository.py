from uuid import UUID
from sqlalchemy.orm import Session
from tcc.api.schemas.condominium_schemas import CreateCondominiumRequest, EditCondominiumRequest, CondominiumResponse
from tcc.infrastructure.models.condominium_models import CondominiumModel


class CondominiumRepository:
    def __init__(
            self,
            session: Session
            ):
        self.session = session