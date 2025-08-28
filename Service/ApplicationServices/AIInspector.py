from Entity.LLM_interface import ILanguageModelClient

class AiInspector():
    def __init__(self, client: ILanguageModelClient):
        self.client = client

    def simple_response(self, input_text) -> str:
        return self.client.query("gpt-3.5-turbo", input_text)

