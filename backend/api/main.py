from fastapi import FastAPI
from routes import product, order
from db.database import engine
from models.product import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product.router)
app.include_router(order.router)
