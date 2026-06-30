from uuid import UUID
from fastapi import APIRouter, Depends, status, HTTPException
from tcc.api.schemas.imovel_schemas import CriarImovelRequest, EditarImovelRequest, ImovelResponse
from tcc.infraestrutura.repositorios.repositorio_imovel import RepositorioImovel
from tcc.infraestrutura.conexao import obter_sessao
from sqlalchemy.orm import Session
from http import HTTPStatus


router = APIRouter(
    prefix='/imoveis',
    tags=['Imóveis'],
)
@router.get(
    '',
    response_model=list[ImovelResponse],
    status_code=status.HTTP_200_OK,
    summary='Listar todos os imóveis cadastrados.',
    responses= {
        200: {
            'description': 'Lista dos imóveis cadastrados',
            'model': list[ImovelResponse]
        },
    },
)
def listar_imoveis(
    session: Session = Depends(obter_sessao)
):
    """Listagem dos imóveis cadastrados."""
    repositorio = RepositorioImovel(sessao=session)

    imoveis = repositorio.listar_imoveis()

    return imoveis


@router.get(
    '{id}',
    response_model=ImovelResponse,
    status_code=status.HTTP_200_OK,
    summary='Listar o imóvel cadastrado.',
    responses= {
        200: {
            'description': 'Imóvel encontrado.',
            'model': ImovelResponse
        },
    },
)
def obter_imovel_por_id(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Buscar um imóvel filtrando pelo seu ID (UUIDv7)."""
    repositorio = RepositorioImovel(sessao=session)

    imovel = repositorio.obter_imovel_por_id(id)

    if not imovel:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado'
        )

    return imovel


@router.delete(
    '{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Apagar um imóvel cadastrado.',
    responses= {
        204: {
            'description': 'Imóvel encontrado e apagago com sucesso!',
        },
        404: {
            'description': 'Imóvel não encontrado.',
        }
    },
)
def apagar_imovel(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Buscar um imóvel filtrando pelo seu ID (UUIDv7) e o apaga."""
    repositorio = RepositorioImovel(sessao=session)

    imovel_para_apagar = repositorio.apagar_imovel(id)

    if not imovel_para_apagar:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado'
        )
    

@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    summary='Criar um imóvel.',
    responses= {
        204: {
            'description': 'Imóvel criado com sucesso!',
        }
    }
)
def criar_imovel(
    imovel: CriarImovelRequest,
    session: Session = Depends(obter_sessao)
):
    """Criar um imóvel novo."""

    repositorio = RepositorioImovel(sessao=session)

    imovel_criado = repositorio.criar_imovel(imovel)

    return imovel_criado


@router.put(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Editar dados de um imóvel',
    responses= {
        204: {
            'description': 'Imóvel encontrado e alterado com sucesso.'
        },
        404: {
            'description': 'Imóvel não encontrado.'
        },
    },
)
def editar_imovel(
    id: UUID,
    dados: EditarImovelRequest,
    session: Session = Depends(obter_sessao)
):
    """Editar dados de um imóvel já cadastrado filtrando por seu ID."""
    repositorio = RepositorioImovel(sessao=session)
    editou = repositorio.editar_imovel(
        id,
        dados
        )
    if not editou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado.'
        )