from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, create_model


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

class Order(BaseModel):
    order_id: int

class OrderModel(Order):
    user_id: Optional[int] = None
    user_session_id: Optional[int] = None
    order_state: str
    tax_exempt_p: bool
    in_basket_date: datetime

    class Config:
        orm_mode = True