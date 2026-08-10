from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.repository.client_repository import ClientRepository
from tcc.infrastructure.connection import get_session
from tcc.api.schemas.clients_schemas import CreateClientRequest, CreateInterestedClientRequest, EditClientRequest, EditInterestedClientRequest, InterestedClientResponse, PaginatedClientResponse, ClientResponse


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
    ordem: Optional[str] = None,
    session: Session = Depends(get_session)
):
    """Listagem de todos os clientes cadastrados."""
    repository = ClientRepository(session=session)

    clients = repository.get_all(
        busca=busca,
        tipo=tipo,
        origem=origem,
        pagina=pagina,
        por_pagina=por_pagina,
        ordem=ordem
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


@router.put(
    '/{id}',
    summary='Editar cliente',
    response_model=ClientResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Cliente editado com sucesso',
            'model': ClientResponse
        },
    },
)
def edit(
    id: UUID,
    client: EditClientRequest,
    session: Session = Depends(get_session)
):
    """Edição de um cliente existente."""
    repository = ClientRepository(session=session)

    edited_client = repository.edit(
        id=id,
        client=client
    )

    return edited_client


@router.put(
    '/{id}/interested',
    summary='Editar cliente interessado',
    response_model=InterestedClientResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Cliente interessado editado com sucesso',
            'model': InterestedClientResponse
        },
    },
)
def edit_interested_client(
    id: UUID,
    interested: EditInterestedClientRequest,
    session: Session = Depends(get_session)
):
    """Edição de um cliente interessado existente."""
    repository = ClientRepository(session=session)

    edited_interested_client = repository.edit_interested_client(
        id=id,
        interested=interested
    )

    return edited_interested_client


@router.delete(
    '/{id}',
    summary='Deletar cliente',
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        204: {
            'description': 'Cliente deletado com sucesso',
        },
        404: {
            'description': 'Cliente não encontrado',
        },
    },
)
def delete(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Deleção de um cliente existente."""
    repository = ClientRepository(session=session)

    deleted = repository.delete(id=id)

    if not deleted:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado'
        )

    return None


@router.get(
    '/{id}',
    summary='Obter cliente por ID',
    response_model=ClientResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Cliente encontrado',
            'model': ClientResponse
        },
        404: {
            'description': 'Cliente não encontrado',
        },
    },
)
def get_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obtenção de um cliente existente por ID."""
    repository = ClientRepository(session=session)

    client = repository.get_by_id(id=id)

    if not client:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado'
        )

    return client


@router.get(
    '/{id}/interested',
    summary='Obter cliente interessado por ID',
    response_model=InterestedClientResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Cliente interessado encontrado',
            'model': InterestedClientResponse
        },
        404: {
            'description': 'Cliente interessado não encontrado',
        },
    },
)
def get_interested_client_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obtenção de um cliente interessado existente por ID."""
    repository = ClientRepository(session=session)

    interested_client = repository.get_interested_client_by_id(id=id)

    if not interested_client:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente interessado não encontrado'
        )

    return interested_client