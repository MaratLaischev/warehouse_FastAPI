from datetime import date
from sqlalchemy import Column, Integer, String
from db.database import Base
from sqlalchemy.orm import Session


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(String, index=True)
    status = Column(String, index=True)


def get_all_orders(db: Session):
    return db.query(Order).all()


def get_order(db: Session, id: int):
    return db.query(Order).filter(Order.id == id).first()


def create_new_order(db: Session, order):
    db_order = Order(status=order.status, date_created=date.today())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_status(id, db, order):
    db_order = db.query(Order).filter(Order.id == id)
    db_order.update(order.dict())
    db.commit()
    return db_order.first()
