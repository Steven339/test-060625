from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.application.use_cases import get_inventory, update_inventory
from app.domain.schemas import InventoryOut
from app.infrastructure.api.dependencies import get_db, get_repository, verify_api_key

router = APIRouter()


@router.get("/inventory/{product_id}", tags=["Inventory"], dependencies=[Depends(verify_api_key)])
def get_inventory_endpoint(product_id: int, db: Session = Depends(get_db)):
    print("get_inventory_endpoint")
    try:
        repository = get_repository(db)
        product, inventory = get_inventory(repository, product_id)
        if inventory:
            return {
                "data": {
                    "type": "inventory",
                    "id": product_id,
                    "attributes": InventoryOut(
                        name=product.name,
                        price=product.price,
                        quantity=inventory.quantity
                    )
                }
            }
        else:
            raise HTTPException(
                status_code=404,
                detail="Inventory not found"
            )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/inventory/{product_id}", tags=["Inventory"], dependencies=[Depends(verify_api_key)])
def update_inventory_endpoint(product_id: int, quantity: int, db: Session = Depends(get_db)):
    try:
        repository = get_repository(db)
        product ,inventory = update_inventory(repository, product_id, quantity)
        if inventory:
            return {
                "data": {
                    "type": "inventory",
                    "id": product_id,
                    "attributes": InventoryOut(
                        name=product.name,
                        price=product.price,
                        quantity=inventory.quantity
                    )
                }
            }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/health", tags=["System"])
def health_check():
    return {
        "type": "health",
        "id": "status",
        "attributes": {
            "status": "ok"
        }
    }

