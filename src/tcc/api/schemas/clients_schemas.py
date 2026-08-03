from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from src.tcc.infrastructure.models.enums.clients_types import ClientType
from src.tcc.infrastructure.models.enums.contact_types import ContactType
from src.tcc.infrastructure.models.enums.finality_types import ClientFinalityTypes
from src.tcc.infrastructure.models.enums.property_types import PropertyTypes


class ClientResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='ID (UUIDv7) do cliente',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )

    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do cliente',
        examples=['João da Silva']
    )

    codigo: str = Field(
        ...,
        min_length=4,
        max_length=4,
        description='Código do cliente',
        examples=['1234', 'CL01']
    )

    numero: str = Field(
        ...,
        min_length=15,
        max_length=15,
        description='Número de telefone do cliente',
        examples=['(47) 91234-5678', '(47) 98765-4321']
    )

    email: str = Field(
        ...,
        min_length=5,
        max_length=60,
        description='Email do cliente',
        examples=['joao@exemplo.com', 'maria@exemplo.com']
    )

    tipo: ClientType = Field(
        ...,
        max_length=11,
        description='Tipo do cliente',
        examples=['interessado', 'cliente']
    )

    como_encontrou: ContactType | None = Field(
        None,
        max_length=18,
        description='Como o cliente encontrou a empresa',
        examples=['Indicação', 'Whatsapp', 'Instagram']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do cliente.',
        examples=['2023-07-21T14:30:00Z']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro do cliente.',
        examples=['2023-07-22T10:15:00Z']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'nome': 'João da Silva',
                    'codigo': '1234',
                    'numero': '(47) 91234-5678',
                    'email': 'joao@exemplo.com',
                    'tipo': 'interessado',
                    'como_encontrou': 'Indicação',
                    'criado_em': '2023-07-21T14:30:00Z',
                    'alterado_em': '2023-07-22T10:15:00Z'
                }
            ]
        }
    }


class CreateClientRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do cliente',
        examples=['João da Silva']
    )

    codigo: str = Field(
        ...,
        min_length=4,
        max_length=4,
        description='Código do cliente',
        examples=['1234', 'CL01']
    )

    numero: str = Field(
        ...,
        min_length=15,
        max_length=15,
        description='Número de telefone do cliente',
        examples=['(47) 91234-5678', '(47) 98765-4321']
    )

    email: str = Field(
        ...,
        min_length=5,
        max_length=60,
        description='Email do cliente',
        examples=['joao@exemplo.com', 'maria@exemplo.com']
    )

    tipo: ClientType = Field(
        ...,
        max_length=11,
        description='Tipo do cliente',
        examples=['interessado', 'cliente']
    )

    como_encontrou: ContactType | None = Field(
        None,
        max_length=18,
        description='Como o cliente encontrou a empresa',
        examples=['Indicação', 'Whatsapp', 'Instagram']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'João da Silva',
                    'codigo': '1234',
                    'numero': '(47) 91234-5678',
                    'email': 'joao@exemplo.com',
                    'tipo': 'interessado',
                    'como_encontrou': 'Indicação'
                }
            ]
        }
    }


class EditClientRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do cliente',
        examples=['João da Silva']
    )

    numero: str = Field(
        ...,
        min_length=15,
        max_length=15,
        description='Número de telefone do cliente',
        examples=['(47) 91234-5678', '(47) 98765-4321']
    )

    email: str = Field(
        ...,
        min_length=5,
        max_length=60,
        description='Email do cliente',
        examples=['joao@exemplo.com', 'maria@exemplo.com']
    )


    como_encontrou: ContactType | None = Field(
        None,
        max_length=18,
        description='Como o cliente encontrou a empresa',
        examples=['Indicação', 'Whatsapp', 'Instagram']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'João da Silva',
                    'numero': '(47) 91234-5678',
                    'email': 'joao@exemplo.com',
                    'como_encontrou': 'Indicação'
                }
            ]
        }
    }


class InterestedClientResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='ID (UUIDv7) do cliente interessado',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )

    cliente_id: UUID = Field(
        ...,
        description='ID (UUIDv7) do cliente (tabela principal) interessado',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )

    procura: PropertyTypes | None = Field(
        None,
        description='Tipo de imóvel que o cliente interessado está procurando',
        examples=['Casa', 'Apartamento', 'Terreno']
    )

    finalidade: ClientFinalityTypes | None = Field(
        None,
        description='Finalidade do cliente interessado',
        examples=['Alugar', 'Comprar']
    )

    preferencia: str | None = Field(
        None,
        min_length=3,
        max_length=60,
        description='Preferência de bairro do cliente interessado',
        examples=['Centro', 'Bairro Novo', 'Jardim das Flores']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do cliente interessado.',
        examples=['2023-07-21T14:30:00Z']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro do cliente interessado.',
        examples=['2023-07-22T10:15:00Z']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'cliente_id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'procura': 'Casa',
                    'finalidade': 'Comprar',
                    'preferencia': 'Centro',
                    'criado_em': '2023-07-21T14:30:00Z',
                    'alterado_em': '2023-07-22T10:15:00Z'
                }
            ]
        }
    }


class CreateInterestedClientRequest(BaseModel):
    cliente_id: UUID = Field(
        ...,
        description='ID (UUIDv7) do cliente (tabela principal) interessado',
        examples=['f47ac10b-58cc-4372-a567-0e02b2c3d479']
    )

    procura: PropertyTypes | None = Field(
        None,
        description='Tipo de imóvel que o cliente interessado está procurando',
        examples=['Casa', 'Apartamento', 'Terreno']
    )

    finalidade: ClientFinalityTypes | None = Field(
        None,
        description='Finalidade do cliente interessado',
        examples=['Alugar', 'Comprar']
    )

    preferencia: str | None = Field(
        None,
        min_length=3,
        max_length=60,
        description='Preferência de bairro do cliente interessado',
        examples=['Centro', 'Bairro Novo', 'Jardim das Flores']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'cliente_id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                    'procura': 'Casa',
                    'finalidade': 'Comprar',
                    'preferencia': 'Centro'
                }
            ]
        }
    }


class EditInterestedClientRequest(BaseModel):
    procura: PropertyTypes | None = Field(
        None,
        description='Tipo de imóvel que o cliente interessado está procurando',
        examples=['Casa', 'Apartamento', 'Terreno']
    )

    finalidade: ClientFinalityTypes | None = Field(
        None,
        description='Finalidade do cliente interessado',
        examples=['Alugar', 'Comprar']
    )

    preferencia: str | None = Field(
        None,
        min_length=3,
        max_length=60,
        description='Preferência de bairro do cliente interessado',
        examples=['Centro', 'Bairro Novo', 'Jardim das Flores']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'procura': 'Casa',
                    'finalidade': 'Comprar',
                    'preferencia': 'Centro'
                }
            ]
        }
    }


class PaginatedClientResponse(BaseModel):
    clientes: list[ClientResponse]

    pagina: int

    por_pagina: int

    total: int
    
    total_paginas: int