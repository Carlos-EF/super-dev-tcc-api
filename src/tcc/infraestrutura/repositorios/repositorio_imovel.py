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