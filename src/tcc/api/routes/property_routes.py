from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query, UploadFile, File, Form
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.infrastructure.connection import get_session, get_storage
from tcc.repository.property_repository import PropertyRepository
from tcc.api.schemas.property_schemas import CreatePropertyImageRequest, CreatePropertyRequest, CreateHouseRequest, CreateApartmentRequest, CreateLandRequest, EditPropertyImageRequest, EditPropertyRequest, EditHouseRequest, EditApartmentRequest, EditLandRequest, PropertyResponse, HouseResponse, ApartmentResponse, LandResponse, CompletePropertyResponse, PaginatedPropertyResponse, HouseData, ApartmentData, LandData


router = APIRouter(
    prefix='/propertys',
    tags=['Propertys'],
)

@router.get(
    '',
    summary='Listar imóveis',
    response_model=PaginatedPropertyResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Lista dos imóveis cadastrados',
            'model': PaginatedPropertyResponse
        },
    },
)
def get_all(
    pagina: int = Query(1, ge=1),
    por_pagina: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session)
):
    """Listagem de todos os imóveis cadastrados."""
    repository = PropertyRepository(session=session)

    propertys = repository.get_all(
        pagina=pagina,
        por_pagina=por_pagina,
    )

    return propertys


@router.post(
    '',
    summary='Criar imóvel',
    response_model=CompletePropertyResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Imóvel criado com sucesso',
            'model': CompletePropertyResponse
        },
    },
)
def create(
    property: CreatePropertyRequest,
    session: Session = Depends(get_session)
):
    """Criação de um novo imóvel."""
    repository = PropertyRepository(session=session)

    created_property = repository.create(property)

    return created_property


@router.post(
    '/{id}/house',
    summary='Criar casa',
    response_model=HouseResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Casa criada com sucesso',
            'model': HouseResponse
        },
    },
)
def create_house(
    id: UUID,
    house: CreateHouseRequest,
    session: Session = Depends(get_session)
):
    """Criação de uma nova casa."""
    repository = PropertyRepository(session=session)

    created_house = repository.create_house(
        id=id,
        house=house
    )

    return created_house


@router.post(
    '/{id}/land',
    summary='Criar terreno',
    response_model=LandResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Terreno criado com sucesso',
            'model': LandResponse
        },
    },
)
def create_land(
    id: UUID,
    land: CreateLandRequest,
    session: Session = Depends(get_session)
):
    """Criação de um novo terreno."""
    repository = PropertyRepository(session=session)

    created_land = repository.create_land(
        id=id,
        land=land
    )

    return created_land


@router.post(
    '/{id}/apartment',
    summary='Criar apartamento',
    response_model=ApartmentResponse,
    status_code=status.HTTP_201_CREATED,
    responses= {
        201: {
            'description': 'Apartamento criado com sucesso',
            'model': ApartmentResponse
        },
    },
)
def create_apartment(
    id: UUID,
    apartment: CreateApartmentRequest,
    session: Session = Depends(get_session)
):
    """Criação de um novo apartamento."""
    repository = PropertyRepository(session=session)

    created_apartment = repository.create_apartment(
        id=id,
        apartment=apartment
    )

    return created_apartment


@router.post(
    '/{imovel_id}/images'
)
async def create_image(
    imovel_id: UUID,
    principal: bool = Form(False),
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
    storage = Depends(get_storage)
):
    allowed_types = {
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'image/webp': 'webp'
}

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail='Formato de imagem não permitido.'
        )

    file_bytes = await file.read()

    max_size = 5 * 1024 * 1024

    if len(file_bytes) > max_size:
        raise HTTPException(
            status_code=400,
            detail='A imagem deve possuir no máximo 5 MB.'
        )

    request = CreatePropertyImageRequest(
        imovel_id=imovel_id,
        principal=principal
    )

    repository = PropertyRepository(
        session=session,
        storage=storage
        )

    return repository.create_image(
        image=request,
        file_bytes=file_bytes,
        content_type=file.content_type,
        extension=allowed_types[file.content_type]
    )


@router.put(
    '/{id}',
    summary='Editar imóvel',
    response_model=CompletePropertyResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Imóvel editado com sucesso',
            'model': CompletePropertyResponse
        },
    },
)
def edit(
    id: UUID,
    property: EditPropertyRequest,
    session: Session = Depends(get_session)
):
    """Edição de um imóvel existente."""
    repository = PropertyRepository(session=session)

    edited_property = repository.edit_property(
        id=id,
        property=property
    )

    return edited_property


