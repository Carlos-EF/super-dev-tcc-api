from fastapi import APIRouter, Depends, status
from src.tcc.api.schemas.imovel_schemas import ImovelResponse
from src.tcc.infraestrutura.repositorios.repositorio_imovel import RepositorioImovel
from tcc.infraestrutura.conexao import obter_sessao
from sqlalchemy.orm import Session


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