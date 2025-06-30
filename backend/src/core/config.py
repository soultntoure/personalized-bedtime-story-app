from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Personalized Bedtime Story Backend"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str
    OPENAI_API_KEY: str
    GOOGLE_TTS_API_KEY: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()