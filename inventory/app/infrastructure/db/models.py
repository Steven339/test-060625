from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm.decl_api import declarative_base

Base = declarative_base()

class InventoryDB(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)