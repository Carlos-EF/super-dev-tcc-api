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