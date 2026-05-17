from __future__ import annotations

from enum import Enum
from typing import Any, Literal, Optional, Union

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


class CallerTransformType(str, Enum):
    ADD_PREFIX = "add_prefix"
    ADD_SUFFIX = "add_suffix"
    REPLACE = "replace"
    STRIP_DIGITS_END = "strip_digits_end"
    STRIP_DIGITS_START = "strip_digits_start"


class SIPTrunkAuthType(str, Enum):
    DIGEST = "digest"
    ACL = "acl"
    NONE = "none"


class RegistrationStatus(str, Enum):
    NOT_REGISTERED = "not_registered"
    PENDING = "pending"
    REGISTERED = "registered"
    FAILED = "failed"
    AUTH_FAILED = "auth_failed"


class PbxType(str, Enum):
    THREE_CX = "3cx"
    YEASTAR = "yeastar"
    WEBEX = "webex"
    GENERIC = "generic"


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
    type: Union[CallerTransformType, str]
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


class GenerateSessionTokenRequest(BaseModel):
    agent_id: str
    version_id: Optional[str] = None
    chat_id: Optional[str] = None
    transport: Optional[Literal["websocket", "webrtc"]] = None
    first_message: Optional[str] = None
    prompt: Optional[str] = None
    chat: Optional[bool] = None


class SessionTokenResponse(BaseModel):
    token: str
    room: Optional[str] = None
    identity: Optional[str] = None
    url: Optional[str] = None
    webrtc_token: Optional[str] = None


class CallStatus(str, Enum):
    CONNECTED = "connected"
    STARTED = "started"
    IN_PROGRESS = "in_progress"
    AUTH_FAILED = "auth_failed"
    ENDED = "ended"


class CallSource(str, Enum):
    TWILIO = "twilio"
    SIP = "sip"
    SIMULATION = "simulation"
    API = "api"


class CallOutcome(str, Enum):
    TRANSFERRED = "transferred"
    ENDED_BY_AGENT = "ended_by_agent"
    ENDED_BY_USER = "ended_by_user"


class ContextVariable(BaseModel):
    name: Optional[str] = None
    type: Optional[Literal["system", "input", "extracted"]] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    dataType: Optional[Literal["string", "number", "boolean", "object", "array"]] = None
    rationale: Optional[str] = None


class TranscriptEntryType(str, Enum):
    MESSAGE = "message"
    TOOL_CALL = "tool_call"
    TOOL_CALL_OUTPUT = "tool_call_output"
    INTERRUPTION = "interruption"


class TranscriptToolCall(BaseModel):
    itemId: Optional[str] = None
    callId: Optional[str] = None
    toolName: Optional[str] = None
    arguments: Optional[str] = None
    output: Optional[str] = None
    startedAt: Optional[str] = None
    endedAt: Optional[str] = None


class TranscriptEntry(BaseModel):
    index: Optional[int] = None
    role: Optional[str] = None
    message: Optional[str] = None
    type: Optional[str] = None
    toolCall: Optional[TranscriptToolCall] = None
    toolCallOutput: Optional[str] = None
    createdAt: Optional[str] = None
    durationMs: Optional[int] = None
    turnId: Optional[str] = None


class Transcript(BaseModel):
    entries: list[TranscriptEntry]


class CallFeedback(BaseModel):
    stars: int
    notes: str


class Call(BaseModel):
    id: Optional[str] = None
    agent_id: Optional[str] = None
    graph_version_id: Optional[str] = None
    organization_id: Optional[str] = None
    party_number: Optional[str] = None
    status: Optional[str] = None
    source: Optional[str] = None
    termination_reason: Optional[str] = None
    extracted_variables: Optional[list[ContextVariable]] = None
    outbound: Optional[bool] = None
    outbound_contact_id: Optional[str] = None
    outbound_list_run_id: Optional[str] = None
    created_at: Optional[str] = None
    connected_at: Optional[str] = None
    started_at: Optional[str] = None
    ended_at: Optional[str] = None
    summary: Optional[str] = None
    transcript: Optional[Transcript] = None
    cost: Optional[float] = None
    tags: Optional[list[str]] = None
    duration_seconds: Optional[int] = None
    feedback: Optional[CallFeedback] = None


class PaginationInfo(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool


class PaginatedCallsResponse(BaseModel):
    calls: list[Call]
    pagination: PaginationInfo


class ErrorResponse(BaseModel):
    error: str
