import logging
from typing import List, Optional

from fastapi import Depends, FastAPI
from sqlmodel import Session

from src.api import api_router

from .database import get_db

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()

# we add all API routes to the Web API framework
app.include_router(api_router, prefix="/v1")


@app.get("/v1")
async def root():
    return {"message": "Hello World"}