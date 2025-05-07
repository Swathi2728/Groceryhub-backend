from modules .products .products_model import ProductBase
from modules .products .products_schema import ProductCreate,UpdateProduct
from modules .products .products_model import ProductDAO
from uuid import UUID

class ProductService:
    def create_product(create_product:ProductCreate):
        products=ProductBase(
            product_name=create_product.product_name,
            p_img=create_product.p_img,
            p_price=create_product.p_price,
            product_quantity=create_product.product_quantity,
            category_name=create_product.category_name
        )
        ProductDAO.create_products(products)
        return {"status":"201 created"}
    def update_product(update_product:UpdateProduct,product_id:UUID):
        return ProductDAO.update_product(update_product,product_id)
    def get_all_products():
        return ProductDAO.get_all_products()
    def get_product_by_categoryname(category_name:str):
        return ProductDAO.get_product_by_categoryname(category_name)
    def search_products_by_name(name:str,category:str):
        return ProductDAO.select_products_by_name(name,category)
    def get_products_by_product_id(product_id:UUID):
        return ProductDAO.get_products_by_product_id(product_id)
    
        