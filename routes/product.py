from fastapi import APIRouter, Depends, Path, status
from typing import List, Annotated
from pydantic_schemas.product import (ProductCreate, ProductResponse,
                                      ProductUpdate)
from models.product import (create_new_product, get_all_products,
                            delete_product)
from exceptions.product import single_product_exp, update_single_product_exp
from sqlalchemy.orm import Session
from db.database import get_db


router = APIRouter(tags=['Product'])


@router.get('/products', response_model=List[ProductResponse])
async def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.post('/products', response_model=ProductCreate)
async def create_products(
    product: ProductCreate, db: Session = Depends(get_db)
) -> ProductCreate:
    return create_new_product(db=db, prod=product)


@router.get('/products/{id}', response_model=ProductResponse)
async def single_product(
    id: Annotated[int, Path(..., title='Указывается id продукта',
                            ge=1, lt=100)],
    db: Session = Depends(get_db),
):
    return single_product_exp(db=db, id=id)


@router.put('/products/{id}', response_model=ProductResponse)
async def update_product(id: int, product: ProductUpdate,
                         db: Session = Depends(get_db)):
    return update_single_product_exp(id=id, values=dict(product), db=db)


@router.delete('/products/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_products(id: int, db: Session = Depends(get_db)):
    return delete_product(id=id, db=db)
