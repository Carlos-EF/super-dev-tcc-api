from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from src.tcc.repository.client_repository import ClientRepository
from tcc.infrastructure.connection import get_session
from tcc.api.schemas.clients_schemas import CreateClientRequest, CreateInterestedClientRequest, EditClientRequest, InterestedClientResponse, PaginatedClientResponse, ClientResponse


router = APIRouter(
    prefix='/clients',
    tags=['Clients'],
)

@router.get(
    '',
    summary='Listar clientes',
    response_model=PaginatedClientResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos clientes cadastrados',
            'model': PaginatedClientResponse
        },
    },
)
def get_all(
    busca: Optional[str] = None,
    tipo: Optional[str] = None,
    origem: Optional[str] = None,
    pagina: int = Query(1, ge=1),
    por_pagina: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session)
):
    """Listagem de todos os clientes cadastrados."""
    repository = ClientRepository(session=session)

    clients = repository.get_all(
        busca=busca,
        tipo=tipo,
        origem=origem,
        pagina=pagina,
        por_pagina=por_pagina
    )

    return clients


@router.post(
    '',
    summary='Criar cliente',
    response_model=ClientResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Cliente criado com sucesso',
            'model': ClientResponse
        },
    },
)
def create(
    client: CreateClientRequest,
    session: Session = Depends(get_session)
):
    """Criação de um novo cliente."""
    repository = ClientRepository(session=session)

    created_client = repository.create(client=client)

    return created_client


@router.post(
    '/{id}/interested',
    summary='Criar cliente interessado',
    response_model=InterestedClientResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Cliente interessado criado com sucesso',
            'model': InterestedClientResponse
        },
    },
)
def create_interested_client(
    id: UUID,
    interested: CreateInterestedClientRequest,
    session: Session = Depends(get_session)
):
    """Criação de um novo cliente interessado."""
    repository = ClientRepository(session=session)

    created_interested_client = repository.create_interested_client(
        id=id,
        interested=interested
    )

    return created_interested_client