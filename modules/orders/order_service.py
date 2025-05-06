from uuid import UUID,uuid4
from modules.orders.order_model import OrderDAO
from modules .orders.order_schema import OrderCreateRequest









class OrderService:
    def place_order(order_data:OrderCreateRequest,user_id:UUID):
        return OrderDAO.place_order(order_data,user_id)
    def get_order_history(user_id:UUID):
        return OrderDAO.get_order_history(user_id)
    
        
