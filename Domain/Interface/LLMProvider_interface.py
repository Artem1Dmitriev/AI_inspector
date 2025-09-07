from abc import ABC, abstractmethod
class ILLMProvider(ABC):
    def __init__(self, summarizer_prompt: str):
        pass