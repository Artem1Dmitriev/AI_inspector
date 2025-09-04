from abc import ABC, abstractmethod

class ILanguageModelClient(ABC):
    @abstractmethod
    def query(self, input: list[dict], instructions: str | None = None) -> str:
        pass
