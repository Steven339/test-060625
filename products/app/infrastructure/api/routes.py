from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.application.use_cases import (
    create_product,
    delete_product,
    get_product_by_id,
    get_products,
    update_product,
)
from app.domain.schemas import (
    ProductCreate,
    ProductDataResponse,
    ProductListResponse,
    ProductMeta,
    ProductOut,
    ProductResponse,
)
from app.infrastructure.api.dependencies import get_db, get_repository, verify_api_key

router = APIRouter()

@router.post("/products", response_model=ProductDataResponse, status_code=status.HTTP_201_CREATED, tags=["Products"], dependencies=[Depends(verify_api_key)])
async def create_product_endpoint(request: ProductCreate, db: Session = Depends(get_db)):
    repository = get_repository(db)
    try:
        product = create_product(repository, request)
        product_out = ProductOut.from_orm(product)
        return ProductDataResponse(data=ProductResponse(type="products", id=product.id, attributes=product_out))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product could not be created"
        )

@router.get("/products/{product_id}", response_model=ProductDataResponse, tags=["Products"], dependencies=[Depends(verify_api_key)])
async def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    repository = get_repository(db)
    try:
        product = get_product_by_id(repository, product_id)
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        product_out = ProductOut.from_orm(product)
        return ProductDataResponse(data=ProductResponse(type="products", id=product.id, attributes=product_out))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

@router.get("/products", response_model=ProductListResponse, tags=["Products"], dependencies=[Depends(verify_api_key)])
async def get_products_endpoint(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    try:
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
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve products"
        )

@router.put("/products/{product_id}", response_model=ProductDataResponse, tags=["Products"], dependencies=[Depends(verify_api_key)])
async def update_product_endpoint(
    product_id: int,
    request: ProductCreate,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    try:
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
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product could not be updated"
        )

@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"], dependencies=[Depends(verify_api_key)])
async def delete_product_endpoint(
    product_id: int,
    db: Session = Depends(get_db)
):
    repository = get_repository(db)
    try:
        product = get_product_by_id(repository, product_id)
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        delete_product(repository, product_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product could not be deleted"
        )

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

