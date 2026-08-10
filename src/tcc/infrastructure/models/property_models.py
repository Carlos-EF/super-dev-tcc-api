from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from tcc.infrastructure.models.base_model import BaseModel


class PropertyModel(BaseModel):
    __tablename__= 'imoveis'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )
    
    proprietario_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('clientes.id', ondelete='SET NULL'),
        nullable=True,
    )

    corretor_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('corretores.id', ondelete='SET NULL'),
        nullable=True,
    )

    codigo = Column(
        String(4),
        nullable=False
    )

    finalidade = Column(
        String(7),
        nullable=False
    )

    tipo = Column(
        String(11),
        nullable=False
    )

    em_condominio = Column(
        Boolean,
        nullable=True
    )

    condominio = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('condominios.id', ondelete='SET NULL'),
        nullable=True,
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

    complemento = Column(
        String(60),
        nullable=True
    )

    valor = Column(
        Numeric(precision=10, scale=2),
        nullable=False
    )

    valor_condominio = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    valor_iptu = Column(
        Numeric(precision=10, scale=2),
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