from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer
from tcc.infrastructure.models.base_model import BaseModel

class CondominiumModel(BaseModel):
    __tablename__ = 'condominios'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )

    nome = Column(
        String(50),
        nullable=False
    )

    cep = Column(
        String(9),
        nullable=False
    )

    logradouro = Column(
        String(60),
        nullable=False
    )

    numero = Column(
        Integer,
        nullable=False
    )

    bairro = Column(
        String(50),
        nullable=False
    )

    estado = Column(
        String(20),
        nullable=False
    )

    cidade = Column(
        String(40),
        nullable=False
    )