from typing import Optional

import httpx

from vatel.api.agents import AgentsAPI
from vatel.api.base import BaseAPI, DEFAULT_BASE_URL
from vatel.api.llms import LLMsAPI
from vatel.api.organization import OrganizationAPI
from vatel.api.session import SessionAPI
from vatel.api.sip_trunks import SipTrunksAPI
from vatel.api.twilio_numbers import TwilioNumbersAPI
from vatel.api.voices import VoicesAPI
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
        self.organization = OrganizationAPI(self._api)
        self.llms = LLMsAPI(self._api)
        self.voices = VoicesAPI(self._api)
        self.agents = AgentsAPI(self._api)
        self.twilio_numbers = TwilioNumbersAPI(self._api)
        self.sip_trunks = SipTrunksAPI(self._api)
        self.session = SessionAPI(self._api)

    def close(self) -> None:
        self._api.close()

    async def aclose(self) -> None:
        await self._api.aclose()

    async def connect(
        self, token: str, url: Optional[str] = None, path: Optional[str] = None
    ) -> Connection:
        return await ws_connect(token=token, url=url, path=path)
