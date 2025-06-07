from dataclasses import dataclass


@dataclass
class Inventory:
    product_id: int
    quantity: int

@dataclass
class Product:
    id: int
    name: str
    price: float