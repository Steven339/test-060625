from abc import ABC, abstractmethod

from app.domain.models import Product


class AbstractProductRepository(ABC):
    """ Interface for product repository """
    @abstractmethod
    def create(self, product: Product) -> Product:
        """ Create product """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        """ Get product by id """
        raise NotImplementedError

    @abstractmethod
    def get_all(self, page: int, size: int) -> list[Product]:
        """ Get all products """
        raise NotImplementedError
    
    @abstractmethod
    def update(self, product: Product) -> Product:
        """ Update product """
        raise NotImplementedError

    @abstractmethod 
    def delete(self, product_id: int) -> bool:
        """ Delete product """
        raise NotImplementedError
