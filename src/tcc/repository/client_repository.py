from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from math import ceil
from tcc.api.schemas.clients_schemas import CreateClientRequest, CreateInterestedClientRequest, EditClientRequest, EditInterestedClientRequest, InterestedClientResponse, PaginatedClientResponse, ClientResponse
from tcc.infrastructure.models.client_models import ClientModel, InterestedClientModel


class ClientRepository:
    def __init__(
            self,
            session: Session
            ):
        self.session = session


    def create(
            self,
            client: CreateClientRequest,
    ) -> ClientResponse:
        client_to_create = ClientModel(
            id= uuid7(),
            nome= client.nome,
            codigo= client.codigo, 
            numero= client.numero, 
            email= client.email, 
            tipo= client.tipo, 
            como_encontrou= client.como_encontrou, 
            criado_em= datetime.now()
        )

        self.session.add(client_to_create)
        self.session.flush()
        self.session.commit()

        return self.create_response(client_to_create)


    def create_response(
            self,
            client: ClientModel
    ) -> ClientResponse:
        
        return ClientResponse(
            id= client.id,
            nome= client.nome,
            codigo= client.codigo, 
            numero= client.numero, 
            email= client.email, 
            tipo= client.tipo, 
            como_encontrou= client.como_encontrou, 
            criado_em= client.criado_em,
            alterado_em= client.alterado_em
        )


    def create_interested_client(
            self,
            id: UUID,
            interested: CreateInterestedClientRequest
    ) -> InterestedClientResponse:

        interested_to_create = InterestedClientModel(
            id= uuid7(),
            client_id= id,
            procura= interested.procura,
            finalidade= interested.finalidade,
            preferencia= interested.preferencia,
            criado_em= datetime.now()
        )
         
        self.session.add(interested_to_create)
        self.session.flush()
        self.session.commit()

        return self.create_interested_client_response(interested_to_create)


    def create_interested_client_response(
            self,
            interested: InterestedClientModel
    ) -> InterestedClientResponse:
        
        return InterestedClientResponse(
            id= interested.id,
            cliente_id= interested.cliente_id,
            procura= interested.procura,
            finalidade= interested.finalidade,
            preferencia= interested.preferencia,
            criado_em= interested.criado_em,
            alterado_em= interested.alterado_em
        )


    def edit(
            self,
            id: UUID,
            client: EditClientRequest
    ) -> ClientResponse:
        client_to_edit = self.session.query(
            ClientModel
            ).filter(
                ClientModel.id == id
                ).first()

        if not client_to_edit:
            return None

        client_to_edit.nome = client.nome
        client_to_edit.numero = client.numero
        client_to_edit.email = client.email
        client_to_edit.como_encontrou = client.como_encontrou
        client_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_response(client_to_edit)


    def edit_interested_client(
            self,
            id: UUID,
            interested: EditInterestedClientRequest
    ) -> InterestedClientResponse:
        interested_to_edit = self.session.query(
            InterestedClientModel
            ).filter(
                InterestedClientModel.cliente_id == id
                ).first()

        if not interested_to_edit:
            return None

        interested_to_edit.procura = interested.procura
        interested_to_edit.finalidade = interested.finalidade
        interested_to_edit.preferencia = interested.preferencia
        interested_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_interested_client_response(interested_to_edit)


    def delete(
            self,
            id: UUID
    ) -> bool:
        client_to_delete = self.session.query(
            ClientModel
            ).filter(
                ClientModel.id == id
                ).first()

        if not client_to_delete:
            return False

        self.session.delete(client_to_delete)
        self.session.commit()

        return True


    def get_by_id(
            self,
            id: UUID
    ) -> ClientResponse:
        client = self.session.query(
            ClientModel
            ).filter(
                ClientModel.id == id
                ).first()

        if not client:
            return None

        return self.create_response(client)


    def get_interested_client_by_id(
            self,
            id: UUID
    ) -> InterestedClientResponse:
        interested_client = self.session.query(
            InterestedClientModel
            ).filter(
                InterestedClientModel.cliente_id == id
                ).first()

        if not interested_client:
            return None

        return self.create_interested_client_response(interested_client)