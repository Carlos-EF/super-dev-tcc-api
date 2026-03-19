from uuid import UUID
from sqlalchemy.orm import Session
from tcc.infraestrutura.banco_dados.modelos.modelo_cliente import ModeloCliente


class RepositorioCliente:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar(self, cliente: ModeloCliente) -> ModeloCliente:
        self.sessao.add(cliente)
        self.sessao.commit()
        self.sessao.flush(cliente)


        return cliente
    

    def editar(
            self,
            id: UUID,
            nome: str,
            codigo: int,
            tipo: str,
            celular: int,
            email: str,
            como_encontrou: str):
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente.nome = nome
        cliente.codigo = codigo
        cliente.tipo = tipo
        cliente.celular = celular
        cliente.email = email
        cliente.como_encontrou = como_encontrou

        self.sessao.commit()
        return True
    

    def listar(self) -> list[ModeloCliente]:
        clientes = self.sessao.query(ModeloCliente).all()

        return clientes
    

    def inativar(self, id: UUID):
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente.status = "INATIVO"
        self.sessao.commit()
        return True
    

    def ativar(self, id: UUID):
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente.status = "ATIVO"
        self.sessao.commit()
        return True
    

    def apagar(self, id: UUID):
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        self.sessao.delete(cliente)
        self.sessao.commit()
        return True