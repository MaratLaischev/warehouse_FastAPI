from fastapi import status, HTTPException
from models.product import get_product, update_product


def single_product_exp(id, db):
    product = get_product(id=id, db=db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Product not found!')
    return product


def update_single_product_exp(id, values, db):
    product = update_product(id=id, values=values, db=db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='You cannot perform this action!')
    return product
