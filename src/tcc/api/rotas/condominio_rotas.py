from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID
from uuid6 import uuid7

from tcc.infraestrutura.conexao import obter_sessao
from tcc.infraestrutura.banco_dados.modelos.modelo_condominio import ModeloCondominio
from tcc.api.schemas.condominio_schemas import CondominioResponse, CriarCondominioRequest, AlterarCondominioRequest
from tcc.infraestrutura.repositorios.repositorio_condominio import RepositorioCondominio


router = APIRouter(
    prefix='/condominios',
    tags=['Condomínios'],
)
@router.get(
    '',
    summary='Listar condomínios',
    response_model=list[CondominioResponse],
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos condomínios cadastrados',
            'model': list[CondominioResponse]
        },
    },
)
def listar_condominios(
    session: Session = Depends(obter_sessao)
):
    """Listagem de todos os condomínios cadastrados."""
    repositorio = RepositorioCondominio(sessao=session)

    condominios = repositorio.obter_todos()
    
    return condominios