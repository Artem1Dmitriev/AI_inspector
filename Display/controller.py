from Display.Composition import Composition


class Controller:
    def __init__(self):
        self.services = Composition()

    def run(self):
        inp = input()
        self.services.message.append(inp)
        # print(self.services.MessageHistory.count_tokens())
        # print(self.services.MessageHistory.get_message())
        self.services.message.append(
            self.services.ai_inspector.simple_response(self.services.message.get_message()))
        # print(self.services.MessageHistory.count_tokens())
        print(self.services.message.get_message())


if __name__ == "__main__":
    c = Controller()
    c.run()
