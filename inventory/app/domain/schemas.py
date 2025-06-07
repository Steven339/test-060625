from pydantic import BaseModel


class InventoryOut(BaseModel):
    name: str
    price: float
    quantity: int
