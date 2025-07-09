from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    llm_api_key: str = Field(alias='llm-api-key')
    llm_agent_name: str = Field(alias='llm-agent-name')
    postgres_user: str = Field(alias='postgres-user')
    postgres_password: str = Field(alias='postgres-password')
    postgres_db: str = Field(alias='postgres-db')
    postgres_host: str = Field(alias='postgres-host')
    postgres_port: int = Field(alias='postgres-port')

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # ty: ignore[missing-argument]
