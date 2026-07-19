from sqlalchemy.ext.declarative import declarative_base # pyright: ignore[reportMissingImports]
from sqlalchemy import Column, Integer, String ,Float # pyright: ignore[reportMissingImports]




Base = declarative_base()

class Products(Base):
    
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)
  
  