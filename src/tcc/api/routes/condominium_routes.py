from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.infrastructure.connection import get_session
from tcc.api.schemas.condominium_schemas import CitiesResponse, CondominiumResponse, CreateCondominiumRequest, DistrictsResponse, EditCondominiumRequest, PaginatedCondominiumResponse
from tcc.repository.condominium_repository import CondominiumRepository

router = APIRouter(
    prefix='/condominiums',
    tags=['Condominiums'],
)


@router.get(
    '',
    summary='Listar condomínios',
    response_model=PaginatedCondominiumResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos condomínios cadastrados',
            'model': PaginatedCondominiumResponse
        },
    },
)
def get_all(
    busca: Optional[str] = None,
    cidade: Optional[str] = None,
    bairro: Optional[str] = None,
    pagina: int = Query(1, ge=1),
    por_pagina: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session)
):
    """Listagem de todos os condomínios cadastrados."""
    repository = CondominiumRepository(session=session)

    condominiums = repository.get_all(
        busca=busca,
        cidade=cidade,
        bairro=bairro,
        pagina=pagina,
        por_pagina=por_pagina
    )


@router.get(
    '/cities',
    summary='Listar cidades',
    response_model=CitiesResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos cidades cadastradas',
            'model': CitiesResponse
        },
    },
)
def get_all_cities(
    session: Session = Depends(get_session)
):
    """Listagem de todas as cidades cadastradas."""
    repository = CondominiumRepository(session=session)

    cities = repository.get_all_cities()

    return cities


@router.get(
    '/districts',
    summary='Listar bairros',
    response_model=DistrictsResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos bairros cadastrados',
            'model': DistrictsResponse
        },
    },
)
def get_all_districts(
    session: Session = Depends(get_session)
):
    """Listagem de todos os bairros cadastrados."""
    repository = CondominiumRepository(session=session)

    districts = repository.get_all_districts( )

    return districts


@router.get(
    '/{id}',
    summary='Obter condomínio filtrando por ID',
    response_model=CondominiumResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Condomínio encontrado',
            'model': CondominiumResponse
        },
        404: {
            'description': 'Condomínio não encontrado',
        },
    },
)
def get_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obter um condomínio específico filtrando por ID."""
    repository = CondominiumRepository(session=session)

    condominium = repository.get_by_id(id)

    if not condominium:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Condomínio não encontrado.')

    return condominium


@router.delete(
    '/{id}',
    summary='Excluir um condomínio existente',
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        204: {
            'description': 'Condomínio excluído com sucesso',
        },
        404: {
            'description': 'Condomínio não encontrado',
        },
    },
)
def delete(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Excluir um condomínio existente filtrando por ID."""
    repository = CondominiumRepository(session=session)

    condominium_to_delete = repository.get_by_id(id)

    if not condominium_to_delete:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Condomínio não encontrado.')

    repository.delete(condominium_to_delete.id)


@router.put(
    '/{id}',
    summary='Alterar um condomínio existente',
    response_model=CondominiumResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Condomínio alterado com sucesso',
            'model': CondominiumResponse
        },
        404: {
            'description': 'Condomínio não encontrado',
        },
    },
)
def edit(
    id: UUID,
    condominium: EditCondominiumRequest,
    session: Session = Depends(get_session)
):
    """Alterar um condomínio existente filtrando por ID."""
    repository = CondominiumRepository(session=session)

    condominium_to_edit = repository.edit(id, condominium)

    if condominium_to_edit == False:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Condomínio não encontrado.')

    return condominium_to_edit


@router.post(
    '',
    summary='Criar um novo condomínio',
    response_model=CondominiumResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Condomínio criado com sucesso',
            'model': CondominiumResponse
        },
    },
)
def create(
    condominium: CreateCondominiumRequest,
    session: Session = Depends(get_session)
):
    """Criar um novo condomínio."""
    repositorio = CondominiumRepository(session=session)

    new_condominium = repositorio.create(condominium)

    return new_condominium
