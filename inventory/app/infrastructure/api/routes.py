from app.application.use_cases import get_inventory, update_inventory
from app.infrastructure.api.dependencies import get_db, get_repository
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/inventory/{product_id}", tags=["Inventory"])
def get_inventory_endpoint(product_id: int, db: Session = Depends(get_db)):
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
    return {
        "data": {
            "type": "inventory",
            "id": product_id,
            "attributes": {
                "quantity": 0
            }
        }
    }

    

@router.post("/inventory/{product_id}", tags=["Inventory"])
def update_inventory_endpoint(product_id: int, quantity: int, db: Session = Depends(get_db)):
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
    return {
        "data": {
            "type": "inventory",
            "id": product_id,
            "attributes": {
                "quantity": 0
            }
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
