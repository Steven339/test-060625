from abc import ABC, abstractmethod

from app.domain.models import Inventory


class AbstractRepository(ABC):
    """ Interface for inventory repository """
    @abstractmethod
    def get(self, product_id: int) -> Inventory:
        """ Get inventory by product id """
        raise NotImplementedError
    
    @abstractmethod
    def update(self, inventory: Inventory) -> Inventory:
        """ Update inventory """
        raise NotImplementedError
