from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI(title="product-catalog-svc", description="Product Catalog Service", version="0.1.0")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

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
def get_product(product_id: int):
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
