from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "FlowMind AI"
    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    OPENAI_API_KEY: str = ""

    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.5-flash"
    GEMINI_IMAGE_MODEL: str = "imagen-4.0-generate-001"
    GEMINI_VIDEO_MODEL: str = "veo-3.0-generate-001"
    GEMINI_TTS_MODEL: str = "gemini-2.5-flash-preview-tts"

    ELEVENLABS_API_KEY: str = ""

    GITHUB_TOKEN: str = ""

    DATABASE_URL: str = "sqlite:///./flowmind.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()