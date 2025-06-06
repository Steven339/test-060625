from app.domain.models import Product
from app.infrastructure.db.models import Base
from app.infrastructure.db.repositories import ProductRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_test_db():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_product():
    db = get_test_db()
    repository = ProductRepository(db)
    product = Product(name="Test Product", price=10)
    created_product = repository.create(product)

    assert created_product.id is not None
    assert created_product.name == "Test Product"
    assert created_product.price == 10