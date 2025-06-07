from sqlalchemy.orm import Session

from app.domain.models import Inventory
from app.domain.repositories import AbstractRepository
from app.infrastructure.db.models import InventoryDB


class InventoryRepository(AbstractRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, product_id: int) -> Inventory:
        db_inventory = self.db.query(InventoryDB).filter(InventoryDB.product_id == product_id).first()
        if db_inventory:
            return Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)
        return None

    def update(self, inventory: Inventory) -> Inventory:
        db_inventory = self.db.query(InventoryDB).filter(InventoryDB.product_id == inventory.product_id).first()
        if db_inventory:
            db_inventory.quantity = inventory.quantity
            self.db.commit()
            self.db.refresh(db_inventory)
            return Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)
        else:
            db_inventory = InventoryDB(product_id=inventory.product_id, quantity=inventory.quantity)
            self.db.add(db_inventory)
            self.db.commit()
            self.db.refresh(db_inventory)
            return Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)