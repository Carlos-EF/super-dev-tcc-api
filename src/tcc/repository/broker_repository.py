from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from math import ceil
from tcc.api.schemas.broker_schemas import CreateBrokerRequest, EditBrokerRequest, FilteredBrokerResponse, BrokerResponse
from tcc.infrastructure.models.broker_models import BrokerModel


class BrokerRepository:
    def __init__(
            self,
            session: Session
            ):
        self.session = session


    def create(
            self,
            broker: CreateBrokerRequest,
    ) -> BrokerResponse:
        broker_to_create = BrokerModel(
            id= uuid7(),
            nome= broker.nome,
            codigo= broker.codigo, 
            creci= broker.creci, 
            numero= broker.numero, 
            email= broker.email, 
            data_nascimento= broker.data_nascimento, 
            rg= broker.rg, 
            cpf= broker.cpf, 
            criado_em= datetime.now()
        )

        self.session.add(broker_to_create)
        self.session.flush()
        self.session.commit()

        return self.create_response(broker_to_create)


    def edit(
            self,
            id: UUID,
            broker: EditBrokerRequest
    ) -> BrokerResponse | False:
        broker_to_edit = self.session.query(
            BrokerModel
        ).filter(
            BrokerModel.id == id
        ).first()

        if not broker_to_edit:
            return False


        broker_to_edit.nome= broker.nome
        broker_to_edit.creci= broker.creci
        broker_to_edit.numero= broker.numero
        broker_to_edit.email= broker.email
        broker_to_edit.rg= broker.rg
        broker_to_edit.cpf= broker.cpf
        broker_to_edit.data_nascimento= broker.data_nascimento
        broker_to_edit.alterado_em= datetime.now()

        self.session.commit()

        return self.create_response(broker_to_edit)


    def get_by_id(
            self,
            id: UUID
    ) -> BrokerResponse | False:
        broker = self.session.query(
            BrokerResponse
        ).filter(
            BrokerResponse.id == id
        ).first()

        if not broker:
            return False

        return self.create_response(broker)


    
    def delete(
            self,
            id: UUID,
    ) -> bool:
        broker_to_delete = self.session.query(
            BrokerModel
        ).filter(
            BrokerModel.id == id
        ).first()

        if not broker_to_delete:
            return False

        self.session.delete(broker_to_delete)
        self.session.commit()

        return True

    
    def create_response(
            self,
            broker: BrokerModel
    ) -> BrokerResponse:
        broker_response = BrokerResponse(
            id= broker.id,
            nome= broker.nome,
            codigo= broker.codigo, 
            creci= broker.creci, 
            numero= broker.numero, 
            email= broker.email, 
            data_nascimento= broker.data_nascimento, 
            rg= broker.rg, 
            cpf= broker.cpf,
            criado_em=broker.criado_em,
            alterado_em=broker.alterado_em,
        )

        return broker_response