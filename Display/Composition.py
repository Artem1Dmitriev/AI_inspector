from Service.Application.AIInspector import AiInspector
from Service.Application.JsonInspector import JsonInspector
from Domain.Interface.JSON_interface import IConfigProvider
from Domain.Interface.LLM_interface import ILanguageModelClient
from Domain.Interface.LLMProvider_interface import ILLMProvider
from Domain.DTO.MessageAI import MessageAI


class Composition():
    def __init__(self):
        json_provider = IConfigProvider()
        json_inspector = JsonInspector(json_provider)
        api_key, model = json_inspector.get_chat_gpt_api()
        summarizer_prompt = json_inspector.get_prompt("Summarizer")

        llm_client = ILanguageModelClient(api_key, model)
        llm_provider = ILLMProvider(summarizer_prompt)
        self.ai_inspector = AiInspector(llm_client, llm_provider)

        self.message = MessageAI()
