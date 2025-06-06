from app.application.use_cases import create_product as create_product_use_case  # renamed import
from app.domain.schemas import ProductCreate
from app.infrastructure.db.session import SessionLocal
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.infrastructure.db.repositories import ProductRepository

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(request: ProductCreate, db: Session = Depends(get_db)):  # renamed function
    repository = ProductRepository(db)
    product = create_product_use_case(repository, request)  # use renamed import
    return {
        "data":{
            "type": "products",
            "id": product.id,
            "attributes": product
        }
    }