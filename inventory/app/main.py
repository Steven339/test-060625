from fastapi import FastAPI
from app.infrastructure.api.routes import router

app = FastAPI(
    title="Inventory API",
    description="API for managing inventory",
    version="1.0.0",
)

app.include_router(router)
