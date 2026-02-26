# AetherLoom Specification (v0.1.0-alpha)

## 1. Structure
All AetherLoom messages follow a compressed header-payload structure.

### 1.1 Header
`[AGENT_ID:SESSION_ID:NONCE]`

### 1.2 Intent Codes
- `REQ`: Request
- `RES`: Response
- `INF`: Information/Broadcast
- `ACT`: Action Trigger
- `ERR`: Error State

### 1.3 Payload
Payloads are serialized as **MiniJSON** (a subset of JSON optimized for token count, removing whitespace and using short keys).

## 2. Examples

### Requesting Weather (Human vs AL-1)
**Human-like Agent:**
"Hello, could you please provide the current weather for New York City?" (14 tokens)

**AL-1:**
`[REQ:WX]{"l":"NYC"}` (6 tokens)

### Task Delegation
`[ACT:TASK]{"id":"99","cmd":"build_db","dep":["auth"]}`

## 3. Efficiency Target
The goal is to achieve a **Token Reduction Ratio (TRR)** of 0.1 or lower (90% reduction) compared to GPT-4o's standard conversational output for the same intent.
