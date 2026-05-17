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
        version_id: Optional[str] = None,
        chat_id: Optional[str] = None,
        transport: Optional[Literal["websocket", "webrtc"]] = None,
        first_message: Optional[str] = None,
        prompt: Optional[str] = None,
        chat: Optional[bool] = None,
    ) -> SessionTokenResponse:
        client = self._base._get_client()
        body = self._token_body(
            agent_id=agent_id,
            version_id=version_id,
            chat_id=chat_id,
            transport=transport,
            first_message=first_message,
            prompt=prompt,
            chat=chat,
        )
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
        version_id: Optional[str] = None,
        chat_id: Optional[str] = None,
        transport: Optional[Literal["websocket", "webrtc"]] = None,
        first_message: Optional[str] = None,
        prompt: Optional[str] = None,
        chat: Optional[bool] = None,
    ) -> SessionTokenResponse:
        client = self._base._get_async_client()
        body = self._token_body(
            agent_id=agent_id,
            version_id=version_id,
            chat_id=chat_id,
            transport=transport,
            first_message=first_message,
            prompt=prompt,
            chat=chat,
        )
        r = await client.post(
            "/v1/session-token",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SessionTokenResponse.model_validate(r.json())

    @staticmethod
    def _token_body(
        *,
        agent_id: str,
        version_id: Optional[str],
        chat_id: Optional[str],
        transport: Optional[Literal["websocket", "webrtc"]],
        first_message: Optional[str],
        prompt: Optional[str],
        chat: Optional[bool],
    ) -> GenerateSessionTokenRequest:
        return GenerateSessionTokenRequest(
            agent_id=agent_id,
            version_id=version_id,
            chat_id=chat_id,
            transport=transport,
            first_message=first_message,
            prompt=prompt,
            chat=chat,
        )
