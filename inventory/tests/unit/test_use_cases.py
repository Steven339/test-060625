from unittest.mock import patch

from app.application.use_cases import get_inventory, update_inventory
from app.domain.models import Inventory, Product
from app.domain.repositories import AbstractRepository


class FakeRepository(AbstractRepository):
    def get(self, product_id: int) -> Inventory:
        return Inventory(product_id=product_id, quantity=10)

    def update(self, inventory: Inventory) -> Inventory:
        return inventory

@patch("app.application.use_cases.check_product")
def test_get_inventory(mock_check_product):
    mock_check_product.return_value = Product(
        id=1,
        name="Test Product",
        price=10
    )
    repository = FakeRepository()
    product, inventory = get_inventory(repository, 1)
    assert product.id == 1
    assert inventory.quantity == 10
    mock_check_product.assert_called_once_with(1)

@patch("app.application.use_cases.check_product")
def test_update_inventory(mock_check_product):
    mock_check_product.return_value = Product(
        id=1,
        name="Test Product",
        price=10
    )
    repository = FakeRepository()
    product, inventory = update_inventory(repository, 1, 10)
    assert product.id == 1
    assert inventory.quantity == 10
    mock_check_product.assert_called_once_with(1)