from enum import Enum


class ClientType(str, Enum):
    INTERESSADO = 'Interessado'
    PROPRIETARIO = 'Proprietário'
    LOCATARIO = 'Locatário'