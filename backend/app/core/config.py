from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "moneyZ"
    DATABASE_URL: str = "sqlite:///./moneyz.db"
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        env_file = ".env"


settings = Settings()
