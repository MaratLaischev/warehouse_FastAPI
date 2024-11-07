from fastapi import status, HTTPException
from models.product import Product, quantity_reservation
from models.order import create_new_order, get_order, update_status
from models.orderItem import createbulk_order_item
from pydantic_schemas.orderitem import CreatOrderItem


def checking_availability_and_product(product: Product, value: dict[str: int]):
    '''Проверка наличия продуктов в ассортименте'''
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product (id: {value['id_product']}) not found!'
        )
    if product.quantity < value['quantity']:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product (id: {value.id_product}) not enough in stock!'
        )


def object_creation_schem_orderitem(dborder, order):
    order_items = []
    for product in order.products:
        order_item = CreatOrderItem(
            order=dborder.id, product=product.id_product,
            quantity=product.quantity
        )
        order_items.append(order_item)
    return order_items


def create_order_exp(db, order):
    for value_product in order.products:
        value_product = dict(value_product)
        db_product = db.query(Product).filter(
            Product.id == value_product['id_product']
        )
        product = db_product.first()
        checking_availability_and_product(product, value_product)
        value_product['quantity'] = (
            product.quantity - value_product['quantity']
        )
        del value_product['id_product']
        quantity_reservation(db=db, db_product=db_product, value=value_product)
    db_order = create_new_order(db=db, order=order)
    order_items = object_creation_schem_orderitem(db_order, order)
    createbulk_order_item(db, order_items=order_items)
    return db_order


def single_order_exp(id, db):
    order = get_order(id=id, db=db)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Order not found!')
    return order


def update_status_exp(id, db, order):
    single_order_exp(id=id, db=db)
    return update_status(id=id, db=db, order=order)
