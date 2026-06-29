from typing import List, Optional

from pydantic import BaseModel


class LivingRoomDimensionsSchema(BaseModel):
    width: float
    height: float
    depth: float
    weight: float


class LivingRoomSchema(BaseModel):
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
    dimensions: LivingRoomDimensionsSchema
    is_featured: bool = False
    tags: List[str] = []

    class Config:
        orm_mode = True
