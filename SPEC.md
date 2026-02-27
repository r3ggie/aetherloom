# AetherLoom Specification (v0.2.0-beta)

## 1. Structure
AetherLoom (AL-1) messages support two transport encodings: **Text (Compact JSON)** and **Binary (CBOR/Protobuf)**.

### 1.1 Envelope Structure
Every message consists of a **Header** and a **Payload**.

#### Header (Text)
Format: `[VER:INTENT:SENDER_ID:NONCE]`
- `VER`: Protocol version (e.g., `1`)
- `INTENT`: 3-character intent code.
- `SENDER_ID`: Unique identifier for the sending agent.
- `NONCE`: Optional sequence number for idempotency.

#### Header (Binary - CBOR)
A map containing keys `v` (version), `i` (intent), `s` (sender), and `n` (nonce).

### 1.2 Intent Codes
- `REQ`: Request - Expects a response.
- `RES`: Response - Result of a request.
- `INF`: Information - Unidirectional broadcast/telemetry.
- `ACT`: Action - Trigger a specific capability.
- `ERR`: Error - Protocol or execution failure.
- `ACK`: Acknowledgment - Confirmation of receipt.

### 1.3 Payload Encodings

#### MiniJSON (Default for LLMs)
- JSON without whitespace.
- Keys should be abbreviated (e.g., `t` for `task`, `u` for `url`).
- Example: `{"t":"sum","u":"http://..."}`

#### CBOR (Default for Machine-to-Machine)
- Concise Binary Object Representation (RFC 8949).
- Used when LLM parsing is not required (e.g., agent-to-infrastructure).

#### Protobuf (High-Performance)
- Recommended for high-throughput or strictly-typed interactions.
- Schema defined in `aetherloom.proto`.

## 2. Examples

### Requesting Summary (Text)
`[1:REQ:REGGIE:101]{"t":"sum","u":"https://r3ggie.ai"}`

### Error Response (Text)
`[1:ERR:REGGIE:101]{"c":404,"m":"Not Found"}`

## 3. Efficiency Target
- **TRR (Token Reduction Ratio)**: < 0.1.
- **Binary Overhead**: < 10% of payload size.
