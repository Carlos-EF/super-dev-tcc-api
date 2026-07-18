from uuid import UUID
from pydantic import BaseModel, Field
from tcc.dominio.enums.status import Status
from datetime import datetime


class CriarImovelRequest(BaseModel):
    codigo: str = Field(
        ...,
        min_length=1,
        max_length=10,
        description='Código único do imóvel.',
        examples=['IMV12345']
    )

    proprietario: UUID | None = Field(
        None,
        description=['UUIDv7 do proprietário responsável pelo imóvel'],
        examples=['019db9eb-db4c-7246-9025-0e0b7da207d7']
    )

    corretor: UUID | None = Field(
        None,
        description=['UUIDv7 do corretor responsável.'],
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    status: str = Field(
        default=Status.ATIVO,
        description='Status do imóvel dentro do sistema.',
        examples=['ATIVO']
    )

    tipo: str = Field(
        ...,
        min_length=1,
        max_length=12,
        description='Tipo do imóvel (ex: apartamento, casa, terreno).',
        examples=['Apartamento']
    )

    finalidade: str = Field(
        ...,
        max_length=10,
        description='Finalidade do imóvel (ex: venda, aluguel).',
        examples=['Venda']
    )

    logradouro: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description='Endereço completo do imóvel.',
        examples=['Rua das Flores']
    )

    bairro: str = Field(
        ...,
        max_length=50,
        description='Bairro onde o imóvel está localizado.',
        examples=['Centro']
    )

    cidade: str = Field(
        ...,
        max_length=50,
        description='Cidade onde o imóvel está localizado.',
        examples=['São Paulo']
    )

    estado: str = Field(
        ...,
        min_length=4,
        max_length=16,
        description='Estado onde o imóvel está localizado.',
        examples=['São Paulo']
    )

    cep: str = Field(
        ...,
        min_length=8,
        max_length=9,
        description='CEP do imóvel.',
        examples=['01001-000']
    )

    numero: int = Field(
        ...,
        description='Número do imóvel.',
        examples=[123]
    )

    complemento: str | None = Field(
        None,
        max_length=50,
        description='Complemento do endereço do imóvel.',
        examples=['Apto 101', 'Bloco B']
    )

    em_condominio: bool = Field(
        ...,
        description='Indica se o imóvel é parte de um condomínio.',
        examples=[True]
    )

    condominio: str | None = Field(
        None,
        description='Condomínio em que se localiza o imóvel',
        examples=[None]
    )

    valor: float = Field(
        ...,
        description='Valor de venda do imóvel.',
        examples=[350000.00, 450000.00]
    )

    valor_condominio: float | None = Field(
        None,
        description='Valor do condomínio do imóvel.',
        examples=[None]
    )

    valor_iptu: float | None = Field(
        None,
        description='Valor do iptu do imóvel.',
        examples=[1000.00, 1500.00]
    )
    
    quantidade_quartos: int | None = Field(
        None,
        description='Número de quartos do imóvel.',
        examples=[2]
    )

    quantidade_suites: int | None = Field(
        None,
        description='Número de suítes do imóvel.',
        examples=[1]
    )

    quantidade_banheiros: int | None = Field(
        None,
        description='Número de banheiros do imóvel.',
        examples=[2]
    )

    quantidade_vagas: int | None = Field(
        None,
        description='Número de vagas de garagem do imóvel.',
        examples=[1]
    )

    quantidade_andares: int | None = Field(
        None,
        description='Número de andares do imóvel.',
        examples=[1]
    )

    quantidade_salas: int | None = Field(
        None,
        description='Número de salas do imóvel.',
        examples=[1]
    )

    eh_mobiliado: bool | None = Field(
        None,
        description='Indica se o imóvel é mobiliado.',
        examples=[True]
    )

    model_config = {
        'json_schema_extra': {
            'examples':[{
                'codigo': 'IMV12345',
                'proprietario': '019db9eb-db4c-7246-9025-0e0b7da207d7',
                'corretor': '019d45ea-997b-7451-9905-cb38b791fe93',
                'status': 'ATIVO',
                'tipo': 'Apartamento',
                'finalidade': 'Venda',
                'logradouro': 'Rua das Flores',
                'bairro': 'Centro',
                'cidade': 'São Paulo',
                'estado': 'São Paulo',
                'cep': '01001-000',
                'numero': 123,
                'complemento': None,
                'em_condominio': True,
                'condominio': None,
                'valor': 350000.00,
                'valor_condominio': None,
                'valor_iptu': 1000.00,
                'quantidade_quartos': 2,
                'quantidade_suites': 1,
                'quantidade_banheiros': 2,
                'quantidade_vagas': 1,
                'quantidade_andares': 1,
                'quantidade_salas': 1,
                'eh_mobiliado': True
            }]
        }
    }


class ImovelResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Indentificador único (UUID v7) do imóvel',
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    proprietario: UUID | None = Field(
        None,
        description='Indentificador único (UUID v7) do proprietário do imóvel',
        examples=['019db9eb-db4c-7246-9025-0e0b7da207d7']
    )

    corretor: UUID | None = Field(
        None,
        description='Indentificador único (UUID v7) do corretor do imóvel',
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    codigo: str = Field(
        ...,
        min_length=1,
        max_length=10,
        description='Código único do imóvel.',
        examples=['IMV12345']
    )

    status: str = Field(
        default=Status.ATIVO,
        description='Status do imóvel dentro do sistema.',
        examples=['ATIVO']
    )

    tipo: str = Field(
        ...,
        min_length=1,
        max_length=12,
        description='Tipo do imóvel (ex: apartamento, casa, terreno).',
        examples=['Apartamento']
    )

    finalidade: str = Field(
        ...,
        max_length=10,
        description='Finalidade do imóvel (ex: venda, aluguel).',
        examples=['Venda']
    )

    logradouro: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description='Endereço completo do imóvel.',
        examples=['Rua das Flores']
    )

    bairro: str = Field(
        ...,
        max_length=50,
        description='Bairro onde o imóvel está localizado.',
        examples=['Centro']
    )

    cidade: str = Field(
        ...,
        max_length=50,
        description='Cidade onde o imóvel está localizado.',
        examples=['São Paulo']
    )

    estado: str = Field(
        ...,
        min_length=4,
        max_length=16,
        description='Estado onde o imóvel está localizado.',
        examples=['São Paulo']
    )

    cep: str = Field(
        ...,
        min_length=8,
        max_length=9,
        description='CEP do imóvel.',
        examples=['01001-000']
    )

    numero: int = Field(
        ...,
        description='Número do imóvel.',
        examples=[123]
    )

    complemento: str | None = Field(
        None,
        max_length=50,
        description='Complemento do endereço do imóvel.',
        examples=['Apto 101', 'Bloco B']
    )

    em_condominio: bool = Field(
        ...,
        description='Indica se o imóvel é parte de um condomínio.',
        examples=[True]
    )

    condominio: UUID | None = Field(
        None,
        description='Indentificador único (UUID v7) do condomínio do imóvel',
        examples=[None]
    )

    valor: float = Field(
        ...,
        description='Valor de venda do imóvel.',
        examples=[350000.00, 450000.00]
    )

    valor_iptu: float | None = Field(
        None,
        description='Valor do iptu do imóvel.',
        examples=[1000.00, 1500.00]
    )

    valor_condominio: float | None = Field(
        None,
        description='Valor do condomínio do imóvel.',
        examples=[1000.00, 1500.00]
    )
    
    quantidade_quartos: int | None = Field(
        None,
        description='Número de quartos do imóvel.',
        examples=[2]
    )

    quantidade_suites: int | None = Field(
        None,
        description='Número de suítes do imóvel.',
        examples=[1]
    )

    quantidade_banheiros: int | None = Field(
        None,
        description='Número de banheiros do imóvel.',
        examples=[2]
    )

    quantidade_vagas: int | None = Field(
        None,
        description='Número de vagas de garagem do imóvel.',
        examples=[1]
    )

    quantidade_andares: int | None = Field(
        None,
        description='Número de andares do imóvel.',
        examples=[1]
    )

    quantidade_salas: int | None = Field(
        None,
        description='Número de salas do imóvel.',
        examples=[1]
    )

    eh_mobiliado: bool | None = Field(
        None,
        description='Indica se o imóvel é mobiliado.',
        examples=[True]
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro do imóvel.',
        examples=['2026-03-26T08:35:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro do imóvel.',
        examples=['2026-04-01T14:20:00']
    )

    model_config = {
        'json_schema_extra': {
            'examples':[{
                'id': '019d45ea-997b-7451-9905-cb38b791fe93',
                'proprietario': '019db9eb-db4c-7246-9025-0e0b7da207d7',
                'corretor': '019d45ea-997b-7451-9905-cb38b791fe93',
                'codigo': 'IMV12345',
                'status': 'ATIVO',
                'tipo': 'Apartamento',
                'finalidade': 'Venda',
                'logradouro': 'Rua das Flores',
                'bairro': 'Centro',
                'cidade': 'São Paulo',
                'estado': 'São Paulo',
                'cep': '01001-000',
                'numero': 123,
                'em_condominio': True,
                'condominio': None,
                'valor': 350000.00,
                'valor_iptu': 1000.00,
                'valor_condominio': None,
                'quantidade_quartos': 2,
                'quantidade_suites': 1,
                'quantidade_banheiros': 2,
                'quantidade_vagas': 1,
                'quantidade_andares': 1,
                'quantidade_salas': 1,
                'eh_mobiliado': True,
                'criado_em': '2026-03-26T08:35:00',
                'alterado_em': '2026-04-01T14:20:00'
            }]
        }
    }


class EditarImovelRequest(BaseModel):
    proprietario: UUID | None = Field(
        None,
        description=['UUIDv7 do proprietário responsável pelo imóvel'],
        examples=['019db9eb-db4c-7246-9025-0e0b7da207d7']
    )

    corretor: UUID | None = Field(
        None,
        description=['UUIDv7 do corretor responsável.'],
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    tipo: str | None = Field(
        None,
        min_length=1,
        max_length=12,
        description='Tipo do imóvel (ex: apartamento, casa, terreno).',
        examples=['Apartamento']
    )

    finalidade: str | None = Field(
        None,
        max_length=10,
        description='Finalidade do imóvel (ex: venda, aluguel).',
        examples=['Venda']
    )

    logradouro: str | None = Field(
        None,
        min_length=5,
        max_length=100,
        description='Endereço completo do imóvel.',
        examples=['Rua das Flores']
    )

    bairro: str | None = Field(
        None,
        max_length=50,
        description='Bairro onde o imóvel está localizado.',
        examples=['Centro']
    )

    cidade: str | None = Field(
        None,
        max_length=50,
        description='Cidade onde o imóvel está localizado.',
        examples=['São Paulo']
    )

    estado: str | None = Field(
        None,
        min_length=4,
        max_length=16,
        description='Estado onde o imóvel está localizado.',
        examples=['São Paulo']
    )

    cep: str | None = Field(
        None,
        min_length=8,
        max_length=9,
        description='CEP do imóvel.',
        examples=['01001-000']
    )

    numero: int | None = Field(
        None,
        description='Número do imóvel.',
        examples=[123]
    )

    complemento: str | None = Field(
        None,
        max_length=50,
        description='Complemento do endereço do imóvel.',
        examples=['Apto 101', 'Bloco B']
    )

    em_condominio: bool | None = Field(
        None,
        description='Indica se o imóvel é parte de um condomínio.',
        examples=[True]
    )

    condominio: UUID | None = Field(
        None,
        description='Indentificador único (UUID v7) do condomínio do imóvel',
        examples=[None]
    )

    valor: float | None = Field(
        None,
        description='Valor de venda do imóvel.',
        examples=[350000.00, 450000.00]
    )

    valor_iptu: float | None = Field(
        None,
        description='Valor do iptu do imóvel.',
        examples=[1000.00, 1500.00]
    )

    valor_condominio: float | None = Field(
        None,
        description='Valor do condomínio do imóvel.',
        examples=[1000.00, 1500.00]
    )

    quantidade_quartos: int | None = Field(
        None,
        description='Número de quartos do imóvel.',
        examples=[2]
    )

    quantidade_suites: int | None = Field(
        None,
        description='Número de suítes do imóvel.',
        examples=[1]
    )

    quantidade_banheiros: int | None = Field(
        None,
        description='Número de banheiros do imóvel.',
        examples=[2]
    )

    quantidade_vagas: int | None = Field(
        None,
        description='Número de vagas de garagem do imóvel.',
        examples=[1]
    )

    quantidade_andares: int | None = Field(
        None,
        description='Número de andares do imóvel.',
        examples=[1]
    )

    quantidade_salas: int | None = Field(
        None,
        description='Número de salas do imóvel.',
        examples=[1]
    )

    eh_mobiliado: bool | None = Field(
        None,
        description='Indica se o imóvel é mobiliado.',
        examples=[True]
    )

    model_config = {
        'json_schema_extra': {
            'examples':[{
                'proprietario': '019db9eb-db4c-7246-9025-0e0b7da207d7',
                'corretor': '019d45ea-997b-7451-9905-cb38b791fe93',
                'tipo': 'Apartamento',
                'finalidade': 'Venda',
                'logradouro': 'Rua das Flores',
                'bairro': 'Centro',
                'cidade': 'São Paulo',
                'estado': 'São Paulo',
                'cep': '01001-000',
                'numero': 123,
                'complemento': None,
                'em_condominio': False,
                'condominio': None,
                'valor': 350000.00,
                'valor_iptu': 1000.00,
                'valor_condominio': 1000.00,
                'quantidade_quartos': 2,
                'quantidade_suites': 1,
                'quantidade_banheiros': 2,
                'quantidade_vagas': 1,
                'quantidade_andares': 1,
                'quantidade_salas': 1,
                'eh_mobiliado': True
            }]
        }
    }


class CriarImagensImovelRequest(BaseModel):
    imagem: str | None = Field(
        None,
        description=['URL ou título do arquivo da imagem.'],
        examples=[None]
    )

    imagem_principal: bool | None = Field(
        None,
        description=['Diz se a imagem é a principal ou não.'],
        examples=[True]
    )

    model_config = {
        'json_schema_extra': {
            'examples': [{
                'id_imovel': '019f752e-2191-7757-97b7-b9b2871a29ee',
                'imagem': None,
                'imagem_principal': None
            }]
        }
    }


class EditarImagensImovelRequest(BaseModel):
    imagem: str | None = Field(
        None,
        description=['URL ou título do arquivo da imagem.'],
        examples=[None]
    )

    imagem_principal: bool | None = Field(
        None,
        description=['Diz se a imagem é a principal ou não.'],
        examples=[True]
    )

    model_config = {
        'json_schema_extra': {
            'examples': [{
                'imagem': None,
                'imagem_principal': None
            }]
        }
    }


class ImagensImovelResponse(BaseModel):
    id: UUID = Field(
        ...,
        description=['Identificador (UUIDv7) na tabela de imagens.'],
        examples=['019f752d-1dc5-7888-aa71-6c11e280cb3c']
    )

    id_imovel: UUID = Field(
        ...,
        description=['Identificador (UUIDv7) da tabela principal de imóveis.'],
        examples=['019f752e-2191-7757-97b7-b9b2871a29ee']
    )

    imagem: str | None = Field(
        None,
        description=['URL ou título do arquivo da imagem.'],
        examples=[None]
    )

    imagem_principal: bool | None = Field(
        None,
        description=['Diz se a imagem é a principal ou não.'],
        examples=[True]
    )

    criado_em: datetime = Field(
        description='Data e hora da criação do registro das imagens.',
        examples=['2026-07-18T09:31:22']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última modificação do registro das imagens.',
        examples=[None]
    )

    model_config = {
        'json_schema_extra': {
            'examples': [{
                'id': '019f752d-1dc5-7888-aa71-6c11e280cb3c',
                'id_imovel': '019f752e-2191-7757-97b7-b9b2871a29ee',
                'imagem': None,
                'imagem_principal': None,
                'criado_em': '2026-07-18T09:31:22',
                'alterado_em': None
            }]
        }
    }