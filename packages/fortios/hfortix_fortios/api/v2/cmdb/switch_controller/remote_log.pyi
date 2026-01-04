from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class RemoteLogPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/remote_log payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class RemoteLog:
    """
    Configure logging by FortiSwitch device to a remote syslog server.
    
    Path: switch_controller/remote_log
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: RemoteLogPayload | None = ...,
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