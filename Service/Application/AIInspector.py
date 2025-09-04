from Domain.Interface.LLM_interface import ILanguageModelClient


class AiInspector():
    def __init__(self, client: ILanguageModelClient):
        self.client = client

    def simple_response(self, input: list[dict]) -> str:
        return self.client.query(input)

    def conf_response(self, input: list[dict], conf: str) -> str:
        conf = conf + "30%"
        return self.client.query(input, conf)
