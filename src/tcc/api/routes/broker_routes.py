from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.infrastructure.connection import get_session
from tcc.api.schemas.broker_schemas import CreateBrokerRequest, EditBrokerRequest, PaginatedBrokerResponse, BrokerResponse
from tcc.repository.broker_repository import BrokerRepository
from tcc.infrastructure.models.enums.broker_tables_types import BrokerTablesTypes
from tcc.infrastructure.models.enums.sort_types import SortTypes

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
    com_imoveis: Optional[str] = None,
    sem_imoveis: Optional[str] = None,
    pagina: int = Query(1, ge=1),
    por_pagina: int = Query(10, ge=1, le=100),
    ordenar_por: BrokerTablesTypes = Query(BrokerTablesTypes.NOME),
    direcao: SortTypes = Query(SortTypes.ASC),
    session: Session = Depends(get_session)
):
    """Listagem de todos os corretores cadastrados."""
    repository = BrokerRepository(session=session)

    brokers = repository.get_all(
        busca=busca,
        com_imoveis=com_imoveis,
        sem_imoveis=sem_imoveis,
        pagina=pagina,
        por_pagina=por_pagina,
        ordenar_por=ordenar_por,
        direcao=direcao
    )

    return brokers


@router.get(
    '/list',
    summary='Buscar corretores para listas',
    response_model=list[BrokerResponse],
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos corretores cadastrados',
            'model': list[BrokerResponse]
        },
    },
)
def get_all(
    session: Session = Depends(get_session)
):
    """Listagem de todos os corretores cadastrados."""
    repository = BrokerRepository(session=session)

    brokers = repository.get_all_for_list()

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


@router.put(
    '/{id}',
    summary='Alterar um corretor existente',
    response_model=BrokerResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Corretor alterado com sucesso',
            'model': BrokerResponse
        },
        404: {
            'description': 'Corretor não encontrado',
        },
    },
)
def edit(
    id: UUID,
    condominium: EditBrokerRequest,
    session: Session = Depends(get_session)
):
    """Alterar um corretor existente filtrando por ID."""
    repository = BrokerRepository(session=session)

    broker_to_edit = repository.edit(id, condominium)

    if broker_to_edit == False:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Corretor não encontrado.')

    return broker_to_edit


@router.post(
    '',
    summary='Criar um novo corretor',
    response_model=BrokerResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Corretor criado com sucesso',
            'model': BrokerResponse
        },
    },
)
def create(
    condominium: CreateBrokerRequest,
    session: Session = Depends(get_session)
):
    """Criar um novo corretor."""
    repository = BrokerRepository(session=session)

    new_broker = repository.create(condominium)

    return new_broker
