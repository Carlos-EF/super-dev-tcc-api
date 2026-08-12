from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from src.tcc.infrastructure.models.enums.zoning_types import ZoningTypes
from tcc.infrastructure.models.enums.property_types import PropertyTypes
from tcc.infrastructure.models.enums.finality_types import FinalityTypes
from tcc.infrastructure.models.enums.furnished_types import FurnishedTypes, FurnitureTypes


class PropertyResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='ID (UUIDv7) do imóvel',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )

    proprietario: UUID | None = Field(
        None,
        description='ID do proprietário',
        examples=[None]
    )

    corretor: UUID | None = Field(
        None,
        description='ID do corretor',
        examples=[None]
    )

    codigo: str = Field(
        ...,
        min_length=4,
        max_length=4,
        description='Código do imóvel',
        examples=['1234']
    )

    finalidade: FinalityTypes = Field(
        ...,
        min_length=7,
        max_length=7,
        description='finalidade do imóvel',
        examples=['Venda']
    )

    tipo: PropertyTypes = Field(
        ...,
        max_length=11,
        description='Tipo do imóvel',
        examples=['Casa', 'Apartamento']
    )

    em_condominio: bool = Field(
        default=False,
        description='Diz se está ou não em um imóvel',
        examples=[False]
    )

    condominio: UUID | None = Field(
        None,
        description='ID do condomínio',
        examples=[None]
    )

    cep: str = Field(
        ...,
        min_length=9,
        max_length=9,
        description='CEP do imóvel',
        examples=['89040-001']
    )

    logradouro: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Logradouro do imóvel',
        examples=['Rua dos Caçadores']
    )

    numero: int = Field(
        ...,
        description='Número do imóvel',
        examples=[204]
    )

    bairro: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Bairro do imóvel',
        examples=['Velha']
    )

    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description='UF onde se localiza o imóvel',
        examples=['SC']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Cidade do imóvel',
        examples=['Blumenau']
    )

    complemento: str | None = Field(
        None,
        max_length=60,
        description='Complemento da localização do imóvel',
        examples=['Perto do TOP']
    )

    valor: float | None = Field(
        None,
        description='Valor de venda do imóvel.',
        examples=[350000.00, 450000.00]
    )

    valor_iptu: float | None = Field(
        None,
        description='Valor do iptu do imóvel.',
        examples=[1000.00]
    )

    valor_condominio: float | None = Field(
        None,
        description='Valor do condomínio do imóvel.',
        examples=[1000.00]
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro.',
        examples=['2023-07-21T14:30:00Z']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro.',
        examples=['2023-07-22T10:15:00Z']
    )

    model_config = { 
      'json_schema_extra': { 
          'examples': [ 
              { 
                    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'proprietario': '9b2c3d4e-5f6a-47b8-9c0d-1e2f3a4b5c6d',
                    'corretor': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b',
                    'codigo': '1234',
                    'finalidade': 'Venda',
                    'tipo': 'Casa',
                    'em_condominio': False,
                    'condominio': None,
                    'cep': '89040-001',
                    'logradouro': 'Rua dos Caçadores',
                    'numero': 204,
                    'bairro': 'Velha',
                    'uf': 'SC',
                    'cidade': 'Blumenau',
                    'complemento': 'Perto do TOP',
                    'valor': 350000.00,
                    'valor_iptu': 1200.00,
                    'valor_condominio': None,
                    'criado_em': '2023-07-21T14:30:00Z',
                    'alterado_em': '2023-07-22T10:15:00Z' 
                }
            ]
        }
    }


