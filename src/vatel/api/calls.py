from __future__ import annotations

from typing import Literal, Optional, Union

from vatel.api.base import BaseAPI
from vatel.models.rest import Call, CallOutcome, CallSource, CallStatus, PaginatedCallsResponse


class CallsAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def list(
        self,
        *,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        agent_ids: Optional[str] = None,
        status: Optional[Union[CallStatus, str]] = None,
        source: Optional[Union[CallSource, str]] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        outbound: Optional[Literal["true", "false"]] = None,
        search: Optional[str] = None,
        tag: Optional[str] = None,
        outcome: Optional[Union[CallOutcome, str]] = None,
    ) -> PaginatedCallsResponse:
        client = self._base._get_client()
        r = client.get("/v1/calls", params=self._list_params(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            agent_ids=agent_ids,
            status=status,
            source=source,
            date_from=date_from,
            date_to=date_to,
            outbound=outbound,
            search=search,
            tag=tag,
            outcome=outcome,
        ))
        r.raise_for_status()
        return PaginatedCallsResponse.model_validate(r.json())

    async def list_async(
        self,
        *,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        agent_ids: Optional[str] = None,
        status: Optional[Union[CallStatus, str]] = None,
        source: Optional[Union[CallSource, str]] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        outbound: Optional[Literal["true", "false"]] = None,
        search: Optional[str] = None,
        tag: Optional[str] = None,
        outcome: Optional[Union[CallOutcome, str]] = None,
    ) -> PaginatedCallsResponse:
        client = self._base._get_async_client()
        r = await client.get("/v1/calls", params=self._list_params(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            agent_ids=agent_ids,
            status=status,
            source=source,
            date_from=date_from,
            date_to=date_to,
            outbound=outbound,
            search=search,
            tag=tag,
            outcome=outcome,
        ))
        r.raise_for_status()
        return PaginatedCallsResponse.model_validate(r.json())

    def get(self, call_id: str) -> Call:
        client = self._base._get_client()
        r = client.get(f"/v1/calls/{call_id}")
        r.raise_for_status()
        return Call.model_validate(r.json())

    async def get_async(self, call_id: str) -> Call:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/calls/{call_id}")
        r.raise_for_status()
        return Call.model_validate(r.json())

    def download_recording(self, call_id: str) -> bytes:
        client = self._base._get_client()
        r = client.get(f"/v1/calls/{call_id}/recording")
        r.raise_for_status()
        return r.content

    async def download_recording_async(self, call_id: str) -> bytes:
        client = self._base._get_async_client()
        r = await client.get(f"/v1/calls/{call_id}/recording")
        r.raise_for_status()
        return r.content

    @staticmethod
    def _list_params(
        *,
        organization_id: Optional[str],
        page: Optional[int],
        page_size: Optional[int],
        agent_ids: Optional[str],
        status: Optional[Union[CallStatus, str]],
        source: Optional[Union[CallSource, str]],
        date_from: Optional[str],
        date_to: Optional[str],
        outbound: Optional[Literal["true", "false"]],
        search: Optional[str],
        tag: Optional[str],
        outcome: Optional[Union[CallOutcome, str]],
    ) -> dict[str, str | int]:
        params: dict[str, str | int] = {}
        if organization_id is not None:
            params["organization_id"] = organization_id
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if agent_ids is not None:
            params["agent_ids"] = agent_ids
        if status is not None:
            params["status"] = status.value if isinstance(status, CallStatus) else status
        if source is not None:
            params["source"] = source.value if isinstance(source, CallSource) else source
        if date_from is not None:
            params["date_from"] = date_from
        if date_to is not None:
            params["date_to"] = date_to
        if outbound is not None:
            params["outbound"] = outbound
        if search is not None:
            params["search"] = search
        if tag is not None:
            params["tag"] = tag
        if outcome is not None:
            params["outcome"] = outcome.value if isinstance(outcome, CallOutcome) else outcome
        return params
