from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import  Column,String, Date, Boolean
from tcc.infrastructure.models.base_model import BaseModel

class UserModel(BaseModel):
    __tablename__= 'usuarios'

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