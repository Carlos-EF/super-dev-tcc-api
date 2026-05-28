from datetime import datetime
from tcc.api.schemas.imovel_schemas import CriarImovelRequest, EditarImovelRequest
from sqlalchemy.orm import Session
from uuid import UUID
from uuid6 import uuid7
from tcc.infraestrutura.banco_dados.modelos.modelo_imovel import ModeloImovel


class RepositorioImovel:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar_imovel(
            self,
            imovel: ModeloImovel
    ) -> ModeloImovel:
        self.sessao.add(imovel)

        self.sessao.flush()

        self.sessao.commit()

        return imovel
    

    def editar_imovel(
            self,
            id: UUID,
            dados: EditarImovelRequest
    ) -> bool:
        imovel = self.sessao.query(
            ModeloImovel).filter(
            ModeloImovel.id == id).first()
        
        if not imovel:
            return False
        
        imovel.tipo = dados.tipo
        imovel.finalidade = dados.finalidade
        imovel.logradouro = dados.logradouro
        imovel.bairro = dados.bairro
        imovel.cidade = dados.cidade
        imovel.estado = dados.estado
        imovel.cep = dados.cep
        imovel.numero = dados.numero
        imovel.eh_condominio = dados.eh_condominio
        imovel.valor = dados.valor
        imovel.valor_iptu = dados.valor_iptu
        imovel.quantidade_quartos = dados.quantidade_quartos
        imovel.quantidade_suites = dados.quantidade_suites
        imovel.quantidade_banheiros = dados.quantidade_banheiros
        imovel.quantidade_vagas = dados.quantidade_vagas
        imovel.quantidade_andares = dados.quantidade_andares
        imovel.quantidade_salas = dados.quantidade_salas
        imovel.eh_mobiliado = dados.eh_mobiliado
        imovel.alterado_em = datetime.now()

        self.sessao.commit()

        return imovel