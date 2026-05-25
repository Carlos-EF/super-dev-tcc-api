from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Date, String, Integer, Numeric, Boolean
from tcc.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase


class ModeloImovel(ModeloBase):
    __tablename__ = 'imoveis'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    codigo = Column(
        String(10),
        nullable=False
    )

    status = Column(
        String(7),
        nullable=False
    )

    tipo = Column(
        String(12),
        nullable=False
    )

    finalidade = Column(
        String(10),
        nullable=False
    )

    logradouro = Column(
        String(100),
        nullable=False
    )

    bairro = Column(
        String(50),
        nullable=False
    )

    cidade = Column(
        String(50),
        nullable=False
    )

    estado = Column(
        String(2),
        nullable=False
    )

    cep = Column(
        String(9),
        nullable=False
    )

    numero = Column(
        String(10),
        nullable=False
    )

    eh_condominio = Column(
        Boolean,
        nullable=False
    )

    valor = Column(
        Numeric(precision=10, scale=2),
        nullable=False
    )

    valor_iptu = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    quantidade_quartos = Column(
        Integer,
        nullable=True
    )

    quantidade_suites = Column(
        Integer,
        nullable=True
    )

    quantidade_banheiros = Column(
        Integer,
        nullable=True
    )

    quantidade_vagas = Column(
        Integer,
        nullable=True
    )

    quantidade_andares = Column(
        Integer,
        nullable=True
    )

    quantidade_salas = Column(
        Integer,
        nullable=True
    )

    eh_mobiliado = Column(
        Boolean,
        nullable=False
    )

    criado_em = Column(
        Date,
        nullable=False
    )

    alterado_em = Column(
        Date,
        nullable=True
    )


class ModeloImagemImovel(ModeloBase):
    __tablename__ = 'imagens_imoveis'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    id_imovel = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    imagem = Column(
        String(255),
        nullable=False
    )

    imagem_principal = Column(
        Boolean,
        nullable=True
    )