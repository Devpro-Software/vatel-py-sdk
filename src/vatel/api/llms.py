from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import LLMStringsResponse


class LLMsAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def list(self) -> LLMStringsResponse:
        client = self._base._get_client()
        r = client.get("/v1/llms")
        r.raise_for_status()
        return LLMStringsResponse.model_validate(r.json())

    async def list_async(self) -> LLMStringsResponse:
        client = self._base._get_async_client()
        r = await client.get("/v1/llms")
        r.raise_for_status()
        return LLMStringsResponse.model_validate(r.json())
