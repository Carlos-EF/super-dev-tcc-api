from enum import Enum


class TipoPessoa(str, Enum):
    INTERESSADO = 'Interessado'
    PROPRIETARIO = 'Proprietário'
    LOCATARIO = 'Locatário'
    CORRETOR = 'Corretor'