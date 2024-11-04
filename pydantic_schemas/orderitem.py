from pydantic import BaseModel
from typing import Optional


class OrderItemBase(BaseModel):
    order: Optional[int]
    product: Optional[int]
    quantity: Optional[int]


class OrderItem(OrderItemBase):
    id: Optional[int]

    class Config:
        from_attributes = True


class CreatOrderItem(OrderItemBase):
    pass
