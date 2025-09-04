class MessageAI():
    def __init__(self):
        self.message = []

    def get_message(self):
        return self.message

    def append(self, content: str, role: str = "user"):
        self.message.append({
            "role": role,
            "content": content
        })

    def clear(self):
        self.message = []