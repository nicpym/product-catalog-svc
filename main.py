from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import List, Dict, Optional
from models import Product, ProductCreate, ProductUpdate
from pydantic import BaseModel

app = FastAPI(title="product-catalog-svc", description="Product Catalog Service", version="0.1.0")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database simulation
fake_db = {
    1: Product(
        id=1,
        name="Wireless Headphones",
        description="High-quality wireless headphones with noise-canceling feature.",
        price=99.99,
        category="Electronics",
        availability="In Stock",
        specifications={
            "battery_life": "20 hours",
            "color": "Black",
            "weight": "250g"
        },
        images=["image1.jpg", "image2.jpg"]
    )
}

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

@app.get("/api/products", response_model=List[Product])
def list_products():
    return list(fake_db.values())

@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    if product_id in fake_db:
        return fake_db[product_id]
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/api/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    new_id = max(fake_db.keys(), default=0) + 1
    new_product = Product(id=new_id, **product.dict())
    fake_db[new_id] = new_product
    return new_product

@app.put("/api/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate):
    if product_id in fake_db:
        existing_product = fake_db[product_id]
        updated_product = existing_product.copy(update=product.dict())
        fake_db[product_id] = updated_product
        return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/api/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    if product_id in fake_db:
        del fake_db[product_id]
        return
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/api/products/search", response_model=List[Product])
def search_products(
    name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    results = [
        product for product in fake_db.values()
        if (name is None or name.lower() in product.name.lower())
        and (category is None or category.lower() == product.category.lower())
        and (min_price is None or product.price >= min_price)
        and (max_price is None or product.price <= max_price)
    ]
    return results

@app.get("/api/products/categories", response_model=List[str])
def get_categories():
    categories = set(product.category for product in fake_db.values())
    return list(categories)

@app.get("/api/products/{product_id}/specifications")
def get_product_specifications(product_id: int):
    if product_id in fake_db:
        return fake_db[product_id].specifications
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/api/products/{product_id}/images", response_model=Product)
def add_product_images(product_id: int, images: List[str]):
    if product_id in fake_db:
        product = fake_db[product_id]
        product.images.extend(images)
        fake_db[product_id] = product
        return product
    raise HTTPException(status_code=404, detail="Product not found")

class SpecificationsUpdate(BaseModel):
    specifications: dict

@app.put("/api/products/{product_id}/specifications", response_model=Product)
def update_product_specifications(product_id: int, specs_update: SpecificationsUpdate):
    if product_id in fake_db:
        product = fake_db[product_id]
        product.specifications = specs_update.specifications
        fake_db[product_id] = product
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/api/products/availability/{availability_status}", response_model=List[Product])
def get_products_by_availability(availability_status: str):
    results = [
        product for product in fake_db.values()
        if product.availability.lower() == availability_status.lower()
    ]
    return results