class CreatePropertyRequest(BaseModel):
    proprietario: UUID | None = Field(
        None,
        description='ID do proprietário',
        examples=[None]
    )

    corretor: UUID | None = Field(
        None,
        description='ID do corretor',
        examples=[None]
    )

    codigo: str = Field(
        ...,
        min_length=4,
        max_length=4,
        description='Código do imóvel',
        examples=['1234']
    )

    finalidade: FinalityTypes = Field(
        ...,
        min_length=7,
        max_length=7,
        description='finalidade do imóvel',
        examples=['Venda']
    )

    tipo: PropertyTypes = Field(
        ...,
        max_length=11,
        description='Tipo do imóvel',
        examples=['Casa', 'Apartamento']
    )

    em_condominio: bool = Field(
        default=False,
        description='Diz se está ou não em um imóvel',
        examples=[False]
    )

    condominio: UUID | None = Field(
        None,
        description='ID do condomínio',
        examples=[None]
    )

    cep: str = Field(
        ...,
        min_length=9,
        max_length=9,
        description='CEP do imóvel',
        examples=['89040-001']
    )

    logradouro: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Logradouro do imóvel',
        examples=['Rua dos Caçadores']
    )

    numero: int = Field(
        ...,
        description='Número do imóvel',
        examples=[204]
    )

    bairro: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Bairro do imóvel',
        examples=['Velha']
    )

    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description='UF onde se localiza o imóvel',
        examples=['SC']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Cidade do imóvel',
        examples=['Blumenau']
    )

    complemento: str | None = Field(
        None,
        max_length=60,
        description='Complemento da localização do imóvel',
        examples=['Perto do TOP']
    )

    valor: float | None = Field(
        None,
        description='Valor de venda do imóvel.',
        examples=[350000.00, 450000.00]
    )

    valor_iptu: float | None = Field(
        None,
        description='Valor do iptu do imóvel.',
        examples=[1000.00]
    )

    valor_condominio: float | None = Field(
        None,
        description='Valor do condomínio do imóvel.',
        examples=[1000.00]
    )

    model_config = { 
      'json_schema_extra': { 
          'examples': [ 
              { 
                    'proprietario': '9b2c3d4e-5f6a-47b8-9c0d-1e2f3a4b5c6d',
                    'corretor': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b',
                    'codigo': '1234',
                    'finalidade': 'Venda',
                    'tipo': 'Casa',
                    'em_condominio': False,
                    'condominio': None,
                    'cep': '89040-001',
                    'logradouro': 'Rua dos Caçadores',
                    'numero': 204,
                    'bairro': 'Velha',
                    'uf': 'SC',
                    'cidade': 'Blumenau',
                    'complemento': 'Perto do TOP',
                    'valor': 350000.00,
                    'valor_iptu': 1200.00,
                    'valor_condominio': None 
                }
            ]
        }
    }


class EditPropertyRequest(BaseModel):
    proprietario: UUID | None = Field(
        None,
        description='ID do proprietário',
        examples=[None]
    )

    corretor: UUID | None = Field(
        None,
        description='ID do corretor',
        examples=[None]
    )

    finalidade: FinalityTypes = Field(
        ...,
        min_length=7,
        max_length=7,
        description='finalidade do imóvel',
        examples=['Venda']
    )

    em_condominio: bool = Field(
        default=False,
        description='Diz se está ou não em um imóvel',
        examples=[False]
    )

    condominio: UUID | None = Field(
        None,
        description='ID do condomínio',
        examples=[None]
    )

    cep: str = Field(
        ...,
        min_length=9,
        max_length=9,
        description='CEP do imóvel',
        examples=['89040-001']
    )

    logradouro: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Logradouro do imóvel',
        examples=['Rua dos Caçadores']
    )

    numero: int = Field(
        ...,
        description='Número do imóvel',
        examples=[204]
    )

    bairro: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Bairro do imóvel',
        examples=['Velha']
    )

    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description='UF onde se localiza o imóvel',
        examples=['SC']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Cidade do imóvel',
        examples=['Blumenau']
    )

    complemento: str | None = Field(
        None,
        max_length=60,
        description='Complemento da localização do imóvel',
        examples=['Perto do TOP']
    )

    valor: float | None = Field(
        None,
        description='Valor de venda do imóvel.',
        examples=[350000.00, 450000.00]
    )

    valor_iptu: float | None = Field(
        None,
        description='Valor do iptu do imóvel.',
        examples=[1000.00]
    )

    valor_condominio: float | None = Field(
        None,
        description='Valor do condomínio do imóvel.',
        examples=[1000.00]
    )

    model_config = { 
      'json_schema_extra': { 
          'examples': [ 
              { 
                    'proprietario': '9b2c3d4e-5f6a-47b8-9c0d-1e2f3a4b5c6d',
                    'corretor': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b',
                    'finalidade': 'Venda',
                    'em_condominio': False,
                    'condominio': None,
                    'cep': '89040-001',
                    'logradouro': 'Rua dos Caçadores',
                    'numero': 204,
                    'bairro': 'Velha',
                    'uf': 'SC',
                    'cidade': 'Blumenau',
                    'complemento': 'Perto do TOP',
                    'valor': 350000.00,
                    'valor_iptu': 1200.00,
                    'valor_condominio': None 
                }
            ]
        }
    }


class HouseResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='ID (UUIDv7) da casa',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )
        
    imovel_id: UUID = Field(
        ...,
        description='ID do imóvel (tabela principal)',
        examples=['2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b']
    )

    metragem: float | None = Field(
        None,
        description='Metragem total da casa',
        examples=[65.20]
    )

    quartos: int | None = Field(
        None,
        description='Quantidade de quartos',
        examples=[2]
    )

    suites: int | None = Field(
        None,
        description='Quantidade de quartos que são suítes',
        examples=[1]
    )

    banheiros: int | None = Field(
        None,
        description='Quantidade de banheiros',
        examples=[2]
    )

    garagens: int | None = Field(
        None,
        description='Quantidade de vagas de garagens',
        examples=[2]
    )

    andares: int | None = Field(
        None,
        description='Quantidade de pavimentos',
        examples=[1]
    )

    salas: int | None = Field(
        None,
        description='Quantidade de salas',
        examples=[4]
    )

    esta_mobiliado: FurnishedTypes | None = Field(
        None,
        description='Diz se a casa possui mobília ou não',
        examples=[FurnishedTypes.SEMI, FurnishedTypes.NAO]
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro.',
        examples=['2023-07-21T14:30:00Z']
    )
    
    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro.',
        examples=['2023-07-22T10:15:00Z']
    )

    mobilia: list[FurnitureTypes] | None = Field(
        None,
        description='Lugares que possuí mobília',
        examples=[
            [
                FurnitureTypes.SOFA,
                FurnitureTypes.ARMARIOS_QUARTOS,
                FurnitureTypes.ARMARIOS_BANHEIROS,
                FurnitureTypes.COZINHA_PLANEJADA,
            ]
        ]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'imovel_id': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b', 
                    'metragem': 120.5, 
                    'quartos': 3, 
                    'suites': 1, 
                    'banheiros': 2, 
                    'garagens': 2, 
                    'andares': 1, 
                    'salas': 2, 
                    'esta_mobiliado': 'Semi mobiliado', 
                    'mobilia': 
                    [ 
                    'Sofá', 
                    'Armários nos quartos', 
                    'Armários nos banheiros',
                    'Cozinha planejada' 
                    ],
                    'criado_em': '2023-07-21T14:30:00Z',
                    'alterado_em': '2023-07-22T10:15:00Z' 
                }
            ] 
        } 
     }

    
class CreateHouseRequest(BaseModel):
    imovel_id: UUID = Field(
        ...,
        description='ID do imóvel (tabela principal)',
        examples=['2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b']
    )

    metragem: float | None = Field(
        None,
        description='Metragem total da casa',
        examples=[65.20]
    )

    quartos: int | None = Field(
        None,
        description='Quantidade de quartos',
        examples=[2]
    )

    suites: int | None = Field(
        None,
        description='Quantidade de quartos que são suítes',
        examples=[1]
    )

    banheiros: int | None = Field(
        None,
        description='Quantidade de banheiros',
        examples=[2]
    )

    garagens: int | None = Field(
        None,
        description='Quantidade de vagas de garagens',
        examples=[2]
    )

    andares: int | None = Field(
        None,
        description='Quantidade de pavimentos',
        examples=[1]
    )

    salas: int | None = Field(
        None,
        description='Quantidade de salas',
        examples=[4]
    )

    esta_mobiliado: FurnishedTypes | None = Field(
        None,
        description='Diz se a casa possui mobília ou não',
        examples=[FurnishedTypes.SEMI, FurnishedTypes.NAO]
    )

    mobilia: list[FurnitureTypes] | None = Field(
        None,
        description='Lugares que possuí mobília',
        examples=[
            [
                FurnitureTypes.SOFA,
                FurnitureTypes.ARMARIOS_QUARTOS,
                FurnitureTypes.ARMARIOS_BANHEIROS,
                FurnitureTypes.COZINHA_PLANEJADA,
            ]
        ]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'imovel_id': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b', 
                    'metragem': 120.5, 
                    'quartos': 3, 
                    'suites': 1, 
                    'banheiros': 2, 
                    'garagens': 2, 
                    'andares': 1, 
                    'salas': 2, 
                    'esta_mobiliado': 'Semi mobiliado', 
                    'mobilia': 
                    [ 
                    'Sofá', 
                    'Armários nos quartos', 
                    'Armários nos banheiros',
                    'Cozinha planejada' 
                    ] 
                }
            ] 
        } 
     }

    
class EditHouseRequest(BaseModel):
    metragem: float | None = Field(
        None,
        description='Metragem total da casa',
        examples=[65.20]
    )

    quartos: int | None = Field(
        None,
        description='Quantidade de quartos',
        examples=[2]
    )

    suites: int | None = Field(
        None,
        description='Quantidade de quartos que são suítes',
        examples=[1]
    )

    banheiros: int | None = Field(
        None,
        description='Quantidade de banheiros',
        examples=[2]
    )

    garagens: int | None = Field(
        None,
        description='Quantidade de vagas de garagens',
        examples=[2]
    )

    andares: int | None = Field(
        None,
        description='Quantidade de pavimentos',
        examples=[1]
    )

    salas: int | None = Field(
        None,
        description='Quantidade de salas',
        examples=[4]
    )

    esta_mobiliado: FurnishedTypes | None = Field(
        None,
        description='Diz se a casa possui mobília ou não',
        examples=[FurnishedTypes.SEMI, FurnishedTypes.NAO]
    )

    mobilia: list[FurnitureTypes] | None = Field(
        None,
        description='Lugares que possuí mobília',
        examples=[
            [
                FurnitureTypes.SOFA,
                FurnitureTypes.ARMARIOS_QUARTOS,
                FurnitureTypes.ARMARIOS_BANHEIROS,
                FurnitureTypes.COZINHA_PLANEJADA,
            ]
        ]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'metragem': 120.5, 
                    'quartos': 3, 
                    'suites': 1, 
                    'banheiros': 2, 
                    'garagens': 2, 
                    'andares': 1, 
                    'salas': 2, 
                    'esta_mobiliado': 'Semi mobiliado', 
                    'mobilia': 
                    [ 
                    'Sofá', 
                    'Armários nos quartos', 
                    'Armários nos banheiros',
                    'Cozinha planejada' 
                    ] 
                }
            ] 
        } 
     }

    
class ApartmentResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='ID (UUIDv7) do apartamento',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )
        
    imovel_id: UUID = Field(
        ...,
        description='ID do imóvel (tabela principal)',
        examples=['2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b']
    )

    metragem: float | None = Field(
        None,
        description='Metragem total do apartamento',
        examples=[65.20]
    )

    quartos: int | None = Field(
        None,
        description='Quantidade de quartos',
        examples=[2]
    )

    suites: int | None = Field(
        None,
        description='Quantidade de quartos que são suítes',
        examples=[1]
    )

    banheiros: int | None = Field(
        None,
        description='Quantidade de banheiros',
        examples=[2]
    )

    garagens: int | None = Field(
        None,
        description='Quantidade de vagas de garagens',
        examples=[2]
    )

    andares: int | None = Field(
        None,
        description='Quantidade de pavimentos',
        examples=[1]
    )

    salas: int | None = Field(
        None,
        description='Quantidade de salas',
        examples=[4]
    )

    esta_mobiliado: FurnishedTypes | None = Field(
        None,
        description='Diz se o apartamento possui mobília ou não',
        examples=[FurnishedTypes.SEMI, FurnishedTypes.NAO]
    )

    mobilia: list[FurnitureTypes] | None = Field(
        None,
        description='Lugares que possuí mobília',
        examples=[
            [
                'Sofá', 
                'Armários nos quartos', 
                'Armários nos banheiros',
                'Cozinha planejada' 
            ]
        ]
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro.',
        examples=['2023-07-21T14:30:00Z']
    )
    
    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro.',
        examples=['2023-07-22T10:15:00Z']
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'imovel_id': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b', 
                    'metragem': 120.5, 
                    'quartos': 3, 
                    'suites': 1, 
                    'banheiros': 2, 
                    'garagens': 2, 
                    'andares': 1, 
                    'salas': 2, 
                    'esta_mobiliado': 'Semi mobiliado', 
                    'mobilia': 
                    [ 
                    'Sofá', 
                    'Armários nos quartos', 
                    'Armários nos banheiros',
                    'Cozinha planejada' 
                    ],
                    'criado_em': '2023-07-21T14:30:00Z',
                    'alterado_em': '2023-07-22T10:15:00Z' 
                }
            ] 
        } 
     }

    
class CreateApartmentRequest(BaseModel):
    imovel_id: UUID = Field(
        ...,
        description='ID do imóvel (tabela principal)',
        examples=['2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b']
    )

    metragem: float | None = Field(
        None,
        description='Metragem total do apartamento',
        examples=[65.20]
    )

    quartos: int | None = Field(
        None,
        description='Quantidade de quartos',
        examples=[2]
    )

    suites: int | None = Field(
        None,
        description='Quantidade de quartos que são suítes',
        examples=[1]
    )

    banheiros: int | None = Field(
        None,
        description='Quantidade de banheiros',
        examples=[2]
    )

    garagens: int | None = Field(
        None,
        description='Quantidade de vagas de garagens',
        examples=[2]
    )

    andares: int | None = Field(
        None,
        description='Quantidade de pavimentos',
        examples=[1]
    )

    salas: int | None = Field(
        None,
        description='Quantidade de salas',
        examples=[4]
    )

    esta_mobiliado: FurnishedTypes | None = Field(
        None,
        description='Diz se o apartamento possui mobília ou não',
        examples=[FurnishedTypes.SEMI, FurnishedTypes.NAO]
    )

    mobilia: list[FurnitureTypes] | None = Field(
        None,
        description='Lugares que possuí mobília',
        examples=[
            [
                'Sofá', 
                'Armários nos quartos', 
                'Armários nos banheiros',
                'Cozinha planejada' 
            ]
        ]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'imovel_id': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b', 
                    'metragem': 120.5, 
                    'quartos': 3, 
                    'suites': 1, 
                    'banheiros': 2, 
                    'garagens': 2, 
                    'andares': 1, 
                    'salas': 2, 
                    'esta_mobiliado': 'Semi mobiliado', 
                    'mobilia': 
                    [ 
                    'Sofá', 
                    'Armários nos quartos', 
                    'Armários nos banheiros',
                    'Cozinha planejada' 
                    ] 
                }
            ] 
        } 
     }

    
