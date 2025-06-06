from app.domain.models import Product
from app.infrastructure.db.repositories import ProductRepository
from sqlalchemy.orm import Session


def create_product(db: Session, product: Product):
    product_repository = ProductRepository(db)
    return product_repository.create(product)
