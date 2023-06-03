from pydantic import BaseSettings, AnyHttpUrl
from decouple import config
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1/"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_TOKEN: str = config("JWT_REFRESH_TOKEN", cast=str)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRATION: int = 15
    REFERESH_TOKEN_EXPIRATION: int = 60 * 24 * 7
    BACKEND_COURSE_ORIGIN: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "FARM-STACK_PROJECT"

    # database connection
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    class Config:
        case_sensitive = True


settings = Settings()
