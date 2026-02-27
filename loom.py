import json

class AetherLoom:
    VERSION = "1"

    def __init__(self, agent_id):
        self.agent_id = agent_id

    def encode(self, intent, payload, nonce=0):
        """Encodes an intent and payload into AL-1 Text format."""
        header = f"[{self.VERSION}:{intent}:{self.agent_id}:{nonce}]"
        # MiniJSON serialization
        payload_str = json.dumps(payload, separators=(',', ':'))
        return f"{header}{payload_str}"

    def decode(self, message):
        """Decodes an AL-1 Text message."""
        if not message.startswith("[") or "]" not in message:
            raise ValueError("Invalid AL-1 format")
        
        header_end = message.find("]")
        header_parts = message[1:header_end].split(":")
        
        if len(header_parts) < 3:
            raise ValueError("Incomplete AL-1 header")

        payload = json.loads(message[header_end+1:])
        
        return {
            "version": header_parts[0],
            "intent": header_parts[1],
            "sender_id": header_parts[2],
            "nonce": header_parts[3] if len(header_parts) > 3 else None,
            "payload": payload
        }

    # Binary encoding placeholders (requires cbor2 / protobuf)
    def encode_binary(self, intent, payload, format="cbor"):
        raise NotImplementedError("Binary encoding requires external libraries (cbor2/protobuf)")

if __name__ == "__main__":
    loom = AetherLoom("REGGIE")
    msg = loom.encode("REQ", {"t": "sum", "u": "https://r3ggie.ai"}, nonce=42)
    print(f"Encoded: {msg}")
    print(f"Decoded: {loom.decode(msg)}")
