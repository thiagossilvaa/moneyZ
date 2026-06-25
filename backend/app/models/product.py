from sqlmodel import SQLModel, Field
from typing import Optional


class ProductBase(SQLModel):
    title: str
    description: Optional[str] = None
    price_cents: int = 0
    is_published: bool = True


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass
