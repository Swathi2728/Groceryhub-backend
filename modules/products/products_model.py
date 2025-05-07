from sqlmodel import SQLModel, Field,select
from typing import List,Dict
from utils.database import Session,engine
from uuid import UUID,uuid4
from sqlalchemy import Column, Float
from .products_schema import UpdateProduct







class ProductBase(SQLModel,table=True):
    id:UUID=Field(primary_key=True,default_factory=uuid4)
    product_name: str  
    p_img: str         
    p_price:float
    product_quantity:str
    category_name: str
    
class ProductDAO:
    def create_products(products:ProductBase):
        with Session(engine) as session:
            session.add(products)
          
            session.commit()
        return {"Status": "201 Created"}
    def update_product(update_product:UpdateProduct,product_id:UUID):
        with Session(engine) as session:
            product=session.exec(select(ProductBase).where(ProductBase.id==product_id)).first()
            if not product:
                return {"error": "product not found"}
            product.product_name=update_product.product_name
            product.category_name=update_product.category_name
            product.p_img=update_product.p_img
            product.p_price=update_product.p_price
            product.product_quantity=update_product.product_quantity
            session.add(product)
            session.commit( )
            session.refresh(product)
        return {"product Updated succefully"}
    def get_all_products():
        with Session(engine) as session:
         products = session.exec(select(ProductBase)).all()
        return products
    def get_product_by_categoryname(category_name:str):
        with Session(engine) as session:
         products_in_category = session.exec(
            select(ProductBase).where(
                ProductBase.category_name==category_name
            )
        ).all()
        return products_in_category
    def select_products_by_name(name:str,category:str):
        with Session(engine) as session:
         query = select(ProductBase).where(
            ProductBase.product_name.ilike(f"%{name}%"),
            ProductBase.category_name == category
        )
        result = session.exec(query)
        return result.all()

    def get_products_by_product_id(product_id:UUID):
        with Session(engine) as session:
            products=session.exec(select(ProductBase).where(ProductBase.id==product_id)).first()
        return products
    
            
        
        
    
    
    

    