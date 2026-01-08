from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ThreatWeightPayload(TypedDict, total=False):
    """
    Type hints for log/threat_weight payload fields.
    
    Configure threat weight settings.
    
    **Usage:**
        payload: ThreatWeightPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the threat weight feature.
    level: NotRequired[str]  # Score mapping for threat weight levels.
    blocked_connection: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for blocked connections.
    failed_connection: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for failed connections.
    url_block_detected: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for URL blocking.
    botnet_connection_detected: NotRequired[Literal["disable", "low", "medium", "high", "critical"]]  # Threat weight score for detected botnet connections.
    malware: NotRequired[str]  # Anti-virus malware threat weight settings.
    ips: NotRequired[str]  # IPS threat weight settings.
    web: NotRequired[list[dict[str, Any]]]  # Web filtering threat weight settings.
    geolocation: NotRequired[list[dict[str, Any]]]  # Geolocation-based threat weight settings.
    application: NotRequired[list[dict[str, Any]]]  # Application-control threat weight settings.


class ThreatWeightObject(FortiObject[ThreatWeightPayload]):
    """Typed FortiObject for log/threat_weight with IDE autocomplete support."""
    
    # Enable/disable the threat weight feature.
    status: Literal["enable", "disable"]
    # Score mapping for threat weight levels.
    level: str
    # Threat weight score for blocked connections.
    blocked_connection: Literal["disable", "low", "medium", "high", "critical"]
    # Threat weight score for failed connections.
    failed_connection: Literal["disable", "low", "medium", "high", "critical"]
    # Threat weight score for URL blocking.
    url_block_detected: Literal["disable", "low", "medium", "high", "critical"]
    # Threat weight score for detected botnet connections.
    botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"]
    # Anti-virus malware threat weight settings.
    malware: str
    # IPS threat weight settings.
    ips: str
    # Web filtering threat weight settings.
    web: list[str]  # Auto-flattened from member_table
    # Geolocation-based threat weight settings.
    geolocation: list[str]  # Auto-flattened from member_table
    # Application-control threat weight settings.
    application: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ThreatWeightPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ThreatWeight:
    """
    Configure threat weight settings.
    
    Path: log/threat_weight
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ThreatWeightObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ThreatWeight",
    "ThreatWeightPayload",
    "ThreatWeightObject",
]