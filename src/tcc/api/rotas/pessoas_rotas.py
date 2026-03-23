from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid6 import uuid7

from tcc.infraestrutura.conexao import obter_sessao
from tcc.infraestrutura.banco_dados.modelos.modelo_cliente import ModeloCliente
from tcc.infraestrutura.repositorios.repositorio_cliente import RepositorioCliente
from tcc.api.schemas.cliente_schemas import AlterarClienteRequest, ClienteResponse, CriarClienteRequest


router = APIRouter(
    prefix='/clientes',
    tags=['Clientes'],
)
router.post(
    '',
    response_model=ClienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary='Criar novo cliente',
    responses={
        201: {
            'description': 'Cliente criado com sucesso.',
            'model': ClienteResponse
        },
    },
)
def criar_cliente(
        dados: CriarClienteRequest,
        session: Session = Depends(obter_sessao)
) -> ClienteResponse:
    """Cadastrar um novo cliente."""
    cliente = ModeloCliente(
        id=uuid7(),
        nome=dados.nome,
        status=dados.status,
        codigo=dados.codigo,
        celular=dados.celular,
        email=dados.email,
        tipo=dados.tipo,
        como_encontrou=dados.como_encontrou
    )

    repositorio = RepositorioCliente(sessao=session)
    cliente = repositorio.criar(cliente)
    return cliente


@router.get(
    "",
    response_model=list[ClienteResponse],
    status_code=status.HTTP_200_OK,
    summary='Listar todos os clientes cadastrados',
    responses= {
        200: {
            'description': 'Lista de clientes cadastrados',
            'model': list[ClienteResponse]
        }
    }
)
def listar_clientes(
    session: Session = Depends(obter_sessao)
):
    """Listagem de todos os clientes cadastrados."""
    repositorio = RepositorioCliente(sessao=session)
    clientes = repositorio.listar()
    return clientes


@router.put(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Editar dados de um cliente',
    responses= {
        204: {
            'description': 'Cliente encontrado e modificado com sucesso.'
        },
        404: {
            'description': 'Cliente não encontrado.'
        }
    }
)
def editar_cliente(
    id: UUID,
    dados: AlterarClienteRequest,
    session: Session = Depends(obter_sessao)
):
    """Editar dados de um cliente já cadastrado buscando por seu ID."""
    repositorio = RepositorioCliente(sessao=session)
    editou = repositorio.editar(
        id,
        nome=dados.nome,
        celular=dados.celular,
        email=dados.email,
        tipo=dados.tipo
    )
    if not editou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado.'
        )
    

@router.get(
    "/{id}",
    response_model=ClienteResponse,
    status_code=status.HTTP_200_OK,
    summary='Buscar um cliente filtrando por seu ID.',
    description="""
        Busca um cliente específico pelo seu ID (UUID v7).""",
    responses= {
        200: {
            'description': 'Cliente encontrado.',
            'model': ClienteResponse
        },
    },
)
def buscar_cliente(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Busca um cliente por seu ID."""
    repositorio = RepositorioCliente(sessao=session)
    cliente = repositorio.buscar_por_id(id)
    if not cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado.'
        )
    
    return cliente