from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AgentStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class TTSStrategy(str, Enum):
    ELEVENLABS = "elevenlabs"
    OPENAI = "openai"
    CARTESIA = "cartesia"


class TimeoutAction(str, Enum):
    END_CALL = "end_call"
    TRANSFER_CALL = "transfer_call"


class VoiceSettings(BaseModel):
    speed: Optional[float] = None
    stability: Optional[float] = None
    similarity_boost: Optional[float] = None
    volume: Optional[float] = None


class VadSettings(BaseModel):
    start_secs: Optional[float] = None
    starting_secs: Optional[float] = None
    stop_secs: Optional[float] = None
    stopping_secs: Optional[float] = None
    silence_timeout_secs: Optional[float] = None


class NoiseCancelSettings(BaseModel):
    enabled: Optional[bool] = None
    level: Optional[float] = None


class TimeoutAction:
    END_CALL = "end_call"
    TRANSFER_CALL = "transfer_call"


class TimeoutSettings(BaseModel):
    defaultTimeout: Optional[float] = None
    timeoutAction: Optional[str] = None
    transferNumber: Optional[str] = None
    transferMessage: Optional[str] = None
    silenceCounter: Optional[int] = None
    silenceTimeoutAction: Optional[str] = None
    silenceTransferNumber: Optional[str] = None
    silenceTransferMessage: Optional[str] = None


class Agent(BaseModel):
    id: Optional[str] = None
    phone_number_id: Optional[str] = None
    name: Optional[str] = None
    llm: Optional[str] = None
    status: Optional[str] = None
    prompt: Optional[str] = None
    first_message: Optional[str] = None
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


class SessionTokenResponse(BaseModel):
    token: str = Field(..., description="Short-lived JWT for session/embed auth")
