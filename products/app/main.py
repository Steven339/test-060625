from app.infrastructure.api.routes import router
from fastapi import FastAPI

app = FastAPI(
    title="Products API",
    description="API for products",
    version="1.0.0"
)
app.include_router(router)