from Entity.JSON_interface import IConfigProvider


class JsonInspector():
    def __init__(self, provider: IConfigProvider):
        self.provider = provider

    def get_chat_gpt_token(self) -> str:
        token = self.provider.get("API")
        return token.chat_gpt_token
