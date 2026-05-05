from uuid import UUID
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
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
        Integer,
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

    interessado = relationship('ModeloClienteInteressado', back_populates='cliente', uselist=False)

    proprietario = relationship('ModeloClienteProprietario', back_populates='cliente', uselist=False)

    locatario = relationship('ModeloClienteLocatario', back_populates='cliente', uselist=False)


class ModeloClienteInteressado(ModeloBase):
    __tablename__ = 'interessados'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    id_cliente = Column(
        UUID(as_uuid=True),
        ForeignKey('clientes.id'),
        nullable=False
    )

    procurando = Column(
        String(11),
        nullable=False
    )

    orcamento = Column(
        Integer,
        nullable=False
    )

    orcamento_minimo = Column(
        Integer,
        nullable=True
    )
    
    orcamento_maximo = Column(
        Integer,
        nullable=True
    )

    quantidade_quartos = Column(
        Integer,
        nullable=True
    )

    quantidade_suites = Column(
        Integer,
        nullable=True
    )
    
    quantidade_banheiros = Column(
        Integer,
        nullable=True
    )

    quantidade_vagas_garagem = Column(
        Integer,
        nullable=True
    )
    
    quantidade_andares = Column(
        Integer,
        nullable=True
    )

    quantidade_salas = Column(
        Integer,
        nullable=True
    )

    cliente = relationship('ModeloCliente', back_populates='interessado')


class ModeloClienteProprietario(ModeloBase):
    __tablename__ = 'proprietarios'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    id_cliente = Column(
        UUID(as_uuid=True),
        ForeignKey('clientes.id'),
        nullable=False
    )

    imovel_proprietario = Column(
        String,
        nullable=True
    )

    cliente = relationship('ModeloCliente', back_populates='proprietario')


class ModeloClienteLocatario(ModeloBase):
    __tablename__ = 'locatarios'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    id_cliente = Column(
        UUID(as_uuid=True),
        ForeignKey('clientes.id'),
        nullable=False
    )

    imovel_locatario = Column(
        String,
        nullable=True
    )

    cliente = relationship('ModeloCliente', back_populates='locatario')