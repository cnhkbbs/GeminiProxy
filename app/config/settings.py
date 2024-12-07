from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH_SECRET_KEY: str
    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com"
    
    class Config:
        env_file = ".env"

settings = Settings()
