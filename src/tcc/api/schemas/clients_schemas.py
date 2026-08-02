from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from src.tcc.infrastructure.models.enums.clients_types import ClientType
from src.tcc.infrastructure.models.enums.contact_types import ContactType


class CreateClientRequest(BaseModel):
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