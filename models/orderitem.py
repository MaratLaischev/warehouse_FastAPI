from sqlalchemy import Column, Integer, ForeignKey
from db.database import Base


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
