from typing import Optional

import httpx

DEFAULT_BASE_URL = "https://api.vatel.ai"
DEFAULT_WS_URL = "wss://api.vatel.ai"


class BaseAPI:
    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        http_client: Optional[httpx.Client] = None,
        async_http_client: Optional[httpx.AsyncClient] = None,
    ):
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._client = http_client
        self._async_client = async_http_client

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

    def _get_client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(
                base_url=self._base_url,
                headers=self._headers(),
                timeout=30.0,
            )
        return self._client

    def _get_async_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                headers=self._headers(),
                timeout=30.0,
            )
        return self._async_client

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None
        if self._async_client is not None:
            self._async_client.close()
            self._async_client = None

    async def aclose(self) -> None:
        if self._async_client is not None:
            await self._async_client.aclose()
            self._async_client = None
