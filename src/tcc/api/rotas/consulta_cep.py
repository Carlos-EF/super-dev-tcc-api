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

    response = requests.get(url)

    if response.status_code == 200:
        resposta_cep = response.json()
    else:
        raise HTTPException(
            status_code=404, 
            detail='CEP não encontrado')

    return resposta_cep