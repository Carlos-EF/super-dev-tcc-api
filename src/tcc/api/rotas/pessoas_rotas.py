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