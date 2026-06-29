from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from app.features.desks.repositories.in_memory_desk_repository import (
    InMemoryDeskRepository,
)
from app.features.desks.schemas.desk import DeskSchema
from app.features.desks.services.desk_service import DeskService

router = APIRouter()

_repository = InMemoryDeskRepository()
_service = DeskService(_repository)


def get_desk_service() -> DeskService:
    return _service


@router.get("/", response_model=List[DeskSchema])
def list_desks(service: DeskService = Depends(get_desk_service)) -> List[DeskSchema]:
    return service.get_all()


@router.get("/{desk_id}", response_model=DeskSchema)
def get_desk(desk_id: str, service: DeskService = Depends(get_desk_service)) -> DeskSchema:
    desk = service.get_by_id(desk_id)
    if desk is None:
        raise HTTPException(status_code=404, detail="Desk not found")
    return desk


@router.get("/category/{category}", response_model=List[DeskSchema])
def list_desks_by_category(
    category: str, service: DeskService = Depends(get_desk_service)
) -> List[DeskSchema]:
    return service.get_by_category(category)


@router.get("/featured", response_model=List[DeskSchema])
def list_featured_desks(service: DeskService = Depends(get_desk_service)) -> List[DeskSchema]:
    return service.get_featured()


@router.get("/search", response_model=List[DeskSchema])
def search_desks(
    q: str = Query(..., min_length=1),
    service: DeskService = Depends(get_desk_service),
) -> List[DeskSchema]:
    return service.search(q)
