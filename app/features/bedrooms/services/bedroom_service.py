from typing import List, Optional

from app.features.bedrooms.repositories.bedroom_repository import BedroomRepository
from app.features.bedrooms.schemas.bedroom import BedroomSchema


class BedroomService:
    """Encapsulates bedroom-specific business logic."""

    def __init__(self, repository: BedroomRepository):
        self._repository = repository

    def get_all(self) -> List[BedroomSchema]:
        return self._repository.list_all()

    def get_by_id(self, bedroom_id: str) -> Optional[BedroomSchema]:
        return self._repository.get_by_id(bedroom_id)

    def get_by_category(self, category: str) -> List[BedroomSchema]:
        return self._repository.list_by_category(category)

    def get_featured(self) -> List[BedroomSchema]:
        return self._repository.list_featured()

    def search(self, query: str) -> List[BedroomSchema]:
        return self._repository.search(query)
