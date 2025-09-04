from openai import OpenAI
from Domain.Interface.LLM_interface import ILanguageModelClient


class ChatGPT_API(ILanguageModelClient):
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def query(self, input_text: list[dict], instructions: str | None = None) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=input_text,
            instructions=instructions
        )
        return response.output_text
