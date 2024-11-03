from fastapi import FastAPI
from routes import product
from db.database import engine
from models.product import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product.router)