class EditApartmentRequest(BaseModel):
    metragem: float | None = Field(
        None,
        description='Metragem total do apartamento',
        examples=[65.20]
    )

    quartos: int | None = Field(
        None,
        description='Quantidade de quartos',
        examples=[2]
    )

    suites: int | None = Field(
        None,
        description='Quantidade de quartos que são suítes',
        examples=[1]
    )

    banheiros: int | None = Field(
        None,
        description='Quantidade de banheiros',
        examples=[2]
    )

    garagens: int | None = Field(
        None,
        description='Quantidade de vagas de garagens',
        examples=[2]
    )

    andares: int | None = Field(
        None,
        description='Quantidade de pavimentos',
        examples=[1]
    )

    salas: int | None = Field(
        None,
        description='Quantidade de salas',
        examples=[4]
    )

    esta_mobiliado: FurnishedTypes | None = Field(
        None,
        description='Diz se o apartamento possui mobília ou não',
        examples=[FurnishedTypes.SEMI, FurnishedTypes.NAO]
    )

    mobilia: list[FurnitureTypes] | None = Field(
        None,
        description='Lugares que possuí mobília',
        examples=[
            [
                'Sofá', 
                'Armários nos quartos', 
                'Armários nos banheiros',
                'Cozinha planejada' 
            ]
        ]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'metragem': 120.5, 
                    'quartos': 3, 
                    'suites': 1, 
                    'banheiros': 2, 
                    'garagens': 2, 
                    'andares': 1, 
                    'salas': 2, 
                    'esta_mobiliado': 'Semi mobiliado', 
                    'mobilia': 
                    [ 
                    'Sofá', 
                    'Armários nos quartos', 
                    'Armários nos banheiros',
                    'Cozinha planejada' 
                    ] 
                }
            ] 
        } 
     }


class LandResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='ID (UUIDv7) do terreno',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )

    imovel_id: UUID = Field(
        ...,
        description='ID do imóvel (tabela principal)',
        examples=['2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b']
    )

    area_total: float | None = Field(
        None,
        description='Área total do terreno',
        examples=[420.22]
    )

    medida_esquerda: float | None = Field(
        None,
        description='Medida do lado esquerdo do terreno',
        examples=[215.22]
    )

    medida_direita: float | None = Field(
        None,
        description='Medida do lado direito do terreno',
        examples=[100.16]
    )

    medida_frente: float | None = Field(
        None,
        description='Medida da frente do terreno',
        examples=[87.20]
    )

    medida_fundo: float | None = Field(
        None,
        description='Medida da fundo do terreno',
        examples=[93.80]
    )

    zoneamento: ZoningTypes | None = Field(
        None,
        description='Tipo de zoneamento do terreno',
        examples=['Residencial', 'Rural']
    )

    coeficiente: float | None = Field(
        None,
        description='Coeficiente do terreno',
        examples=[3.7]
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro.',
        examples=['2023-07-21T14:30:00Z']
    )
        
    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro.',
        examples=['2023-07-22T10:15:00Z']
    )
    

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'imovel_id': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b', 
                    'area_total': 420.22, 
                    'medida_esquerda': 30.0, 
                    'medida_direita': 30.0, 
                    'medida_frente': 14.0, 
                    'medida_fundo': 14.0, 
                    'zoneamento': 'Residencial', 
                    'coeficiente': 2.4,
                    'criado_em': '2023-07-21T14:30:00Z',
                    'alterado_em': '2023-07-22T10:15:00Z' 
                }, 
            ]
        } 
    }


