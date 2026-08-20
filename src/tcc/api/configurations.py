from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Configurations(BaseSettings):
       DATABASE_URL: str

       SUPABASE_URL: str
       SUPABASE_KEY: str
       SUPABASE_BUCKET: str

       ENVIROMENT: str = 'dev'

       LOG_LEVEL: str = 'INFO'

       model_config = SettingsConfigDict(
            env_file=str(
                Path(__file__).parent.parent.parent.parent / '.env'
            ),
            env_file_encoding='utf-8',
            case_sensitive=False,
            extra='ignore'
        )

       @property
       def prod(self) -> bool:
        return self.ENVIROMENT.lower() == 'prod'

       @property
       def swagger_on(self) -> bool:
        return not self.prod
    

configurations = Configurations()