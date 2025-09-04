from Domain.Interface.JSON_interface import IConfigProvider


class JsonInspector():
    def __init__(self, provider: IConfigProvider):
        self.provider = provider

    def get_chat_gpt_api(self) -> list:
        api = self.provider.get("API")
        api = [api.chat_gpt_token, api.model]
        return api

    def get_prompt(self, name):
        prompts = self.provider.get("LLM_Prompt")
        return getattr(prompts, name)
