from enum import Enum


class ClientFinalityTypes(str, Enum):
    ALUGAR = 'alugar'
    COMPRAR = 'comprar'


class FinalityTypes(str, Enum):
    VENDA = 'Venda'
    LOCAÇÃO = 'Locação'