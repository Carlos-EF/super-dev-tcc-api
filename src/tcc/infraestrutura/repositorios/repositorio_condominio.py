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
        condominio_para_editar = self.sessao.query(
            ModeloCondominio).filter(
                ModeloCondominio.id == id
            ).first()
        
        if not condominio_para_editar:
            return False
        
        condominio_para_editar.nome = condominio.nome
        condominio_para_editar.cep = condominio.cep
        condominio_para_editar.logradouro = condominio.logradouro
        condominio_para_editar.bairro = condominio.bairro
        condominio_para_editar.estado = condominio.estado
        condominio_para_editar.cidade = condominio.cidade

        self.sessao.commit()
        
        return condominio_para_editar
    

    def apagar(
            self,
            id: UUID
    ) -> bool:
        condominio_para_apagar = self.sessao.query(
            ModeloCondominio
        ).filter(
            ModeloCondominio.id == id
        ).first()

        if not condominio_para_apagar:
            return False
        
        self.sessao.delete(condominio_para_apagar)

        self.sessao.commit()

        return True