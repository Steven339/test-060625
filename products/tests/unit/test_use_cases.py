from app.domain.models import Product
from app.application.use_cases import create_product
from app.domain.repositories import AbstractProductRepository

class FakeRepository(AbstractProductRepository):
    def __init__(self):
        self.products = []
        self.id = 0

    def create(self, product: Product) -> Product:
        product.id = self.id
        self.products.append(product)
        self.id += 1
        return product

    def get_by_id(self, product_id: int) -> Product:
        for product in self.products:
            if product.id == product_id:
                return product
        return None

def test_create_product():
    repository = FakeRepository()
    product = Product(name="Test Product", price=10)
    create_product(repository, product)
    assert len(repository.products) == 1