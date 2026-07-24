from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
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
            criado_em= datetime.now()
        )

        self.session.add(condominium_to_create)
        self.session.flush()
        self.session.commit()

        return condominium_to_create


    def edit(
            self,
            id: UUID,
            condominium: EditCondominiumRequest
    ) -> CondominiumModel | False:
        condominium_to_edit = self.session.query(
            CondominiumModel
        ).filter(
            CondominiumModel.id == id
        ).first()

        if not condominium_to_edit:
            return False


        condominium_to_edit.nome= condominium.nome,
        condominium_to_edit.cep= condominium.cep, 
        condominium_to_edit.logradouro= condominium.logradouro, 
        condominium_to_edit.numero= condominium.numero, 
        condominium_to_edit.bairro= condominium.bairro, 
        condominium_to_edit.uf= condominium.uf, 
        condominium_to_edit.cidade= condominium.cidade,
        condominium_to_edit.alterado_em= datetime.now()

        self.session.commit(condominium_to_edit)

        return condominium_to_edit
