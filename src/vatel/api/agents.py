from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import Agent


class AgentsAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def list(self) -> list[Agent]:
        client = self._base._get_client()
        r = client.get("/v1/agents")
        r.raise_for_status()
        return [Agent.model_validate(item) for item in r.json()]

    async def list_async(self) -> list[Agent]:
        client = self._base._get_async_client()
        r = await client.get("/v1/agents")
        r.raise_for_status()
        return [Agent.model_validate(item) for item in r.json()]
