from sqlmodel import SQLModel, Field,select
from typing import List, Optional
from utils.database import Session,engine
from modules.carts.carts_schema import CartBase,QuantityUpdateRequest
from fastapi import HTTPException


from uuid import UUID,uuid4

class Cart(SQLModel, table=True):
   cart_id:UUID=Field(default_factory=uuid4, primary_key=True)
   user_id: UUID = Field(foreign_key="user.id")  # Foreign key to User
   product_id: UUID = Field(foreign_key="productbase.id")
   quantity:int
   weight:str
   
class CartDAO:
    def addproduct_tocart(user_id:UUID,cart:CartBase):
         with Session(engine) as session:
          new_cart_item = Cart(user_id=user_id, product_id=cart.product_id, weight=cart.weight, quantity=cart.quantity)
          session.add(new_cart_item)
          session.commit()
          session.refresh(new_cart_item)
         return new_cart_item
         
    def get_all_product_by_user(user_id):
         with Session(engine) as session:
            cartdetail=session.exec(select(Cart).where(Cart.user_id==user_id)).all()
            return cartdetail
    def delete_cart_products_by_user(user_id,product_id):
         with Session(engine) as session:
           deletecart=session.exec(select(Cart).where(Cart.user_id==user_id and Cart.product_id==product_id)).first()
           session.delete(deletecart)
           session.commit()
         return {"deleted Succefully"}
   
    def get_cart_item(user_id: int,cart:CartBase) :
         with Session(engine) as session:
           stmt = select(Cart).where(
            Cart.user_id == user_id,
            Cart.product_id == cart.product_id,
            Cart.weight == cart.weight
            )
         return session.scalars(stmt).first()
    def update_cart_quantity(user_id,update: QuantityUpdateRequest):
       with Session(engine) as session:
        cart_item = session.get(Cart, update.cart_id)

        if not cart_item or cart_item.user_id != user_id:
            raise HTTPException(status_code=404, detail="Cart item not found or unauthorized")

        if update.action == "increase":
            cart_item.quantity += 1
        elif update.action == "decrease":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                raise HTTPException(status_code=400, detail="Cannot reduce quantity below 1")
        else:
            raise HTTPException(status_code=400, detail="Invalid action")

        session.add(cart_item)
        session.commit()
        session.refresh(cart_item)

        return cart_item
    def delete_total_cart(user_id:UUID):
        with Session(engine) as session:
           deletecart=session.exec(select(Cart).where(Cart.user_id==user_id)).all()
           session.delete(deletecart)
           session.commit()
        return {"deleted Succefully"}
        



   
      
   
       

            
       
        
        
   
    


