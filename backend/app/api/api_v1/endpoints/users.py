from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User, UserCreate

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    # placeholder: create user logic
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/", response_model=List[User])
def list_users():
    # placeholder: list users
    return []
