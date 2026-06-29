from abc import ABC, abstractmethod
from typing import List, Optional

from app.features.living_rooms.schemas.living_room import LivingRoomSchema


class LivingRoomRepository(ABC):
    """Defines the contract for living room data retrieval."""

    @abstractmethod
    def list_all(self) -> List[LivingRoomSchema]:
        ...

    @abstractmethod
    def get_by_id(self, living_room_id: str) -> Optional[LivingRoomSchema]:
        ...

    @abstractmethod
    def list_by_category(self, category: str) -> List[LivingRoomSchema]:
        ...

    @abstractmethod
    def list_featured(self) -> List[LivingRoomSchema]:
        ...

    @abstractmethod
    def search(self, query: str) -> List[LivingRoomSchema]:
        ...
