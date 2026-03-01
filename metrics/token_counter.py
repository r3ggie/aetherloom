class TokenCounter:
    @staticmethod
    def estimate_tokens(text: str) -> int:
        """Rough estimation: 4 chars per token."""
        return len(text) // 4

class EfficiencyReport:
    def __init__(self, raw_tokens: int, processed_tokens: int):
        self.raw_tokens = raw_tokens
        self.processed_tokens = processed_tokens
        self.savings = 100 * (1 - (processed_tokens / raw_tokens)) if raw_tokens > 0 else 0

    def report(self) -> str:
        return f"Raw: {self.raw_tokens} | Optimized: {self.processed_tokens} | Savings: {self.savings:.2f}%"
