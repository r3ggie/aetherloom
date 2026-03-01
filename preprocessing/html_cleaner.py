import re

class HTMLCleaner:
    @staticmethod
    def clean(html_content: str) -> str:
        if not html_content:
            return ""
        
        # Remove script and style elements
        clean_text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        # Remove all other tags
        clean_text = re.sub(r'<[^>]*>', ' ', clean_text)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', clean_text).strip()
        return text

class SnippetSelector:
    @staticmethod
    def select(text: str, query: str, max_chars: int = 1000) -> str:
        # Simple extraction: first max_chars for now, but can be improved
        # to find the most relevant paragraph.
        return text[:max_chars] + "..." if len(text) > max_chars else text
