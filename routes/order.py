from fastapi import APIRouter, Depends, Path
from typing import List, Annotated
from pydantic_schemas.order import OrderResponse, OrderCreate, OrderBase
from models.order import get_all_orders
from exceptions.order import (create_order_exp, single_order_exp,
                              update_status_exp)
from sqlalchemy.orm import Session
from db.database import get_db


router = APIRouter(tags=['Order'])


@router.get('/orders', response_model=List[OrderResponse])
async def get_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)


@router.get('/orders/{id}', response_model=OrderResponse)
async def single_order(
    id: Annotated[int, Path(..., title='Указывается id заказа', ge=1)],
    db: Session = Depends(get_db),
):
    return single_order_exp(db=db, id=id)


@router.post('/orders', response_model=OrderResponse)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order_exp(db=db, order=order)


@router.patch('/products/{id}/status/', response_model=OrderResponse)
async def update_status(id: int, order: OrderBase,
                        db: Session = Depends(get_db)):
    return update_status_exp(id=id, db=db, order=order)
