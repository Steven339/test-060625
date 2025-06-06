from dataclasses import dataclass

@dataclass
class Product:
    id: int | None = None
    name: str = None
    price: int = None
