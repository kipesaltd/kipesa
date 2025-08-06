import os
from typing import List

from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    APP_ENV: str = "development"
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    DATABASE_URL: str = ""
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000", "http://127.0.0.1:3001"]
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    OPENAI_MAX_TOKENS: int = 500
    OPENAI_TEMPERATURE: float = 0.7
    
    # Chatbot Configuration
    CHATBOT_CACHE_TTL: int = 3600  # 1 hour
    CHATBOT_MAX_HISTORY: int = 10
    CHATBOT_RESPONSE_TIMEOUT: int = 30  # seconds
    
    # Redis Configuration (for caching)
    REDIS_URL: str = ""
    REDIS_DB: int = 0

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def assemble_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",") if i.strip()]
        return v

    model_config = {
        "env_file": os.path.join(os.path.dirname(__file__), '../../.env'),
        "env_file_encoding": 'utf-8',
    }


def get_settings() -> Settings:
    return Settings()
