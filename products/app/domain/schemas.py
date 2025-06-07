from typing import List
from pydantic import BaseModel, Field
from app.infrastructure.db.models import ProductDB


class ProductBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Product 1"})
    price: float = Field(..., gt=0, json_schema_extra={"example": 49.99})

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_orm(cls, db_product: ProductDB):
        return cls(
            name=db_product.name,
            price=db_product.price
        )

class ProductResponse(BaseModel):
    type: str = "products"
    id : int
    attributes: ProductOut

    class ConfigDict:
        from_attributes = True

class ProductDataResponse(BaseModel):
    data: ProductResponse

    class ConfigDict:
        from_attributes = True

class ProductMeta(BaseModel):
    total: int
    page: int
    size: int

class ProductListResponse(BaseModel):
    data: List[ProductResponse]
    meta: ProductMeta

    class ConfigDict:
        from_attributes = True