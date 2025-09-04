from abc import ABC, abstractmethod


class ILanguageModelClient(ABC):
    def __init__(self, api_key: str, model: str):
        pass

    @abstractmethod
    def query(self, input: list[dict], instructions: str | None = None) -> str:
        pass
