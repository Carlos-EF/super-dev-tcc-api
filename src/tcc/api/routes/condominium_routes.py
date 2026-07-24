from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID
from uuid6 import uuid7

from tcc.infrastructure.connection import get_session
from tcc.infrastructure.models.condominium_models import  CondominiumModel
from tcc.api.schemas.condominium_schemas import CondominiumResponse, CreateCondominiumRequest, EditCondominiumRequest
from tcc.repository.condominium_repository import CondominiumRepository

router = APIRouter(
    prefix='/condominios',
    tags=['Condomínios'],
)


@router.get(
    '',
    summary='Listar condomínios',
    response_model=list[CondominiumResponse],
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos condomínios cadastrados',
            'model': list[CondominiumResponse]
        },
    },
)
def get_all(
    session: Session = Depends(get_session)
):
    """Listagem de todos os condomínios cadastrados."""
    repository = CondominiumRepository(session=session)

    condominiums = repository.get_all()

    return condominiums


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

    

