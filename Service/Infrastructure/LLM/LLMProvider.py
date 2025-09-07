from Domain.Interface.LLMProvider_interface import ILLMProvider
from .Typifier import Typifier
from .MessageMapper import MessageMapper
from .Configurator import Configurator
from .Summarizer import Summarizer


class LLMProvider(ILLMProvider):
    def __init__(self, summarizer_prompt: str):
        super().__init__(summarizer_prompt)
        self.T = Typifier
        self.M = MessageMapper
        self.C = Configurator
        self.S = Summarizer(summarizer_prompt)
