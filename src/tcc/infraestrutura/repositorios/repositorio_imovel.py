from datetime import datetime
from tcc.api.schemas.imovel_schemas import CriarImagensImovelRequest, CriarImovelRequest, EditarImovelRequest, ImagensImovelResponse
from sqlalchemy.orm import Session
from uuid import UUID
from uuid6 import uuid7
from tcc.infraestrutura.banco_dados.modelos.modelo_imovel import ModeloImagemImovel, ModeloImovel


class RepositorioImovel:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar_imovel(
            self,
            imovel: CriarImovelRequest,
            imagens: list[CriarImagensImovelRequest]
    ) -> ModeloImovel:
        imovel_para_criar = ModeloImovel(
            id=uuid7(),
            codigo= imovel.codigo,
            proprietario= imovel.proprietario,
            corretor= imovel.corretor,
            tipo= imovel.tipo,
            status= 'ATIVO',
            finalidade= imovel.finalidade,
            logradouro= imovel.logradouro,
            bairro= imovel.bairro,
            cidade= imovel.cidade,
            estado= imovel.estado,
            cep= imovel.cep,
            numero= imovel.numero,
            em_condominio= imovel.em_condominio,
            condominio= imovel.condominio,
            complemento=imovel.complemento,
            valor= imovel.valor,
            valor_condominio= imovel.valor_condominio,
            valor_iptu= imovel.valor_iptu,
            quantidade_quartos= imovel.quantidade_quartos,
            quantidade_suites= imovel.quantidade_suites,
            quantidade_banheiros= imovel.quantidade_banheiros,
            quantidade_vagas= imovel.quantidade_vagas,
            quantidade_andares= imovel.quantidade_andares,
            quantidade_salas= imovel.quantidade_salas,
            eh_mobiliado= imovel.eh_mobiliado,
            criado_em= datetime.now(),
        )

        self.sessao.add(imovel_para_criar)

        self.sessao.flush()

        self.sessao.commit()

        return imovel_para_criar
    

    def editar_imovel(
            self,
            id: UUID,
            dados: EditarImovelRequest
    ) -> bool | ModeloImovel:
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
        imovel.complemento = dados.complemento
        imovel.em_condominio = dados.em_condominio
        imovel.condominio = dados.condominio
        imovel.valor = dados.valor
        imovel.valor_condominio = dados.valor_condominio
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
    

    def apagar_imovel(
            self,
            id: UUID
    ) -> bool:
        imovel = self.obter_imovel_por_id(id)
        
        if not imovel:
            return False
        
        self.sessao.delete(imovel)
        self.sessao.commit()

        return True
    

    def obter_imovel_por_id(
            self,
            id: UUID
    ) -> ModeloImovel | None:
        imovel = self.sessao.query(
            ModeloImovel).filter(
            ModeloImovel.id == id).first()
        
        if not imovel:
            return None
        
        return imovel
    

    def listar_imoveis(
            self
    ) -> list[ModeloImovel]:
        imoveis = self.sessao.query(ModeloImovel).all()

        return imoveis


    def ativar_imovel(
            self,
            id: UUID
    ) -> bool:
        imovel = self.obter_imovel_por_id(id)
        
        if not imovel:
            return False
        
        imovel.status = 'ATIVO'
        imovel.alterado_em = datetime.now()

        self.sessao.commit()

        return True
    

    def inativar_imovel(
            self,
            id: UUID
    ) -> bool:
        imovel = self.obter_imovel_por_id(id)
        
        if not imovel:
            return False
        
        imovel.status = 'INATIVO'
        imovel.alterado_em = datetime.now()

        self.sessao.commit()

        return True
    

    def cadastrar_imagens_imovel(
            self,
            id_imovel: UUID,
            imagens: list[CriarImagensImovelRequest]
    )-> ModeloImagemImovel | list[ModeloImagemImovel] | None:
        
        if not imagens:
            return None
        
        imagens_principais = sum(
        1 for imagem in imagens if imagem.imagem_principal
        )

        if imagens_principais > 1:
            raise ValueError('O imóvel possui mais de uma imagem como principal (front-end).')
        
        imagens_cadastradas = []

        for imagem in imagens:
            imagem_modelo = ModeloImagemImovel(
                id= uuid7(),
                id_imovel=id_imovel,
                imagem= imagem.imagem,
                imagem_principal=imagem.imagem_principal
            )

            self.sessao.add(imagem_modelo)

            imagens_cadastradas.append(imagem_modelo)
        
        self.sessao.commit()

        return imagens_cadastradas
    

    def listar_imagens_imovel(self) -> list[ModeloImagemImovel]:
        imagens = self.sessao.query(ModeloImagemImovel).all()

        return imagens