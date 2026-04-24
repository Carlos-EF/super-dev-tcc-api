from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from src.tcc.dominio.enums.tipo_pessoa import TipoPessoa
from tcc.dominio.enums.como_encontrou import ComoEncontrou
from tcc.dominio.enums.status import Status


class CriarClienteRequest(BaseModel):
    status: str = Field(
        ...,
        default=Status.ATIVO,
        description='Status do cliente dentro do sistema.',
        examples=['ATIVO']
    )


    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    codigo: str = Field(
        ...,
        min_length=5,
        max_length=10,
        description='Código de referência do cliente.',
        examples=['007512', '113123']
    )

    celular: str = Field(
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

    como_encontrou: str = Field(
        ...,
        default=ComoEncontrou.CONTATO_DIRETO,
        description='Como o cliente entrou em contato.',
        examples=['Contato Direto']
    )

    tipo: str = Field(
        ...,
        max_length=12,
        default=TipoPessoa.INTERESSADO,
        description='Tipo do cliente.',
        examples=['Interessado']
    )

    model_config= {
        'json_schema_extra': {
            'examples': {
                'status': 'ATIVO',
                'nome': 'Fagner Silva dos Santos',
                'codigo': '113123',
                'celular': '47912345679',
                'email': 'fagner99@gmail.com',
                'como_encontrou': 'Contato Direto',
                'tipo': 'Interessado',
            }
        }
    }


class AlterarClienteRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    celular: str = Field(
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

    tipo: str = Field(
        ...,
        max_length=12,
        default=TipoPessoa.INTERESSADO,
        description='Tipo do cliente.',
        examples=['Interessado']
    )

    model_config= {
        'json_schema_extra': {
            'examples': {
                'nome': 'Fagner Silva dos Santos',
                'celular': '47912345679',
                'email': 'fagner99@gmail.com',
                'tipo': 'Interessado',
            }
        }
    }


class ClienteResponse(BaseModel):
    id: UUID = Field(
        ...,
        description=['Identificador (UUID v7) único do cliente.'],
        examples=['019d0604-25a5-74c4-a2cb-eeaedaa5bbc1']
    )

    status: str = Field(
        ...,
        description='Status do cliente dentro do sistema.',
        examples=['ATIVO']
    )


    nome: str = Field(
        ...,
        description='Nome completo do cliente.',
        examples=['Fagner Silva dos Santos']
    )

    codigo: str = Field(
        ...,
        description='Código de referência do cliente.',
        examples=['113123']
    )

    celular: str = Field(
        ...,
        description='Número de celular do cliente.',
        examples=['47912345679']
    )

    email: str = Field(
        ...,
        description='E-Mail do cliente.',
        examples=['fagner99@gmail.com']
    )

    como_encontrou: str = Field(
        ...,
        description='Como o cliente entrou em contato.',
        examples=['Contato Direto']
    )

    tipo: str = Field(
        ...,
        description='Tipo do cliente.',
        examples=['Interessado']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do cliente.',
        examples=['2026-03-19T10:30:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última modificação do registro do cliente.',
        examples=['2026-03-19T12:00:43']
    )

    model_config= {
        'json_schema_extra': {
            'examples': {
                'id': '019d0604-25a5-74c4-a2cb-eeaedaa5bbc1',
                'status': 'ATIVO',
                'nome': 'Fagner Silva dos Santos',
                'codigo': '113123',
                'celular': '47912345679',
                'email': 'fagner99@gmail.com',
                'como_encontrou': 'Contato Direto',
                'tipo': 'Interessado',
                'criado_em': '2026-03-19T10:30:00',
                'alterado_em': None,
            }
        }
    }


class CriarClienteInteressadoRequest(BaseModel):
    id: UUID = Field(
    ...,
    description=['Identificador (UUID v7) único do cliente na tabela de intessado.'],
    examples=['019db9eb-db4c-7246-9025-0e0b7da207d7']
    )
    
    id_cliente: UUID = Field(
        ...,
        description=['Identificador (UUID v7) único do cliente.'],
        examples=['019d0604-25a5-74c4-a2cb-eeaedaa5bbc1']
    )

    tipo_imovel: str = Field(
        ...,
        description=['Tipo de imóvel que o cliente está procurando.'],
        examples=['Casa']
    )

    orcamento: int = Field(
        ...,
        description=['Orçamento do cliente.'],
        examples=[500000]
    )

    orcamento_minimo: int = Field(
        description=['Orçamento mínimo do cliente'],
        examples=[350000]
    )

    orcamento_maximo: int = Field(
        description=['Orçamento máximo do cliente'],
        examples=[650000]
    )

    quantidade_quartos: int = Field(
        description=['Quantidade desejada de quartos do cliente.'],
        examples=[3]
    )

    quantidade_suites: int = Field(
        description=['Quantidade desejada de suítes do cliente.'],
        examples=[1]
    )

    quantidade_banheiros: int = Field(
        description=['Quantidade desejada de banheiros do cliente.'],
        examples=[2]
    )

    quantidade_vagas_garagem: int = Field(
        description=['Quantidade desejada de vagas de garagem do cliente.'],
        examples=[2]
    )

    quantidade_andares: int = Field(
        description=['Quantidade desejada de andares do cliente.'],
        examples=[1]
    )

    quantidade_salas: int = Field(
        description=['Quantidade desejada de salas do cliente.'],
        examples=[1]
    )

    model_config = {
    'json_schema_extra': {
        'examples': {
            'id': '019db9eb-db4c-7246-9025-0e0b7da207d7',
            'id_cliente': '019d0604-25a5-74c4-a2cb-eeaedaa5bbc1',
            'tipo_imovel': 'Casa',
            'orcamento': 500000,
            'orcamento_minimo': 350000,
            'orcamento_maximo': 650000,
            'quantidade_quartos': 3,
            'quantidade_suites': 1,
            'quantidade_banheiros': 2,
            'quantidade_vagas': 2,
            'quantidade_andares': 1,
            'quantidade_salas': 1
        }
    }
}
    

class EditarClienteInteressadoRequest(BaseModel):
    tipo_imovel: str = Field(
        ...,
        description=['Tipo de imóvel que o cliente está procurando.'],
        examples=['Casa']
    )

    orcamento: int = Field(
        ...,
        description=['Orçamento do cliente.'],
        examples=[500000]
    )

    orcamento_minimo: int = Field(
        description=['Orçamento mínimo do cliente'],
        examples=[350000]
    )

    orcamento_maximo: int = Field(
        description=['Orçamento máximo do cliente'],
        examples=[650000]
    )

    quantidade_quartos: int = Field(
        description=['Quantidade desejada de quartos do cliente.'],
        examples=[3]
    )

    quantidade_suites: int = Field(
        description=['Quantidade desejada de suítes do cliente.'],
        examples=[1]
    )

    quantidade_banheiros: int = Field(
        description=['Quantidade desejada de banheiros do cliente.'],
        examples=[2]
    )

    quantidade_vagas_garagem: int = Field(
        description=['Quantidade desejada de vagas de garagem do cliente.'],
        examples=[2]
    )

    quantidade_andares: int = Field(
        description=['Quantidade desejada de andares do cliente.'],
        examples=[1]
    )

    quantidade_salas: int = Field(
        description=['Quantidade desejada de salas do cliente.'],
        examples=[1]
    )

    model_config = {
    'json_schema_extra': {
        'examples': {
            'tipo_imovel': 'Casa',
            'orcamento': 500000,
            'orcamento_minimo': 350000,
            'orcamento_maximo': 650000,
            'quantidade_quartos': 3,
            'quantidade_suites': 1,
            'quantidade_banheiros': 2,
            'quantidade_vagas': 2,
            'quantidade_andares': 1,
            'quantidade_salas': 1
        }
    }
}
    

class ClienteInteressadoResponse(BaseModel):
    id: UUID = Field(
    ...,
    description=['Identificador (UUID v7) único do cliente na tabela de intessado.'],
    examples=['019db9eb-db4c-7246-9025-0e0b7da207d7']
    )
    
    id_cliente: UUID = Field(
        ...,
        description=['Identificador (UUID v7) único do cliente.'],
        examples=['019d0604-25a5-74c4-a2cb-eeaedaa5bbc1']
    )

    tipo_imovel: str = Field(
        ...,
        description=['Tipo de imóvel que o cliente está procurando.'],
        examples=['Casa']
    )

    orcamento: int = Field(
        ...,
        description=['Orçamento do cliente.'],
        examples=[500000]
    )

    orcamento_minimo: int = Field(
        description=['Orçamento mínimo do cliente'],
        examples=[350000]
    )

    orcamento_maximo: int = Field(
        description=['Orçamento máximo do cliente'],
        examples=[650000]
    )

    quantidade_quartos: int = Field(
        description=['Quantidade desejada de quartos do cliente.'],
        examples=[3]
    )

    quantidade_suites: int = Field(
        description=['Quantidade desejada de suítes do cliente.'],
        examples=[1]
    )

    quantidade_banheiros: int = Field(
        description=['Quantidade desejada de banheiros do cliente.'],
        examples=[2]
    )

    quantidade_vagas_garagem: int = Field(
        description=['Quantidade desejada de vagas de garagem do cliente.'],
        examples=[2]
    )

    quantidade_andares: int = Field(
        description=['Quantidade desejada de andares do cliente.'],
        examples=[1]
    )

    quantidade_salas: int = Field(
        description=['Quantidade desejada de salas do cliente.'],
        examples=[1]
    )

    criado_em: datetime = Field(
        ...,
        description=['Data de criação do cliente na tabela de interessado.'],
        examples=['2026-04-23T08:24:00']
    )

    alterado_em: datetime | None = Field(
        ...,
        description=['Data de edição do cliente na tabela de interessado.'],
        examples=['']
    )

    model_config = {
    'json_schema_extra': {
        'examples': {
            'id': '019db9eb-db4c-7246-9025-0e0b7da207d7',
            'id_cliente': '019d0604-25a5-74c4-a2cb-eeaedaa5bbc1',
            'tipo_imovel': 'Casa',
            'orcamento': 500000,
            'orcamento_minimo': 350000,
            'orcamento_maximo': 650000,
            'quantidade_quartos': 3,
            'quantidade_suites': 1,
            'quantidade_banheiros': 2,
            'quantidade_vagas': 2,
            'quantidade_andares': 1,
            'quantidade_salas': 1,
            'criado_em': '2026-04-23T08:24:00',
            'alterado_em': None
        }
    }
}
    

class CriarClienteProprietarioRequest(BaseModel):
    id: UUID = Field(
        ...,
        description=['Identificador (UUIDv7) único do cliente na tabela de proprietários.'],
        examples=['019dbf01-46bf-7d93-89fc-41235daeda65']
    )

    id_cliente: UUID = Field(
        ...,
        description=['Identificador (UUID v7) único do cliente.'],
        examples=['019d0604-25a5-74c4-a2cb-eeaedaa5bbc1']
    )

    imovel_associado: str | None = Field(
        description=['Link do imóvel cadastrado do proprietário.'],
        examples=['']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'id': '019dbf01-46bf-7d93-89fc-41235daeda65',
                'id_cliente': '019d0604-25a5-74c4-a2cb-eeaedaa5bbc1',
                'imovel_associado': None
            }
        }
    }   


class EditarClienteProprietarioRequest(BaseModel):
    imovel_associado: str | None = Field(
        description=['Link do imóvel cadastrado do proprietário.'],
        examples=['']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'imovel_associado': None
            }
        }
    }


class ClienteProprietarioResponse(BaseModel):
    id: UUID = Field(
        ...,
        description=['Identificador (UUIDv7) único do cliente na tabela de proprietários.'],
        examples=['019dbf01-46bf-7d93-89fc-41235daeda65']
    )

    id_cliente: UUID = Field(
        ...,
        description=['Identificador (UUID v7) único do cliente.'],
        examples=['019d0604-25a5-74c4-a2cb-eeaedaa5bbc1']
    )

    imovel_associado: str | None = Field(
        description=['Link do imóvel cadastrado do proprietário.'],
        examples=['']
    )

    criado_em: datetime = Field(
        description='Data e hora da Criação do registro do cliente.',
        examples=['2026-04-24T08:25:14']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última modificação do registro do cliente.',
        examples=['']
    )

    model_config = {
        'json_schema_extra': {
            'examples': {
                'id': '019dbf01-46bf-7d93-89fc-41235daeda65',
                'id_cliente': '019d0604-25a5-74c4-a2cb-eeaedaa5bbc1',
                'imovel_associado': None,
                'criado_em': '2026-04-24T08:25:14',
                'alterado_em': None,
            }
        }
    }      