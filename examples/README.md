# Examples

Use the SDK from the repo via `sys.path` (no publish required).

## Run a session

Full-duplex demo: mic → server, agent audio → speaker. Requires `numpy` and `sounddevice`.

```bash
pip install -r examples/requirements-optional.txt
python examples/run_session.py --api-key YOUR_API_KEY --agent-id AGENT_UUID
```

Or set `VATEL_API_KEY` and `VATEL_AGENT_ID`. Optional: `--base-url` or `VATEL_BASE_URL`.
