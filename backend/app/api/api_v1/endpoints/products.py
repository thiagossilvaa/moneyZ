from fastapi import APIRouter
from typing import List
from app.models.product import Product, ProductCreate
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.product import Product, ProductCreate
from app.models.order import Order

router = APIRouter()

# implementação do endpoint de checkout


@router.post("/checkout")
def checkout(items: list[int], session: Session = Depends(get_session)):
    total = 0
    for item_id in items:
        product = session.get(Product, item_id)
        if product:
            total += product.price_cents

    order = Order(user_id=1, total_cents=total, status="pending")
    session.add(order)
    session.commit()
    session.refresh(order)

    return {"message": "Pedido criado", "order_id": order.id, "total_cents": total}


@router.get("/", response_model=List[Product])
def list_products():
    return []


@router.post("/", response_model=Product)
def create_product(p: ProductCreate):
    raise NotImplementedError


# implementação do endpoint de criação de produto com persistência no banco de dados
router = APIRouter()


@router.post("/", response_model=Product)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product(**product.dict())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

# implementação do endpoint de listagem de produtos publicados


@router.get("/", response_model=list[Product])
def list_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product).where(
        Product.is_published == True)).all()
    return products

# implementação do endpoint de obtenção de produto por ID


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

# implementação do endpoint de listagem de pedidos


@router.get("/orders")
def list_orders(session: Session = Depends(get_session)):
    orders = session.exec(select(Order)).all()
    return orders
