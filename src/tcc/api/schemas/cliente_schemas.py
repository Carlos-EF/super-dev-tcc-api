from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from tcc.dominio.enums.tipo_cliente import TipoCliente
from tcc.dominio.enums.como_encontrou import ComoEncontrou
from tcc.dominio.enums.status import Status


class CriarClienteRequest(BaseModel):
    status: str = Field(
        ...,
        default=Status.ATIVO,
        description='Status do cliente dentro do sistema.',
        examples=['ATIVO']
    )


    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    codigo: int = Field(
        ...,
        min_length=5,
        max_length=10,
        description='Código de referência do cliente.',
        examples=['007512', '113123']
    )

    celular: int = Field(
        ...,
        max_length=11,
        description='Número de celular do cliente.',
        examples=['47912345679']
    )

    email: str = Field(
        ...,
        max_length=40,
        description='E-Mail do cliente.',
        examples=['fagner99@gmail.com']
    )

    como_encontrou: str = Field(
        ...,
        default=ComoEncontrou.CONTATO_DIRETO,
        description='Como o cliente entrou em contato.',
        examples=['Contato Direto']
    )

    tipo: str = Field(
        ...,
        max_length=12,
        default=TipoCliente.INTERESSADO,
        description='Tipo do cliente.',
        examples=['Interessado']
    )

    model_config= {
        'json_schema_extra': {
            'examples': {
                'status': 'ATIVO',
                'nome': 'Fagner Silva dos Santos',
                'codigo': '113123',
                'celular': '47912345679',
                'email': 'fagner99@gmail.com',
                'como_encontrou': 'Contato Direto',
                'tipo': 'Interessado',
            }
        }
    }


class AlterarClienteRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    celular: int = Field(
        ...,
        max_length=11,
        description='Número de celular do cliente.',
        examples=['47912345679']
    )

    email: str = Field(
        ...,
        max_length=40,
        description='E-Mail do cliente.',
        examples=['fagner99@gmail.com']
    )

    tipo: str = Field(
        ...,
        max_length=12,
        default=TipoCliente.INTERESSADO,
        description='Tipo do cliente.',
        examples=['Interessado']
    )

    model_config= {
        'json_schema_extra': {
            'examples': {
                'nome': 'Fagner Silva dos Santos',
                'celular': '47912345679',
                'email': 'fagner99@gmail.com',
                'tipo': 'Interessado',
            }
        }
    }


class ClienteResponse(BaseModel):
    id: UUID = Field(
        ...,
        description=['Identificador (UUID v7) único do cliente.'],
        examples=['019d0604-25a5-74c4-a2cb-eeaedaa5bbc1']
    )

    status: str = Field(
        ...,
        description='Status do cliente dentro do sistema.',
        examples=['ATIVO']
    )


    nome: str = Field(
        ...,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    codigo: int = Field(
        ...,
        description='Código de referência do cliente.',
        examples=['113123']
    )

    celular: int = Field(
        ...,
        description='Número de celular do cliente.',
        examples=['47912345679']
    )

    email: str = Field(
        ...,
        description='E-Mail do cliente.',
        examples=['fagner99@gmail.com']
    )

    como_encontrou: str = Field(
        ...,
        description='Como o cliente entrou em contato.',
        examples=['Contato Direto']
    )

    tipo: str = Field(
        ...,
        description='Tipo do cliente.',
        examples=['Interessado']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do cliente.',
        examples=['2026-03-19T10:30:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última modificação do registro do cliente.',
        examples=['2026-03-19T12:00:43']
    )

    model_config= {
        'json_schema_extra': {
            'examples': {
                'id': '019d0604-25a5-74c4-a2cb-eeaedaa5bbc1',
                'status': 'ATIVO',
                'nome': 'Fagner Silva dos Santos',
                'codigo': '113123',
                'celular': '47912345679',
                'email': 'fagner99@gmail.com',
                'como_encontrou': 'Contato Direto',
                'tipo': 'Interessado',
                'criado_em': '2026-03-19T10:30:00',
                'alterado_em': None,
            }
        }
    }