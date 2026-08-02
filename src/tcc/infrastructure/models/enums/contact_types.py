from enum import Enum


class ContactType(str, Enum):
    WHATSAPP = 'WhatsApp'
    INDICACAO = 'Indicação'
    INSTAGRAM = 'Instagram'
    PORTAL_IMOBILIARIO = 'Portal imobiliário'
    PLACA_NO_IMOVEL = 'Placa no imóvel'
