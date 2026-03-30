from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AgentStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class TTSStrategy(str, Enum):
    ELEVENLABS = "elevenlabs"
    OPENAI = "openai"
    CARTESIA = "cartesia"
    HUME = "hume"
    MINIMAX = "minimax"
    FISH = "fish"


class TimeoutAction(str, Enum):
    END_CALL = "end_call"
    TRANSFER_CALL = "transfer_call"


class VoiceSettings(BaseModel):
    id: Optional[str] = None
    provider: Optional[str] = None
    speed: Optional[float] = None
    stability: Optional[float] = None
    similarity_boost: Optional[float] = None
    volume: Optional[float] = None


class VadSettings(BaseModel):
    start_secs: Optional[float] = None
    stop_secs: Optional[float] = None
    silence_timeout_secs: Optional[float] = None


class NoiseCancelSettings(BaseModel):
    enabled: Optional[bool] = None
    level: Optional[float] = None


class TimeoutSettings(BaseModel):
    default_timeout: Optional[float] = None
    timeout_action: Optional[str] = None
    transfer_number: Optional[str] = None
    transfer_message: Optional[str] = None
    silence_counter: Optional[int] = None
    silence_timeout_action: Optional[str] = None
    silence_transfer_number: Optional[str] = None


class Agent(BaseModel):
    id: Optional[str] = None
    phone_number_id: Optional[str] = None
    name: Optional[str] = None
    llm: Optional[str] = None
    fallback_llm: Optional[str] = None
    status: Optional[str] = None
    prompt: Optional[str] = None
    first_message: Optional[str] = None
    first_message_interruption_time: Optional[float] = None
    default_language: Optional[str] = None
    summarize_calls: Optional[bool] = None
    tts_strategy: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    noise_cancel_settings: Optional[NoiseCancelSettings] = None
    vad_settings: Optional[VadSettings] = None
    enable_first_message_outbound: Optional[bool] = None
    voice_settings: Optional[VoiceSettings] = None
    timeout_settings: Optional[TimeoutSettings] = None
    keyterms: Optional[list[str]] = None


class AgentCreateInput(BaseModel):
    name: str
    phone_number_id: Optional[str] = None
    llm: Optional[str] = None
    fallback_llm: Optional[str] = None
    status: Optional[str] = None
    prompt: Optional[str] = None
    first_message: Optional[str] = None
    first_message_interruption_time: Optional[float] = None
    default_language: Optional[str] = None
    summarize_calls: Optional[bool] = None
    noise_cancel_settings: Optional[NoiseCancelSettings] = None
    vad_settings: Optional[VadSettings] = None
    enable_first_message_outbound: Optional[bool] = None
    timeout_settings: Optional[TimeoutSettings] = None
    keyterms: Optional[list[str]] = None
    voice_settings: Optional[VoiceSettings] = None


class AgentUpdateInput(BaseModel):
    phone_number_id: Optional[str] = None
    name: Optional[str] = None
    llm: Optional[str] = None
    fallback_llm: Optional[str] = None
    status: Optional[str] = None
    prompt: Optional[str] = None
    first_message: Optional[str] = None
    first_message_interruption_time: Optional[float] = None
    default_language: Optional[str] = None
    summarize_calls: Optional[bool] = None
    noise_cancel_settings: Optional[NoiseCancelSettings] = None
    vad_settings: Optional[VadSettings] = None
    enable_first_message_outbound: Optional[bool] = None
    timeout_settings: Optional[TimeoutSettings] = None
    keyterms: Optional[list[str]] = None
    voice_settings: Optional[VoiceSettings] = None


class Organization(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None


class LLMStringsResponse(BaseModel):
    llms: list[str]


class VoiceCatalogEntry(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    provider: str
    languages: list[str]
    preview_url: Optional[str] = None
    featured: Optional[bool] = None


class VoicesListResponse(BaseModel):
    voices: list[VoiceCatalogEntry]


class GraphVersion(BaseModel):
    id: Optional[str] = None
    agent_id: Optional[str] = None
    created_at: Optional[str] = None
    published_at: Optional[str] = None
    tag: Optional[str] = None


class GraphNode(BaseModel):
    model_config = ConfigDict(extra="allow")


class GraphVersionDetail(BaseModel):
    version: GraphVersion
    nodes: list[GraphNode]


class DialAgentResponse(BaseModel):
    success: bool


class TwilioPhoneNumber(BaseModel):
    id: Optional[str] = None
    phone_number: Optional[str] = None
    phone_sid: Optional[str] = None
    label: Optional[str] = None
    account_sid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class TwilioPhoneNumberImportInput(BaseModel):
    phone_number: str
    account_sid: str
    auth_token: str
    label: Optional[str] = None


class TwilioPhoneNumberLabelPatchInput(BaseModel):
    label: str


class SipTrunkCallerIDTransform(BaseModel):
    type: str
    value: Optional[str] = None
    value2: Optional[str] = None
    number: Optional[int] = None


class SipTrunk(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: Optional[str] = None
    created_at: Optional[str] = None
    pbx: Optional[str] = None
    caller_id_transforms: Optional[list[SipTrunkCallerIDTransform]] = None
    inbound_host: Optional[str] = None
    inbound_auth_type: Optional[str] = None
    inbound_sip_username: Optional[str] = None
    inbound_registration_status: Optional[str] = None
    outbound_host: Optional[str] = None
    outbound_sip_username: Optional[str] = None
    register_trunk: Optional[bool] = Field(default=None, validation_alias="register", serialization_alias="register")
    outbound_registration_status: Optional[str] = None
    remain_in_dialog: Optional[bool] = None


class SipTrunkCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    pbx: str
    caller_id_transforms: Optional[list[SipTrunkCallerIDTransform]] = None
    inbound_host: Optional[str] = None
    inbound_auth_type: Optional[str] = None
    inbound_sip_username: Optional[str] = None
    inbound_sip_password: Optional[str] = None
    outbound_host: Optional[str] = None
    outbound_sip_username: Optional[str] = None
    outbound_sip_password: Optional[str] = None
    register_trunk: Optional[bool] = Field(default=None, validation_alias="register", serialization_alias="register")
    remain_in_dialog: Optional[bool] = None


class SipTrunkUpdateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    pbx: Optional[str] = None
    caller_id_transforms: Optional[list[SipTrunkCallerIDTransform]] = None
    inbound_host: Optional[str] = None
    inbound_auth_type: Optional[str] = None
    inbound_sip_username: Optional[str] = None
    inbound_sip_password: Optional[str] = None
    outbound_host: Optional[str] = None
    outbound_sip_username: Optional[str] = None
    outbound_sip_password: Optional[str] = None
    register_trunk: Optional[bool] = Field(default=None, validation_alias="register", serialization_alias="register")
    remain_in_dialog: Optional[bool] = None


class SipTrunkAgentAssignment(BaseModel):
    id: Optional[str] = None
    agent_id: Optional[str] = None
    sip_trunk_id: Optional[str] = None
    number: Optional[str] = None
    alternate_number: Optional[str] = None
    created_at: Optional[str] = None


class SipTrunkAgentAssignmentCreateInput(BaseModel):
    agent_id: str
    number: Optional[str] = None
    alternate_number: Optional[str] = None


class SipTrunkAgentAssignmentPatchInput(BaseModel):
    number: Optional[str] = None
    alternate_number: Optional[str] = None


class SessionTokenResponse(BaseModel):
    token: str = Field(..., description="Short-lived JWT for session/embed auth")


class ErrorResponse(BaseModel):
    error: str
