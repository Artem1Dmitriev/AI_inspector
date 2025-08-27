from openai import OpenAI


class ChatGPT_API():
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

    def __init__(self, api_key):
        """
        Этот метод инициализирует ключ API из конфигурации и создает клиент OpenAI для отправки запросов.

        Args:
            self (API): Экземпляр самого класса API.
        """
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)

    def query_handler(self, model_name, input, instructions=None):
        # Отправляем текущий запрос
        response = self.client.responses.create(
            model=model_name,
            input=input,
            instructions=instructions
        )

        return response.output_text



# Тоже кладовщик, только работает не с базой, а с другим сервисом.
# Например: твое приложение хочет получить погоду из внешнего API.
# Сервис говорит клиенту: «дай погоду для Москвы».
# Клиент идёт в чужой сервис и возвращает результат.


