from uuid import UUID
from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File, Form
from tcc.api.schemas.imovel_schemas import CriarImagensImovelRequest, CriarImovelRequest, EditarImovelRequest, ImagensImovelResponse, ImovelResponse
from tcc.infraestrutura.repositorios.repositorio_imovel import RepositorioImovel
from tcc.infraestrutura.conexao import obter_sessao
from sqlalchemy.orm import Session
from http import HTTPStatus
from pathlib import Path
import shutil


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
    '/imagens',
    status_code=status.HTTP_200_OK,
    summary='Listar as imagens cadastradas',
    response_model= list[ImagensImovelResponse] | None,
    responses= {
        200: {
            'description': 'Lista de todas as imagens cadastradas.',
            'response_model': list[ImagensImovelResponse] | None
        }
    }
)
def listar_imagens(
    session: Session = Depends(obter_sessao)
):
    repositorio = RepositorioImovel(sessao=session)

    imagens = repositorio.listar_imagens_imovel()

    return imagens


@router.get(
    '/{id}',
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
    '/{id}',
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
    response_model=ImovelResponse,
    status_code=status.HTTP_201_CREATED,
    summary='Criar um imóvel.',
    responses= {
        204: {
            'description': 'Imóvel criado com sucesso!',
            'response_model': ImovelResponse
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



@router.post(
    '/imagens/cadastrar',
    summary='Salvar imagens no disco.',
    response_model=list[ImagensImovelResponse]
)
def fazer_upload_imagens(
    id_imovel: UUID = Form(...),
    imagens: list[UploadFile] = File(...),
    session: Session = Depends(obter_sessao)
):
    """Fazer o upload na pasta das imagens do imóvel."""
    repositorio = RepositorioImovel(sessao=session)

    pasta = Path('uploads/imoveis') / str(id_imovel)

    pasta.mkdir(
        parents=True,
        exist_ok=True
    )

    imagens_para_salvar = []

    for imagem in imagens:
        caminho = pasta / imagem.filename

        caminho_relativo = caminho.as_posix()

        with open(caminho, 'wb') as buffer:
            shutil.copyfileobj(
                imagem.file,
                buffer
            )

        imagens_para_salvar.append(
            CriarImagensImovelRequest(
                id_imovel=id_imovel,
                imagem=caminho_relativo,
                imagem_principal=False
            )
        )

    return repositorio.cadastrar_imagens_imovel(
        id_imovel=id_imovel,
        imagens=imagens_para_salvar
    )

@router.put(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Editar dados de um imóvel',
    responses= {
        204: {
            'description': 'Imóvel encontrado e alterado com sucesso.',
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
    
    return editou
    

@router.put(
    '/{id}/ativar',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Ativar um imóvel.',
    responses= {
        204: {
            'description': 'Imóvel encontrado e ativado com sucesso.'
        },
        404: {
            'description': 'Imóvel não encontrado.'
        },
    },
)
def ativar_imovel(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Ativar um imóvel já cadastrado filtrando por seu ID."""
    repositorio = RepositorioImovel(sessao=session)

    ativou = repositorio.ativar_imovel(id)
    
    if not ativou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado.'
        )


@router.put(
    '/{id}/inativar',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Inativar um imóvel.',
    responses= {
        204: {
            'description': 'Imóvel encontrado e inativado com sucesso.'
        },
        404: {
            'description': 'Imóvel não encontrado.'
        },
    },
)
def inativar_imovel(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Inativar um imóvel já cadastrado filtrando por seu ID."""
    repositorio = RepositorioImovel(sessao=session)

    inativou = repositorio.inativar_imovel(id)

    if not inativou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado.'
        )
    