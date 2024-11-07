from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priсe: Optional[int]
    quantity: Optional[int]


class Product(ProductBase):
    id: Optional[int]

    class Config:
        from_attributes = True


class ProductResponse(Product):
    pass


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass
