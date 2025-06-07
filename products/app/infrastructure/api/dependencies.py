from app.infrastructure.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.infrastructure.db.repositories import ProductRepository

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repository(db: Session):
    return ProductRepository(db)