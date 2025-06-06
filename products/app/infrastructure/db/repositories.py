from app.domain.models import Product
from app.infrastructure.db.models import ProductDB
from sqlalchemy.orm import Session
from app.domain.repositories import AbstractProductRepository


class ProductRepository(AbstractProductRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def create(self, product: Product):
        db_product = ProductDB(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return Product(**db_product.dict())

        