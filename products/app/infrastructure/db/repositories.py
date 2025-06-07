from app.domain.models import Product
from app.infrastructure.db.models import ProductDB
from sqlalchemy.orm import Session
from app.domain.repositories import AbstractProductRepository


class ProductRepository(AbstractProductRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def create(self, product: Product) -> Product:
        db_product = ProductDB(
            name=product.name,
            price=product.price,
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return Product(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
        )
    
    def get_by_id(self, product_id: int) -> Product:
        db_product = self.db.query(ProductDB).filter(ProductDB.id == product_id).first()
        if db_product is None:
            return None
        return Product(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
        )

    def get_all(self, page: int, size: int) -> list[Product]:
        db_products = self.db.query(ProductDB).offset((page - 1) * size).limit(size).all()
        return [
            Product(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
            )
            for db_product in db_products
        ]
    
    def update(self, product: Product) -> Product:
        db_product = self.db.query(ProductDB).filter(ProductDB.id == product.id).first()
        if db_product is None:
            return None
        db_product.name = product.name
        db_product.price = product.price
        self.db.commit()
        self.db.refresh(db_product)
        return Product(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
        )
    
    def delete(self, product_id: int) -> bool:
        db_product = self.db.query(ProductDB).filter(ProductDB.id == product_id).first()
        if db_product is None:
            return None
        self.db.delete(db_product)
        self.db.commit()
        return True