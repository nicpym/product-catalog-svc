from fastapi import FastAPI

app = FastAPI(title="product-catalog-svc", description="Product Catalog Service", version="0.1.0")

@app.get("/api/products")
def list_products():
    products = [
        {
            "id": "1",
            "name": "Wireless Headphones",
            "description": "High-quality wireless headphones with noise-canceling feature.",
            "price": 99.99,
            "category": "Electronics",
            "availability": "In Stock"
        },
        # Add more products here
    ]
    return products

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}