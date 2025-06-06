from app.domain.models import Product
from app.application.use_cases import create_product, get_product_by_id
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

def test_get_product_by_id():
    repository = FakeRepository()
    product = Product(name="Test Product", price=10)
    created_product = create_product(repository, product)
    retrieved_product = get_product_by_id(repository, created_product.id)
    assert retrieved_product is not None
    assert retrieved_product.name == "Test Product"
    assert retrieved_product.price == 10