from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from src.tcc.repository.client_repository import ClientRepository
from tcc.infrastructure.connection import get_session
from tcc.api.schemas.clients_schemas import CreateClientRequest, EditClientRequest, PaginatedClientResponse, ClientResponse


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