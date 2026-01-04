from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Syslogd4SettingPayload(TypedDict, total=False):
    """
    Type hints for log/syslogd4_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Syslogd4SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable remote syslog logging.
    server: str  # Address of remote syslog server.
    mode: NotRequired[Literal["udp", "legacy-reliable", "reliable"]]  # Remote syslog logging over UDP/Reliable TCP.
    port: NotRequired[int]  # Server listen port.
    facility: NotRequired[Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]]  # Remote syslog facility.
    source_ip_interface: NotRequired[str]  # Source interface of syslog.
    source_ip: NotRequired[str]  # Source IP address of syslog.
    format: NotRequired[Literal["default", "csv", "cef", "rfc5424", "json"]]  # Log format.
    priority: NotRequired[Literal["default", "low"]]  # Set log transmission priority.
    max_log_rate: NotRequired[int]  # Syslog maximum log rate in MBps (0 = unlimited).
    enc_algorithm: NotRequired[Literal["high-medium", "high", "low", "disable"]]  # Enable/disable reliable syslogging with TLS encryption.
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    certificate: NotRequired[str]  # Certificate used to communicate with Syslog server.
    custom_field_name: NotRequired[list[dict[str, Any]]]  # Custom field name for CEF format logging.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class Syslogd4Setting:
    """
    Global settings for remote syslog server.
    
    Path: log/syslogd4_setting
    Category: cmdb
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
        payload_dict: Syslogd4SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        port: int | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        source_ip_interface: str | None = ...,
        source_ip: str | None = ...,
        format: Literal["default", "csv", "cef", "rfc5424", "json"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        certificate: str | None = ...,
        custom_field_name: list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Syslogd4SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        port: int | None = ...,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = ...,
        source_ip_interface: str | None = ...,
        source_ip: str | None = ...,
        format: Literal["default", "csv", "cef", "rfc5424", "json"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        certificate: str | None = ...,
        custom_field_name: list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
        payload_dict: Syslogd4SettingPayload | None = ...,
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