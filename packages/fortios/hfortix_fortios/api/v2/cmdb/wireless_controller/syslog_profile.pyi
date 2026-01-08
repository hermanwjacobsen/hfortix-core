from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SyslogProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/syslog_profile payload fields.
    
    Configure Wireless Termination Points (WTP) system log server profile.
    
    **Usage:**
        payload: SyslogProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WTP system log server profile name.
    comment: NotRequired[str]  # Comment.
    server_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiAP units to send log messages to a syslo
    server: NotRequired[str]  # Syslog server CN domain name or IP address.
    server_port: NotRequired[int]  # Port number of syslog server that FortiAP units send log mes
    server_type: NotRequired[Literal["standard", "fortianalyzer"]]  # Configure syslog server type (default = standard).
    log_level: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]]  # Lowest level of log messages that FortiAP units send to this

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SyslogProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/syslog_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    server_status: Literal["enable", "disable"]
    server: str
    server_port: int
    server_type: Literal["standard", "fortianalyzer"]
    log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]


@final
class SyslogProfileObject:
    """Typed FortiObject for wireless_controller/syslog_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WTP system log server profile name.
    name: str
    # Comment.
    comment: str
    # Enable/disable FortiAP units to send log messages to a syslog server
    server_status: Literal["enable", "disable"]
    # Syslog server CN domain name or IP address.
    server: str
    # Port number of syslog server that FortiAP units send log messages to
    server_port: int
    # Configure syslog server type (default = standard).
    server_type: Literal["standard", "fortianalyzer"]
    # Lowest level of log messages that FortiAP units send to this server
    log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SyslogProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SyslogProfile:
    """
    Configure Wireless Termination Points (WTP) system log server profile.
    
    Path: wireless_controller/syslog_profile
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SyslogProfileObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SyslogProfileObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[SyslogProfileObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> SyslogProfileResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> SyslogProfileResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[SyslogProfileResponse]: ...
    
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
    ) -> SyslogProfileObject | list[SyslogProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SyslogProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SyslogProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
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
    ) -> SyslogProfileObject: ...
    
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
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
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
    "SyslogProfile",
    "SyslogProfilePayload",
    "SyslogProfileObject",
]