from fastapi import APIRouter, HTTPException
import requests


router = APIRouter(
    prefix='/cep',
    tags=['Consulta CEP'],
)

@router.get('/{cep}')
def consultar_cep(
    cep: str):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    resposta_cep = requests.get(url)
    if resposta_cep.status_code != 200:
        raise HTTPException(
            status_code=404, 
            detail='CEP não encontrado')
    
    dados_cep = resposta_cep.json()
    if 'erro' in dados_cep:
        raise HTTPException(
            status_code=404, 
            detail='CEP não encontrado')
    
    return dados_cep