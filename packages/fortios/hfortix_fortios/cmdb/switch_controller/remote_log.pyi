from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class RemoteLogPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/remote_log payload fields.
    
    Configure logging by FortiSwitch device to a remote syslog server.
    
    **Usage:**
        payload: RemoteLogPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Remote log name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging by FortiSwitch device to a remote sys
    server: str  # IPv4 address of the remote syslog server.
    port: NotRequired[int]  # Remote syslog server listening port.
    severity: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Severity of logs to be transferred to remote log server.
    csv: NotRequired[Literal["enable", "disable"]]  # Enable/disable comma-separated value (CSV) strings.
    facility: NotRequired[Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]]  # Facility to log to remote syslog server.


class RemoteLogObject(FortiObject[RemoteLogPayload]):
    """Typed FortiObject for switch_controller/remote_log with IDE autocomplete support."""
    
    # Remote log name.
    name: str
    # Enable/disable logging by FortiSwitch device to a remote syslog server.
    status: Literal["enable", "disable"]
    # IPv4 address of the remote syslog server.
    server: str
    # Remote syslog server listening port.
    port: int
    # Severity of logs to be transferred to remote log server.
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Enable/disable comma-separated value (CSV) strings.
    csv: Literal["enable", "disable"]
    # Facility to log to remote syslog server.
    facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RemoteLogPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class RemoteLog:
    """
    Configure logging by FortiSwitch device to a remote syslog server.
    
    Path: switch_controller/remote_log
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
    ) -> RemoteLogObject: ...
    
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
    ) -> list[RemoteLogObject]: ...
    
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
    ) -> RemoteLogObject | list[RemoteLogObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RemoteLogObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RemoteLogObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
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
    ) -> RemoteLogObject: ...
    
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
        payload_dict: RemoteLogPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        csv: Literal["enable", "disable"] | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
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
    "RemoteLog",
    "RemoteLogPayload",
    "RemoteLogObject",
]