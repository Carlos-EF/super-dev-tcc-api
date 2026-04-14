from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Date
from tcc.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase


class ModeloCorretor(ModeloBase):
    __tablename__ = 'corretores'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
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

    nome_completo = Column(
        String(60),
        nullable=False
    )

    codigo = Column(
        Integer,
        nullable=False
    )

    celular = Column(
        String(15),
        nullable=False
    )

    email = Column(
        String(50),
        nullable=False
    )

    creci = Column(
        String(7),
        nullable=False
    )

    data_nascimento = Column(
        String(10),
        nullable=True
    )

    rg = Column(
        String(9),
        nullable=True
    )

    cpf = Column(
        String(14), 
        nullable=True
    )

    