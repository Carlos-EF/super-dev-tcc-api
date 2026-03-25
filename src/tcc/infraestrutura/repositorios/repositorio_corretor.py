from uuid import UUID
from sqlalchemy.orm import Session
from datetime import datetime
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
    

    def editar(
            self,
            id: UUID,
            nome: str,
            celular: int,
            email: str,
            data_nascimento: datetime,
            rg: int,
            cpf: int
    ):
        corretor = self.sessao.query(ModeloCorretor).filter(ModeloCorretor.id == id).first()
        if not corretor:
            return False
        
        corretor.nome_completo = nome
        corretor.celular = celular
        corretor.email = email
        corretor.data_nascimento = data_nascimento
        corretor.rg = rg
        corretor.cpf = cpf

        self.sessao.commit()
        return True
    

    def listar(
            self
    ) -> list[ModeloCorretor]:
        corretores = self.sessao.query(ModeloCorretor).all()

        return corretores
    

    def obter_por_id(
            self,
            id: UUID
    ) -> ModeloCorretor | None:
        corretor = self.sessao.query(ModeloCorretor).filter(ModeloCorretor.id == id).first()
        if not corretor:
            return False
        
        return corretor
    

    def apagar(
            self,
            id: UUID
    ):
        corretor = self.sessao.query(ModeloCorretor).filter(ModeloCorretor.id == id).first()
        if not corretor:
            return False
        
        self.sessao.delete(corretor)
        self.sessao.commit()
        return True
    

    def ativar(
            self,
            id: UUID
    ):
        corretor = self.sessao.query(ModeloCorretor).filter(ModeloCorretor.id == id).first()
        if not corretor:
            return False

        corretor.status = "ATIVO"
        self.sessao.commit()
        return True