from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class OverrideSettingPayload(TypedDict, total=False):
    """
    Type hints for log/syslogd2/override_setting payload fields.
    
    Override settings for remote syslog server.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)

    **Usage:**
        payload: OverrideSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable remote syslog logging.
    server: str  # Address of remote syslog server.
    mode: NotRequired[Literal["udp", "legacy-reliable", "reliable"]]  # Remote syslog logging over UDP/Reliable TCP.
    use_management_vdom: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of management VDOM as source VDOM for log
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


class OverrideSettingObject(FortiObject[OverrideSettingPayload]):
    """Typed FortiObject for log/syslogd2/override_setting with IDE autocomplete support."""
    
    # Enable/disable remote syslog logging.
    status: Literal["enable", "disable"]
    # Address of remote syslog server.
    server: str
    # Remote syslog logging over UDP/Reliable TCP.
    mode: Literal["udp", "legacy-reliable", "reliable"]
    # Enable/disable use of management VDOM as source VDOM for logs sent to syslog ser
    use_management_vdom: Literal["enable", "disable"]
    # Server listen port.
    port: int
    # Remote syslog facility.
    facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]
    # Source interface of syslog.
    source_ip_interface: str
    # Source IP address of syslog.
    source_ip: str
    # Log format.
    format: Literal["default", "csv", "cef", "rfc5424", "json"]
    # Set log transmission priority.
    priority: Literal["default", "low"]
    # Syslog maximum log rate in MBps (0 = unlimited).
    max_log_rate: int
    # Enable/disable reliable syslogging with TLS encryption.
    enc_algorithm: Literal["high-medium", "high", "low", "disable"]
    # Minimum supported protocol version for SSL/TLS connections (default is to follow
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Certificate used to communicate with Syslog server.
    certificate: str
    # Custom field name for CEF format logging.
    custom_field_name: list[str]  # Auto-flattened from member_table
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OverrideSettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class OverrideSetting:
    """
    Override settings for remote syslog server.
    
    Path: log/syslogd2/override_setting
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
    ) -> OverrideSettingObject: ...
    
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
    ) -> OverrideSettingObject: ...
    
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
    ) -> OverrideSettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OverrideSettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
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
        custom_field_name: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OverrideSettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OverrideSettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
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
        custom_field_name: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: OverrideSettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
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
        custom_field_name: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: OverrideSettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
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
        custom_field_name: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
        payload_dict: OverrideSettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        mode: Literal["udp", "legacy-reliable", "reliable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
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
        custom_field_name: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "OverrideSetting",
    "OverrideSettingPayload",
    "OverrideSettingObject",
]