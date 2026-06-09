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
    ):
        self.sessao.add(condominio)

        self.sessao.flush()

        self.sessao.commit()

        return condominio