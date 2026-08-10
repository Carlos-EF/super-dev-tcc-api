from enum import Enum


class FurnishedTypes(Enum):
    SIM = 'Sim'
    NAO = 'Não'
    SEMI = 'Semimobiliado'


class FurnitureTypes(str, Enum): 
    COZINHA_PLANEJADA = 'Cozinha planejada' 
    ARMARIOS_QUARTOS = 'Armários nos quartos' 
    ARMARIOS_BANHEIROS = 'Armários nos banheiros' 
    AR_CONDICIONADO = 'Ar-condicionado' 
    ELETRODOMESTICOS = 'Eletrodomésticos' 
    SOFA = 'Sofá' 
    MESA_JANTAR = 'Mesa de jantar' 
    CAMAS = 'Camas' 
    CORTINAS_PERSIANAS = 'Cortinas e persianas'