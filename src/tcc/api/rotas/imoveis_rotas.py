from fastapi import APIRouter, Depends, status, HTTPException
from src.tcc.api.schemas.imovel_schemas import ImovelResponse
from src.tcc.infraestrutura.repositorios.repositorio_imovel import RepositorioImovel
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
def obter_imovel_por_id(
    id: str,
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