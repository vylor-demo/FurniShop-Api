from abc import ABC, abstractmethod
from typing import List, Optional

from app.features.desks.schemas.desk import DeskSchema


class DeskRepository(ABC):
    """Defines the contract for desk data retrieval."""

    @abstractmethod
    def list_all(self) -> List[DeskSchema]:
        ...

    @abstractmethod
    def get_by_id(self, desk_id: str) -> Optional[DeskSchema]:
        ...

    @abstractmethod
    def list_by_category(self, category: str) -> List[DeskSchema]:
        ...

    @abstractmethod
    def list_featured(self) -> List[DeskSchema]:
        ...

    @abstractmethod
    def search(self, query: str) -> List[DeskSchema]:
        ...
