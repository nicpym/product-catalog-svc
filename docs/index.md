# Product Catalog Service Documentation

Product Catalog Service.

## Overview

The `Product Catalog Service` is a microservice designed to manage and serve product-related information for an e-commerce platform. It is responsible for maintaining the product inventory, including product details, pricing, categories, and availability. This service allows other microservices, such as the Shopping Cart Service, Order Management Service, and User Account Service, to interact with the product data in a reliable and scalable manner.

## Features

* Product Management: Create, update, and delete product records.
* Category Management: Organize products into categories and subcategories for easier navigation.
* Price Management: Handle different pricing strategies, including discounts and special offers.
* Inventory Tracking: Keep track of stock levels and update availability in real-time.
* Search and Filtering: Allow users to search for products and apply various filters such as category, price range, and availability.
* Product Details: Provide detailed information for each product, including descriptions, images, specifications, and customer reviews.

## API Endpoints

1. Get All Products

**Endpoint:** /api/products
**Method:** GET
**Description:** Retrieve a list of all products in the catalog.

**Request Example:**

```bash
GET /api/products
```

**Response Example:**

```json
[
    {
        "id": "1",
        "name": "Wireless Headphones",
        "description": "High-quality wireless headphones with noise-canceling feature.",
        "price": 99.99,
        "category": "Electronics",
        "availability": "In Stock"
    },
    ...
]
```

2. Get Product by ID

**Endpoint:** /api/products/{id}
**Method:** GET
**Description:** Retrieve detailed information about a specific product by its ID.

**Request Example:**

```bash
GET /api/products/1
```

**Response Example:**


```json
{
    "id": "1",
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
```
