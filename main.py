from fastapi import FastAPI

from utils.database import create_db_and_table

# The lifespan context manager doesn't need to be async
from contextlib import asynccontextmanager
from modules.users.users_controller import user_router
from modules.products.products_controller import product_router
from modules.carts.carts_controller import cart_router
from fastapi.middleware.cors import CORSMiddleware
from modules.orders.order_controller import order_router


@asynccontextmanager
async def lifespan(app):
    create_db_and_table()
    yield
    

    
      
app=FastAPI(title="Grocery Hub",lifespan=lifespan)
app.include_router(router=user_router)
app.include_router(router=product_router)
app.include_router(router=cart_router)
app.include_router(router=order_router)


# Add the CORS middleware to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods like GET, POST, PUT, DELETE
    allow_headers=["*"],  # Allows all headers
)


