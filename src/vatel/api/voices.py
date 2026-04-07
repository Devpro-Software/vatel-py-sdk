from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import VoicesListResponse


class VoicesAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def list(self) -> VoicesListResponse:
        client = self._base._get_client()
        r = client.get("/v1/voices")
        r.raise_for_status()
        return VoicesListResponse.model_validate(r.json())

    async def list_async(self) -> VoicesListResponse:
        client = self._base._get_async_client()
        r = await client.get("/v1/voices")
        r.raise_for_status()
        return VoicesListResponse.model_validate(r.json())
