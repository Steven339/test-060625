import logging

from dotenv import load_dotenv
from fastapi import FastAPI

from app.infrastructure.api.routes import router

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Loading products API...")


app = FastAPI(
    title="Products API",
    description="API for products",
    version="1.0.0"
)
app.include_router(router)