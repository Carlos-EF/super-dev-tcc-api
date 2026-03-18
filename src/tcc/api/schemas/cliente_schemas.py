from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from tcc.dominio.enums.tipo_cliente import TipoCliente


class ClienteCriarRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    codigo: str | int = Field(
        ...,
        min_length=5,
        max_length=10,
        description='Código de referência do cliente.',
        examples=['007512', 'ASD3123']
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

    como_encontrou: str = Field()

    tipo: str = Field(
        default=TipoCliente.INTERESSADO,
        description='Tipo do cliente.',
        examples=['Interessado']
    )