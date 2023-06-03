from typing import Union

from fastapi import FastAPI
from app.core.config import settings
from beanie import Document, Indexed, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapiurl=settings.API_V1_STR,
)


@app.on_event("startup")
async def app_init():
    """
    initialixe crucial application
    """
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).farm_full_stack_app

    await init_beanie(database=db_client, document_models={})


@app.get("/")
def read_root():
    return {"Hello": "World"}
