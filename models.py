from pydantic import BaseModel
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category: str
    availability: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    specifications: Optional[dict] = None
    images: Optional[List[str]] = None

    class Config:
        orm_mode = True
