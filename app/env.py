from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Server configuration
    server_port: int = 8080
    server_log_level: str = "info"

    # JWT Authentication configuration
    secret_key: str = ""
    algorithm: str = ""
    access_token_expire_minutes: int = 30

    # API key configuration
    api_key: str = ""


SETTINGS = Settings()
