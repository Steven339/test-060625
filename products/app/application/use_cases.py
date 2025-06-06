from app.domain.models import Product
from app.domain.repositories import AbstractProductRepository


def create_product(repository: AbstractProductRepository, product: Product):
    return repository.create(product)
