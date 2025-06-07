from app.domain.models import Inventory
from app.infrastructure.db.models import Base
from app.infrastructure.db.repositories import InventoryRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
This is a test for the inventory repository
"""

def get_test_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def test_get_inventory():
    db = get_test_db()
    repository = InventoryRepository(db)
    inventory = repository.get(1)
    assert inventory is None

def test_update_inventory():
    db = get_test_db()
    repository = InventoryRepository(db)
    inventory = repository.update(Inventory(product_id=1, quantity=10))
    assert inventory.quantity == 10