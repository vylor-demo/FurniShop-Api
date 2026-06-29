from typing import List, Optional

from app.features.living_rooms.data.mock_data import LIVING_ROOMS_DATA
from app.features.living_rooms.repositories.living_room_repository import (
    LivingRoomRepository,
)
from app.features.living_rooms.schemas.living_room import LivingRoomSchema


class InMemoryLivingRoomRepository(LivingRoomRepository):
    """In-memory repository backed by the living rooms mock catalog."""

    def __init__(self):
        self._living_rooms = [LivingRoomSchema(**data) for data in LIVING_ROOMS_DATA]

    def list_all(self) -> List[LivingRoomSchema]:
        return list(self._living_rooms)

    def get_by_id(self, living_room_id: str) -> Optional[LivingRoomSchema]:
        return next(
            (room for room in self._living_rooms if room.id == living_room_id),
            None,
        )

    def list_by_category(self, category: str) -> List[LivingRoomSchema]:
        normalized = category.strip().lower()
        return [
            room
            for room in self._living_rooms
            if room.category.strip().lower() == normalized
        ]

    def list_featured(self) -> List[LivingRoomSchema]:
        return [room for room in self._living_rooms if room.is_featured]

    def search(self, query: str) -> List[LivingRoomSchema]:
        normalized = query.strip().lower()
        results: List[LivingRoomSchema] = []
        for room in self._living_rooms:
            if normalized in room.name.lower():
                results.append(room)
                continue
            if normalized in room.description.lower():
                results.append(room)
                continue
            if normalized in room.category.lower():
                results.append(room)
                continue
            if any(normalized in tag.lower() for tag in room.tags):
                results.append(room)
                continue
        return results
