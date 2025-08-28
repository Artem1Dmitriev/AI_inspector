from Service.ApplicationServices.AIInspector import AiInspector
from Service.ApplicationServices.JsonInspector import JsonInspector
from Entity.LLM_interface import ILanguageModelClient
from Service.Infrastructure.JsonInspector.JsonConfigProvider import JsonConfigProvider
from Service.Infrastructure.LLM.ChatGPT_API import ChatGPT_API

class Composition():
    def __init__(self):
        provider = JsonConfigProvider()
        self.json_inspector = JsonInspector(provider)
        api_key = self.json_inspector.get_chat_gpt_token()

        self.llm_client: ILanguageModelClient = ChatGPT_API(api_key)
        self.ai_inspector = AiInspector(self.llm_client)

