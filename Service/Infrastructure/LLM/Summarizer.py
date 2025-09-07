import tiktoken


class Summarizer():
    def __init__(self, summarizer_prompt: str, message: list[dict]):
        self.prompt = summarizer_prompt
        self.message = message

    def count_tokens(self, model: str, total_tokens_max: int) -> None:
        encoding = tiktoken.encoding_for_model(model)

        total_tokens = 0
        for msg in self.message:
            total_tokens += len(encoding.encode(msg["content"]))
            total_tokens += len(encoding.encode(msg["role"]))
        if total_tokens > total_tokens_max:
            self.summarize()

    def summarize(self):
        pass
