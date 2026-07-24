from uuid import UUID
from uuid6 import uuid7
from sqlalchemy.orm import Session
from tcc.api.schemas.condominium_schemas import CreateCondominiumRequest, EditCondominiumRequest, CondominiumResponse
from tcc.infrastructure.models.condominium_models import CondominiumModel


class CondominiumRepository:
    def __init__(
            self,
            session: Session
            ):
        self.session = session


    def create(
            self,
            condominium: CreateCondominiumRequest,
    ) -> CondominiumModel:
        condominium_to_create = CondominiumModel(
            id= uuid7(),
            nome= condominium.nome,
            cep= condominium.cep, 
            logradouro= condominium.logradouro, 
            numero= condominium.numero, 
            bairro= condominium.bairro, 
            uf= condominium.uf, 
            cidade= condominium.cidade, 
        )

        self.session.add(condominium_to_create)
        self.session.flush()
        self.session.commit()

        return condominium_to_create