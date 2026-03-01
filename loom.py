import json

class AetherLoom:
    VERSION = "1"
    
    INTENTS = {
        "REQ": "Q", "RES": "R", "INF": "I", "ERR": "E", "LMB": "L"
    }
    INV_INTENTS = {v: k for k, v in INTENTS.items()}

    def __init__(self, agent_id):
        self.agent_id = agent_id[:3].upper() # Use 3-char alias for S-Loom

    def s_encode(self, intent, payload_parts, nonce=0):
        """Encodes into AL-1 Symbolic (S-Loom) format for token efficiency."""
        intent_code = self.INTENTS.get(intent, intent)
        header = f"AL{self.VERSION}|{intent_code}|{self.agent_id}|{nonce}"
        payload = "|".join(payload_parts)
        return f"{header}|{payload}"

    def encode(self, intent, payload, nonce=0):
        """Encodes an intent and payload into AL-1 Text format."""
        header = f"[{self.VERSION}:{intent}:{self.agent_id}:{nonce}]"
        # MiniJSON serialization
        payload_str = json.dumps(payload, separators=(',', ':'))
        return f"{header}{payload_str}"

    def decode(self, message):
        """Decodes an AL-1 Text message."""
        if not message.startswith("[") or "]" not in message:
            raise ValueError("Invalid AL-1 format: Missing brackets")
        
        header_end = message.find("]")
        header_parts = message[1:header_end].split(":")
        
        if len(header_parts) < 3:
            raise ValueError(f"Incomplete AL-1 header: {header_parts}")

        try:
            payload = json.loads(message[header_end+1:])
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid AL-1 payload (JSON error): {e}")
        
        return {
            "version": header_parts[0],
            "intent": header_parts[1],
            "sender_id": header_parts[2],
            "nonce": header_parts[3] if len(header_parts) > 3 else None,
            "payload": payload
        }

    def limb_i2c(self, bus, addr, reg, data, nonce=0):
        """Formats an I2C write as a Symbolic (S-Loom) LMB message."""
        payload_parts = [f"B:{bus}", f"A:{addr:02x}", f"R:{reg:02x}", f"D:{data:02x}"]
        return self.s_encode("LMB", payload_parts, nonce=nonce)

    def manifest(self, text, tags=None, nonce=0):
        """Formats a thought manifestation as a Symbolic (S-Loom) INF message."""
        payload_parts = [f"T:{text}"]
        if tags:
            payload_parts.append(f"G:{','.join(tags)}")
        return self.s_encode("INF", payload_parts, nonce=nonce)

    # Binary encoding placeholders (requires cbor2 / protobuf)
    def encode_binary(self, intent, payload, format="cbor"):
        raise NotImplementedError("Binary encoding requires external libraries (cbor2/protobuf)")

if __name__ == "__main__":
    loom = AetherLoom("REGGIE")
    msg = loom.encode("REQ", {"t": "sum", "u": "https://r3ggie.ai"}, nonce=42)
    print(f"Encoded: {msg}")
    print(f"Decoded: {loom.decode(msg)}")
