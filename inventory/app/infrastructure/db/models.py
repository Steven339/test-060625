from sqlalchemy import Column, Integer
from sqlalchemy.orm.decl_api import declarative_base

Base = declarative_base()

class InventoryDB(Base):
    __tablename__ = "inventory"
    product_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)