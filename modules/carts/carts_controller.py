from fastapi import APIRouter,Request
from modules.carts.carts_schema import CartBase,QuantityUpdateRequest
from utils.auth import authenticate
from modules.carts.carts_service import CartService
from uuid import UUID

cart_router=APIRouter(prefix="/Cart",tags=["Carts"])


@cart_router.post("/addproduct")
def add_product_tocart(req:Request,cart:CartBase):
    user_id=authenticate(req)
    return CartService.add_product_tocart(user_id,cart)
@cart_router.get("/getallproducts")
def get_all_product_by_user(req:Request):
    user_id=authenticate(req)
    return CartService.get_all_product_by_user(user_id)
@cart_router.delete("/deleteproducts")
def delete_cart_products_by_user(req:Request,product_id:UUID):
    user_id=authenticate(req)
    return CartService.delete_cart_products_by_user(user_id,product_id)
@cart_router.put("/cart/updatequantity")
def updatequantity(req:Request,update:QuantityUpdateRequest):
    user_id=authenticate(req)
    return CartService.update_quantity(user_id,update)
@cart_router.delete("cart/delete/totalcart")
def delete_total_cart(req:Request):
    user_id=authenticate(req)
    return CartService.delete_total_cart(user_id)


    
    
    
    
    















