from uuid import UUID
from sqlalchemy.orm import Session
from tcc.infraestrutura.banco_dados.modelos.modelo_condominio import ModeloCondominio


class RepositorioCondominio:
    def __init__(
            self,
            sessao: Session
            ):
        self.sessao = sessao


    def criar(
            self,
            condominio: ModeloCondominio
    ) -> ModeloCondominio:
        self.sessao.add(condominio)

        self.sessao.flush()

        self.sessao.commit()

        return condominio
    

    def editar(
            self,
            id: UUID,
            condominio: ModeloCondominio
    ) -> bool | ModeloCondominio:
        condominio = self.sessao.query(
            ModeloCondominio).filter(
                ModeloCondominio.id == id
            ).first()
        
        if not condominio:
            return False
        
        return condominio