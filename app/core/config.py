import pathlib

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

IS_ENV_FOUND = load_dotenv(
    dotenv_path=pathlib.Path(__file__).parent.parent / ".env"
)


class Settings(BaseSettings):
    """Represents the configuration settings for the application."""

    # BACKEND_CORS_ORIGINS and ALLOWED_HOSTS
    # are a JSON-formatted list of origins
    # For example: ["http://localhost:4200", "https://myfrontendapp.com"]
    BACKEND_CORS_ORIGINS: list[str] = []
    ALLOWED_HOSTS: list[str] = ["localhost:5173", "127.0.0.1"]

    BASE_API_PATH: str
    API_VERSION: str
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str


settings: Settings = Settings()
