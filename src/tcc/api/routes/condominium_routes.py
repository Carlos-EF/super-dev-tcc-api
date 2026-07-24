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
    repository = CondominiumRepository(sessao=session)

    condominiums = repository.get_all()

    return condominiums