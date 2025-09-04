from abc import ABC, abstractmethod


class IFileProcessing(ABC):
    @abstractmethod
    def processing(self, file_path: str) -> str:
        pass
