from fastapi import APIRouter
from modules.products.products_schema import ProductCreate,UpdateProduct
from modules.products.products_service import ProductService
from uuid import UUID




product_router=APIRouter(prefix="/products",tags=["Products"])


@product_router.post("/createproduct")
def crete_product(product_create:ProductCreate):
    return ProductService.create_product(product_create)
@product_router.put("/updateproduct{product_id}")
def update_product(update_product:UpdateProduct,product_id:UUID):
    return ProductService.update_product(update_product,product_id)
@product_router.get("/getproducts")
def get_all_product():
    return ProductService.get_all_products()
@product_router.get("/get/{category_name}")
def get_product_by_categoryname(category_name:str):
    return ProductService.get_product_by_categoryname(category_name)
@product_router.get("/search")
def search_products_by_name(name:str,category:str):
    return ProductService.search_products_by_name(name,category)

    

    

