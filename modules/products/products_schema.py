from pydantic import BaseModel
from typing import List,Dict


class ProductCreate(BaseModel):
    product_name: str  
    p_img: str         
    p_price: float
    product_quantity:str
    category_name: str

class UpdateProduct(BaseModel):
    product_name: str  
    p_img: str         
    p_price: float
    product_quantity:str
    category_name: str
    

    

    
    