from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from app.features.chairs.repositories.in_memory_chair_repository import (
    InMemoryChairRepository,
)
from app.features.chairs.schemas.chair import ChairSchema
from app.features.chairs.services.chair_service import ChairService

router = APIRouter()

_repository = InMemoryChairRepository()
_service = ChairService(_repository)


def get_chair_service() -> ChairService:
    return _service


@router.get("/", response_model=List[ChairSchema])
def list_chairs(service: ChairService = Depends(get_chair_service)) -> List[ChairSchema]:
    return service.get_all()


@router.get("/{chair_id}", response_model=ChairSchema)
def get_chair(chair_id: str, service: ChairService = Depends(get_chair_service)) -> ChairSchema:
    chair = service.get_by_id(chair_id)
    if chair is None:
        raise HTTPException(status_code=404, detail="Chair not found")
    return chair


@router.get("/category/{category}", response_model=List[ChairSchema])
def list_chairs_by_category(
    category: str, service: ChairService = Depends(get_chair_service)
) -> List[ChairSchema]:
    return service.get_by_category(category)


@router.get("/featured", response_model=List[ChairSchema])
def list_featured_chairs(service: ChairService = Depends(get_chair_service)) -> List[ChairSchema]:
    return service.get_featured()


@router.get("/search", response_model=List[ChairSchema])
def search_chairs(
    q: str = Query(..., min_length=1), service: ChairService = Depends(get_chair_service)
) -> List[ChairSchema]:
    return service.search(q)
