from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from app.features.chairs.schemas.chair import ChairSchema


class ChairRepository(ABC):
    """Defines the contract for fetching chair data."""

    @abstractmethod
    def list_all(self) -> List[ChairSchema]:
        ...

    @abstractmethod
    def get_by_id(self, chair_id: str) -> Optional[ChairSchema]:
        ...

    @abstractmethod
    def list_by_category(self, category: str) -> List[ChairSchema]:
        ...

    @abstractmethod
    def list_featured(self) -> List[ChairSchema]:
        ...

    @abstractmethod
    def search(self, query: str) -> List[ChairSchema]:
        ...
