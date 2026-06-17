from fastapi import APIRouter, Depends
from tcc.infraestrutura.conexao import obter_sessao
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/imoveis',
    tags=['Imóveis'],
)