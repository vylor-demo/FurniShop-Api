from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from app.features.bedrooms.repositories.in_memory_bedroom_repository import (
    InMemoryBedroomRepository,
)
from app.features.bedrooms.schemas.bedroom import BedroomSchema
from app.features.bedrooms.services.bedroom_service import BedroomService

bedrooms_router = APIRouter()

_repository = InMemoryBedroomRepository()
_service = BedroomService(_repository)


def get_bedroom_service() -> BedroomService:
    return _service


@bedrooms_router.get("/", response_model=List[BedroomSchema])
def list_bedrooms(
    service: BedroomService = Depends(get_bedroom_service),
) -> List[BedroomSchema]:
    return service.get_all()


@bedrooms_router.get("/featured", response_model=List[BedroomSchema])
def list_featured_bedrooms(
    service: BedroomService = Depends(get_bedroom_service),
) -> List[BedroomSchema]:
    return service.get_featured()


@bedrooms_router.get("/search", response_model=List[BedroomSchema])
def search_bedrooms(
    q: str = Query(..., min_length=1),
    service: BedroomService = Depends(get_bedroom_service),
) -> List[BedroomSchema]:
    return service.search(q)


@bedrooms_router.get("/category/{category}", response_model=List[BedroomSchema])
def list_bedrooms_by_category(
    category: str,
    service: BedroomService = Depends(get_bedroom_service),
) -> List[BedroomSchema]:
    return service.get_by_category(category)


@bedrooms_router.get("/{bedroom_id}", response_model=BedroomSchema)
def get_bedroom(
    bedroom_id: str,
    service: BedroomService = Depends(get_bedroom_service),
) -> BedroomSchema:
    bedroom = service.get_by_id(bedroom_id)
    if bedroom is None:
        raise HTTPException(status_code=404, detail="Bedroom not found")
    return bedroom
