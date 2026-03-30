from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import Organization


class OrganizationAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def get(self) -> Organization:
        client = self._base._get_client()
        r = client.get("/v1/organization")
        r.raise_for_status()
        return Organization.model_validate(r.json())

    async def get_async(self) -> Organization:
        client = self._base._get_async_client()
        r = await client.get("/v1/organization")
        r.raise_for_status()
        return Organization.model_validate(r.json())
