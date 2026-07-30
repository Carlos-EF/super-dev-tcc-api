from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.infrastructure.connection import get_session
from tcc.api.schemas.broker_schemas import CreateBrokerRequest, EditBrokerRequest, PaginatedBrokerResponse, BrokerResponse
from tcc.repository.broker_repository import BrokerRepository


router = APIRouter(
    prefix='/brokers',
    tags=['Brokers'],
)


@router.get(
    '',
    summary='Listar corretores',
    response_model=PaginatedBrokerResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos corretores cadastrados',
            'model': PaginatedBrokerResponse
        },
    },
)
def get_all(
    busca: Optional[str] = None,
    pagina: int = Query(1, ge=1),
    por_pagina: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session)
):
    """Listagem de todos os corretores cadastrados."""
    repository = BrokerRepository(session=session)

    brokers = repository.get_all(
        busca=busca,
        pagina=pagina,
        por_pagina=por_pagina
    )

    return brokers


@router.get(
    '/{id}',
    summary='Obter corretor filtrando por ID',
    response_model=BrokerResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Corretor encontrado',
            'model': BrokerResponse
        },
        404: {
            'description': 'Corretor não encontrado',
        },
    },
)
def get_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obter um corretor específico filtrando por ID."""
    repository = BrokerRepository(session=session)

    broker = repository.get_by_id(id)

    if not broker:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='corretor não encontrado.')

    return broker


@router.delete(
    '/{id}',
    summary='Excluir um corretor existente',
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        204: {
            'description': 'Corretor excluído com sucesso',
        },
        404: {
            'description': 'Corretor não encontrado',
        },
    },
)
def delete(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Excluir um corretor existente filtrando por ID."""
    repository = BrokerRepository(session=session)

    broker_to_delete = repository.get_by_id(id)

    if not broker_to_delete:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Corretor não encontrado.')

    repository.delete(broker_to_delete.id)