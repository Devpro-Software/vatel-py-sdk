from __future__ import annotations

from typing import Any, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class VoiceSessionEmptyData(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ToolCallArgument(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    dataType: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    value: Optional[Any] = None


class SessionStartedData(BaseModel):
    id: str


class SessionStarted(BaseModel):
    type: Literal["session_started"] = "session_started"
    data: SessionStartedData


class ResponseAudioData(BaseModel):
    turn_id: str
    audio: str = Field(..., description="Base64-encoded audio in PCM 16 24000Hz mono")
    is_final: bool


class ResponseAudio(BaseModel):
    type: Literal["response_audio"] = "response_audio"
    data: ResponseAudioData


class ResponseTextData(BaseModel):
    turn_id: str
    text: str
    is_final: bool


class ResponseText(BaseModel):
    type: Literal["response_text"] = "response_text"
    data: ResponseTextData


class InputAudioTranscriptData(BaseModel):
    transcript: str
    turn_id: Optional[str] = None
    is_final: bool


class InputAudioTranscript(BaseModel):
    type: Literal["input_audio_transcript"] = "input_audio_transcript"
    data: InputAudioTranscriptData


class SpeechStartedData(BaseModel):
    emulated: bool


class SpeechStarted(BaseModel):
    type: Literal["speech_started"] = "speech_started"
    data: SpeechStartedData


class SpeechStopped(BaseModel):
    type: Literal["speech_stopped"] = "speech_stopped"
    data: VoiceSessionEmptyData = Field(default_factory=VoiceSessionEmptyData)


class SessionEnded(BaseModel):
    type: Literal["session_ended"] = "session_ended"
    data: VoiceSessionEmptyData = Field(default_factory=VoiceSessionEmptyData)


class Interruption(BaseModel):
    type: Literal["interruption"] = "interruption"
    data: VoiceSessionEmptyData = Field(default_factory=VoiceSessionEmptyData)


class ToolCallData(BaseModel):
    toolCallId: str
    toolName: str
    arguments: list[ToolCallArgument] = Field(default_factory=list)


class ToolCall(BaseModel):
    type: Literal["tool_call"] = "tool_call"
    data: ToolCallData


class InputAudioData(BaseModel):
    audio: str = Field(..., description="Base64-encoded audio in PCM 16 24000Hz mono")


class InputAudio(BaseModel):
    type: Literal["input_audio"] = "input_audio"
    data: InputAudioData


class ToolCallOutputData(BaseModel):
    toolCallId: str
    output: str


class ToolCallOutput(BaseModel):
    type: Literal["tool_call_output"] = "tool_call_output"
    data: ToolCallOutputData


ServerMessage = Union[
    SessionStarted,
    ResponseAudio,
    ResponseText,
    InputAudioTranscript,
    SpeechStarted,
    SpeechStopped,
    SessionEnded,
    Interruption,
    ToolCall,
]

_EMPTY_DATA_TYPES = frozenset({"speech_stopped", "session_ended", "interruption"})


def _normalize_server_message(raw: dict[str, Any]) -> dict[str, Any]:
    if raw.get("type") in _EMPTY_DATA_TYPES and raw.get("data") is None:
        return {**raw, "data": {}}
    return raw


def parse_server_message(raw: dict[str, Any]) -> ServerMessage:
    raw = _normalize_server_message(raw)
    t = raw.get("type")
    if t == "session_started":
        return SessionStarted.model_validate(raw)
    if t == "response_audio":
        return ResponseAudio.model_validate(raw)
    if t == "response_text":
        return ResponseText.model_validate(raw)
    if t == "input_audio_transcript":
        return InputAudioTranscript.model_validate(raw)
    if t == "speech_started":
        return SpeechStarted.model_validate(raw)
    if t == "speech_stopped":
        return SpeechStopped.model_validate(raw)
    if t == "session_ended":
        return SessionEnded.model_validate(raw)
    if t == "interruption":
        return Interruption.model_validate(raw)
    if t == "tool_call":
        return ToolCall.model_validate(raw)
    raise ValueError(f"Unknown server message type: {t!r}")
