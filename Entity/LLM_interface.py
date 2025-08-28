from abc import ABC, abstractmethod

class ILanguageModelClient(ABC):
    @abstractmethod
    def query(self, model_name: str, input_text: str, instructions: str | None = None) -> str:
        pass
