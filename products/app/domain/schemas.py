from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., exmaple="Product 1")
    price: int = Field(..., gt=0, example=49.99)

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True
