from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    allowed_origins: str = "http://test"
    allowed_hosts: str = "test"
    host: str = "127.0.0.1"
    port: int = 8000
    reload_value: str = "true"
    telex_webhook_url: str = "https://example.com/telex"
    curl_command: str | None = "curl" # might require path/to/curl e.g. `/usr/bin/curl`
    app_logo_url: str = "https://example.com/logo.png"
    app_url: str = "https://example.com"
    target_url: str = "https://example.com/target"
    background_color_hexcode: str = "#FFFFFF"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
