from abc import ABC, abstractmethod
from typing import List, Optional

from app.features.bedrooms.schemas.bedroom import BedroomSchema


class BedroomRepository(ABC):
    """Defines the contract for bedroom data retrieval."""

    @abstractmethod
    def list_all(self) -> List[BedroomSchema]:
        ...

    @abstractmethod
    def get_by_id(self, bedroom_id: str) -> Optional[BedroomSchema]:
        ...

    @abstractmethod
    def list_by_category(self, category: str) -> List[BedroomSchema]:
        ...

    @abstractmethod
    def list_featured(self) -> List[BedroomSchema]:
        ...

    @abstractmethod
    def search(self, query: str) -> List[BedroomSchema]:
        ...
