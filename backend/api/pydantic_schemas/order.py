from pydantic import BaseModel
from typing import Optional, List, Literal


class OrderBase(BaseModel):
    status: Optional[Literal['в процессе', 'отправлен', 'доставлен']]


class Order(OrderBase):
    id: Optional[int]

    class Config:
        from_attributes = True


class OrderResponse(Order):
    date_created: Optional[str]


class OrderItems(BaseModel):
    id_product: Optional[int]
    quantity: Optional[int]


class OrderCreate(OrderBase):
    products: Optional[List[OrderItems]]
