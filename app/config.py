from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Markazlashgan sozlamalar. Qiymatlar .env faylidan o'qiladi.
    Production muhitida SECRET_KEY va DATABASE_URL albatta almashtirilishi shart.
    """

    app_name: str = "OPTOM MARKET API"
    database_url: str = "sqlite:///./optom_market.db"

    secret_key: str = "CHANGE_THIS_SECRET_KEY_IN_PRODUCTION"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 30

    admin_secret_key: str = "CHANGE_THIS_ADMIN_SESSION_KEY_IN_PRODUCTION"

    cors_origins: str = "*"

    upload_dir: str = "uploads"  # mahsulot suratlari shu papkaga saqlanadi
    documents_dir: str = "static_docs"  # shartnoma namunasi va boshqa hujjatlar shu yerda

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
