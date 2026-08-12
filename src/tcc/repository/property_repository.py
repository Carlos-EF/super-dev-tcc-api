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


    def create(
            self,
            property: CreatePropertyRequest
    ) -> PropertyResponse:
        property_to_create = PropertyModel(
            id = uuid7(),
            propretario_id= property.proprietario,
            corretor_id= property.corretor,
            codigo= property.codigo,
            finalidade= property.finalidade,
            tipo= property.tipo,
            em_condominio= property.em_condominio,
            condominio= property.condominio,
            cep= property.cep,
            logradouro= property.logradouro,
            numero= property.numero,
            bairro= property.bairro,
            uf= property.uf,
            cidade= property.cidade,
            complemento= property.complemento,
            valor= property.valor,
            valor_condominio= property.valor_condominio,
            valor_iptu= property.valor_iptu,
            criado_em= datetime.now(),
        )

        
        self.session.add(property_to_create)
        self.session.flush()
        self.session.commit()
