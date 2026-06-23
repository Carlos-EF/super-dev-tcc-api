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

@router.get(
    '/{id}',
    summary='Obter condomínio filtrando por ID',
    response_model=CondominioResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Condomínio encontrado',
            'model': CondominioResponse
        },
        404: {
            'description': 'Condomínio não encontrado',
        },
    },
)
def obter_condominio_por_id(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Obter um condomínio específico filtrando por ID."""
    repositorio = RepositorioCondominio(sessao=session)

    condominio = repositorio.obter_por_id(id)

    if not condominio:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Condomínio não encontrado.')

    return condominio


@router.post(
    '',
    summary='Criar um novo condomínio',
    response_model=CondominioResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Condomínio criado com sucesso',
            'model': CondominioResponse
        },
    },
)
def criar_condominio(
    condominio: CriarCondominioRequest,
    session: Session = Depends(obter_sessao)
):
    """Criar um novo condomínio."""
    repositorio = RepositorioCondominio(sessao=session)

    novo_condominio = ModeloCondominio(
        id=uuid7(),
        nome=condominio.nome,
        cep=condominio.cep,
        logradouro=condominio.logradouro,
        numero=condominio.numero,
        bairro=condominio.bairro,
        estado=condominio.estado,
        cidade=condominio.cidade
    )

    condominio_criado = repositorio.criar(novo_condominio)

    return condominio_criado


@router.put(
    '/{id}',
    summary='Alterar um condomínio existente',
    response_model=CondominioResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Condomínio alterado com sucesso',
            'model': CondominioResponse
        },
        404: {
            'description': 'Condomínio não encontrado',
        },
    },
)
def alterar_condominio(
    condominio: AlterarCondominioRequest,
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Alterar um condomínio existente filtrando por ID."""
    repositorio = RepositorioCondominio(sessao=session)

    condominio_para_editar = repositorio.obter_por_id(id)

    if not condominio_para_editar:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Condomínio não encontrado.')

    condominio_para_editar.nome = condominio.nome
    condominio_para_editar.cep = condominio.cep
    condominio_para_editar.logradouro = condominio.logradouro
    condominio_para_editar.numero = condominio.numero
    condominio_para_editar.bairro = condominio.bairro
    condominio_para_editar.estado = condominio.estado
    condominio_para_editar.cidade = condominio.cidade

    condominio_alterado = repositorio.editar(condominio_para_editar.id, condominio_para_editar)

    return condominio_alterado


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
def excluir_condominio(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Excluir um condomínio existente filtrando por ID."""
    repositorio = RepositorioCondominio(sessao=session)

    condominio_para_apagar = repositorio.obter_por_id(id)

    if not condominio_para_apagar:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail='Condomínio não encontrado.')

    repositorio.apagar(condominio_para_apagar.id)