from abc import ABC, abstractmethod

class BaseLLMAdapter(ABC):
    @abstractmethod
    def call_model(self, prompt: str, max_tokens: int = 500) -> str:
        pass

class CerebrasAdapter(BaseLLMAdapter):
    def __init__(self, api_key: str, model_name: str = "gpt-oss-120b"):
        from openai import OpenAI
        self.client = OpenAI(base_url="https://api.cerebras.ai/v1", api_key=api_key)
        self.model_name = model_name

    def call_model(self, prompt: str, max_tokens: int = 500) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
