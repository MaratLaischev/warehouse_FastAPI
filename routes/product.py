from fastapi import APIRouter
from typing import Optional, Dict
from pydantic_schemas.product import Product


router = APIRouter(tags=['Product'])


@router.get('/products')
async def get_products() -> Dict[str, Optional[Product]]:
    return {'data': 'massage'}


@router.post('/products')
async def create_products():
    return 'create'


@router.get('/products/{id}')
async def single_product(id: int):
    return 1


@router.put('/products/{id}')
async def update_product(id: int):
    return 2


@router.delete('/products/{id}')
async def delete_product(id: int):
    return 3
