from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
from sqlalchemy import or_, func
from sqlalchemy.orm import Session, joinedload
from math import ceil

from tcc.api.schemas.property_schemas import CreatePropertyRequest, CreateHouseRequest, CreateApartmentRequest, CreateLandRequest, EditPropertyRequest, EditHouseRequest, EditApartmentRequest, EditLandRequest, PropertyResponse, HouseResponse, ApartmentResponse, LandResponse, CompletePropertyResponse, PaginatedPropertyResponse, HouseData, ApartmentData, LandData
from tcc.infrastructure.models.property_models import PropertyModel, LandModel, HouseModel, ApartmentModel


class PropertyRepository:
    def __init__(
            self,
            session: Session
            ):
        self.session = session