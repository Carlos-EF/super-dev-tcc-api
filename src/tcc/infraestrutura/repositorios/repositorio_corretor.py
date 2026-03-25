from uuid import UUID
from sqlalchemy.orm import Session
from tcc.infraestrutura.banco_dados.modelos.modelo_corretor import ModeloCorretor


class RepositorioCorretor:
    def __init__(
        self,
        sessao: Session
        ):
        self.sessao = sessao

    
    def criar(
        self,
        corretor: ModeloCorretor
    ) -> ModeloCorretor:
        self.sessao.add(corretor)
        self.sessao.commit()
        self.sessao.flush(corretor)

        return corretor