from uuid import UUID
from pydantic import BaseModel, Field
from tcc.dominio.enums.status import Status
from datetime import datetime


class CriarCorretorRequest(BaseModel):
    status: str = Field(
        ...,
        default=Status.ATIVO,
        description='Status do corretor dentro do sistema.',
        examples=['ATIVO']
    )

    nome_completo: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome completo do corretor.',
        examples=['Maria Souza dos Santos']
    )

    codigo: str = Field(
        ...,
        min_length=5,
        max_length=10,
        description='Código de referência do corretor.',
        examples=['100302', '1111032']
    )

    celular: str = Field(
        ...,
        min_length=11,
        max_length=11,
        description='Número de celular do corretor.',
        examples=['47901234567']
    )

    email: str = Field(
        ...,
        max_length=50,
        description='E-mail do corretor.',
        examples=['maria.santos44@outlook.com']
    )

    creci: str = Field(
        ...,
        max_length=5,
        description='CRECI ativo do corretor.',
        examples=['34215']
    )

    data_nascimento: str | None = Field(
        description='Data de nascimento do corretor.',
        examples=['1999-02-10']
    )

    rg: str | None = Field(
        min_length=7,
        max_length=7,
        description='RG do corretor.',
        examples=['9543265']
    )

    cpf: str | None = Field(
        min_length=11,
        max_length=11,
        description='CPF do corretor.',
        examples=['78986532114']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'status': 'ATIVO',
                'nome_completo': 'Maria Souza dos Santos',
                'codigo': '1111032',
                'celular': '47901234567',
                'email': 'maria.santos44@outlook.com',
                'data_nascimento': '1999-02-10',
                'rg': '9543265',
                'cpf': '78986532114',
            }
        }
    }