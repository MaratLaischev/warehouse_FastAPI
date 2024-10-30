from fastapi import FastAPI
from routes import product


app = FastAPI()


app.include_router(product.router)
