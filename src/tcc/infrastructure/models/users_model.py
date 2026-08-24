from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ARRAY, Column, Integer, Numeric, String, Date, ForeignKey, Boolean
from tcc.infrastructure.models.base_model import BaseModel

class UserModel(BaseModel):
    id = Column(
        UUID(
            as_uuid=True
        ),
        primary_key=True
    )

    nome= Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True
    )

    ativo = Column(
        Boolean,
        default=True,
        server_default='true'
    )

    criado_em = Column(
        Date,
        nullable=False
    )

    alterado_em = Column(
        Date,
        nullable=True
    )