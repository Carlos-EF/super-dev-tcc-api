from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Configuracoes(BaseSettings):
    DATABASE_URL: str

    AMBIENTE: str = 'dev'

    LOG_LEVEL: str = 'INFO'

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent.parent.parent / '.env'),
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    @property
    def producao(self) -> bool:
        return self.AMBIENTE.lower() == 'prod'
    @property
    def swagger_habilitado(self) -> bool:
        return not self.producao
    

configuracoes = Configuracoes()