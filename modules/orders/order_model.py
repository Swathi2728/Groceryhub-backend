from sqlmodel import SQLModel, Field,select
from typing import List, Optional
from utils.database import Session,engine
from uuid import UUID,uuid4
from datetime import datetime
from modules .orders.order_schema import OrderCreateRequest
from modules .carts .carts_model import Cart
from modules .products.products_model import ProductBase

class Order(SQLModel, table=True):
    order_id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    address: str
    total: float
    order_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = "Placed"

   
class OrderItem(SQLModel, table=True):
    order_item_id: UUID = Field(default_factory=uuid4, primary_key=True)
    order_id: UUID = Field(foreign_key="order.order_id")
    product_id: UUID = Field(foreign_key="productbase.id")
    quantity: int
    weight: str
    price_per_unit: float
    
class OrderDAO:
    def place_order(order_data: OrderCreateRequest, user_id: UUID):
     print("Placing order for user:", user_id)
     print("Order data:", order_data)

     try:

      with Session(engine) as session:
        order = Order(
            order_id=uuid4(),
            user_id=user_id,
            address=order_data.address,
            total=order_data.total
        )
        session.add(order)
        session.flush()  # Ensure order_id is generat
        session.commit()

        for item in order_data.items:
            order_item = OrderItem(
                order_id=order.order_id,
                product_id=item.product_id,
                quantity=item.quantity,
                weight=item.weight,
                price_per_unit=item.price_per_unit
            )
            session.add(order_item)

        session.commit()
        OrderDAO.delete_total_cart(user_id,session)
        return {"message": "Order placed successfully", "order_id": str(order.order_id)}
     except Exception as e:
            print(f"Error placing order: {e}")
            return None
    def delete_total_cart(user_id: UUID, session: Session):
        try:
           
            session.query(Cart).filter(Cart.user_id == user_id).delete()
            session.commit()  
            print(f"Cart for user {user_id} cleared.")
        except Exception as e:
            print(f"Error clearing cart: {e}")
    def get_order_history(user_id: UUID):
      try:
        with Session(engine) as session:
            orders = session.exec(
                select(Order).where(Order.user_id == user_id).order_by(Order.order_date.desc())
            ).all()

            order_list = []
            for order in orders:
                items = session.exec(
                    select(OrderItem).where(OrderItem.order_id == order.order_id)
                ).all()

                item_details = []
                for item in items:
                    product = session.exec(
                        select(ProductBase).where(ProductBase.id == item.product_id)
                    ).first()

                    item_data = {
                        "product_id": str(item.product_id),
                        "product_name": product.product_name if product else "Unknown",
                        "product_img": product.p_img if product else None,
                        "quantity": item.quantity,
                        "weight": item.weight,
                        "price_per_unit": item.price_per_unit
                    }
                    item_details.append(item_data)

                order_data = {
                    "order_id": str(order.order_id),
                    "user_id": str(order.user_id),
                    "address": order.address,
                    "total": order.total,
                    "order_date": order.order_date.isoformat(),
                    "status": order.status,
                    "items": item_details
                }
                order_list.append(order_data)

            return order_list

      except Exception as e:
        print(f"Error retrieving order history: {e}")
        return None
