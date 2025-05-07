from pydantic import BaseModel
from uuid import UUID

class CartBase(BaseModel):
    product_id:UUID
    weight:str
    quantity:int
class QuantityUpdateRequest(BaseModel):
    cart_id: UUID
    action: str  