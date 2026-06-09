from uuid import UUID
from pydantic import BaseModel, Field


class CriarCondominioRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Nome do condomínio',
        examples=['Atlanta']
    )

    cep: str = Field(
        ...,
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

    estado: str = Field(
        ...,
        description='Estado onde se localiza o condomínio',
        examples=['Santa Catarina']
    )

    cidade: str = Field(
        ...,
        min_length=3,
        max_length=40,
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
                    'estado': 'Santa Catarina',
                    'cidade': 'Blumenau'
                }
            ]
        }
    }