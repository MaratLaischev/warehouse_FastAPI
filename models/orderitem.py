from sqlalchemy import Column, Integer, ForeignKey
from db.database import Base
from sqlalchemy.orm import Session


class OrderItem(Base):
    __tablename__ = 'orderitems'

    id = Column(Integer, primary_key=True, index=True)
    order = Column(
        Integer, ForeignKey('orders.id', ondelete='CASCADE'),
        nullable=False, index=True
    )
    product = Column(
        Integer, ForeignKey('products.id', ondelete='CASCADE'),
        nullable=False, index=True
    )
    quantity = Column(Integer)


def createbulk_order_item(db: Session, order_items):
    order_item_objects = [
        order_item.dict() for order_item in order_items
    ]
    db.bulk_insert_mappings(OrderItem, order_item_objects)
    db.commit()
