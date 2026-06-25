from sqlmodel import SQLModel, Field
from typing import Optional


class Affiliate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    code: str
    payout_percentage: int = 10


class Commission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    affiliate_id: Optional[int] = Field(default=None, foreign_key="affiliate.id")
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")
    amount_cents: int = 0
