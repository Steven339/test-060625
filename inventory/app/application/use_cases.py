import httpx
from app.domain.models import Inventory
from app.domain.repositories import AbstractRepository


def check_product(producto_id: int):
    response = httpx.get(f"http://products:8000/products/{producto_id}")
    if response.status_code != 200:
        raise ValueError("Producto no existe")

def get_inventory(repository: AbstractRepository, product_id: int) -> Inventory:
    check_product(product_id)
    inventory = repository.get(product_id)
    if inventory:
        return Inventory(product_id=inventory.product_id, quantity=inventory.quantity)
    return None

def update_inventory(repository: AbstractRepository, product_id: int, quantity: int) -> Inventory:
    check_product(product_id)
    db_inventory = repository.update(Inventory(product_id=product_id, quantity=quantity))
    if db_inventory:
        return Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)
    return None
