from vatel.api.base import BaseAPI
from vatel.models.rest import SessionTokenResponse


class SessionAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def generate_token(self, agent_id: str) -> SessionTokenResponse:
        client = self._base._get_client()
        r = client.post(
            "/v1/session-token",
            params={"agentId": agent_id},
        )
        r.raise_for_status()
        return SessionTokenResponse.model_validate(r.json())

    async def generate_token_async(self, agent_id: str) -> SessionTokenResponse:
        client = self._base._get_async_client()
        r = await client.post(
            "/v1/session-token",
            params={"agentId": agent_id},
        )
        r.raise_for_status()
        return SessionTokenResponse.model_validate(r.json())
