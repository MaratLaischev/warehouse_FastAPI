from sqlalchemy import Column, Integer, String
from db.database import Base
from sqlalchemy.orm import Session
from pydantic_schemas.product import ProductCreate


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priсe = Column(Integer)
    quantity = Column(Integer)


def get_all_product(db: Session):
    return db.query(Product).all()


def create_new_product(db: Session, prod: ProductCreate):
    db_product = Product(
        title=prod.title, description=prod.description,
        priсe=prod.priсe, quantity=prod.quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
