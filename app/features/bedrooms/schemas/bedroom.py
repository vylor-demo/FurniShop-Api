from typing import List, Optional

from pydantic import BaseModel


class BedroomDimensionsSchema(BaseModel):
    width: float
    height: float
    depth: float
    weight: float


class BedroomSchema(BaseModel):
    id: str
    name: str
    description: str
    price: float
    original_price: Optional[float] = None
    image_url: str
    rating: float
    review_count: int
    in_stock: bool
    category: str
    material: str
    color: str
    dimensions: BedroomDimensionsSchema
    is_featured: bool = False
    tags: List[str] = []

    class Config:
        orm_mode = True
