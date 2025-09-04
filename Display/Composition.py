from Service.Application.AIInspector import AiInspector
from Service.Application.JsonInspector import JsonInspector
from Domain.Interface.JSON_interface import IConfigProvider
from Domain.Interface.LLM_interface import ILanguageModelClient
from Domain.Interface.LLMProvider_interface import ILLMProvider
from Domain.DTO.MessageAI import MessageAI


class Composition():
    def __init__(self):
        JsonProvider = IConfigProvider()
        json_inspector = JsonInspector(JsonProvider)
        api_key, model = json_inspector.get_chat_gpt_api()

        LLMClient = ILanguageModelClient(api_key, model)
        LLMProvider = ILLMProvider()
        self.ai_inspector = AiInspector(LLMClient, LLMProvider)

        self.message = MessageAI()
