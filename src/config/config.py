from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    allowed_origins: str
    allowed_hosts: str
    host: str
    port: int
    reload_value: str
    telex_webhook_url: str
    curl_command: str | None = "curl" # might require path/to/curl e.g. `/usr/bin/curl`

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
