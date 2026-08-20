from uuid import UUID
from uuid6 import uuid7
from datetime import datetime
from sqlalchemy import or_, func
from sqlalchemy.orm import Session, joinedload
from math import ceil

from tcc.api.schemas.property_schemas import CreatePropertyRequest, CreateHouseRequest, CreateApartmentRequest, CreateLandRequest, EditPropertyRequest, EditHouseRequest, EditApartmentRequest, EditLandRequest, HouseResponse, ApartmentResponse, LandResponse, CompletePropertyResponse, PaginatedPropertyResponse, CreatePropertyImageRequest, EditPropertyImageRequest, PropertyImageResponse, HouseData, ApartmentData, LandData
from tcc.infrastructure.models.property_models import PropertyModel, LandModel, HouseModel, ApartmentModel, PropertyImageModel
from tcc.infrastructure.services.supabase_storage import SupabaseStorage


class PropertyRepository:
    def __init__(
            self,
            session: Session,
            storage: SupabaseStorage
            ):
        self.session = session
        self.storage = storage


    def create(
            self,
            property: CreatePropertyRequest
    ) -> CompletePropertyResponse:
        property_to_create = PropertyModel(
            id = uuid7(),
            proprietario_id= property.proprietario,
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


    def create_image(
        self,
        image: CreatePropertyImageRequest,
        file_bytes: bytes,
        content_type: str,
        extension: str
    ) -> PropertyImageResponse:

        property_image_id = uuid7()

        path = (
            f'{image.imovel_id}/'
            f'{property_image_id}.{extension}'
        )

        url = self.storage.upload(
            file_bytes=file_bytes,
            path=path,
            content_type=content_type
        )

        if image.principal:

            self.session.query(
                PropertyImageModel
            ).filter(
                PropertyImageModel.imovel_id
                == image.imovel_id
            ).update(
                {
                    PropertyImageModel.principal: False
                }
            )

        image_to_create = PropertyImageModel(
            id=property_image_id,
            imovel_id=image.imovel_id,
            caminho=path,
            url=url,
            principal=image.principal,
            criado_em=datetime.now()
        )

        self.session.add(
            image_to_create
        )

        self.session.commit()

        return self.create_image_response(
            image_to_create
        )


    def create_image_response(
        self,
        image: PropertyImageModel
    ) -> PropertyImageResponse:
        return PropertyImageResponse(
            id=image.id,
            imovel_id=image.imovel_id,
            caminho=image.caminho,
            url=image.url,
            principal=image.principal,
            criado_em=image.criado_em,
            alterado_em=image.alterado_em
        )


    def create_response(
            self,
            property: PropertyModel
    ) -> CompletePropertyResponse:
        return CompletePropertyResponse(
            id= property.id,
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
    ) -> ApartmentResponse:
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
        ).options(
            joinedload(
                PropertyModel.casa
            ),
            joinedload(
                PropertyModel.apartamento
            ),
            joinedload(
                PropertyModel.terreno
            )
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

    
    def get_land_by_id(
            self,
            id: UUID
    ) -> LandResponse | None:
        land = self.session.query(
            LandModel
        ).filter(
            LandModel.imovel_id == id
        ).first()

        if not land:
            return None

        return self.create_land_response(land)


    def get_image_by_id(
        self,
        id: UUID
    ) -> PropertyImageResponse | None:

        image = self.session.query(
            PropertyImageModel
        ).filter(
            PropertyImageModel.id == id
        ).first()

        if not image:
            return None

        return self.create_image_response(
            image
        )


    def delete(
            self,
            id: UUID
    ) -> bool:
        property_to_delete = self.session.query(
            PropertyModel.id
        ).filter(
            PropertyModel.id == id
        ).first()

        if not property_to_delete:
            return False


        self.session.delete(property_to_delete)
        self.session.commit()

        return True


    def edit_property(
            self,
            id: UUID,
            property: EditPropertyRequest
    ) -> CompletePropertyResponse | None: 
        property_to_edit = self.session.query(
            PropertyModel
        ).filter(
            PropertyModel.id == id
        ).first()

        if not property_to_edit:
            return None

        property_to_edit.proprietario_id = property.proprietario
        property_to_edit.corretor_id = property.corretor
        property_to_edit.finalidade = property.finalidade
        property_to_edit.em_condominio = property.em_condominio
        property_to_edit.condominio = property.condominio
        property_to_edit.cep = property.cep
        property_to_edit.logradouro = property.logradouro
        property_to_edit.numero = property.numero
        property_to_edit.uf = property.uf
        property_to_edit.cidade = property.cidade
        property_to_edit.complemento = property.complemento
        property_to_edit.valor = property.valor
        property_to_edit.valor_condominio = property.valor_condominio
        property_to_edit.valor_iptu = property.valor_iptu
        property_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_response(
            property_to_edit
        )


    def edit_land(
            self,
            id: UUID,
            land: EditLandRequest
    ) -> LandResponse | None:
        land_to_edit = self.session.query(
            LandModel
        ).filter(
            LandModel.imovel_id == id
        ).first()

        if not land_to_edit:
            return None

        land_to_edit.area_total = land.area_total
        land_to_edit.medida_esquerda = land.medida_esquerda
        land_to_edit.medida_direita = land.medida_direita
        land_to_edit.medida_frente = land.medida_frente
        land_to_edit.medida_fundo = land.medida_fundo
        land_to_edit.coeficiente = land.coeficiente
        land_to_edit.zoneamento = land.zoneamento
        land_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_land_response(
            land_to_edit
        )


    def edit_house(
            self,
            id: UUID,
            house: EditHouseRequest
    ) -> HouseResponse | None:
        house_to_edit = self.session.query(
            HouseModel
        ).filter(
            HouseModel.imovel_id == id
        ).first()

        if not house_to_edit:
            return None

        house_to_edit.metragem = house.metragem
        house_to_edit.quartos = house.quartos
        house_to_edit.suites = house.suites
        house_to_edit.banheiros = house.banheiros
        house_to_edit.garagens = house.garagens
        house_to_edit.andares = house.andares
        house_to_edit.salas = house.salas
        house_to_edit.esta_mobiliado = house.esta_mobiliado
        house_to_edit.mobilia = house.mobilia
        house_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_house_response(
            house_to_edit
        )

    
    def edit_apartment(
            self,
            id: UUID,
            apartment: EditApartmentRequest
    ) -> ApartmentResponse | None:
        apartment_to_edit = self.session.query(
            ApartmentModel
        ).filter(
            ApartmentModel.imovel_id == id
        ).first()

        if not apartment_to_edit:
            return None

        apartment_to_edit.metragem = apartment.metragem
        apartment_to_edit.quartos = apartment.quartos
        apartment_to_edit.suites = apartment.suites
        apartment_to_edit.banheiros = apartment.banheiros
        apartment_to_edit.garagens = apartment.garagens
        apartment_to_edit.andares = apartment.andares
        apartment_to_edit.salas = apartment.salas
        apartment_to_edit.esta_mobiliado = apartment.esta_mobiliado
        apartment_to_edit.mobilia = apartment.mobilia
        apartment_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_apartment_response(
            apartment_to_edit
        )


    def get_all(
            self,
            pagina: int,
            por_pagina: int
    ) -> PaginatedPropertyResponse:
        query = self.session.query(
            PropertyModel
        ).options(
            joinedload(
                PropertyModel.casa
            ),
            joinedload(
                PropertyModel.apartamento
            ),
            joinedload(
                PropertyModel.terreno
            ),
        )

        total_propertys = query.count()

        total_pages = ceil(
            total_propertys / por_pagina
        ) if total_propertys >  0 else 1

        propertys = (
            query
            .offset((pagina - 1) * por_pagina)
            .limit(por_pagina)
            .all()
        )

        return PaginatedPropertyResponse(
            imoveis=[self.create_response(property) for property in propertys],
            total=total_propertys,
            total_paginas=total_pages,
            pagina=pagina,
            por_pagina=por_pagina
        )


    def get_images_by_property_id(
            self,
            imovel_id: UUID
    ) -> list[PropertyImageResponse]:
        images = self.session.query(
            PropertyImageModel
        ).filter(
            PropertyImageModel.imovel_id == imovel_id
        ).order_by(
            PropertyImageModel.principal.desc(),
            PropertyImageModel.criado_em.asc()
        ).all()

        return [
            self.create_image_response(image)
            for image in images
        ]


    def edit_image(
        self,
        id: UUID,
        image: EditPropertyImageRequest
    ) -> PropertyImageResponse | None:

        image_to_edit = self.session.query(
            PropertyImageModel
        ).filter(
            PropertyImageModel.id == id
        ).first()

        if not image_to_edit:
            return None

        if image.principal:

            self.session.query(
                PropertyImageModel
            ).filter(
                PropertyImageModel.imovel_id
                == image_to_edit.imovel_id,
                PropertyImageModel.id != id
            ).update(
                {
                    PropertyImageModel.principal: False
                }
            )

        image_to_edit.principal = image.principal

        image_to_edit.alterado_em = datetime.now()

        self.session.commit()

        return self.create_image_response(
            image_to_edit
        )


    def delete_image(
        self,
        id: UUID
    ) -> bool:
        image_to_delete = self.session.query(
            PropertyImageModel
        ).filter(
            PropertyImageModel.id == id
        ).first()

        if not image_to_delete:
            return False

        self.storage.delete(
            image_to_delete.caminho
        )

        self.session.delete(
            image_to_delete
        )

        self.session.commit()

        return True