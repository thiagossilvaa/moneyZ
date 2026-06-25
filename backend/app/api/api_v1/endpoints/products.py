from fastapi import APIRouter
from typing import List
from app.models.product import Product, ProductCreate

router = APIRouter()


@router.get("/", response_model=List[Product])
def list_products():
    return []


@router.post("/", response_model=Product)
def create_product(p: ProductCreate):
    raise NotImplementedError
