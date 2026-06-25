from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from .env
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --------------------------------------------------
    # Application
    # --------------------------------------------------
    PROJECT_NAME: str = "AccuIQ"
    PROJECT_VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    API_V1_PREFIX: str = "/api/v1"

    # --------------------------------------------------
    # Database
    # --------------------------------------------------
    DATABASE_URL: str


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()