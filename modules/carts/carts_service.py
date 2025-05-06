from modules.carts.carts_model import Cart
from uuid import UUID
from modules.carts.carts_model import CartDAO
from modules .products.products_model import ProductDAO
from modules.carts.carts_schema import CartBase,QuantityUpdateRequest
from fastapi import HTTPException



class CartService:
    def add_product_tocart(user_id: UUID, cart: CartBase):
        product_id = cart.product_id
        product = ProductDAO.get_products_by_product_id(product_id)
        cart_item = CartDAO.get_cart_item(user_id, cart)

        if cart_item:
            update_request = QuantityUpdateRequest(cart_id=cart_item.cart_id, action="increase")  # or "decrease"
            updated_item = CartDAO.update_cart_quantity(user_id, update_request)
        else:
            updated_item = CartDAO.addproduct_tocart(user_id, cart)
        

        return {
            "message": "Product added to cart" if not cart_item else "Cart quantity updated",
            "product_id": product.id,
            "product_name": product.product_name,
            "weight": product.product_quantity,
            "quantity": updated_item.quantity,
            "price_per_unit": product.p_price,
        }


        
        
    def get_all_product_by_user(user_id:UUID):
        response = []
        cart_items = CartDAO.get_all_product_by_user(user_id)
        for cart in cart_items:
           product = ProductDAO.get_products_by_product_id(cart.product_id)
           response.append({
            "cart_id":cart.cart_id,
            "product_id": product.id,
            "product_name": product.product_name,
            "price_per_unit": product.p_price,
            "available_weight": product.product_quantity,
            "selected_weight": cart.weight,
            "quantity_in_cart": cart.quantity,
            "product_image":product.p_img,
            "subtotal": cart.quantity * product.p_price

            })
        return response
    def delete_cart_products_by_user(user_id:UUID,product_id:UUID):
        return CartDAO.delete_cart_products_by_user(user_id,product_id)
    def update_quantity(user_id,update:QuantityUpdateRequest):
        return CartDAO.update_cart_quantity(user_id,update)
    def delete_total_cart(user_id:UUID):
        return CartDAO.delete_total_cart(user_id)
         
        
        
        
        
        