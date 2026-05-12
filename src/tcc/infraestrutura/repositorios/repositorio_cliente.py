from typing import Union
from uuid import UUID
from uuid6 import uuid7
from sqlalchemy.orm import Session, joinedload
from tcc.api.schemas.cliente_schemas import ClienteResponse, CriarClienteInteressadoRequest, CriarClienteLocatarioRequest, CriarClienteProprietarioRequest
from tcc.infraestrutura.banco_dados.modelos.modelo_cliente import ModeloCliente, ModeloClienteInteressado, ModeloClienteLocatario, ModeloClienteProprietario


class RepositorioCliente:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar(self, cliente: ModeloCliente, dados_adicionais):
        self.sessao.add(cliente)
        self.sessao.flush()

        self.criar_cliente_por_tipo(cliente, cliente.tipo, dados_adicionais)

        self.sessao.commit()

        return cliente
    

    def editar (
            self,
            id: UUID,
            nome: str,
            tipo: str,
            celular: int,
            email: str,
            dados_adicionais
            ) -> bool:
        cliente = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente:
            return False
        
        tipo_original = cliente.tipo
        if tipo_original != tipo:
            self.criar_cliente_por_tipo(cliente, tipo, dados_adicionais)
            self.apagar_cliente_por_tipo(cliente, tipo_original)
        else:
            self.editar_cliente_por_tipo(cliente, tipo, dados_adicionais)

        cliente.nome = nome
        cliente.tipo = tipo
        cliente.celular = celular
        cliente.email = email
        

        self.sessao.commit()
        return True
    

    def listar(self) -> list[ClienteResponse]:
        clientes = self.sessao.query(ModeloCliente).options(
            joinedload(ModeloCliente.interessado), 
            joinedload(ModeloCliente.locatario), 
            joinedload(ModeloCliente.proprietario)).all()

        clientes = [
            self.montar_resposta_clientes(clientes)
            for clientes in clientes
            ]
        
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
        cliente_para_apagar = self.sessao.query(ModeloCliente).filter(ModeloCliente.id == id).first()
        if not cliente_para_apagar:
            return False
        
        self.apagar_cliente_por_tipo(cliente_para_apagar, cliente_para_apagar.tipo)
        
        self.sessao.delete(cliente_para_apagar)
        self.sessao.commit()
        return True
    

    def obter_por_id(self, id: UUID) -> ClienteResponse | False:
        cliente = self.sessao.query(ModeloCliente).filter(
            ModeloCliente.id == id).options(
                joinedload(ModeloCliente.interessado),
                joinedload(ModeloCliente.locatario),
                joinedload(ModeloCliente.proprietario)
            ).first()
        if not cliente:
            return False
             
        return self.montar_resposta_clientes(cliente)
    

    def obter_cliente_locatario_por_id(self, id: UUID) -> ModeloClienteLocatario | None:
        cliente_locatario = self.sessao.query(ModeloClienteLocatario).filter(ModeloClienteLocatario.id_cliente == id).first()
        if not cliente_locatario:
            return False
        

        return cliente_locatario
    

    def obter_cliente_proprietario_por_id(self, id: UUID) -> ModeloClienteProprietario | None:
        cliente_proprietario = self.sessao.query(ModeloClienteProprietario).filter(ModeloClienteProprietario.id_cliente == id).first()
        if not cliente_proprietario:
            return False
        
        return cliente_proprietario
    

    def obter_cliente_interessado_por_id(self, id: UUID) -> ModeloClienteInteressado | None:
        cliente_interessado = self.sessao.query(ModeloClienteInteressado).filter(ModeloClienteInteressado.id_cliente == id).first()
        if not cliente_interessado:
            return False
        
        return cliente_interessado
    

    def listar_clientes_interessados(self) -> list[ClienteResponse]:
        clientes_interessados = self.sessao.query(
            ModeloCliente
            ).options(
                joinedload(ModeloCliente.interessado)
            ).filter(
                ModeloCliente.tipo == "Interessado"
            ).all()

        clientes_interessados = [
            self.montar_resposta_clientes(cliente) for cliente in clientes_interessados
        ]

        return clientes_interessados
    

    def criar_cliente_interessado(self, cliente: ModeloCliente, dados: CriarClienteInteressadoRequest) -> ModeloClienteInteressado:
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
            quantidade_vagas = dados.quantidade_vagas,
            quantidade_andares = dados.quantidade_andares,
            quantidade_salas = dados.quantidade_salas,
        )

        self.sessao.add(cliente_interessado)

        return cliente_interessado
    

    def editar_cliente_interessado(
            self,
            id: UUID,
            dados: ModeloClienteInteressado
    ) -> bool:
        cliente_interessado_para_alterar = self.obter_cliente_interessado_por_id(id)
        if not cliente_interessado_para_alterar:
            return False
        
        cliente_interessado_para_alterar.orcamento = dados.orcamento
        cliente_interessado_para_alterar.orcamento_maximo = dados.orcamento_maximo
        cliente_interessado_para_alterar.procurando = dados.procurando
        cliente_interessado_para_alterar.quantidade_andares = dados.quantidade_andares
        cliente_interessado_para_alterar.quantidade_banheiros = dados.quantidade_banheiros
        cliente_interessado_para_alterar.quantidade_quartos = dados.quantidade_quartos
        cliente_interessado_para_alterar.quantidade_salas = dados.quantidade_salas
        cliente_interessado_para_alterar.quantidade_suites = dados.quantidade_suites
        cliente_interessado_para_alterar.quantidade_vagas = dados.quantidade_vagas

        return True
    

    def apagar_cliente_interessado(self, id: UUID) -> bool:
        cliente_interessado = self.obter_cliente_interessado_por_id(id)
        if not cliente_interessado:
            return False
        
        self.sessao.delete(cliente_interessado)
        return True
    

    def criar_cliente_proprietario(self, cliente: ModeloCliente, dados: CriarClienteProprietarioRequest) -> ModeloClienteProprietario:
        cliente_proprietario = ModeloClienteProprietario(
            id = uuid7(),
            id_cliente = cliente.id,
            imovel_associado = dados.imovel_associado,
        )

        self.sessao.add(cliente_proprietario)

        return cliente_proprietario
    

    def editar_cliente_proprietario(
            self,
            id: UUID,
            dados: ModeloClienteProprietario
    ) -> bool:
        cliente_proprietario_para_alterar = self.obter_cliente_proprietario_por_id(id)
        if not cliente_proprietario_para_alterar:
            return False
        
        cliente_proprietario_para_alterar.imovel_proprietario = dados.imovel_proprietario
        
        return True
    

    def listar_clientes_proprietarios(self) -> list[ClienteResponse]:
        clientes_proprietarios = self.sessao.query(
            ModeloCliente
            ).options(
            joinedload(ModeloCliente.proprietario)
            ).filter(
            ModeloCliente.tipo == 'Proprietário'
            ).all()

        clientes_proprietarios = [
            self.montar_resposta_clientes(cliente) for cliente in clientes_proprietarios
            ]

        return clientes_proprietarios
    

    def apagar_cliente_proprietario(self, id: UUID) -> bool:
        cliente_proprietario = self.obter_cliente_proprietario_por_id(id)
        if not cliente_proprietario:
            return False
        
        self.sessao.delete(cliente_proprietario)
        return True
    

    def criar_cliente_locatario(self, cliente: ModeloCliente, dados: CriarClienteLocatarioRequest) -> ModeloClienteLocatario:
        cliente_locatario = ModeloClienteLocatario(
            id = uuid7(),
            id_cliente = cliente.id,
            imovel_associado = dados.imovel_associado
        )

        self.sessao.add(cliente_locatario)

        return cliente_locatario
    

    def editar_cliente_locatario(
            self,
            id: UUID,
            dados: ModeloClienteLocatario
    ) -> bool:
        cliente_locatario_para_alterar = self.obter_cliente_locatario_por_id(id)
        if not cliente_locatario_para_alterar:
            return False
        
        cliente_locatario_para_alterar.imovel_locatario = dados.imovel_locatario

        return True
    

    def listar_clientes_locatarios(self) -> list[ClienteResponse]:
        clientes_locatarios = self.sessao.query(
            ModeloCliente
            ).options(
            joinedload(ModeloCliente.locatario)
            ).filter(
                ModeloCliente.tipo == 'Locatário'
                ).all()
        
        clientes_locatarios = [
            self.montar_resposta_clientes(cliente) 
            for cliente in clientes_locatarios
        ]

        return clientes_locatarios


    def apagar_cliente_locatario(self, id: UUID) -> bool:
        cliente_locatario = self.obter_cliente_locatario_por_id(id)
        if not cliente_locatario:
            return False
        
        self.sessao.delete(cliente_locatario)
        return True
    

    def apagar_cliente_por_tipo(self, cliente: ModeloCliente, tipo: str):
        if tipo == 'Interessado':
            self.apagar_cliente_interessado(cliente.id)
        elif tipo == 'Locatário':
            self.apagar_cliente_locatario(cliente.id)
        elif tipo == 'Proprietário':
            self.apagar_cliente_proprietario(cliente.id)

    
    def criar_cliente_por_tipo(self, cliente: ModeloCliente, tipo: str, dados_adicionais):
        if tipo == 'Interessado':
            self.criar_cliente_interessado(cliente, dados_adicionais)
        elif tipo == 'Locatário':
            self.criar_cliente_locatario(cliente, dados_adicionais)
        elif tipo == 'Proprietário':
            self.criar_cliente_proprietario(cliente, dados_adicionais)


    def editar_cliente_por_tipo(self, cliente: ModeloCliente, tipo: str, dados_adicionais: Union[ModeloClienteInteressado | ModeloClienteLocatario | ModeloClienteProprietario]):
        if tipo == 'Interessado':
            self.editar_cliente_interessado(cliente.id, dados_adicionais)
        elif tipo == 'Locatário':
            self.editar_cliente_locatario(cliente.id, dados_adicionais)
        elif tipo == 'Proprietário':
            self.editar_cliente_proprietario(cliente.id, dados_adicionais)


    def obter_cliente_por_tipo(self, tipo: str, id: UUID):
        if tipo == 'Interessado':
            self.obter_cliente_interessado_por_id(id)
        elif tipo == 'Locatário':
            self.obter_cliente_locatario_por_id(id)
        elif tipo == 'Proprietário':
            self.obter_cliente_proprietario_por_id(id)


    def montar_resposta_clientes(self, cliente: ModeloCliente) -> ClienteResponse:
        dados_adicionais = self.obter_dados_por_tipo(cliente)

        return ClienteResponse(
            id=cliente.id,
            nome=cliente.nome,
            status=cliente.status,
            codigo=cliente.codigo,
            celular=cliente.celular,
            email=cliente.email,
            tipo=cliente.tipo,
            como_encontrou=cliente.como_encontrou,
            dados_adicionais=dados_adicionais
        )
    

    def obter_dados_por_tipo(self, cliente: ModeloCliente):
        if cliente.tipo == 'Interessado':
            return cliente.interessado
        elif cliente.tipo == 'Locatário':
            return cliente.locatario
        elif cliente.tipo == 'Proprietário':
            return cliente.proprietario
        

