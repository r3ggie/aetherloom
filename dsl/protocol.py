import json
import re

class AL1Protocol:
    VERSION = "1"

    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    def encode(self, intent: str, payload: dict, nonce: int = 0) -> str:
        """Encodes an intent and payload into AL-1 Text format (MiniJSON)."""
        header = f"[{self.VERSION}:{intent}:{self.agent_id}:{nonce}]"
        # MiniJSON serialization
        payload_str = json.dumps(payload, separators=(',', ':'))
        return f"{header}{payload_str}"

    def encode_mcs(self, intent: str, mcs_string: str, nonce: int = 0) -> str:
        """Encodes an intent and MCS string into AL-1 Text format."""
        header = f"[{self.VERSION}:{intent}:{self.agent_id}:{nonce}]"
        return f"{header}{mcs_string}"

    def decode(self, message: str) -> dict:
        """Decodes an AL-1 Text message (supports both MiniJSON and MCS)."""
        if not message.startswith("[") or "]" not in message:
            raise ValueError("Invalid AL-1 format")
        
        header_end = message.find("]")
        header_parts = message[1:header_end].split(":")
        
        if len(header_parts) < 3:
            raise ValueError("Incomplete AL-1 header")

        payload_raw = message[header_end+1:]
        
        # Try JSON first, then assume MCS
        try:
            payload = json.loads(payload_raw)
        except json.JSONDecodeError:
            payload = payload_raw # Return raw MCS string

        return {
            "version": header_parts[0],
            "intent": header_parts[1],
            "sender_id": header_parts[2],
            "nonce": header_parts[3] if len(header_parts) > 3 else None,
            "payload": payload
        }
