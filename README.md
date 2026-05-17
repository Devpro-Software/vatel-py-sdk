# Vatel Python SDK

Use the Call Agent Builder REST and WebSocket APIs from Python.

## Install

```bash
pip install "git+https://github.com/Devpro-Software/vatel-py-sdk.git@v0.4.1"
```

Requires Python 3.9+.

## Setup

You need an **organization API key**. Use it to create a client and to obtain short-lived **session tokens** for real-time calls.

```python
from vatel import Client

client = Client(api_key="your-organization-api-key")
```

To use a different host:

```python
client = Client(api_key="your-api-key", base_url="https://api.vatel.ai")
```

## REST API

### List agents

```python
agents = client.agents.list()
for agent in agents:
    print(agent.id, agent.name)
```

Async: `agents = await client.agents.list_async()`.

### Get a session token

Required for connecting to the WebSocket. Pass the **agent UUID** (and optional `version_id`) you want to run the call with; those values are encoded in the JWT returned as `token`.

```python
resp = client.session.generate_token(agent_id="agent-uuid-here")
token = resp.token
```

Async: `resp = await client.session.generate_token_async(agent_id="...")`.

## Real-time calls (WebSocket)

Connect with the session token from `generate_token`. Agent and graph version are read from the JWT on `GET /v1/connection`; only `token` is sent as a query parameter. The connection is **async-only**. You receive events (agent audio, transcripts, tool calls, session lifecycle) and send input audio and tool results.

```python
import asyncio
from vatel import Client
from vatel.models.ws import ToolCall

async def main():
    client = Client(api_key="your-api-key")
    agent_id = "agent-uuid"
    token = (await client.session.generate_token_async(agent_id=agent_id)).token
    conn = await client.connect(token=token)

    async for msg in conn.stream_messages():
        if getattr(msg, "type", None) == "session_started":
            print("Call started:", msg.data.id)
        elif getattr(msg, "type", None) == "response_text":
            print("Agent:", msg.data.text)
        elif getattr(msg, "type", None) == "input_audio_transcript":
            print("You:", msg.data.transcript)
        elif getattr(msg, "type", None) == "response_audio":
            # Base64 PCM 16-bit 24 000 Hz mono — decode and play or process
            pass
        elif getattr(msg, "type", None) == "session_ended":
            break
        elif isinstance(msg, ToolCall):
            await conn.send_tool_call_output(msg.data.toolCallId, "your-result")

    await conn.close()
    await client.aclose()

asyncio.run(main())
```

### Sending your audio

Send captured audio as base64-encoded **PCM 16-bit, 24 000 Hz, mono**:

```python
await conn.send_input_audio(audio_base64="...")
```

### Tool calls

When the server sends a `tool_call` message, run your logic and send the result back:

```python
await conn.send_tool_call_output(tool_call_id=msg.data.toolCallId, output="result string")
```

## Message types (server → client)

| Type                     | Description                          |
|--------------------------|--------------------------------------|
| `session_started`        | Call started; `data.id` is session ID |
| `session_ended`          | Call ended                            |
| `response_audio`         | Agent TTS chunk; `data.audio` base64, `data.turn_id`, `data.is_final` |
| `response_text`          | Agent text; `data.is_final` when committed for the turn |
| `input_audio_transcript` | Your speech (STT); `data.is_final` for final transcript |
| `speech_started` / `speech_stopped` | VAD events       |
| `interruption`           | You interrupted the agent            |
| `tool_call`              | Server requests a tool; reply with `send_tool_call_output` |

## Example app

The repo includes a small **full-duplex demo** (mic → server, agent audio → speaker):

```bash
pip install -r examples/requirements-optional.txt
python examples/run_session.py --api-key YOUR_KEY --agent-id AGENT_UUID
```

See `examples/README.md` for details.
