from abc import ABC, abstractmethod

class IConfigProvider(ABC):
    @abstractmethod
    def get(self, name: str):
        pass
