from app.domain.models import Product
from app.infrastructure.db.models import Base
from app.infrastructure.db.repositories import ProductRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_test_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

def test_create_product():
    db = get_test_db()
    repository = ProductRepository(db)
    product = Product(name="Test Product", price=10)
    created_product = repository.create(product)

    assert created_product.id is not None
    assert created_product.name == "Test Product"
    assert created_product.price == 10

def test_get_product_by_id():
    db = get_test_db()
    repository = ProductRepository(db)
    product = Product(name="Test Product", price=10)
    created_product = repository.create(product)

    retrieved_product = repository.get_by_id(created_product.id)

    assert retrieved_product is not None
    assert retrieved_product.id == created_product.id
    assert retrieved_product.name == "Test Product"
    assert retrieved_product.price == 10

def test_get_products():
    db = get_test_db()
    repository = ProductRepository(db)
    product1 = Product(name="Test Product 1", price=10)
    product2 = Product(name="Test Product 2", price=20)
    repository.create(product1)
    repository.create(product2)

    products = repository.get_all(1, 10)

    assert len(products) == 2

def test_update_product():
    db = get_test_db()
    repository = ProductRepository(db)
    product = Product(name="Test Product", price=10)
    created_product = repository.create(product)

    updated_product = Product(id=created_product.id, name="Updated Product", price=20)
    repository.update(updated_product)

    retrieved_product = repository.get_by_id(created_product.id)

    assert retrieved_product is not None
    assert retrieved_product.id == created_product.id
    assert retrieved_product.name == "Updated Product"
    assert retrieved_product.price == 20

def test_delete_product():
    db = get_test_db()
    repository = ProductRepository(db)
    product = Product(name="Test Product", price=10)
    created_product = repository.create(product)

    repository.delete(created_product.id)

    retrieved_product = repository.get_by_id(created_product.id)

    assert retrieved_product is None
