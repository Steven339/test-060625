from app.application.use_cases import create_product, get_product_by_id
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

def get_repository(db: Session):
    return ProductRepository(db)

@router.post("/products", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(request: ProductCreate, db: Session = Depends(get_db)):
    repository = get_repository(db)
    product = create_product(repository, request)
    return {
        "data":{
            "type": "products",
            "id": product.id,
            "attributes": product
        }
    }

@router.get("/products/{product_id}", response_model=dict)
def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    repository = get_repository(db)
    product = get_product_by_id(repository, product_id)
    if product is None:
        return {"message": "Product not found"}
    return {
        "data":{
            "type": "products",
            "id": product.id,
            "attributes": product
        }
    }