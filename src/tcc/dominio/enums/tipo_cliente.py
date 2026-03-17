from enum import Enum


class TipoCliente(str, Enum):
    INTERESSADO = 'Interessado'
    PROPRIETARIO = 'Proprietário'
    LOCATARIO = 'Locatário'