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

@app.get("/api/products/{product_id}")
def geet_product(product_id: int):
    return {
        "id": product_id,
        "name": "Wireless Headphones",
        "description": "High-quality wireless headphones with noise-canceling feature.",
        "price": 99.99,
        "category": "Electronics",
        "availability": "In Stock",
        "specifications": {
            "battery_life": "20 hours",
            "color": "Black",
            "weight": "250g"
        },
        "images": [
            "image1.jpg",
            "image2.jpg"
        ]
    }
