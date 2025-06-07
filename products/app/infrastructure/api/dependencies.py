import logging

from fastapi import Header, HTTPException, status
from sqlalchemy.orm import Session

from app.config import API_KEY
from app.infrastructure.db.repositories import ProductRepository
from app.infrastructure.db.session import SessionLocal

logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repository(db: Session):
    return ProductRepository(db)


def verify_api_key(x_api_key: str = Header(...)):
    logger.info("Verifying api key... %s, %s", x_api_key, API_KEY)
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Api key not valid"
        )