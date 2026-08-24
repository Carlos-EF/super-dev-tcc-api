import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions
from tcc.infrastructure.services.supabase_storage import SupabaseStorage
from tcc.api.configurations import configurations

logger = logging.getLogger(__name__)

engine = create_engine(
    configurations.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def get_session() -> Session:
    db = SessionLocal()
    try:
        logger.debug("Sessão de banco de dados criada.")
        yield db
    finally:
        db.close()
        logger.debug("Sessão de banco de dados finalizada.")


supabase: Client = create_client(
    configurations.SUPABASE_URL,
    configurations.SUPABASE_KEY,
    options=ClientOptions(
        auto_refresh_token=False,
        persist_session=False,
        detect_session_in_url=False,
    ),
)


def get_storage():
    settings = configurations

    return SupabaseStorage(
        url=settings.SUPABASE_URL,
        key=settings.SUPABASE_KEY,
        bucket=settings.SUPABASE_BUCKET
    )