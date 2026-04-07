from __future__ import annotations

from typing import Literal, Optional

from vatel.api.base import BaseAPI
from vatel.models.rest import GenerateSessionTokenRequest, SessionTokenResponse


class SessionAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def generate_token(
        self,
        agent_id: str,
        *,
        transport: Optional[Literal["websocket", "webrtc"]] = None,
    ) -> SessionTokenResponse:
        client = self._base._get_client()
        body = GenerateSessionTokenRequest(agent_id=agent_id, transport=transport)
        r = client.post(
            "/v1/session-token",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SessionTokenResponse.model_validate(r.json())

    async def generate_token_async(
        self,
        agent_id: str,
        *,
        transport: Optional[Literal["websocket", "webrtc"]] = None,
    ) -> SessionTokenResponse:
        client = self._base._get_async_client()
        body = GenerateSessionTokenRequest(agent_id=agent_id, transport=transport)
        r = await client.post(
            "/v1/session-token",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SessionTokenResponse.model_validate(r.json())
