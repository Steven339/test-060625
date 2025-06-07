from app.application.use_cases import create_product, get_product_by_id, get_products
from app.domain.schemas import ProductCreate
from app.infrastructure.db.session import SessionLocal
from fastapi import APIRouter, Depends, status
from app.domain.schemas import ProductsListResponse
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
async def create_product_endpoint(request: ProductCreate, db: Session = Depends(get_db)):
    repository = get_repository(db)
    product = create_product(repository, request)
    return {
        "data":{
            "type": "products",
            "attributes": product
        }
    }

@router.get("/products/{product_id}", response_model=dict)
async def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    repository = get_repository(db)
    product = get_product_by_id(repository, product_id)
    if product is None:
        return {"details": "Product not found"}
    return {
        "data":{
            "type": "products",
            "attributes": product
        }
    }

@router.get("/products", response_model=dict)
async def get_products_endpoint(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    products = get_products(repository, page, size)
    total = len(products)
    return {
        "data": [
            {
                "type": "products",
                "attributes": p
            }
            for p in products
        ],
        "meta": {
            "total": total,
            "page": page,
            "size": size
        }
    }