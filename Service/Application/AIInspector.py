from Domain.Interface.LLM_interface import ILanguageModelClient
from Domain.Interface.LLMProvider_interface import ILLMProvider

class AiInspector():
    def __init__(self, client: ILanguageModelClient, provider: ILLMProvider):
        self.client = client
        self.provider = provider

    def simple_response(self, input: list[dict]) -> str:
        return self.client.query(input)

    def conf_response(self, input: list[dict], conf: str) -> str:
        conf = conf + "30%"
        return self.client.query(input, conf)
