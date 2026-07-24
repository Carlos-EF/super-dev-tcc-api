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