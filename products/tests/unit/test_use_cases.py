from app.domain.models import Product
from app.application.use_cases import create_product, get_product_by_id, get_products, update_product, delete_product
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
    
    def get_all(self, page: int, size: int) -> list[Product]:
        return self.products[(page-1)*size:page*size]
    
    def update(self, product: Product) -> Product:
        for i, p in enumerate(self.products):
            if p.id == product.id:
                self.products[i] = product
                return product
        return None

    def delete(self, product_id: int) -> bool:
        for i, product in enumerate(self.products):
            if product.id == product_id:
                del self.products[i]
                return True
        return False


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

def test_get_products():
    repository = FakeRepository()
    product1 = Product(name="Test Product 1", price=10)
    product2 = Product(name="Test Product 2", price=20)
    create_product(repository, product1)
    create_product(repository, product2)
    products = get_products(repository, 1, 10)
    assert len(products) == 2

def test_get_products_page_size():
    repository = FakeRepository()
    for i in range(100):
        create_product(repository, Product(name=f"Test Product {i}", price=10))
    products = get_products(repository, 1, 10)
    assert len(products) == 10

def test_update_product():
    repository = FakeRepository()
    product = Product(name="Test Product", price=10)
    created_product = create_product(repository, product)
    created_product.name = "Test Product 2"
    updated_product = update_product(repository, created_product)
    assert updated_product.name == "Test Product 2"

def test_delete_product():
    repository = FakeRepository()
    product = Product(name="Test Product", price=10)
    created_product = create_product(repository, product)
    assert len(repository.products) == 1
    delete_product(repository, created_product.id)
    assert len(repository.products) == 0
