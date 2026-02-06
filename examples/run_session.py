#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import base64
import os
import queue
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vatel import Client
from vatel.connection import Connection
from vatel.models.ws import ToolCall

SAMPLE_RATE = 24000
BLOCKSIZE = 480

try:
    import numpy as np
    import sounddevice as sd
except ImportError:
    print("error: pip install numpy sounddevice", file=sys.stderr)
    sys.exit(1)


def mic_thread(
    loop: asyncio.AbstractEventLoop,
    out_queue: asyncio.Queue[str | None],
    stop: threading.Event,
) -> None:
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="int16", blocksize=BLOCKSIZE) as stream:
        while not stop.is_set():
            data, _ = stream.read(BLOCKSIZE)
            if data.size > 0:
                loop.call_soon_threadsafe(out_queue.put_nowait, base64.b64encode(data.tobytes()).decode("ascii"))


async def send_mic(conn: Connection, q: asyncio.Queue[str | None]) -> None:
    while True:
        chunk = await q.get()
        if chunk is None:
            break
        await conn.send_input_audio(chunk)


def make_player():
    q: queue.Queue[bytes | None] = queue.Queue()
    buf = np.array([], dtype=np.int16)

    def callback(outdata: np.ndarray, frames: int, time: object, status: object) -> None:
        nonlocal buf
        need = frames * outdata.shape[1]
        if status:
            outdata.flat[:] = 0
            return
        while len(buf) < need:
            try:
                chunk = q.get_nowait()
                if chunk is None:
                    break
                buf = np.concatenate([buf, np.frombuffer(chunk, dtype=np.int16)])
            except queue.Empty:
                break
        n = min(need, len(buf))
        if n:
            outdata.flat[:n] = buf[:n]
            buf = buf[n:]
        outdata.flat[n:] = 0

    stream = sd.OutputStream(samplerate=SAMPLE_RATE, channels=1, dtype=np.int16, blocksize=BLOCKSIZE, callback=callback)
    stream.start()
    return q, stream


async def run(api_key: str, agent_id: str, base_url: str | None) -> None:
    base_url = base_url or "https://staging.api.vatel.ai"
    client = Client(api_key=api_key, base_url=base_url)
    audio_q, playback = make_player()
    try:
        token = (await client.session.generate_token_async(agent_id)).token
        conn = await client.connect(token=token, url=base_url)
        mic_stop = threading.Event()
        mic_q: asyncio.Queue[str | None] = asyncio.Queue()
        mic_t = threading.Thread(target=mic_thread, args=(asyncio.get_running_loop(), mic_q, mic_stop), daemon=True)
        mic_t.start()
        send_task = asyncio.create_task(send_mic(conn, mic_q))
        try:
            async for msg in conn.stream_messages():
                t = getattr(msg, "type", None)
                if t == "session_started":
                    print("Session started:", msg.data.id)
                elif t == "response_text":
                    print("Agent:", msg.data.text)
                elif t == "input_audio_transcript":
                    print("You:", msg.data.transcript)
                elif t == "response_audio":
                    audio_q.put(base64.b64decode(msg.data.audio))
                elif isinstance(msg, ToolCall):
                    print("Tool:", msg.data.toolName)
                    await conn.send_tool_call_output(msg.data.toolCallId, "ok")
                elif t == "session_ended":
                    print("Session ended.")
                    break
        finally:
            mic_stop.set()
            mic_q.put_nowait(None)
            await send_task
            mic_t.join(timeout=2.0)
            await conn.close()
        audio_q.put(None)
        await asyncio.sleep(0.4)
        playback.stop()
        playback.close()
    finally:
        await client.aclose()


def main() -> None:
    p = argparse.ArgumentParser(description="Run a call session (mic + speaker) using the Vatel SDK.")
    p.add_argument("--api-key", default=os.environ.get("VATEL_API_KEY"), help="API key")
    p.add_argument("--agent-id", default=os.environ.get("VATEL_AGENT_ID"), help="Agent UUID")
    p.add_argument("--base-url", default=os.environ.get("VATEL_BASE_URL"), help="Optional base URL")
    args = p.parse_args()
    if not args.api_key or not args.agent_id:
        print("error: set --api-key and --agent-id (or VATEL_API_KEY, VATEL_AGENT_ID)", file=sys.stderr)
        sys.exit(1)
    asyncio.run(run(args.api_key, args.agent_id, args.base_url))


if __name__ == "__main__":
    main()
