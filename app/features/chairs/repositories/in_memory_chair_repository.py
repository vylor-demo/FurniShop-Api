from typing import List, Optional

from app.features.chairs.data.mock_data import CHAIRS_DATA
from app.features.chairs.schemas.chair import ChairSchema
from app.features.chairs.repositories.chair_repository import ChairRepository


class InMemoryChairRepository(ChairRepository):
    """Simple repository backed by the hard-coded chair catalog."""

    def __init__(self):
        self._chairs = [ChairSchema(**data) for data in CHAIRS_DATA]

    def list_all(self) -> List[ChairSchema]:
        return list(self._chairs)

    def get_by_id(self, chair_id: str) -> Optional[ChairSchema]:
        return next((chair for chair in self._chairs if chair.id == chair_id), None)

    def list_by_category(self, category: str) -> List[ChairSchema]:
        normalized = category.strip().lower()
        return [
            chair
            for chair in self._chairs
            if chair.category.strip().lower() == normalized
        ]

    def list_featured(self) -> List[ChairSchema]:
        return [chair for chair in self._chairs if chair.is_featured]

    def search(self, query: str) -> List[ChairSchema]:
        normalized = query.strip().lower()
        results = []
        for chair in self._chairs:
            if normalized in chair.name.lower():
                results.append(chair)
                continue
            if normalized in chair.description.lower():
                results.append(chair)
                continue
            if normalized in chair.category.lower():
                results.append(chair)
                continue
            if any(normalized in tag.lower() for tag in chair.tags):
                results.append(chair)
                continue
        return results
