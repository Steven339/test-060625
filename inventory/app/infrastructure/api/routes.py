from app.application.use_cases import get_inventory, update_inventory
from app.infrastructure.api.dependencies import get_db, get_repository
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/inventory/{product_id}", tags=["Inventory"])
def get_inventory_endpoint(product_id: int, db: Session = Depends(get_db)):
    try:
        repository = get_repository(db)
        inventory = get_inventory(repository, product_id)
        if inventory:
            return {
                "data": {
                    "type": "inventory",
                    "id": product_id,
                    "attributes": {
                        "quantity": inventory.quantity
                    }
                }
            }
    except ValueError as e:
        return {
            "data": {
                "type": "error",
                "id": product_id,
                "attributes": {
                    "message": str(e)
                },
            }
        }

    

@router.post("/inventory/{product_id}", tags=["Inventory"])
def update_inventory_endpoint(product_id: int, quantity: int, db: Session = Depends(get_db)):
    try:
        repository = get_repository(db)
        inventory = update_inventory(repository, product_id, quantity)
        if inventory:
            return {
                "data": {
                    "type": "inventory",
                    "id": product_id,
                    "attributes": {
                        "quantity": inventory.quantity
                    }
                }
            }
    except ValueError as e:
        return {
            "data": {
                "type": "error",
                "id": product_id,
                "attributes": {
                    "message": str(e)
                },
            }
        }

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
