from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
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
        String(60),
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

    uf = Column(
        String(2),
        nullable=False
    )

    cidade = Column(
        String(50),
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

    imoveis = relationship(
    'PropertyModel',
    foreign_keys='PropertyModel.condominio',
    back_populates='condominio_relacionado'
    )