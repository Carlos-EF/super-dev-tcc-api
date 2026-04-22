from uuid import UUID
from sqlalchemy import Column, String, Integer
from tcc.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase


class ModeloCliente(ModeloBase):
    __tablename__ = 'clientes'

    id= Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    nome= Column(
        String(100),
        nullable=False
    )

    codigo = Column(
        Integer(10),
        nullable=False
    )

    tipo = Column(
        String(12),
        nullable=False
    )

    celular = Column(
        String(14),
        nullable=False
    )

    email = Column(
        String(40),
        nullable=False
    )

    como_encontrou = Column(
        String(14),
        nullable=True
    )

    status = Column(
        String(7),
        nullable=False
    )