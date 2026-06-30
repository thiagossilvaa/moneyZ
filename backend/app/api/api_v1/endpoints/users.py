from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User, UserCreate
from sqlmodel import SQLModel, Field
from typing import Optional

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    # placeholder: create user logic
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/", response_model=List[User])
def list_users():
    # placeholder: list users
    return []


class StudentAccess(SQLModel, table=True):
    table_args = {"extend_existing": True}  # Proteção contra erros de MetaData

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    is_active: bool = True
