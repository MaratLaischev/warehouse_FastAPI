from sqlalchemy import Column, Integer, String
from db.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(String, index=True)
    status = Column(String, index=True)
