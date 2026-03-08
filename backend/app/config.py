import os

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://app_user:app_password@postgres:5432/app_db"
    )

settings = Settings()