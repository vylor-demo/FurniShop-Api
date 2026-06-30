from typing import List, Optional

from app.features.bedrooms.data.mock_data import BEDROOMS_DATA
from app.features.bedrooms.repositories.bedroom_repository import BedroomRepository
from app.features.bedrooms.schemas.bedroom import BedroomSchema


class InMemoryBedroomRepository(BedroomRepository):
    """In-memory repository backed by the bedrooms mock catalog."""

    def __init__(self):
        self._bedrooms = [BedroomSchema(**data) for data in BEDROOMS_DATA]

    def list_all(self) -> List[BedroomSchema]:
        return list(self._bedrooms)

    def get_by_id(self, bedroom_id: str) -> Optional[BedroomSchema]:
        return next((item for item in self._bedrooms if item.id == bedroom_id), None)

    def list_by_category(self, category: str) -> List[BedroomSchema]:
        normalized = category.strip().lower()
        return [
            item
            for item in self._bedrooms
            if item.category.strip().lower() == normalized
        ]

    def list_featured(self) -> List[BedroomSchema]:
        return [item for item in self._bedrooms if item.is_featured]

    def search(self, query: str) -> List[BedroomSchema]:
        normalized = query.strip().lower()
        results: List[BedroomSchema] = []
        for item in self._bedrooms:
            if normalized in item.name.lower():
                results.append(item)
                continue
            if normalized in item.description.lower():
                results.append(item)
                continue
            if normalized in item.category.lower():
                results.append(item)
                continue
            if any(normalized in tag.lower() for tag in item.tags):
                results.append(item)
                continue
        return results
