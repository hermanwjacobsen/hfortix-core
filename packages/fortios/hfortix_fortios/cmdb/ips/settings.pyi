from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SettingsPayload(TypedDict, total=False):
    """
    Type hints for ips/settings payload fields.
    
    Configure IPS VDOM parameter.
    
    **Usage:**
        payload: SettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    packet_log_history: NotRequired[int]  # Number of packets to capture before and including the one in
    packet_log_post_attack: NotRequired[int]  # Number of packets to log after the IPS signature is detected
    packet_log_memory: NotRequired[int]  # Maximum memory can be used by packet log (64 - 8192 kB).
    ips_packet_quota: NotRequired[int]  # Maximum amount of disk space in MB for logged packets when l
    proxy_inline_ips: NotRequired[Literal["disable", "enable"]]  # Enable/disable proxy-mode policy inline IPS support.
    ha_session_pickup: NotRequired[Literal["connectivity", "security"]]  # IPS HA failover session pickup preference.


class SettingsObject(FortiObject[SettingsPayload]):
    """Typed FortiObject for ips/settings with IDE autocomplete support."""
    
    # Number of packets to capture before and including the one in which the IPS signa
    packet_log_history: int
    # Number of packets to log after the IPS signature is detected (0 - 255).
    packet_log_post_attack: int
    # Maximum memory can be used by packet log (64 - 8192 kB).
    packet_log_memory: int
    # Maximum amount of disk space in MB for logged packets when logging to disk. Rang
    ips_packet_quota: int
    # Enable/disable proxy-mode policy inline IPS support.
    proxy_inline_ips: Literal["disable", "enable"]
    # IPS HA failover session pickup preference.
    ha_session_pickup: Literal["connectivity", "security"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Settings:
    """
    Configure IPS VDOM parameter.
    
    Path: ips/settings
    Category: cmdb
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> SettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        packet_log_history: int | None = ...,
        packet_log_post_attack: int | None = ...,
        packet_log_memory: int | None = ...,
        ips_packet_quota: int | None = ...,
        proxy_inline_ips: Literal["disable", "enable"] | None = ...,
        ha_session_pickup: Literal["connectivity", "security"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        packet_log_history: int | None = ...,
        packet_log_post_attack: int | None = ...,
        packet_log_memory: int | None = ...,
        ips_packet_quota: int | None = ...,
        proxy_inline_ips: Literal["disable", "enable"] | None = ...,
        ha_session_pickup: Literal["connectivity", "security"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        packet_log_history: int | None = ...,
        packet_log_post_attack: int | None = ...,
        packet_log_memory: int | None = ...,
        ips_packet_quota: int | None = ...,
        proxy_inline_ips: Literal["disable", "enable"] | None = ...,
        ha_session_pickup: Literal["connectivity", "security"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        packet_log_history: int | None = ...,
        packet_log_post_attack: int | None = ...,
        packet_log_memory: int | None = ...,
        ips_packet_quota: int | None = ...,
        proxy_inline_ips: Literal["disable", "enable"] | None = ...,
        ha_session_pickup: Literal["connectivity", "security"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingsPayload | None = ...,
        packet_log_history: int | None = ...,
        packet_log_post_attack: int | None = ...,
        packet_log_memory: int | None = ...,
        ips_packet_quota: int | None = ...,
        proxy_inline_ips: Literal["disable", "enable"] | None = ...,
        ha_session_pickup: Literal["connectivity", "security"] | None = ...,
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
    "Settings",
    "SettingsPayload",
    "SettingsObject",
]