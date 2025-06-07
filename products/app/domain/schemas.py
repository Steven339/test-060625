from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Product 1"})
    price: float = Field(..., gt=0, json_schema_extra={"example": 49.99})

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    name: str
    price: float

    class ConfigDict:
        from_attributes = True
