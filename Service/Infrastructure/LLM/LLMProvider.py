from Domain.Interface.LLMProvider_interface import ILLMProvider
from .Typifier import Typifier
from .Configurator import Configurator
from .Summarizer import Summarizer


class LLMProvider(ILLMProvider):
    def __init__(self):
        self.T = Typifier
        self.C = Configurator
        self.S = Summarizer
