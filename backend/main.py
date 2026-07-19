from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Products
from database import SessionLocal ,engine
import database_models
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]


app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    Products(id =1,name ="phone",description="budget item",price=99,quantity=10),
    Products(id =2,name ="Laptop",description="gaming laptop",price=320.00,quantity=12),
    Products(id =3,name ="Watch",description="luxury item",price=109,quantity=9),
    Products(id =4,name ="Camera",description="CCTV Camera",price=89,quantity=5),
]

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    #count  = 0
    count = db.query(database_models.Products).count
    
    if count == 0:
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()
    
init_db()

@app.get("/")
async def greet():
   return {"welcome to yzz Trac"}


@app.get("/products")
async def get_all(db:Session =Depends(get_db)):
    db_products = db.query(database_models.Products).all()
    return db_products
    
    
    
@app.get("/products/{product_id}")
async def get_product_by_id(product_id:int , db:Session =Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if db_product:
        return db_product       
    return {"Message":"Product not found"}

@app.post("/products")
async def add_product(data:Products ,db:Session =Depends(get_db)):
    db.add(database_models.Products(**data.model_dump()))
    db.commit()
    return "Product has been added"

@app.put("/products/{product_id}")
async def update_product(product_id:int , data:Products ,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if not db_product:
        return {"Error":f"The id: {product_id} is no valid "}
    
    if data.name is not None:
        db_product.name = data.name
    if data.description is not None:
        db_product.description = data.description
    if data.price is not None:
        db_product.price = data.price
    if data.quantity is not None:
        db_product.quantity = data.quantity
    db.commit()
    return {"Message":f"Product id : {product_id} has been updated "}
    
@app.delete("/products/{product_id}")
async def delete_product(product_id:int , db:Session=Depends(get_db)):
    db_product =db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if not db_product:
        return {"Error":f"The id: {product_id} is no valid "}

    db.delete(db_product)
    db.commit()
    return {"Message":f"Product:{product_id} was Removed"}