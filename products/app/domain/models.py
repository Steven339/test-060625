from dataclasses import dataclass

@dataclass
class Product:
    id: init | None = None
    name: str = None
    price: int = None
