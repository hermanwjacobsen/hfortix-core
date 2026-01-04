from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class NetworkPolicyPayload(TypedDict, total=False):
    """
    Type hints for system/lldp/network_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: NetworkPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # LLDP network policy name.
    comment: NotRequired[str]  # Comment.
    voice: NotRequired[str]  # Voice.
    voice_signaling: NotRequired[str]  # Voice signaling.
    guest: NotRequired[str]  # Guest.
    guest_voice_signaling: NotRequired[str]  # Guest Voice Signaling.
    softphone: NotRequired[str]  # Softphone.
    video_conferencing: NotRequired[str]  # Video Conferencing.
    streaming_video: NotRequired[str]  # Streaming Video.
    video_signaling: NotRequired[str]  # Video Signaling.


class NetworkPolicy:
    """
    Configure LLDP network policy.
    
    Path: system/lldp/network_policy
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "NetworkPolicy",
    "NetworkPolicyPayload",
]