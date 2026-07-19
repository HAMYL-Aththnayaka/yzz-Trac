from fastapi import FastAPI
from models import Products

app = FastAPI()

products = [
    Products(id =1,name ="phone",description="budget item",price=99,quantity=10),
    Products(id =2,name ="Laptop",description="gaming laptop",price=320.00,quantity=12),
    Products(id =3,name ="Watch",description="luxury item",price=109,quantity=9),
    Products(id =4,name ="Camera",description="CCTV Camera",price=89,quantity=5),
]


@app.get("/")
async def greet():
   return {"welcome to yzz Trac"}


@app.get("/products")
async def get_all():
    return products
    
@app.get("/products/{product_id}")
async def get_product_by_id(product_id:int):
    for product in products:
        if product.id == product_id:
            return product       
    return {"Message":"Product not found"}

@app.post("/products")
async def add_product(data:Products):
    products.append(data)
    return "Product has been added"

@app.put("/product/{product_id}")
async def update_product(product_id:int , data:Products):
    for product in products:
        if product.id == product_id:
            if data.name is not None:
                product.name = data.name
            if data.description is not None:
                product.description = data.description
            if data.price is not None:
                product.price = data.price
            if data.quantity is not None:
                product.quantity = data.quantity
            
            return {"message":f"product : {product_id} was Updated successfully"}
    return {"error":f"product {product_id} was not found"}


@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
    for product in products :
        if product.id == product_id:
            products.remove(product)
            return {
                "Message":"Product deleted successfully"
            }
    return {"Message":f"Product:{product_id} was not found"}