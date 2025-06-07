from app.domain.models import Product
from app.domain.repositories import AbstractProductRepository


def create_product(repository: AbstractProductRepository, product: Product):
    return repository.create(product)

def get_product_by_id(repository: AbstractProductRepository, product_id: int):
    return repository.get_by_id(product_id)

def get_products(repository: AbstractProductRepository, page: int, size: int):
    return repository.get_all(page, size)

def update_product(repository: AbstractProductRepository, product: Product):
    return repository.update(product)

def delete_product(repository: AbstractProductRepository, product_id: int):
    return repository.delete(product_id)
    