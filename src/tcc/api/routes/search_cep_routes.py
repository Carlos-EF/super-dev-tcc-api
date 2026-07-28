from fastapi import APIRouter, HTTPException
import requests


router = APIRouter(
    prefix='/ceps',
    tags=['CEP']
)
@router.get(
    '/{cep}'
)
def search_cep(
    cep: str
):
    url = f'https://brasilapi.com.br/api/cep/v2/{cep}'

    response = requests.get(url)
    if response.status_code == 400:
        raise HTTPException(
            status_code=400,
            detail='CEP inválido ou mal formatado.'
        )
    elif response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail='CEP não encontrado em nenhum provedor.'
        )
    elif response.status_code == 500:
        raise HTTPException(
            status_code=500,
            detail='Ocorreu um erro interno no serviço de CEP.'
        )

    return response.json()