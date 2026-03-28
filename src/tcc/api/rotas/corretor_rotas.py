from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid6 import uuid7


from tcc.infraestrutura.conexao import obter_sessao
from tcc.infraestrutura.banco_dados.modelos.modelo_corretor import ModeloCorretor
from tcc.infraestrutura.repositorios.repositorio_corretor import RepositorioCorretor
from tcc.api.schemas.corretor_schemas import CorretorResponse, CriarCorretorRequest, AlterarCorretorRequest


router = APIRouter(
    prefix='/corretores',
    tags=['Corretores'],
)
@router.get(
    '',
    response_model=list[CorretorResponse],
    status_code=status.HTTP_200_OK,
    summary='Listar todos os corretores cadastrados.',
    responses= {
        200: {
            'description': 'Lista dos corretores cadastrados',
            'model': list[CorretorResponse]
        },
    },
)
def listar_corretores(
    session: Session = Depends(obter_sessao)
):
    """Listagem de todos os corretores cadastrados."""
    repositorio = RepositorioCorretor(sessao=session)
    corretores = repositorio.listar()
    return corretores


@router.get(
    '{id}',
    response_model= CorretorResponse,
    status_code=status.HTTP_200_OK,
    summary='Busca um corretor filtrando por seu ID.',
    description="""
        Busca um corretor específico pelo seu ID (UUID v7).""",
    responses= {
        200: {
            'description': 'Corretor encontrado',
            'model': CorretorResponse
        },
    },
)
def buscar_corretor(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Busca um corretor por seu ID."""
    repositorio = RepositorioCorretor(sessao=session)
    corretor = repositorio.obter_por_id(id)
    if not corretor:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Corretor não encontrado.'
        )
    
    return corretor


@router.delete(
    '{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Deleta um corretor.',
    description="""
        Busca um corretor específico pelo seu ID (UUID v7) e o apaga.""",
    responses= {
        204: {
            'description': 'Corretor encontrado e deletado com sucesso.',
        },
        404: {
            'description': 'Corretor não encontrado.',
        },
    },
)
def deletar_corretor(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Deleta um corretor buscando por seu ID."""
    repositorio = RepositorioCorretor(sessao=session)
    apagou = repositorio.apagar(id)
    if not apagou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Corretor não encontrado.'
        )