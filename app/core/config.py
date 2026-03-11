from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Agentic Financial Research API"
    app_version: str = "0.1.0"

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    price_csv_path: str = "/app/data/stock_prices.csv"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()