import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tcc.api.configurations import configurations
from tcc.api.routes.condominium_routes import router as condominium_router

logging.basicConfig(
    level=configurations.LOG_LEVEL,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    if configurations.prod:
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

    # Resgistrando rotas
    logger.info('Registrando rotas')
    # Condomínios
    app.include_router(condominium_router)
    logger.info('Rota "/condominio" registrada com sucesso.')

    @app.get(
        '/health',
        tags=["Sistema"],
        summary='Health Check',
        description='Verificando se a API está respondendo'
    )
    def health_check():
        return {
            'status': 'OK',
            'ambiente': configurations.ENVIROMENT,
            'swagger_habilitado': configurations.swagger_on
        }
    logger.info('Aplicação configurada com sucesso.')

    return app

app = create_app()