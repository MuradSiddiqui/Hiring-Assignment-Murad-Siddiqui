from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # Load from .env file

# Initialize the settings
settings = Settings()
