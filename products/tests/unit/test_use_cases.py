from app.domain.models import Product
from app.application.use_cases import create_product
from app.infrastructure.repositories import AbstractProductRepository

class FakeRepository(AbstractProductRepository):
    def __init__(self):
        self.products = []

    def create(self, product: Product):
        self.products.append(product)

def test_create_product():
    repository = FakeRepository()
    product = Product(name="Test Product", price=10)
    create_product(repository, product)
    assert len(db.products) == 1