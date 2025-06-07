from app.application.use_cases import create_product, get_product_by_id, get_products, update_product, delete_product
from app.domain.schemas import ProductCreate, ProductDataResponse, ProductResponse, ProductListResponse, ProductOut, ProductMeta
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.api.dependencies import get_db, get_repository
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/products", response_model=ProductDataResponse, status_code=status.HTTP_201_CREATED)
async def create_product_endpoint(request: ProductCreate, db: Session = Depends(get_db)):
    repository = get_repository(db)
    product = create_product(repository, request)
    product_out = ProductOut.from_orm(product)
    return ProductDataResponse(data=ProductResponse(type="products", id=product.id, attributes=product_out))

@router.get("/products/{product_id}", response_model=ProductDataResponse)
async def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    repository = get_repository(db)
    product = get_product_by_id(repository, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    product_out = ProductOut.from_orm(product)
    return ProductDataResponse(data=ProductResponse(type="products", id=product.id ,attributes=product_out))

@router.get("/products", response_model=ProductListResponse)
async def get_products_endpoint(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    products = get_products(repository, page, size)
    total = len(products)
    
    return ProductListResponse(
        data=[
            ProductResponse(
                type="products",
                id=p.id,
                attributes=ProductOut.from_orm(p)
            ) for p in products
        ],
        meta=ProductMeta(
            page=page,
            size=size,
            total=total
        )
    )

@router.put("/products/{product_id}", response_model=ProductDataResponse)
async def update_product_endpoint(
    product_id: int,
    request: ProductCreate,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    product = get_product_by_id(repository, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    product.name = request.name
    product.price = request.price
    updated_product = update_product(repository, product)
    product_out = ProductOut.from_orm(updated_product)
    return ProductDataResponse(data=ProductResponse(type="products", id=updated_product.id, attributes=product_out))


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_endpoint(
    product_id: int,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    product = get_product_by_id(repository, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    delete_product(repository, product_id)


@router.get("/health", tags=["System"])
def health_check():
    return {
        "data": {
            "type": "health",
            "id": "status",
            "attributes": {
                "status": "ok"
            }
        }
    }