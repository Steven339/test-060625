from pydantic import BaseModel

class InventoryOut(BaseModel):
    product_id: int
    quantity: int

    class ConfigDict:
        from_attributes = True
