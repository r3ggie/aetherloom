from .llm_agent import BaseLLMAdapter

class MockAdapter(BaseLLMAdapter):
    def call_model(self, prompt: str, max_tokens: int = 500) -> str:
        return f"[Mocked Summary for {prompt[:20]}...]"
