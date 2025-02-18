from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    allowed_origins: str
    allowed_hosts: str
    host: str
    port: int
    reload_value: str 
    
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()