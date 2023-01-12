from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    is_active: Optional[bool] = None
    email: Optional[str] = None
    role: Optional[int]=None
    updated_at: datetime

    class Config:
        orm_mode = True

