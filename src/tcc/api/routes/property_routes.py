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