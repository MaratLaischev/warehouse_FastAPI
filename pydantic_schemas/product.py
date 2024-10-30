from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
