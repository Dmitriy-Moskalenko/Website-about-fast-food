from typing import Optional

from pydantic import BaseModel


# Валидация для User
class UserConfig(BaseModel):
    id: int
    name: str
    email: str
    password: str


# Валидация для Category
class CategoryConfig(BaseModel):
    id: int
    title: str


# Валидация для Product
class ProductConfig(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
