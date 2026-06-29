from typing import List, Optional

from app.features.chairs.repositories.chair_repository import ChairRepository
from app.features.chairs.schemas.chair import ChairSchema


class ChairService:
    """Encapsulates chair-specific business logic."""

    def __init__(self, repository: ChairRepository):
        self._repository = repository

    def get_all(self) -> List[ChairSchema]:
        return self._repository.list_all()

    def get_by_id(self, chair_id: str) -> Optional[ChairSchema]:
        return self._repository.get_by_id(chair_id)

    def get_by_category(self, category: str) -> List[ChairSchema]:
        return self._repository.list_by_category(category)

    def get_featured(self) -> List[ChairSchema]:
        return self._repository.list_featured()

    def search(self, query: str) -> List[ChairSchema]:
        return self._repository.search(query)
