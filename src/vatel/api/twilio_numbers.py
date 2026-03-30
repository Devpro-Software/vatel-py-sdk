from __future__ import annotations

from vatel.api.base import BaseAPI
from vatel.models.rest import (
    TwilioPhoneNumber,
    TwilioPhoneNumberImportInput,
    TwilioPhoneNumberLabelPatchInput,
)


class TwilioNumbersAPI:
    def __init__(self, base: BaseAPI):
        self._base = base

    def list(self) -> list[TwilioPhoneNumber]:
        client = self._base._get_client()
        r = client.get("/v1/twilio/numbers")
        r.raise_for_status()
        return [TwilioPhoneNumber.model_validate(x) for x in r.json()]

    async def list_async(self) -> list[TwilioPhoneNumber]:
        client = self._base._get_async_client()
        r = await client.get("/v1/twilio/numbers")
        r.raise_for_status()
        return [TwilioPhoneNumber.model_validate(x) for x in r.json()]

    def import_number(self, body: TwilioPhoneNumberImportInput) -> TwilioPhoneNumber:
        client = self._base._get_client()
        r = client.post(
            "/v1/twilio/numbers",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return TwilioPhoneNumber.model_validate(r.json())

    async def import_number_async(self, body: TwilioPhoneNumberImportInput) -> TwilioPhoneNumber:
        client = self._base._get_async_client()
        r = await client.post(
            "/v1/twilio/numbers",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return TwilioPhoneNumber.model_validate(r.json())

    def update_label(self, number_id: str, body: TwilioPhoneNumberLabelPatchInput) -> TwilioPhoneNumber:
        client = self._base._get_client()
        r = client.patch(
            f"/v1/twilio/numbers/{number_id}",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return TwilioPhoneNumber.model_validate(r.json())

    async def update_label_async(
        self, number_id: str, body: TwilioPhoneNumberLabelPatchInput
    ) -> TwilioPhoneNumber:
        client = self._base._get_async_client()
        r = await client.patch(
            f"/v1/twilio/numbers/{number_id}",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        r.raise_for_status()
        return TwilioPhoneNumber.model_validate(r.json())
