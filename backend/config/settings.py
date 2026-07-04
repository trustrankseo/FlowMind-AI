from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):

    APP_NAME: str = "FlowMind AI"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"

    PORT: int = 8000


    # AI APIs

    OPENAI_API_KEY: str = ""

    GEMINI_API_KEY: str = ""


    # Database

    DATABASE_URL: str = "sqlite:///./flowmind.db"


    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()