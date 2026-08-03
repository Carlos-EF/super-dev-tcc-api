from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from math import ceil
from tcc.api.schemas.clients_schemas import CreateClientRequest, EditClientRequest, PaginatedClientResponse, ClientResponse
from tcc.infrastructure.models.client_models import ClientModel


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
            criado_em= client.criado_em
        )