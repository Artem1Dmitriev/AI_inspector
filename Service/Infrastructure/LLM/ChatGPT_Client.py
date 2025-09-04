from openai import OpenAI
from Domain.Interface.LLM_interface import ILanguageModelClient


class ChatGPT_API(ILanguageModelClient):
    """
    Класс для взаимодействия с API OpenAI GPT.

    Этот класс предоставляет интерфейс для выполнения запросов к OpenAI GPT, включая
    инициализацию клиента, обработку запросов и получение ответов.

    Atributes:
        master (object): Экземпляр класса Master, передается при инициализации.
        api_key (str): Ключ API для доступа к OpenAI.
        client (OpenAI): Экземпляр клиента OpenAI, используемый для отправки запросов.

    Тип модуля:
        Procedure:
          Основная логика работает в процедурном режиме без использования потоков.

    Взаимодействие с модулями:
          Master: Основной управляющий объект, откуда загружаются конфигурации.
          OpenAI (openai): Клиент для выполнения запросов к API OpenAI GPT.
    """

    def __init__(self, api_key: str, model: str):
        """
        Этот метод инициализирует ключ API из конфигурации и создает клиент OpenAI для отправки запросов.

        Args:
            self (API): Экземпляр самого класса API.
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def query(self, input_text: list[dict], instructions: str | None = None) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=input_text,
            instructions=instructions
        )
        return response.output_text
