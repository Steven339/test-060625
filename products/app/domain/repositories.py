from abc import ABC, abstractmethod
from app.domain.models import Product

class AbstractProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, page: int, size: int) -> list[Product]:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod 
    def delete(self, product_id: int) -> bool:
        raise NotImplementedError