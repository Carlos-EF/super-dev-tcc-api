from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
from sqlalchemy import or_
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
    ) -> CondominiumResponse:
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

        return self.create_response(condominium_to_create)


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


        condominium_to_edit.nome= condominium.nome
        condominium_to_edit.cep= condominium.cep
        condominium_to_edit.logradouro= condominium.logradouro
        condominium_to_edit.numero= condominium.numero
        condominium_to_edit.bairro= condominium.bairro
        condominium_to_edit.uf= condominium.uf
        condominium_to_edit.cidade= condominium.cidade
        condominium_to_edit.alterado_em= datetime.now()

        self.session.commit()

        return self.create_response(condominium_to_edit)


    def delete(
            self,
            id: UUID,
    ) -> bool:
        condominium_to_delete = self.session.query(
            CondominiumModel
        ).filter(
            CondominiumModel.id == id
        ).first()

        if not condominium_to_delete:
            return False

        self.session.delete(condominium_to_delete)
        self.session.commit()

        return True


    def get_all(
            self,
            busca: str | None = None,
            cidade: str | None = None,
            bairro: str | None = None,
    ) -> list[CondominiumResponse]:
        query = self.session.query(CondominiumModel)

        if busca:
            query = query.filter(
                or_(
                CondominiumModel.nome.ilike(f"%{busca}%"),
                CondominiumModel.logradouro.ilike(f"%{busca}%"),
                CondominiumModel.cep.ilike(f"%{busca}%"),
                )
            )

        if cidade:
            query = query.filter(
                CondominiumModel.cidade == cidade
            )

        if bairro:
            query = query.filter(
                CondominiumModel.bairro == bairro
            )

        condominiums = query.all()
        
        return [self.create_response(condominium) for condominium in condominiums]


    def get_by_id(
            self,
            id: UUID
    ) -> CondominiumResponse | False:
        condominium = self.session.query(
            CondominiumModel
        ).filter(
            CondominiumModel.id == id
        ).first()

        if not condominium:
            return False

        return self.create_response(condominium)


    def create_response(
            self,
            condominium: CondominiumModel
    ) -> CondominiumResponse:
        condominium_response = CondominiumResponse(
            id= condominium.id,
            nome= condominium.nome,
            cep= condominium.cep,
            logradouro= condominium.logradouro,
            numero= condominium.numero,
            bairro= condominium.bairro,
            cidade= condominium.cidade,
            uf= condominium.uf,
            criado_em= condominium.criado_em,
            alterado_em= condominium.alterado_em,
        )

        return condominium_response

