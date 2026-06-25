from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .user import User
from .product import Product


class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    quantity: int = 1


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    total_cents: int = 0
    status: str = "pending"


class OrderCreate(SQLModel):
    user_id: int
    items: List[int]
