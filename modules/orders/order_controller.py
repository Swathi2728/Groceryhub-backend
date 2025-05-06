from fastapi import APIRouter,Request
from modules .orders.order_schema import OrderCreateRequest
from modules .orders.order_service import OrderService


from utils.auth import authenticate




order_router=APIRouter(prefix="/Order",tags=["Orders"])
@order_router.post("/placeorder")
def  place_order(order_data: OrderCreateRequest,req:Request):
    user_id=authenticate(req)
    return OrderService.place_order(order_data,user_id)
@order_router.get("/vieworder/history")

def get_order_history(req:Request):
    user_id=authenticate(req)
    return OrderService.get_order_history(user_id)
    
    
    

