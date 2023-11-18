from pydantic import BaseModel
from typing import List

class User(BaseModel):
    email: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int

class ProductSearchResult(BaseModel):
    products: List[Product]

class SessionData(BaseModel):
    searchQuery: str
    selectedProducts: List[int]
