import pathlib

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

IS_ENV_FOUND = load_dotenv(
    dotenv_path=pathlib.Path(__file__).parent.parent / ".env"
)


class Settings(BaseSettings):
    """Represents the configuration settings for the application."""

    # ALLOWED_HOSTS
    # is a JSON-formatted list of origins
    # For example: ["http://localhost:4200", "https://myfrontendapp.com"]
    ALLOWED_HOSTS: list[str] = []
    ENVIRONMENT: str = "PROD"

    BASE_API_PATH: str = "v1"
    API_VERSION: str = "0.1.0"
    PROJECT_NAME: str = "Thai Tone Identifier"
    PROJECT_DESCRIPTION: str = "Thai Tone Identifier API"

    SENTRY_DSN: str = ""


settings: Settings = Settings()
