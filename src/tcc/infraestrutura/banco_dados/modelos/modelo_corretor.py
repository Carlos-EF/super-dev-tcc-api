from uuid import UUID
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
        Integer(10),
        nullable=False
    )

    celular = Column(
        String(11),
        nullable=False
    )

    email = Column(
        String(50),
        nullable=False
    )

    creci = Column(
        String(5),
        nullable=False
    )

    data_nascimento = Column(
        Date,
        nullable=True
    )

    rg = Column(
        String(7),
        nullable=True
    )

    cpf = Column(
        String(11), 
        nullable=True
    )

    