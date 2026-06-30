from typing import List, Optional

from app.features.desks.data.mock_data import DESKS_DATA
from app.features.desks.repositories.desk_repository import DeskRepository
from app.features.desks.schemas.desk import DeskSchema


class InMemoryDeskRepository(DeskRepository):
    """In-memory repository backed by the desk mock catalog."""

    def __init__(self):
        self._desks = [DeskSchema(**data) for data in DESKS_DATA]

    def list_all(self) -> List[DeskSchema]:
        return list(self._desks)

    def get_by_id(self, desk_id: str) -> Optional[DeskSchema]:
        return next((desk for desk in self._desks if desk.id == desk_id), None)

    def list_by_category(self, category: str) -> List[DeskSchema]:
        normalized = category.strip().lower()
        return [
            desk
            for desk in self._desks
            if desk.category.strip().lower() == normalized
        ]

    def list_featured(self) -> List[DeskSchema]:
        return [desk for desk in self._desks if desk.is_featured]

    def search(self, query: str) -> List[DeskSchema]:
        normalized = query.strip().lower()
        results: List[DeskSchema] = []
        for desk in self._desks:
            if normalized in desk.name.lower():
                results.append(desk)
                continue
            if normalized in desk.description.lower():
                results.append(desk)
                continue
            if normalized in desk.category.lower():
                results.append(desk)
                continue
            if any(normalized in tag.lower() for tag in desk.tags):
                results.append(desk)
                continue
        return results
