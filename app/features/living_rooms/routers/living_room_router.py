from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from app.features.living_rooms.repositories.in_memory_living_room_repository import (
    InMemoryLivingRoomRepository,
)
from app.features.living_rooms.schemas.living_room import LivingRoomSchema
from app.features.living_rooms.services.living_room_service import LivingRoomService

living_rooms_router = APIRouter()

_repository = InMemoryLivingRoomRepository()
_service = LivingRoomService(_repository)


def get_living_room_service() -> LivingRoomService:
    return _service


@living_rooms_router.get("/", response_model=List[LivingRoomSchema])
def list_living_rooms(
    service: LivingRoomService = Depends(get_living_room_service),
) -> List[LivingRoomSchema]:
    return service.get_all()


@living_rooms_router.get("/featured", response_model=List[LivingRoomSchema])
def list_featured_living_rooms(
    service: LivingRoomService = Depends(get_living_room_service),
) -> List[LivingRoomSchema]:
    return service.get_featured()


@living_rooms_router.get("/search", response_model=List[LivingRoomSchema])
def search_living_rooms(
    q: str = Query(..., min_length=1),
    service: LivingRoomService = Depends(get_living_room_service),
) -> List[LivingRoomSchema]:
    return service.search(q)


@living_rooms_router.get("/category/{category}", response_model=List[LivingRoomSchema])
def list_living_rooms_by_category(
    category: str,
    service: LivingRoomService = Depends(get_living_room_service),
) -> List[LivingRoomSchema]:
    return service.get_by_category(category)


@living_rooms_router.get("/{living_room_id}", response_model=LivingRoomSchema)
def get_living_room(
    living_room_id: str,
    service: LivingRoomService = Depends(get_living_room_service),
) -> LivingRoomSchema:
    room = service.get_by_id(living_room_id)
    if room is None:
        raise HTTPException(status_code=404, detail="Living room not found")
    return room
