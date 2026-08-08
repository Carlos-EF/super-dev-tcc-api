from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from tcc.infrastructure.models.base_model import BaseModel


class ClientModel(BaseModel):
    __tablename__= 'clientes'

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
        String(15),
        nullable=False
    )

    email = Column(
        String(60),
        nullable=False
    )

    tipo = Column(
        String(11),
        nullable=False
    )

    como_encontrou = Column(
        String(18),
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

    interessado = relationship(
        'InterestedClientModel',
        back_populates='cliente',
        uselist=False
    )


class InterestedClientModel(ClientModel):
    __tablename__= 'interessados'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )
    
    cliente_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('clientes.id'),
        nullable=False
    )

    procura = Column(
        String(11),
        nullable=True
    )

    finalidade = Column(
        String(6),
        nullable=True
    )

    preferencia = Column(
        String(50),
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

    cliente = relationship(
        'ClientModel',
        back_populates='interessado',
        uselist=False
    )