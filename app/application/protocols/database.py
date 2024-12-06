from abc import ABC, abstractmethod

from app.application.models import FormTemplate


class UoW(ABC):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def flush(self) -> None:
        raise NotImplementedError


class DatabaseGateway(ABC):
    @abstractmethod
    async def get_matching_forms(self, search_fields: list[FormTemplate]):
        raise NotImplementedError

