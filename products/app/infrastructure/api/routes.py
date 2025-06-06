from app.application.use_cases import create_product
from app.domain.schemas import ProductCreate
from app.infrastructure.db.session import SessionLocal
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_product(request: ProductCreate, db: Session = Depends(get_db)):  # noqa: F811
    product = create_product(db, request)
    return {
        "data":{
            "type": "products",
            "id": product.id,
            "attributes": product
        }
    }
