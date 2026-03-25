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