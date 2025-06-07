from abc import ABC, abstractmethod

from inventory.app.domain.models import Inventory

class AbstractRepository(ABC):
    @abstractmethod
    def get(self, product_id: int) -> Inventory:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, inventory: Inventory) -> Inventory:
        raise NotImplementedError