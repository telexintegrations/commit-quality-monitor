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
    app_logo_url: str
    app_url: str
    target_url: str
    background_color_hexcode: str
    slack_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
