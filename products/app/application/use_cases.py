from app.domain.models import Product
from app.infrastructure.db.repositories import ProductRepository
from sqlalchemy.orm import Session

from products.app.domain.repositories import AbstractProductRepository


def create_product(repository: AbstractProductRepository, product: Product):
    return repository.create(product)
