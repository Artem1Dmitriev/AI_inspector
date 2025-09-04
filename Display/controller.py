from Display.Composition import Composition


class Controller:
    def __init__(self):
        self.services = Composition()

    def run(self):
        inp = "В современном мире разработка программного обеспечения стала крайне сложной задачей. Архитектуры приложений эволюционируют, чтобы справляться с ростом количества пользователей, распределёнными системами и требованиями к безопасности. Одним из подходов является Onion Architecture, которая помогает изолировать бизнес-логику от инфраструктурных зависимостей. Применение этой архитектуры позволяет легче тестировать код, заменять реализации сервисов и упрощает поддержку больших проектов. При этом важно помнить о принципах SOLID, особенно о принципе единственной ответственности и инверсии зависимостей. В учебных проектах можно экспериментировать с различными слоями, внедрять сервисы через Composition Root и обеспечивать взаимодействие через интерфейсы. Этот подход особенно полезен при интеграции с внешними API, такими как OpenAI GPT, где логика работы модели отделена от конкретной реализации клиента и инфраструктуры."
        self.services.MessageHistory.append(inp)
        # print(self.services.MessageHistory.count_tokens())
        # print(self.services.MessageHistory.get_message())
        self.services.MessageHistory.append(
            self.services.ai_inspector.simple_response(self.services.MessageHistory.get_message()))
        # print(self.services.MessageHistory.count_tokens())
        print(self.services.MessageHistory.get_message())


if __name__ == "__main__":
    c = Controller()
    c.run()
