import re

class MCSParser:
    @staticmethod
    def parse(mcs_string: str) -> dict:
        """Parse CMD:SRCH_SUM|Q:GenAI|LIMIT:3 into a dictionary."""
        parts = mcs_string.split('|')
        data = {}
        for part in parts:
            if ':' in part:
                key, value = part.split(':', 1)
                data[key.strip()] = value.strip()
        return data

    @staticmethod
    def to_mcs(command: str, query: str, limit: int = 3, focus: str = None, out: str = "SUM") -> str:
        """Generate a compact MCS string."""
        mcs = f"CMD:{command}|Q:{query}|LIMIT:{limit}"
        if focus:
            mcs += f"|FOCUS:{focus}"
        mcs += f"|OUT:{out}"
        return mcs
