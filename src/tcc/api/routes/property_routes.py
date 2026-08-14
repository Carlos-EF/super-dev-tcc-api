from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from http import HTTPStatus
from uuid import UUID

from tcc.infrastructure.connection import get_session
from tcc.repository.property_repository import PropertyRepository
from tcc.api.schemas.property_schemas import CreatePropertyRequest, CreateHouseRequest, CreateApartmentRequest, CreateLandRequest, EditPropertyRequest, EditHouseRequest, EditApartmentRequest, EditLandRequest, PropertyResponse, HouseResponse, ApartmentResponse, LandResponse, CompletePropertyResponse, PaginatedPropertyResponse, HouseData, ApartmentData, LandData


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

    created_property = repository.create(property=property)

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


@router.put(
    '/{id}',
    summary='Editar imóvel',
    response_model=PropertyResponse,
    status_code=status.HTTP_200_OK,
    responses= {
        200: {
            'description': 'Imóvel editado com sucesso',
            'model': PropertyResponse
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