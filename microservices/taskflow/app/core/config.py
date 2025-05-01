from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # retrocede 2 niveles hasta taskflow/
ENV_PATH = BASE_DIR / ".env"
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ENV_PATH

settings = Settings()
