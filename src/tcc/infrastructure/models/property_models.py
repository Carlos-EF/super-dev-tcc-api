from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ARRAY, Column, Integer, Numeric, String, Date, ForeignKey, Boolean
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
        nullable=False
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

    casa = relationship(
        'HouseModel',
        back_populates='imovel',
        cascade="all, delete-orphan", 
        uselist=False
    )

    apartamento = relationship(
        'ApartmentModel',
        back_populates='imovel',
        cascade="all, delete-orphan", 
        uselist=False
    )

    terreno = relationship(
        'LandModel',
        back_populates='imovel',
        cascade="all, delete-orphan", 
        uselist=False
    )

    imagens = relationship(
    'PropertyImageModel',
    back_populates='imovel',
    cascade='all, delete-orphan',
    order_by='PropertyImageModel.principal.desc()'
    )


class HouseModel(BaseModel):
    __tablename__= 'casas'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )
    
    imovel_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('imoveis.id', ondelete='CASCADE'),
        nullable=False,
    )

    metragem = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    quartos = Column(
        Integer,
        nullable=True
    )

    suites = Column(
        Integer,
        nullable=True
    )

    banheiros = Column(
        Integer,
        nullable=True
    )

    garagens = Column(
        Integer,
        nullable=True
    )

    andares = Column(
        Integer,
        nullable=True
    )

    salas = Column(
        Integer,
        nullable=True
    )

    esta_mobiliado = Column(
        String(15),
        nullable=True
    )

    mobilia = Column( 
        ARRAY(String), 
        nullable=True, 
        default=list 
    )

    criado_em = Column(
        Date,
        nullable=False
    )
    
    alterado_em = Column(
        Date,
        nullable=True
    )

    imovel = relationship(
        'PropertyModel',
        back_populates='casa',
    )


class ApartmentModel(BaseModel):
    __tablename__= 'apartamentos'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )
    
    imovel_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('imoveis.id', ondelete='CASCADE'),
        nullable=False,
    )

    metragem = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    quartos = Column(
        Integer,
        nullable=True
    )

    suites = Column(
        Integer,
        nullable=True
    )

    banheiros = Column(
        Integer,
        nullable=True
    )

    garagens = Column(
        Integer,
        nullable=True
    )

    andares = Column(
        Integer,
        nullable=True
    )

    salas = Column(
        Integer,
        nullable=True
    )

    esta_mobiliado = Column(
        String(15),
        nullable=True
    )

    mobilia = Column( 
        ARRAY(String), 
        nullable=True, 
        default=list 
    )

    criado_em = Column(
        Date,
        nullable=False
    )
    
    alterado_em = Column(
        Date,
        nullable=True
    )

    imovel = relationship(
        'PropertyModel',
        back_populates='apartamento',
    )


class LandModel(BaseModel):
    __tablename__= 'terrenos'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )
    
    imovel_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey('imoveis.id', ondelete='CASCADE'),
        nullable=False,
    )

    area_total = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    medida_esquerda = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    medida_direita = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    medida_frente = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    medida_fundo = Column(
        Numeric(precision=10, scale=2),
        nullable=True
    )

    zoneamento = Column(
        String(11),
        nullable=True
    )

    coeficiente = Column(
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

    imovel = relationship(
        'PropertyModel',
        back_populates='terreno',
    )


class PropertyImageModel(BaseModel):
    __tablename__ = 'imagens_imoveis'

    id = Column(
        UUID(
            as_uuid=True
        ),
        nullable=False,
        primary_key=True
    )

    imovel_id = Column(
        UUID(
            as_uuid=True
        ),
        ForeignKey(
            'imoveis.id',
            ondelete='CASCADE'
        ),
        nullable=False
    )

    caminho = Column(
        String(500),
        nullable=False
    )

    url = Column(
        String(1000),
        nullable=False
    )

    principal = Column(
        Boolean,
        nullable=False,
        default=False
    )

    criado_em = Column(
        Date,
        nullable=False
    )

    alterado_em = Column(
        Date,
        nullable=True
    )

    imovel = relationship(
        'PropertyModel',
        back_populates='imagens'
    )