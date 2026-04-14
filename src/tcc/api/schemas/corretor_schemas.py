from uuid import UUID
from pydantic import BaseModel, Field
from tcc.dominio.enums.status import Status
from tcc.dominio.enums.tipo_pessoa import TipoPessoa
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
        examples=['(47) 90123-4567']
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
        examples=['34.215F']
    )

    data_nascimento: str | None = Field(
        None,
        description='Data de nascimento do corretor.',
        examples=['1999-02-10']
    )

    rg: str | None = Field(
        None,
        min_length=7,
        max_length=7,
        description='RG do corretor.',
        examples=['9.543.265']
    )

    cpf: str | None = Field(
        None,
        min_length=11,
        max_length=11,
        description='CPF do corretor.',
        examples=['789.865.321-14']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'status': 'ATIVO',
                'nome_completo': 'Maria Souza dos Santos',
                'codigo': '1111032',
                'creci': '34.215F',
                'celular': '(47) 90123-4567',
                'email': 'maria.santos44@outlook.com',
                'data_nascimento': '1999-02-10',
                'rg': '9.543.265',
                'cpf': '789.865.321-14',
            }
        }
    }


class AlterarCorretorRequest(BaseModel):
    nome_completo: str = Field(
        ...,
        min_length=3,
        max_length=60,
        description='Nome completo do corretor.',
        examples=['Maria Souza dos Santos']
    )

    celular: str = Field(
        ...,
        min_length=11,
        max_length=11,
        description='Número de celular do corretor.',
        examples=['(47) 90123-4567']
    )

    email: str = Field(
        ...,
        max_length=50,
        description='E-mail do corretor.',
        examples=['maria.santos44@outlook.com']
    )

    data_nascimento: str | None = Field(
        None,
        description='Data de nascimento do corretor.',
        examples=['1999-02-10']
    )

    rg: str | None = Field(
        None,
        min_length=7,
        max_length=7,
        description='RG do corretor.',
        examples=['9.543.265']
    )

    cpf: str | None = Field(
        None,
        min_length=11,
        max_length=11,
        description='CPF do corretor.',
        examples=['789.865.321-14']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'nome_completo': 'Maria Souza dos Santos',
                'celular': '(47) 90123-4567',
                'email': 'maria.santos44@outlook.com',
                'data_nascimento': '1999-02-10',
                'rg': '9543265',
                'cpf': '789.865.321-14',
            }
        }
    }


class CorretorResponse(BaseModel):
    id : UUID = Field(
        ...,
        description='Indentificador único (UUID v7) do corretor',
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    tipo : str = Field(
        ...,
        default=TipoPessoa.CORRETOR,
        description='Tipo de pessoa dentro do sistema.',
        examples=['CORRETOR']
    )
    
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
        examples=['(47) 90123-4567']
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
        examples=['34.215F']
    )

    data_nascimento: str | None = Field(
        None,
        description='Data de nascimento do corretor.',
        examples=['1999-02-10']
    )

    rg: str | None = Field(
        None,
        min_length=7,
        max_length=7,
        description='RG do corretor.',
        examples=['9.543.265']
    )

    cpf: str | None = Field(
        None,
        min_length=11,
        max_length=11,
        description='CPF do corretor.',
        examples=['789.865.321-14']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do corretor.',
        examples=['2026-03-26T08:35:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última modificação do registro do corretor.',
        examples=['']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'status': 'ATIVO',
                'tipo': 'CORRETOR',
                'nome_completo': 'Maria Souza dos Santos',
                'codigo': '1111032',
                'celular': '(47) 90123-4567',
                'email': 'maria.santos44@outlook.com',
                'creci': '34.215F',
                'data_nascimento': '1999-02-10',
                'rg': '9.543.265',
                'cpf': '789.865.321-14',
                'criado_em': '2026-03-26T08:35:00',
                'alterado_em': None
            }
        }
    }
