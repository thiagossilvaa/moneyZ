from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=Token)
def login():
    # placeholder: implement JWT login
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/refresh", response_model=Token)
def refresh():
    raise HTTPException(status_code=501, detail="Not implemented")
