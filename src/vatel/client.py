from typing import Optional

import httpx

from vatel.api.agents import AgentsAPI
from vatel.api.base import BaseAPI, DEFAULT_BASE_URL
from vatel.api.session import SessionAPI
from vatel.connection import Connection, connect as ws_connect


class Client:
    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        http_client: Optional[httpx.Client] = None,
        async_http_client: Optional[httpx.AsyncClient] = None,
    ):
        self._api = BaseAPI(
            api_key=api_key,
            base_url=base_url,
            http_client=http_client,
            async_http_client=async_http_client,
        )
        self.session = SessionAPI(self._api)
        self.agents = AgentsAPI(self._api)

    def close(self) -> None:
        self._api.close()

    async def aclose(self) -> None:
        await self._api.aclose()

    async def connect(
        self, token: str, url: Optional[str] = None, path: Optional[str] = None
    ) -> Connection:
        return await ws_connect(token=token, url=url, path=path)
