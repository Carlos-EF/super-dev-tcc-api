from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class CreateBrokerRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do corretor',
        examples=['João Batista']
    )

    codigo: str = Field(
        ...,
        min_length=4,
        max_length=4,
        description='Codígo do corretor',
        examples=['0001']
    )

    creci: str = Field(
        ...,
        min_length=7,
        max_length=7,
        description='Creci do corretor',
        examples=['12.345F']
    )

    numero: str = Field(
        ...,
        min_length=15,
        max_length=15,
        description='Número de celular do corretor',
        examples=['(47) 91234-5678']
    )

    email: str = Field(
        ...,
        max_length=60,
        description='E-mail do corretor',
        examples=['joaobatis@corretor.com']
    )

    data_nascimento: str | None = Field(
        None,
        min_length=10,
        max_length=10,
        description='Data de nascimento do corretor',
        examples=['07/01/1992']
    )

    rg: str | None = Field(
        None,
        min_length=9,
        max_length=9,
        description='RG do corretor',
        examples=['1.234.567']
    )

    cpf: str | None = Field(
        None,
        min_length=14,
        max_length=14,
        description='CPF do corretor',
        examples=['123.456.789-00']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'João Batista',
                    'codigo': '0001',
                    'creci': '12.345F',
                    'celular': '(47) 91234-5678',
                    'email': 'joaobatis@corretor.com',
                    'data_nascimento': '07/01/1992',
                    'rg': '1.234.567',
                    'cpf': '123.456.789-00'
                }
            ]
        }
    }


class EditBrokerRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do corretor',
        examples=['João Batista']
    )

    creci: str = Field(
        ...,
        min_length=7,
        max_length=7,
        description='Creci do corretor',
        examples=['12.345F']
    )

    numero: str = Field(
        ...,
        min_length=15,
        max_length=15,
        description='Número de celular do corretor',
        examples=['(47) 91234-5678']
    )

    email: str = Field(
        ...,
        max_length=60,
        description='E-mail do corretor',
        examples=['joaobatis@corretor.com']
    )

    data_nascimento: str | None = Field(
        None,
        min_length=10,
        max_length=10,
        description='Data de nascimento do corretor',
        examples=['07/01/1992']
    )

    rg: str | None = Field(
        None,
        min_length=9,
        max_length=9,
        description='RG do corretor',
        examples=['1.234.567']
    )

    cpf: str | None = Field(
        None,
        min_length=14,
        max_length=14,
        description='CPF do corretor',
        examples=['123.456.789-00']
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'João Batista',
                    'creci': '12.345F',
                    'celular': '(47) 91234-5678',
                    'email': 'joaobatis@corretor.com',
                    'data_nascimento': '07/01/1992',
                    'rg': '1.234.567',
                    'cpf': '123.456.789-00'
                }
            ]
        }
    }


class BrokerResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Identificador único (UUID v7) do corretor cadastrado',
        examples=['019eaeb2-5ad8-7d22-abca-1b32e99b734a']
    )

    nome: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome do corretor',
        examples=['João Batista']
    )

    codigo: str = Field(
        ...,
        min_length=4,
        max_length=4,
        description='Codígo do corretor',
        examples=['0001']
    )

    creci: str = Field(
        ...,
        min_length=7,
        max_length=7,
        description='Creci do corretor',
        examples=['12.345F']
    )

    numero: str = Field(
        ...,
        min_length=15,
        max_length=15,
        description='Número de celular do corretor',
        examples=['(47) 91234-5678']
    )

    email: str = Field(
        ...,
        max_length=60,
        description='E-mail do corretor',
        examples=['joaobatis@corretor.com']
    )

    data_nascimento: str | None = Field(
        None,
        min_length=10,
        max_length=10,
        description='Data de nascimento do corretor',
        examples=['07/01/1992']
    )

    rg: str | None = Field(
        None,
        min_length=9,
        max_length=9,
        description='RG do corretor',
        examples=['1.234.567']
    )

    cpf: str | None = Field(
        None,
        min_length=14,
        max_length=14,
        description='CPF do corretor',
        examples=['123.456.789-00']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do corretor.',
        examples=['2026-03-26T08:35:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro do corretor.',
        examples=[None]
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'id': '019eaeb2-5ad8-7d22-abca-1b32e99b734a',
                    'nome': 'João Batista',
                    'codigo': '0001',
                    'creci': '12.345F',
                    'celular': '(47) 91234-5678',
                    'email': 'joaobatis@corretor.com',
                    'data_nascimento': '07/01/1992',
                    'rg': '1.234.567',
                    'cpf': '123.456.789-00',
                    'criado_em': '2026-03-26T08:35:00',
                    'alterado_em': None
                }
            ]
        }
    }