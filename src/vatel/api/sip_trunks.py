from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import (
    SipTrunk,
    SipTrunkAgentAssignment,
    SipTrunkAgentAssignmentCreateInput,
    SipTrunkAgentAssignmentPatchInput,
    SipTrunkCreateInput,
    SipTrunkUpdateInput,
)


class SipTrunksAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def list(self) -> list[SipTrunk]:
        client = self._base._get_client()
        r = client.get("/v1/sip-trunks")
        r.raise_for_status()
        return [SipTrunk.model_validate(x) for x in r.json()]

    async def list_async(self) -> list[SipTrunk]:
        client = self._base._get_async_client()
        r = await client.get("/v1/sip-trunks")
        r.raise_for_status()
        return [SipTrunk.model_validate(x) for x in r.json()]

    def create(self, body: SipTrunkCreateInput) -> SipTrunk:
        client = self._base._get_client()
        r = client.post(
            "/v1/sip-trunks",
            json=body.model_dump(mode="json", exclude_unset=True, by_alias=True),
        )
        r.raise_for_status()
        return SipTrunk.model_validate(r.json())

    async def create_async(self, body: SipTrunkCreateInput) -> SipTrunk:
        client = self._base._get_async_client()
        r = await client.post(
            "/v1/sip-trunks",
            json=body.model_dump(mode="json", exclude_unset=True, by_alias=True),
        )
        r.raise_for_status()
        return SipTrunk.model_validate(r.json())

    def get(self, trunk_id: str) -> SipTrunk:
        client = self._base._get_client()
        r = client.get(f"/v1/sip-trunks/{trunk_id}")
        r.raise_for_status()
        return SipTrunk.model_validate(r.json())

    async def get_async(self, trunk_id: str) -> SipTrunk:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/sip-trunks/{trunk_id}")
        r.raise_for_status()
        return SipTrunk.model_validate(r.json())

    def update(self, trunk_id: str, body: SipTrunkUpdateInput) -> SipTrunk:
        client = self._base._get_client()
        r = client.patch(
            f"/v1/sip-trunks/{trunk_id}",
            json=body.model_dump(mode="json", exclude_unset=True, by_alias=True),
        )
        r.raise_for_status()
        return SipTrunk.model_validate(r.json())

    async def update_async(self, trunk_id: str, body: SipTrunkUpdateInput) -> SipTrunk:
        client = self._base._get_async_client()
        r = await client.patch(
            f"/v1/sip-trunks/{trunk_id}",
            json=body.model_dump(mode="json", exclude_unset=True, by_alias=True),
        )
        r.raise_for_status()
        return SipTrunk.model_validate(r.json())

    def delete(self, trunk_id: str) -> None:
        client = self._base._get_client()
        r = client.delete(f"/v1/sip-trunks/{trunk_id}")
        r.raise_for_status()

    async def delete_async(self, trunk_id: str) -> None:
        client = self._base._get_async_client()
        r = await client.delete(f"/v1/sip-trunks/{trunk_id}")
        r.raise_for_status()

    def list_assignments(self, trunk_id: str) -> list[SipTrunkAgentAssignment]:
        client = self._base._get_client()
        r = client.get(f"/v1/sip-trunks/{trunk_id}/assignments")
        r.raise_for_status()
        return [SipTrunkAgentAssignment.model_validate(x) for x in r.json()]

    async def list_assignments_async(self, trunk_id: str) -> list[SipTrunkAgentAssignment]:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/sip-trunks/{trunk_id}/assignments")
        r.raise_for_status()
        return [SipTrunkAgentAssignment.model_validate(x) for x in r.json()]

    def create_assignment(
        self, trunk_id: str, body: SipTrunkAgentAssignmentCreateInput
    ) -> SipTrunkAgentAssignment:
        client = self._base._get_client()
        r = client.post(
            f"/v1/sip-trunks/{trunk_id}/assignments",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SipTrunkAgentAssignment.model_validate(r.json())

    async def create_assignment_async(
        self, trunk_id: str, body: SipTrunkAgentAssignmentCreateInput
    ) -> SipTrunkAgentAssignment:
        client = self._base._get_async_client()
        r = await client.post(
            f"/v1/sip-trunks/{trunk_id}/assignments",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SipTrunkAgentAssignment.model_validate(r.json())

    def get_assignment(self, assignment_id: str) -> SipTrunkAgentAssignment:
        client = self._base._get_client()
        r = client.get(f"/v1/sip-trunks/assignments/{assignment_id}")
        r.raise_for_status()
        return SipTrunkAgentAssignment.model_validate(r.json())

    async def get_assignment_async(self, assignment_id: str) -> SipTrunkAgentAssignment:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/sip-trunks/assignments/{assignment_id}")
        r.raise_for_status()
        return SipTrunkAgentAssignment.model_validate(r.json())

    def update_assignment(
        self, assignment_id: str, body: SipTrunkAgentAssignmentPatchInput
    ) -> SipTrunkAgentAssignment:
        client = self._base._get_client()
        r = client.patch(
            f"/v1/sip-trunks/assignments/{assignment_id}",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SipTrunkAgentAssignment.model_validate(r.json())

    async def update_assignment_async(
        self, assignment_id: str, body: SipTrunkAgentAssignmentPatchInput
    ) -> SipTrunkAgentAssignment:
        client = self._base._get_async_client()
        r = await client.patch(
            f"/v1/sip-trunks/assignments/{assignment_id}",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return SipTrunkAgentAssignment.model_validate(r.json())

    def delete_assignment(self, assignment_id: str) -> None:
        client = self._base._get_client()
        r = client.delete(f"/v1/sip-trunks/assignments/{assignment_id}")
        r.raise_for_status()

    async def delete_assignment_async(self, assignment_id: str) -> None:
        client = self._base._get_async_client()
        r = await client.delete(f"/v1/sip-trunks/assignments/{assignment_id}")
        r.raise_for_status()
