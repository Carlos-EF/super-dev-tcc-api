from uuid import UUID, uuid7
from sqlalchemy.orm import Session
from tcc.infraestrutura.banco_dados.modelos.modelo_cliente import ModeloCliente, ModeloClienteInteressado, ModeloClienteLocatario, ModeloClienteProprietario


class RepositorioCliente:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar(self, cliente: ModeloCliente) -> ModeloCliente:
        self.sessao.add(cliente)
        self.sessao.flush(cliente)

        if cliente.tipo == 'Interessado':
            self.criar_cliente_interessado(cliente)
        elif cliente.tipo == 'Proprietário':
            self.criar_cliente_proprietario(cliente)
        elif cliente.tipo == 'Locatário':
            self.criar_cliente_locatario(cliente)
         

        self.sessao.commit()

        return cliente
    

    def editar (
            self,
            id: UUID,
            nome: str,
            tipo: str,
            celular: int,
            email: str,
            ) -> bool:
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente.nome = nome
        cliente.tipo = tipo
        cliente.celular = celular
        cliente.email = email

        self.sessao.commit()
        return True
    

    def listar(self) -> list[ModeloCliente]:
        clientes = self.sessao.query(ModeloCliente).all()

        return clientes
    

    def inativar(self, id: UUID) -> bool:
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente.status = "INATIVO"
        self.sessao.commit()
        return True
    

    def ativar(self, id: UUID) -> bool:
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente.status = "ATIVO"
        self.sessao.commit()
        return True
    

    def apagar(self, id: UUID) -> bool:
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        cliente_tipo = cliente.tipo
        if cliente_tipo == 'Interessado':
            self.apagar_cliente_interessado(cliente.id)
        elif cliente_tipo == 'Locatário':
            self.apagar_cliente_locatario(cliente.id)
        elif cliente_tipo == 'Proprietário':
            self.apagar_cliente_proprietario(cliente.id)
        
        self.sessao.delete(cliente)
        self.sessao.commit()
        return True
    

    def obter_por_id(self, id: UUID) -> ModeloCliente | None:
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        return cliente
    

    def listar_clientes_interessados(self) -> list[ModeloClienteInteressado]:
        clientes_interessados = self.sessao.query(ModeloClienteInteressado).all()

        return clientes_interessados
    
    
    def criar_cliente_interessado(self, cliente: ModeloCliente, dados: ModeloClienteInteressado) -> ModeloClienteInteressado:
        cliente_interessado = ModeloClienteInteressado(
            id = uuid7(),
            id_cliente = cliente.id,
            procurando = dados.procurando,
            orcamento = dados.orcamento,
            orcamento_minimo = dados.orcamento_minimo,
            orcamento_maximo = dados.orcamento_maximo,
            quantidade_quartos = dados.quantidade_quartos,
            quantidade_suites = dados.quantidade_suites,
            quantidade_banheiros = dados.quantidade_banheiros,
            quantidade_vagas_garagem = dados.quantidade_vagas_garagem,
            quantidade_andares = dados.quantidade_andares,
            quantidade_salas = dados.quantidade_salas,
        )

        self.sessao.add(cliente_interessado)

        return cliente_interessado
    

    def apagar_cliente_interessado(self, id: UUID) -> bool:
        cliente_interessado = self.sessao.query(ModeloClienteInteressado).filter(ModeloClienteInteressado.id_cliente == id).first()
        if not cliente_interessado:
            return False
        
        self.sessao.delete(cliente_interessado)
        return True
    

    def criar_cliente_proprietario(self, cliente: ModeloCliente, dados: ModeloClienteProprietario) -> ModeloClienteProprietario:
        cliente_prorietario = ModeloClienteProprietario(
            id = uuid7(),
            id_cliente = cliente.id,
            imovel_proprietario = dados.imovel_proprietario,
        )

        self.sessao.add(cliente_prorietario)

        return cliente_prorietario
    

    def listar_clientes_proprietarios(self) -> list[ModeloClienteInteressado]:
        clientes_proprietarios = self.sessao.query(ModeloClienteProprietario).all()

        return clientes_proprietarios
    

    def apagar_cliente_proprietario(self, id: UUID) -> bool:
        cliente_proprietario = self.sessao.query(ModeloClienteProprietario).filter(ModeloClienteProprietario.id_cliente == id).first()
        if not cliente_proprietario:
            return False
        
        self.sessao.delete(cliente_proprietario)
        return True
    

    def criar_cliente_locatario(self, cliente: ModeloCliente, dados: ModeloClienteLocatario) -> ModeloClienteLocatario:
        cliente_locatario = ModeloClienteLocatario(
            id = uuid7(),
            id_cliente = cliente.id,
            imovel_associado = dados.imovel_locatario
        )

        self.sessao.add(cliente_locatario)

        return cliente_locatario
    

    def apagar_cliente_locatario(self, id: UUID) -> bool:
        cliente_locatario = self.sessao.query(ModeloClienteLocatario).filter(ModeloClienteLocatario.id_cliente == id).first()
        if not cliente_locatario:
            return False
        
        self.sessao.delete(cliente_locatario)
        return True