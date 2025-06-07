from abc import ABC, abstractmethod
from app.domain.models import Product

class AbstractProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError