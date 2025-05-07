from typing import List
from pydantic import BaseModel
from uuid import UUID

class OrderItemRequest(BaseModel):
    product_id: UUID
    quantity: int
    weight: str
    price_per_unit: float

class OrderCreateRequest(BaseModel):
    address: str
    total: float
    items: List[OrderItemRequest]
