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


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, id: int):
    return db.query(Product).filter(Product.id == id).first()


def create_new_product(db: Session, prod: ProductCreate):
    db_product = Product(
        title=prod.title, description=prod.description,
        priсe=prod.priсe, quantity=prod.quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(id: int, values: dict, db: Session):
    db_product = db.query(Product).filter(Product.id == id)
    db_product.update(values)
    db.commit()
    return db_product.first()


def delete_product(db: Session, id: int):
    destroy = db.query(Product).filter(Product.id == id)
    deleted = destroy.first()
    destroy.delete()
    db.commit()
    return deleted
