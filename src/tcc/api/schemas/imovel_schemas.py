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
        min_length=2,
        max_length=2,
        description='Estado onde o imóvel está localizado (sigla).',
        examples=['SP']
    )
    cep: str = Field(
        ...,
        min_length=8,
        max_length=9,
        description='CEP do imóvel.',
        examples=['01001-000']
    )
    numero: str = Field(
        ...,
        max_length=10,
        description='Número do imóvel.',
        examples=['123']
    )

    eh_condominio: bool = Field(
        ...,
        description='Indica se o imóvel é parte de um condomínio.',
        examples=[True]
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
                'status': 'ATIVO',
                'tipo': 'Apartamento',
                'finalidade': 'Venda',
                'logradouro': 'Rua das Flores',
                'bairro': 'Centro',
                'cidade': 'São Paulo',
                'estado': 'SP',
                'cep': '01001-000',
                'numero': '123',
                'eh_condominio': True,
                'valor': 350000.00,
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
        min_length=2,
        max_length=2,
        description='Estado onde o imóvel está localizado (sigla).',
        examples=['SP']
    )
    cep: str = Field(
        ...,
        min_length=8,
        max_length=9,
        description='CEP do imóvel.',
        examples=['01001-000']
    )
    numero: str = Field(
        ...,
        max_length=10,
        description='Número do imóvel.',
        examples=['123']
    )

    eh_condominio: bool = Field(
        ...,
        description='Indica se o imóvel é parte de um condomínio.',
        examples=[True]
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
                'codigo': 'IMV12345',
                'status': 'ATIVO',
                'tipo': 'Apartamento',
                'finalidade': 'Venda',
                'logradouro': 'Rua das Flores',
                'bairro': 'Centro',
                'cidade': 'São Paulo',
                'estado': 'SP',
                'cep': '01001-000',
                'numero': '123',
                'eh_condominio': True,
                'valor': 350000.00,
                'valor_iptu': 1000.00,
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
        min_length=2,
        max_length=2,
        description='Estado onde o imóvel está localizado (sigla).',
        examples=['SP']
    )
    cep: str | None = Field(
        None,
        min_length=8,
        max_length=9,
        description='CEP do imóvel.',
        examples=['01001-000']
    )
    numero: str | None = Field(
        None,
        max_length=10,
        description='Número do imóvel.',
        examples=['123']
    )

    eh_condominio: bool | None = Field(
        None,
        description='Indica se o imóvel é parte de um condomínio.',
        examples=[True]
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
                'tipo': 'Apartamento',
                'finalidade': 'Venda',
                'logradouro': 'Rua das Flores',
                'bairro': 'Centro',
                'cidade': 'São Paulo',
                'estado': 'SP',
                'cep': '01001-000',
                'numero': '123',
                'eh_condominio': True,
                'valor': 350000.00,
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


class ImagensImoveisResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Indentificador único (UUID v7) da imagem do imóvel',
        examples=['019e63e5-172a-71c1-887d-8b7c607fba54']
    )

    id_imovel: UUID = Field(
        ...,
        description='Indentificador único (UUID v7) do imóvel associado à imagem',
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    principal: bool = Field(
        ...,
        description='Indica se a imagem é a principal do imóvel.',
        examples=[True]
    )

    caminho: str = Field(
        ...,
        description='Caminho do arquivo da imagem do imóvel.',
        examples=['/imagens/019e63e4-88f2-7dc6-91a9-cf71871401fb.jpg']
    )

    criado_em: datetime = Field(
        ...,
        description='Data e hora da criação do registro da imagem do imóvel.',
        examples=['2026-03-26T08:35:00']
    )

    alterado_em: datetime | None = Field(
        None,
        description='Data e hora da última alteração do registro da imagem do imóvel.',
        examples=['2026-04-01T14:20:00']
    )

    model_config = {
        'json_schema_extra': {
            'examples':[{
                'id': '019e63e5-172a-71c1-887d-8b7c607fba54',
                'id_imovel': '019d45ea-997b-7451-9905-cb38b791fe93',
                'caminho': '/imagens/019e63e4-88f2-7dc6-91a9-cf71871401fb.jpg',
                'principal': True,
                'criado_em': '2026-03-26T08:35:00',
                'alterado_em': '2026-04-01T14:20:00'
            }]
        }
    }


class CriarImagemImovelRequest(BaseModel):
    id_imovel: UUID = Field(
        ...,
        description='Indentificador único (UUID v7) do imóvel associado à imagem',
        examples=['019d45ea-997b-7451-9905-cb38b791fe93']
    )

    caminho: str = Field(
        ...,
        description='Caminho do arquivo da imagem do imóvel.',
        examples=['/imagens/019e63e4-88f2-7dc6-91a9-cf71871401fb.jpg']
    )

    principal: bool = Field(
        ...,
        description='Indica se a imagem é a principal do imóvel.',
        examples=[True]
    )

    model_config = {
        'json_schema_extra': {
            'examples':[{
                'id_imovel': '019d45ea-997b-7451-9905-cb38b791fe93',
                'caminho': '/imagens/019e63e4-88f2-7dc6-91a9-cf71871401fb.jpg',
                'principal': True
            }]
        }
    }


class EditarImagemImovelRequest(BaseModel):
    caminho: str | None = Field(
        None,
        description='Caminho do arquivo da imagem do imóvel.',
        examples=['/imagens/019e63e4-88f2-7dc6-91a9-cf71871401fb.jpg']
    )

    principal: bool | None = Field(
        None,
        description='Indica se a imagem é a principal do imóvel.',
        examples=[True]
    )

    model_config = {
        'json_schema_extra': {
            'examples':[{
                'caminho': '/imagens/019e63e4-88f2-7dc6-91a9-cf71871401fb.jpg',
                'principal': True
            }]
        }
    }