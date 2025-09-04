import tiktoken


class MessageAI():
    def __init__(self, ji, ai, model: str):
        self.ji = ji
        self.ai = ai
        self.model = model
        hello = self.ji.get_prompt("Hello")
        self.message = [{
            "role": "system",
            "content": hello
        }]

    def get_message(self):
        return self.message

    def append(self, content: str, role: str = "user"):
        self.message.append({
            "role": role,
            "content": content
        })
        self.count_tokens()

    def clear(self):
        hello = self.ji.get_prompt("Hello")
        self.message = [{
            "role": "system",
            "content": hello
        }]

    def count_tokens(self) -> int:
        encoding = tiktoken.encoding_for_model(self.model)

        total_tokens = 0
        for msg in self.message:
            total_tokens += len(encoding.encode(msg["content"]))
            total_tokens += len(encoding.encode(msg["role"]))
        if total_tokens > 700:
            self.summarize()
        return total_tokens

    def summarize(self):
        prompt = self.ji.get_prompt("Summarizer")
        summarize_message = self.ai.conf_response(self.get_message(), prompt)
        self.clear()
        self.append(summarize_message, "user")
