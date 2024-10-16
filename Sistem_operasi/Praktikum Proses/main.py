from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Order(BaseModel):
    order_id: int
    customer_name: str
    item: str
    quantity: int
    price: float

# Data pesanan dummy
orders = [
    {"order_id": 1, "customer_name": "Alice", "item": "Laptop", "quantity": 1, "price": 1500.00},
    {"order_id": 2, "customer_name": "Bob", "item": "Smartphone", "quantity": 2, "price": 999.99},
    {"order_id": 3, "customer_name": "Charlie", "item": "Headphones", "quantity": 1, "price": 199.99},
    {"order_id": 4, "customer_name": "Diana", "item": "Monitor", "quantity": 2, "price": 250.00},
    {"order_id": 5, "customer_name": "Eve", "item": "Keyboard", "quantity": 1, "price": 79.99},
    {"order_id": 6, "customer_name": "Frank", "item": "Mouse", "quantity": 3, "price": 49.99},
    {"order_id": 7, "customer_name": "Grace", "item": "Tablet", "quantity": 1, "price": 399.99},
    {"order_id": 8, "customer_name": "Hank", "item": "Camera", "quantity": 1, "price": 1200.00},
    {"order_id": 9, "customer_name": "Ivy", "item": "Printer", "quantity": 1, "price": 150.00},
    {"order_id": 10, "customer_name": "Jack", "item": "Router", "quantity": 2, "price": 59.99}
]

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders
