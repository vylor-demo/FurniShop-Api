from typing import List, Optional

from app.features.living_rooms.repositories.living_room_repository import (
    LivingRoomRepository,
)
from app.features.living_rooms.schemas.living_room import LivingRoomSchema


class LivingRoomService:
    """Encapsulates living room-specific business logic."""

    def __init__(self, repository: LivingRoomRepository):
        self._repository = repository

    def get_all(self) -> List[LivingRoomSchema]:
        return self._repository.list_all()

    def get_by_id(self, living_room_id: str) -> Optional[LivingRoomSchema]:
        return self._repository.get_by_id(living_room_id)

    def get_by_category(self, category: str) -> List[LivingRoomSchema]:
        return self._repository.list_by_category(category)

    def get_featured(self) -> List[LivingRoomSchema]:
        return self._repository.list_featured()

    def search(self, query: str) -> List[LivingRoomSchema]:
        return self._repository.search(query)
