from typing import List, Optional

from app.features.desks.repositories.desk_repository import DeskRepository
from app.features.desks.schemas.desk import DeskSchema


class DeskService:
    """Encapsulates desk-specific business logic."""

    def __init__(self, repository: DeskRepository):
        self._repository = repository

    def get_all(self) -> List[DeskSchema]:
        return self._repository.list_all()

    def get_by_id(self, desk_id: str) -> Optional[DeskSchema]:
        return self._repository.get_by_id(desk_id)

    def get_by_category(self, category: str) -> List[DeskSchema]:
        return self._repository.list_by_category(category)

    def get_featured(self) -> List[DeskSchema]:
        return self._repository.list_featured()

    def search(self, query: str) -> List[DeskSchema]:
        return self._repository.search(query)
