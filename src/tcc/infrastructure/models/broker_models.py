from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, Date
from tcc.infrastructure.models.base_model import BaseModel


class BrokerModel(BaseModel):
    __tablename__= 'corretores'

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

    codigo = Column(
        String(4),
        nullable=False
    )

    numero = Column(
        String(14),
        nullable=False
    )

    email = Column(
        String(60),
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

    criado_em = Column(
        Date,
        nullable=False
    )

    alterado_em = Column(
        Date,
        nullable=True
    )