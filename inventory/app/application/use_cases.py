from app.domain.models import Inventory

def get_inventory(repository, product_id: int) -> Inventory:
    inventory = repository.get(product_id)
    if inventory:
        return Inventory(product_id=inventory.product_id, quantity=inventory.quantity)
    return None

def update_inventory(repository, inventory: Inventory) -> Inventory:
    db_inventory = repository.update(inventory)
    if db_inventory:
        return Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)
    return None


