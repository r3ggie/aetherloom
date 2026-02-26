import json

class AetherLoom:
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def encode(self, intent, payload):
        """Encodes an intent and payload into AL-1 format."""
        header = f"[{intent}:{self.agent_id}]"
        # MiniJSON serialization
        payload_str = json.dumps(payload, separators=(',', ':'))
        return f"{header}{payload_str}"

    def decode(self, message):
        """Decodes an AL-1 message."""
        if not message.startswith("[") or "]" not in message:
            raise ValueError("Invalid AL-1 format")
        
        header_end = message.find("]")
        header = message[1:header_end].split(":")
        payload = json.loads(message[header_end+1:])
        
        return {
            "intent": header[0],
            "agent_id": header[1],
            "payload": payload
        }

if __name__ == "__main__":
    loom = AetherLoom("REGGIE")
    msg = loom.encode("REQ", {"task": "summarize", "url": "https://example.com"})
    print(f"Encoded: {msg}")
    print(f"Decoded: {loom.decode(msg)}")
