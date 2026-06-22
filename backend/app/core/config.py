from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):

    # Application
    APP_NAME: str = os.getenv("APP_NAME", "URL Shortener SaaS")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

    # MongoDB
    MONGODB_URI: str = os.getenv("MONGODB_URI","mongodb://localhost:27017")
    MONGODB_DATABASE: str = os.getenv("MONGODB_DATABASE","url_shortener")

    # JWT
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY","your-secret-key")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM","HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

    SECRET_KEY: str = os.getenv("SECRET_KEY","url_shortener")

    # Email
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.example.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME", "your-email@example.com")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "your-password")
    SMTP_FROM_EMAIL: str = os.getenv("SMTP_FROM_EMAIL", "noreply@example.com")

    # Email Verification
    EMAIL_VERIFICATION_EXPIRE_HOURS: int = int(os.getenv("EMAIL_VERIFICATION_EXPIRE_HOURS", 24))
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    class Config:
      env_file = "../.env"
      case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()