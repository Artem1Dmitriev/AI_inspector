from Service.Application.AIInspector import AiInspector
from Service.Application.JsonInspector import JsonInspector
from Domain.Interface.LLM_interface import ILanguageModelClient
from Service.Infrastructure.JsonInspector.JsonConfigProvider import JsonConfigProvider
from Service.Infrastructure.LLM.Clients.ChatGPT_Client import ChatGPT_API
from Service.Infrastructure.LLM.LLMProvider import LLMProvider
from Domain.Interface.LLMProvider_interface import ILLMProvider
from Domain.DTO.MessageAI import MessageAI


class Composition():
    def __init__(self):
        JsonProvider = JsonConfigProvider()
        json_inspector = JsonInspector(JsonProvider)
        api_key, model = json_inspector.get_chat_gpt_api()

        llm_client: ILanguageModelClient = ChatGPT_API(api_key, model)
        LlmProvider = LLMProvider()
        self.ai_inspector = AiInspector(llm_client, LlmProvider)

        self.message = MessageAI()
