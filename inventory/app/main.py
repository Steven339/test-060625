import logging

from dotenv import load_dotenv
from fastapi import FastAPI

from app.infrastructure.api.routes import router

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading inventory API...")

import os

print("PRODUCTS_API_KEY:", os.getenv("PRODUCTS_API_KEY"))

app = FastAPI(
    title="Inventory API",
    description="API for managing inventory",
    version="1.0.0",
)

app.include_router(router)