class CreateLandRequest(BaseModel):
    imovel_id: UUID = Field(
        ...,
        description='ID do imóvel (tabela principal)',
        examples=['2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b']
    )

    area_total: float | None = Field(
        None,
        description='Área total do terreno',
        examples=[420.22]
    )

    medida_esquerda: float | None = Field(
        None,
        description='Medida do lado esquerdo do terreno',
        examples=[215.22]
    )

    medida_direita: float | None = Field(
        None,
        description='Medida do lado direito do terreno',
        examples=[100.16]
    )

    medida_frente: float | None = Field(
        None,
        description='Medida da frente do terreno',
        examples=[87.20]
    )

    medida_fundo: float | None = Field(
        None,
        description='Medida da fundo do terreno',
        examples=[93.80]
    )

    zoneamento: ZoningTypes | None = Field(
        None,
        description='Tipo de zoneamento do terreno',
        examples=['Residencial', 'Rural']
    )

    coeficiente: float | None = Field(
        None,
        description='Coeficiente do terreno',
        examples=[3.7]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'imovel_id': '2a1b3c4d-5e6f-4789-8a0b-1c2d3e4f5a6b', 
                    'area_total': 420.22, 
                    'medida_esquerda': 30.0, 
                    'medida_direita': 30.0, 
                    'medida_frente': 14.0, 
                    'medida_fundo': 14.0, 
                    'zoneamento': 'Residencial', 
                    'coeficiente': 2.4 
                }, 
            ]
        } 
    }


class EditLandRequest(BaseModel):
    area_total: float | None = Field(
        None,
        description='Área total do terreno',
        examples=[420.22]
    )

    medida_esquerda: float | None = Field(
        None,
        description='Medida do lado esquerdo do terreno',
        examples=[215.22]
    )

    medida_direita: float | None = Field(
        None,
        description='Medida do lado direito do terreno',
        examples=[100.16]
    )

    medida_frente: float | None = Field(
        None,
        description='Medida da frente do terreno',
        examples=[87.20]
    )

    medida_fundo: float | None = Field(
        None,
        description='Medida da fundo do terreno',
        examples=[93.80]
    )

    zoneamento: ZoningTypes | None = Field(
        None,
        description='Tipo de zoneamento do terreno',
        examples=['Residencial', 'Rural']
    )

    coeficiente: float | None = Field(
        None,
        description='Coeficiente do terreno',
        examples=[3.7]
    )

    model_config = { 
        'json_schema_extra': { 
            'examples': 
            [ 
                { 
                    'area_total': 420.22, 
                    'medida_esquerda': 30.0, 
                    'medida_direita': 30.0, 
                    'medida_frente': 14.0, 
                    'medida_fundo': 14.0, 
                    'zoneamento': 'Residencial', 
                    'coeficiente': 2.4 
                }, 
            ]
        } 
    }


class CompletePropertyResponse(BaseModel):
    id: UUID
    
    proprietario: UUID | None = None

    corretor: UUID | None = None

    codigo: str

    finalidade: FinalityTypes

    tipo: PropertyTypes

    em_condominio: bool

    condominio: UUID | None = None

    cep: str

    logradouro: str

    numero: int

    bairro: str

    uf: str

    cidade: str

    complemento: str | None = None

    valor: float | None = None

    valor_iptu: float | None = None

    valor_condominio: float | None = None

    criado_em: datetime

    alterado_em: datetime | None = None

    casa = HouseData | None = None

    apartamento = ApartmentData | None = None

    terreno = LandData | None = None


class HouseData(BaseModel):
    imovel_id: UUID
    
    metragem: float | None = None

    quartos: int | None = None

    suites: int | None = None

    banheiros: int | None = None

    garagens: int | None = None

    andares: int | None = None

    salas: int | None = None

    esta_mobiliado: FurnishedTypes | None = None

    mobilia: list[FurnitureTypes] | None = None


class ApartmentData(BaseModel):
    imovel_id: UUID
    
    metragem: float | None = None

    quartos: int | None = None

    suites: int | None = None

    banheiros: int | None = None

    garagens: int | None = None

    andares: int | None = None

    salas: int | None = None

    esta_mobiliado: FurnishedTypes | None = None

    mobilia: list[FurnitureTypes] | None = None


class LandData(BaseModel):
    imovel_id: UUID 
    
    area_total: float | None = None

    medida_esquerda: float | None = None

    medida_direita: float | None = None

    medida_frente: float | None = None

    medida_fundo: float | None = None

    zoneamento: ZoningTypes | None = None

    coeficiente: float | None = None