from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import (
    Agent,
    AgentCreateInput,
    AgentUpdateInput,
    DialAgentResponse,
    GraphVersion,
    GraphVersionDetail,
)


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

    def create(self, body: AgentCreateInput) -> Agent:
        client = self._base._get_client()
        r = client.post(
            "/v1/agents",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return Agent.model_validate(r.json())

    async def create_async(self, body: AgentCreateInput) -> Agent:
        client = self._base._get_async_client()
        r = await client.post(
            "/v1/agents",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return Agent.model_validate(r.json())

    def get(self, agent_id: str) -> Agent:
        client = self._base._get_client()
        r = client.get(f"/v1/agents/{agent_id}")
        r.raise_for_status()
        return Agent.model_validate(r.json())

    async def get_async(self, agent_id: str) -> Agent:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/agents/{agent_id}")
        r.raise_for_status()
        return Agent.model_validate(r.json())

    def update(self, agent_id: str, body: AgentUpdateInput) -> Agent:
        client = self._base._get_client()
        r = client.patch(
            f"/v1/agents/{agent_id}",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return Agent.model_validate(r.json())

    async def update_async(self, agent_id: str, body: AgentUpdateInput) -> Agent:
        client = self._base._get_async_client()
        r = await client.patch(
            f"/v1/agents/{agent_id}",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return Agent.model_validate(r.json())

    def delete(self, agent_id: str) -> None:
        client = self._base._get_client()
        r = client.delete(f"/v1/agents/{agent_id}")
        r.raise_for_status()

    async def delete_async(self, agent_id: str) -> None:
        client = self._base._get_async_client()
        r = await client.delete(f"/v1/agents/{agent_id}")
        r.raise_for_status()

    def list_versions(self, agent_id: str) -> list[GraphVersion]:
        client = self._base._get_client()
        r = client.get(f"/v1/agents/{agent_id}/versions")
        r.raise_for_status()
        return [GraphVersion.model_validate(x) for x in r.json()]

    async def list_versions_async(self, agent_id: str) -> list[GraphVersion]:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/agents/{agent_id}/versions")
        r.raise_for_status()
        return [GraphVersion.model_validate(x) for x in r.json()]

    def get_version(self, agent_id: str, version_id: str) -> GraphVersionDetail:
        client = self._base._get_client()
        r = client.get(f"/v1/agents/{agent_id}/versions/{version_id}")
        r.raise_for_status()
        return GraphVersionDetail.model_validate(r.json())

    async def get_version_async(self, agent_id: str, version_id: str) -> GraphVersionDetail:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/agents/{agent_id}/versions/{version_id}")
        r.raise_for_status()
        return GraphVersionDetail.model_validate(r.json())

    def publish_version(self, agent_id: str, version_id: str) -> GraphVersion:
        client = self._base._get_client()
        r = client.post(f"/v1/agents/{agent_id}/versions/{version_id}/publish")
        r.raise_for_status()
        return GraphVersion.model_validate(r.json())

    async def publish_version_async(self, agent_id: str, version_id: str) -> GraphVersion:
        client = self._base._get_async_client()
        r = await client.post(f"/v1/agents/{agent_id}/versions/{version_id}/publish")
        r.raise_for_status()
        return GraphVersion.model_validate(r.json())

    def dial(self, agent_id: str, number: str) -> DialAgentResponse:
        client = self._base._get_client()
        r = client.post(f"/v1/agents/{agent_id}/dial", params={"number": number})
        r.raise_for_status()
        return DialAgentResponse.model_validate(r.json())

    async def dial_async(self, agent_id: str, number: str) -> DialAgentResponse:
        client = self._base._get_async_client()
        r = await client.post(f"/v1/agents/{agent_id}/dial", params={"number": number})
        r.raise_for_status()
        return DialAgentResponse.model_validate(r.json())
