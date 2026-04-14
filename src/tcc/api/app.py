import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tcc.api.configuracoes import configuracoes
from tcc.api.rotas.corretor_rotas import router as corretor_router


logging.basicConfig(
    level=configuracoes.LOG_LEVEL,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)


logger = logging.getLogger(__name__)


def criar_aplicacao() -> FastAPI:
    if configuracoes.producao:
        logger.info('Iniciando aplicação em modo PRODUÇÃO (Swagger desabilitado)')
        app = FastAPI(
            docs_url= None,
            redoc_url= None,
            openapi_url= None
        )
    else:
        logger.info('Iniciando aplicação em modo DESENVOLVIMENTO (Swagger habilitado)')
        app = FastAPI(
            title='TCC API',
            version='1.0.0',
            docs_url='/docs',
            redoc_url='/redoc',
            openapi_url='/openapi.json',
        )

    logger.info('Configurando middleware de CORS')
    app.add_middleware(
        CORSMiddleware,
        allow_origins =[
            'http://localhost:4200',
        ],
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=['*']
    )


    logger.info('Registrando rotas')
    # Corretor
    app.include_router(corretor_router)


    @app.get(
        '/health',
        tags=["Sistema"],
        summary='Health Check',
        description='Verificando se a API está respondendo'
    )
    def health_check():
        return {
            'status': 'OK',
            'ambiente': configuracoes.AMBIENTE,
            'swagger_habilitado': configuracoes.swagger_habilitado
        }
    logger.info('Aplicação configurada com sucesso.')

    return app



app = criar_aplicacao()