from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class CreateCondominiumRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do condomínio',
        examples=['Atlanta']
    )

    cep: str = Field(
        ...,
        min_length=9,
        max_length=9,
        description='CEP do condomínio',
        examples=['89040-001']
    )

    logradouro: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Logradouro do condomínio',
        examples=['Rua dos Caçadores']
    )

    numero: int = Field(
        ...,
        description='Número do condomínio',
        examples=[204]
    )

    bairro: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Bairro do condomínio',
        examples=['Velha']
    )

    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description='UF onde se localiza o condomínio',
        examples=['SC']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Cidade do condomínio',
        examples=['Blumenau']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'Atlanta',
                    'cep': '89040-001',
                    'logradouro': 'Rua dos Caçadores',
                    'numero': 204,
                    'bairro': 'Velha',
                    'estado': 'SC',
                    'cidade': 'Blumenau'
                }
            ]
        }
    }


class EditCondominiumRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do condomínio',
        examples=['Atlanta']
    )

    cep: str = Field(
        ...,
        min_length=9,
        max_length=9,
        description='CEP do condomínio',
        examples=['89040-001']
    )

    logradouro: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Logradouro do condomínio',
        examples=['Rua dos Caçadores']
    )

    numero: int = Field(
        ...,
        description='Número do condomínio',
        examples=[204]
    )

    bairro: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Bairro do condomínio',
        examples=['Velha']
    )

    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description='UF onde se localiza o condomínio',
        examples=['SC']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Cidade do condomínio',
        examples=['Blumenau']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'Atlanta',
                    'cep': '89040-001',
                    'logradouro': 'Rua dos Caçadores',
                    'numero': 204,
                    'bairro': 'Velha',
                    'estado': 'SC',
                    'cidade': 'Blumenau'
                }
            ]
        }  
    }


class CondominiumResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Identificador único (UUID v7) do condomínio cadastrado',
        examples=['019eaeb2-5ad8-7d22-abca-1b32e99b734a']
    )


    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do condomínio',
        examples=['Atlanta']
    )

    cep: str = Field(
        ...,
        min_length=9,
        max_length=9,
        description='CEP do condomínio',
        examples=['89040-001']
    )

    logradouro: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Logradouro do condomínio',
        examples=['Rua dos Caçadores']
    )

    numero: int = Field(
        ...,
        description='Número do condomínio',
        examples=[204]
    )

    bairro: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Bairro do condomínio',
        examples=['Velha']
    )

    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description='UF onde se localiza o condomínio',
        examples=['SC']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Cidade do condomínio',
        examples=['Blumenau']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do condomínio.',
        examples=['2026-03-26T08:35:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro do condomínio.',
        examples=[None]
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'id': '019eaeb2-5ad8-7d22-abca-1b32e99b734a',
                    'nome': 'Atlanta',
                    'cep': '89040-001',
                    'logradouro': 'Rua dos Caçadores',
                    'numero': 204,
                    'bairro': 'Velha',
                    'estado': 'SC',
                    'cidade': 'Blumenau',
                    'criado_em': '2026-03-26T08:35:00',
                    'alterado_em': None
                }
            ]
        }
    }


class PaginatedCondominiumResponse(BaseModel):
    condominios: list[CondominiumResponse]

    pagina: int

    por_pagina: int

    total: int
    
    total_paginas: int


class CitiesResponse(BaseModel):
    cidades: list[str]