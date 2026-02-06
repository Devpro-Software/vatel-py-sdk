import json
from typing import Any, AsyncIterator, Optional

import websockets

from vatel.models.ws import (
    InputAudio,
    InputAudioData,
    ServerMessage,
    ToolCallOutput,
    ToolCallOutputData,
    parse_server_message,
)

DEFAULT_WS_BASE = "wss://api.vatel.ai"
CONNECTION_PATH = "/v1/connection"


class Connection:
    def __init__(self, ws: Any, path: str):
        self._ws = ws
        self._path = path

    async def receive(self) -> ServerMessage:
        raw = await self._ws.recv()
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8")
        data = json.loads(raw)
        return parse_server_message(data)

    def receive_raw(self) -> Any:
        raise NotImplementedError("Use async receive(); sync receive not supported")

    async def send_input_audio(self, audio_base64: str) -> None:
        msg = InputAudio(data=InputAudioData(audio=audio_base64))
        await self._ws.send(msg.model_dump_json(exclude_none=True))

    async def send_tool_call_output(self, tool_call_id: str, output: str) -> None:
        msg = ToolCallOutput(data=ToolCallOutputData(toolCallId=tool_call_id, output=output))
        await self._ws.send(msg.model_dump_json(exclude_none=True))

    async def send_json(self, payload: dict[str, Any]) -> None:
        await self._ws.send(json.dumps(payload))

    async def stream_messages(self) -> AsyncIterator[ServerMessage]:
        async for raw in self._ws:
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8")
            data = json.loads(raw)
            yield parse_server_message(data)

    async def close(self) -> None:
        await self._ws.close()


async def connect(
    token: str,
    url: Optional[str] = None,
    path: Optional[str] = None,
) -> Connection:
    base = (url or DEFAULT_WS_BASE).rstrip("/").replace("https://", "wss://").replace("http://", "ws://")
    pathname = path or CONNECTION_PATH
    uri = f"{base}{pathname}?token={token}"
    ws = await websockets.connect(
        uri,
        close_timeout=5,
        open_timeout=10,
        ping_interval=20,
        ping_timeout=20,
    )
    return Connection(ws, pathname)
