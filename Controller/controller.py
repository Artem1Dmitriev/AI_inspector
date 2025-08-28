# controller.py
from Service.Composition import Composition


class Controller:
    def __init__(self):
        self.services = Composition()

    def run(self):
        input_text = input("Введите запрос к LLM: ")
        print(self.services.ai_inspector.simple_response(input_text))


if __name__ == "__main__":
    c = Controller()
    c.run()
