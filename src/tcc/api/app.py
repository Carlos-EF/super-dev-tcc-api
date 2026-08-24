import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tcc.infrastructure.sql.scripts.seed_condominiums import seed_condominiums
from tcc.infrastructure.sql.scripts.seed_brokers import seed_brokers
from tcc.infrastructure.sql.scripts.seed_clients import seed_clients
from tcc.api.configurations import configurations
from tcc.api.routes.condominium_routes import router as condominium_router
from tcc.api.routes.broker_routes import router as broker_router
from tcc.api.routes.search_cep_routes import router as cep_router
from tcc.api.routes.clients_routes import router as clients_router
from tcc.api.routes.property_routes import router as property_router
from tcc.api.routes.user_routes import router as auth_router

logging.basicConfig(
    level=configurations.LOG_LEVEL,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)

logger = logging.getLogger(__name__)

@asynccontextmanager 
async def lifespan(app: FastAPI): 
    logger.info('Executando seeds de inicialização...')
    
    try: 
        seed_condominiums() 
        logger.info('Seed de condomínios executada com sucesso.') 
        seed_brokers() 
        logger.info('Seed de corretores executada com sucesso.') 
        seed_clients() 
        logger.info('Seed de clientes executada com sucesso.') 
    except Exception as e: 
        logger.exception(f'Erro ao executar seed: {e}') 
    
    yield


def create_app() -> FastAPI:
    if configurations.prod:
        logger.info('Iniciando aplicação em modo PRODUÇÃO (Swagger desabilitado)')
        app = FastAPI(
            docs_url= None,
            redoc_url= None,
            openapi_url= None,
            lifespan=lifespan
        )
    else:
        logger.info('Iniciando aplicação em modo DESENVOLVIMENTO (Swagger habilitado)')
        app = FastAPI(
            title='TCC API',
            version='1.0.0',
            docs_url='/docs',
            redoc_url='/redoc',
            openapi_url='/openapi.json',
            lifespan=lifespan
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
    
    app.include_router(auth_router)
    logger.info('Rota "/auth" registrada com sucesso.')

    app.include_router(condominium_router)
    logger.info('Rota "/condominiums" registrada com sucesso.')

    app.include_router(broker_router)
    logger.info('Rota "/brokers" registrada com sucesso.')
    
    app.include_router(cep_router)
    logger.info('Rota "/cep" registrada com sucesso.')

    app.include_router(clients_router)
    logger.info('Rota "/clients" registrada com sucesso.')

    app.include_router(property_router)
    logger.info('Rota "/propertys" registrada com sucesso.')
    
        
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