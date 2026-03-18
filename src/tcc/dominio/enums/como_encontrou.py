from enum import Enum


class ComoEncontrou(str, Enum):
    WHATSAPP = 'WhatsApp'
    ANUNCIO = 'Anúncio'
    CONTATO_DIRETO = 'Contato Direto'
    INSTAGRAM = 'Instagram'