from Service.Application.AIInspector import AiInspector
from Service.Application.JsonInspector import JsonInspector
from Domain.Interface.LLM_interface import ILanguageModelClient
from Service.Infrastructure.JsonInspector.JsonConfigProvider import JsonConfigProvider
from Service.Infrastructure.LLM.ChatGPT_Client import ChatGPT_API
from Domain.DTO.MessageAI import MessageAI


class Composition():
    def __init__(self):
        provider = JsonConfigProvider()
        self.json_inspector = JsonInspector(provider)
        api_key, model = self.json_inspector.get_chat_gpt_api()

        self.llm_client: ILanguageModelClient = ChatGPT_API(api_key, model)
        self.ai_inspector = AiInspector(self.llm_client)
        self.MessageHistory = MessageAI(self.json_inspector, self.ai_inspector, model)