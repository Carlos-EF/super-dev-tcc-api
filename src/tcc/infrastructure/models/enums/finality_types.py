from enum import Enum


class ClientFinalityTypes(str, Enum):
    ALUGAR = 'Alugar'
    COMPRAR = 'Comprar'


class FinalityTypes(str, Enum):
    VENDA = 'Venda'
    LOCAÇÃO = 'Locação'