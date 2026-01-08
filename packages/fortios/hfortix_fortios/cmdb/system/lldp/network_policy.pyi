from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class NetworkPolicyPayload(TypedDict, total=False):
    """
    Type hints for system/lldp/network_policy payload fields.
    
    Configure LLDP network policy.
    
    **Usage:**
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


class NetworkPolicyObject(FortiObject[NetworkPolicyPayload]):
    """Typed FortiObject for system/lldp/network_policy with IDE autocomplete support."""
    
    # LLDP network policy name.
    name: str
    # Comment.
    comment: str
    # Voice.
    voice: str
    # Voice signaling.
    voice_signaling: str
    # Guest.
    guest: str
    # Guest Voice Signaling.
    guest_voice_signaling: str
    # Softphone.
    softphone: str
    # Video Conferencing.
    video_conferencing: str
    # Streaming Video.
    streaming_video: str
    # Video Signaling.
    video_signaling: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> NetworkPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class NetworkPolicy:
    """
    Configure LLDP network policy.
    
    Path: system/lldp/network_policy
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> NetworkPolicyObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[NetworkPolicyObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> NetworkPolicyObject | list[NetworkPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NetworkPolicyObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NetworkPolicyObject: ...
    
    @overload
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NetworkPolicyObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "NetworkPolicyObject",
]