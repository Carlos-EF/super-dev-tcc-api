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
    ) -> CompletePropertyResponse:
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

        return self.create_response(property_to_create)
    

    def create_land(
        self,
        id: UUID,
        land: CreateLandRequest
    ) -> LandResponse:
        land_to_create = LandModel(
            id= uuid7(),
            imovel_id= id,
            area_total= land.area_total,
            medida_esquerda= land.medida_esquerda,
            medida_direita= land.medida_direita,
            medida_frente= land.medida_frente,
            medida_fundo= land.medida_fundo,
            zoneamento= land.zoneamento,
            coeficiente= land.coeficiente,
            criado_em= datetime.now(),
        )

        self.session.add(land_to_create)
        self.session.commit()

        return self.create_land_response(
            land_to_create
        )


    def create_house(
            self,
            id: UUID,
            house: CreateHouseRequest
    ) -> HouseResponse:
        house_to_create = HouseModel(
            id= uuid7(),
            imovel_id= id,
            metragem= house.metragem,
            quartos= house.quartos,
            suites= house.suites,
            banheiros= house.banheiros,
            garagens= house.garagens,
            andares= house.andares,
            salas= house.salas,
            esta_mobiliado= house.esta_mobiliado,
            mobilia= house.mobilia,
            criado_em= datetime.now(),
        )

        self.session.add(house_to_create)
        self.session.commit()

        return self.create_house_response(
            house_to_create
        )

    
    def create_apartment(
            self,
            id: UUID,
            apartment: CreateApartmentRequest
    ) -> ApartmentResponse:
        apartment_to_create = ApartmentModel(
            id= uuid7(),
            imovel_id= id,
            metragem= apartment.metragem,
            quartos= apartment.quartos,
            suites= apartment.suites,
            banheiros= apartment.banheiros,
            garagens= apartment.garagens,
            andares= apartment.andares,
            salas= apartment.salas,
            esta_mobiliado= apartment.esta_mobiliado,
            mobilia= apartment.mobilia,
            criado_em= datetime.now(),
        )

        self.session.add(apartment_to_create)
        self.session.commit()

        return self.create_apartment_response(
            apartment_to_create
        )


    def create_response(
            self,
            property: PropertyModel
    ) -> CompletePropertyResponse:
        return CompletePropertyResponse(
            id= property.id,
            proprietario= property.proprietario_id,
            corretor= property.corretor_id,
            codigo= property.codigo,
            finalidade= property.finalidade,
            tipo= property.tipo,
            em_condominio= property.em_condominio,
            condominio= property.condominio,
            cep= property.cep,
            logradouro= property.logradouro,
            numero= property.numero,
            bairro= property.bairro,
            cidade= property.cidade,
            uf= property.uf,
            complemento= property.complemento,
            valor= property.valor,
            valor_condominio= property.valor_condominio,
            valor_iptu= property.valor_iptu,
            criado_em= property.criado_em,
            alterado_em= property.alterado_em,
            casa= HouseData(
                metragem= property.casa.metragem,
                quartos= property.casa.quartos,
                suites= property.casa.suites,
                banheiros= property.casa.banheiros,
                garagens= property.casa.garagens,
                andares= property.casa.andares,
                salas= property.casa.salas,
                esta_mobiliado= property.casa.esta_mobiliado,
                mobilia= property.casa.mobilia,
            ) if property.casa else None,
            apartamento= ApartmentData(
                metragem= property.apartamento.metragem,
                quartos= property.apartamento.quartos,
                suites= property.apartamento.suites,
                banheiros= property.apartamento.banheiros,
                garagens= property.apartamento.garagens,
                andares= property.apartamento.andares,
                salas= property.apartamento.salas,
                esta_mobiliado= property.apartamento.esta_mobiliado,
                mobilia= property.apartamento.mobilia,
            ) if property.apartamento else None,
            terreno= LandData(
                area_total= property.terreno.area_total,
                medida_esquerda= property.terreno.medida_esquerda,
                medida_direita= property.terreno.medida_direita,
                medida_frente= property.terreno.medida_frente,
                medida_fundo= property.terreno.medida_fundo,
                zoneamento= property.terreno.zoneamento,
                coeficiente= property.terreno.coeficiente,
            ) if property.terreno else None
        )


    def create_land_response(
            self,
            land: LandModel
    ) -> LandResponse:
        return LandResponse(
            id=land.id,
            imovel_id= land.imovel_id,
            area_total= land.area_total,
            medida_esquerda= land.medida_esquerda,
            medida_direita= land.medida_direita,
            medida_frente= land.medida_frente,
            medida_fundo= land.medida_fundo,
            zoneamento= land.zoneamento,
            coeficiente= land.coeficiente,
            criado_em= land.criado_em,
            alterado_em= land.alterado_em,
        )


    def create_house_response(
            self,
            house: HouseModel
    ) -> HouseResponse:
        return HouseResponse(
            id= house.id,
            imovel_id= house.imovel_id,
            metragem= house.metragem,
            quartos= house.quartos,
            suites= house.suites,
            banheiros= house.banheiros,
            garagens= house.garagens,
            andares= house.andares,
            salas= house.salas,
            esta_mobiliado= house.esta_mobiliado,
            mobilia= house.mobilia,
            criado_em= house.criado_em,
            alterado_em= house.alterado_em,
        )

    
    def create_apartment_response(
            self,
            apartment: ApartmentModel
    ) -> HouseResponse:
        return ApartmentResponse(
            id= apartment.id,
            imovel_id= apartment.imovel_id,
            metragem= apartment.metragem,
            quartos= apartment.quartos,
            suites= apartment.suites,
            banheiros= apartment.banheiros,
            garagens= apartment.garagens,
            andares= apartment.andares,
            salas= apartment.salas,
            esta_mobiliado= apartment.esta_mobiliado,
            mobilia= apartment.mobilia,
            criado_em= apartment.criado_em,
            alterado_em= apartment.alterado_em,
        )


    def get_property_by_id(
            self,
            id: UUID
    ) -> CompletePropertyResponse | None:
        property = self.session.query(
            PropertyModel
        ).filter(
            PropertyModel.id == id
        ).first()

        if not property:
            return None

        return self.create_response(property)


    def get_house_by_id(
            self,
            id: UUID
    ) -> HouseResponse | None:
        house = self.session.query(
            HouseModel
        ).filter(
            HouseModel.imovel_id == id
        ).first()

        if not house:
            return None

        return self.create_house_response(house)

    
    def get_apartment_by_id(
            self,
            id: UUID
    ) -> ApartmentResponse | None:
        apartment = self.session.query(
            ApartmentModel
        ).filter(
            ApartmentModel.imovel_id == id
        ).first()

        if not apartment:
            return None

        return self.create_apartment_response(apartment)