@router.put(
    '/{id}/house',
    summary='Editar casa',
    response_model=HouseResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Casa editado com sucesso',
            'model': HouseResponse
        },
    },
)
def edit_house(
    id: UUID,
    house: EditHouseRequest,
    session: Session = Depends(get_session)
):
    """Edição de uma casa existente."""
    repository = PropertyRepository(session=session)

    edited_house = repository.edit_house(
        id=id,
        house=house
    )

    return edited_house


@router.put(
    '/{id}/land',
    summary='Editar terreno',
    response_model=LandResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Terreno editado com sucesso',
            'model': LandResponse
        },
    },
)
def edit_land(
    id: UUID,
    land: EditLandRequest,
    session: Session = Depends(get_session)
):
    """Edição de uma terreno existente."""
    repository = PropertyRepository(session=session)

    edited_land = repository.edit_land(
        id=id,
        land=land
    )

    return edited_land


@router.put(
    '/{id}/land',
    summary='Editar apartamento',
    response_model=ApartmentResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Apartamento editado com sucesso',
            'model': ApartmentResponse
        },
    },
)
def edit_apartment(
    id: UUID,
    apartment: EditApartmentRequest,
    session: Session = Depends(get_session)
):
    """Edição de uma apartamento existente."""
    repository = PropertyRepository(session=session)

    edited_apartment = repository.edit_apartment(
        id=id,
        apartment=apartment
    )

    return edited_apartment


@router.put(
    '/images/{imagem_id}'
)
async def edit_image(
    imagem_id: UUID,
    request: EditPropertyImageRequest,
    session: Session = Depends(get_session),
    storage = Depends(get_storage),
):
    repository = PropertyRepository(
        session=session,
        storage=storage
    )

    image = repository.edit_image(
        imagem_id,
        request
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail='Imagem não encontrada.'
        )

    return image


@router.delete(
    '/{id}',
    summary='Deletar imóvel',
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        204: {
            'description': 'Imóvel deletado com sucesso',
        },
        404: {
            'description': 'Imóvel não encontrado',
        },
    },
)
def delete(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Deleção de um imóvel existente."""
    repository = PropertyRepository(session=session)

    deleted = repository.delete(id=id)

    if not deleted:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado'
        )

    return None


@router.delete(
    '/images/{imagem_id}'
)
async def delete_image(
    imagem_id: UUID,
    session: Session = Depends(get_session),
    storage = Depends(get_storage),
):
    repository = PropertyRepository(
        session=session,
        storage=storage
    )

    image = repository.delete_image(
        imagem_id
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail='Imagem não encontrada.'
        )

    return {
        'detail': 'Imagem excluída com sucesso.'
    }


@router.get(
    '/{id}',
    summary='Obter imóvel por ID',
    response_model=CompletePropertyResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Imóvel encontrado',
            'model': CompletePropertyResponse
        },
        404: {
            'description': 'Imóvel não encontrado',
        },
    },
)
def get_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obtenção de um imóvel existente por ID."""
    repository = PropertyRepository(session=session)

    property = repository.get_property_by_id(id=id)

    if not property:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Imóvel não encontrado'
        )

    return property


@router.get(
    '/{id}/house',
    summary='Obter casa por ID',
    response_model=HouseResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Casa encontrada',
            'model': HouseResponse
        },
        404: {
            'description': 'Casa não encontrada',
        },
    },
)
def get_house_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obtenção de uma casa existente por ID."""
    repository = PropertyRepository(session=session)

    house = repository.get_house_by_id(id=id)

    if not house:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Casa não encontrada'
        )

    return house


@router.get(
    '/{id}/apartment',
    summary='Obter apartamento por ID',
    response_model=ApartmentResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Apartamento encontrada',
            'model': ApartmentResponse
        },
        404: {
            'description': 'Apartamento não encontrada',
        },
    },
)
def get_apartment_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obtenção de um apartamento existente por ID."""
    repository = PropertyRepository(session=session)

    apartment = repository.get_apartment_by_id(id=id)

    if not apartment:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Apartamento não encontrado'
        )

    return apartment


@router.get(
    '/{id}/land',
    summary='Obter terreno por ID',
    response_model=LandResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Terreno encontrada',
            'model': LandResponse
        },
        404: {
            'description': 'Terreno não encontrada',
        },
    },
)
def get_land_by_id(
    id: UUID,
    session: Session = Depends(get_session)
):
    """Obtenção de um terreno existente por ID."""
    repository = PropertyRepository(session=session)

    land = repository.get_land_by_id(id=id)

    if not land:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Terreno não encontrado'
        )

    return land