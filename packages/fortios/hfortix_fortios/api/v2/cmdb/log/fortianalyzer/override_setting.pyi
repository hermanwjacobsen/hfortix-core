from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class OverrideSettingPayload(TypedDict, total=False):
    """
    Type hints for log/fortianalyzer/override_setting payload fields.
    
    Override FortiAnalyzer settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: server-cert-ca)
        - :class:`~.certificate.local.LocalEndpoint` (via: certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: server-cert-ca)

    **Usage:**
        payload: OverrideSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    use_management_vdom: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of management VDOM IP address as source I
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging to FortiAnalyzer.
    ips_archive: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS packet archive logging.
    server: str  # The remote FortiAnalyzer.
    alt_server: NotRequired[str]  # Alternate FortiAnalyzer.
    fallback_to_primary: NotRequired[Literal["enable", "disable"]]  # Enable/disable this FortiGate unit to fallback to the primar
    certificate_verification: NotRequired[Literal["enable", "disable"]]  # Enable/disable identity verification of FortiAnalyzer by use
    serial: NotRequired[list[dict[str, Any]]]  # Serial numbers of the FortiAnalyzer.
    server_cert_ca: NotRequired[str]  # Mandatory CA on FortiGate in certificate chain of server.
    preshared_key: NotRequired[str]  # Preshared-key used for auto-authorization on FortiAnalyzer.
    access_config: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiAnalyzer access to configuration and dat
    hmac_algorithm: NotRequired[Literal["sha256"]]  # OFTP login hash algorithm.
    enc_algorithm: NotRequired[Literal["high-medium", "high", "low"]]  # Configure the level of SSL protection for secure communicati
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections
    conn_timeout: NotRequired[int]  # FortiAnalyzer connection time-out in seconds
    monitor_keepalive_period: NotRequired[int]  # Time between OFTP keepalives in seconds
    monitor_failure_retry_period: NotRequired[int]  # Time between FortiAnalyzer connection retries in seconds
    certificate: NotRequired[str]  # Certificate used to communicate with FortiAnalyzer.
    source_ip: NotRequired[str]  # Source IPv4 or IPv6 address used to communicate with FortiAn
    upload_option: NotRequired[Literal["store-and-upload", "realtime", "1-minute", "5-minute"]]  # Enable/disable logging to hard disk and then uploading to Fo
    upload_interval: NotRequired[Literal["daily", "weekly", "monthly"]]  # Frequency to upload log files to FortiAnalyzer.
    upload_day: NotRequired[str]  # Day of week (month) to upload logs.
    upload_time: NotRequired[str]  # Time to upload logs (hh:mm).
    reliable: NotRequired[Literal["enable", "disable"]]  # Enable/disable reliable logging to FortiAnalyzer.
    priority: NotRequired[Literal["default", "low"]]  # Set log transmission priority.
    max_log_rate: NotRequired[int]  # FortiAnalyzer maximum log rate in MBps (0 = unlimited).
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.

# Nested classes for table field children

@final
class OverrideSettingSerialObject:
    """Typed object for serial table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Serial Number.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class OverrideSettingResponse(TypedDict):
    """
    Type hints for log/fortianalyzer/override_setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    use_management_vdom: Literal["enable", "disable"]
    status: Literal["enable", "disable"]
    ips_archive: Literal["enable", "disable"]
    server: str
    alt_server: str
    fallback_to_primary: Literal["enable", "disable"]
    certificate_verification: Literal["enable", "disable"]
    serial: list[dict[str, Any]]
    server_cert_ca: str
    preshared_key: str
    access_config: Literal["enable", "disable"]
    hmac_algorithm: Literal["sha256"]
    enc_algorithm: Literal["high-medium", "high", "low"]
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    conn_timeout: int
    monitor_keepalive_period: int
    monitor_failure_retry_period: int
    certificate: str
    source_ip: str
    upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"]
    upload_interval: Literal["daily", "weekly", "monthly"]
    upload_day: str
    upload_time: str
    reliable: Literal["enable", "disable"]
    priority: Literal["default", "low"]
    max_log_rate: int
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int


@final
class OverrideSettingObject:
    """Typed FortiObject for log/fortianalyzer/override_setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable use of management VDOM IP address as source IP for logs sent to F
    use_management_vdom: Literal["enable", "disable"]
    # Enable/disable logging to FortiAnalyzer.
    status: Literal["enable", "disable"]
    # Enable/disable IPS packet archive logging.
    ips_archive: Literal["enable", "disable"]
    # The remote FortiAnalyzer.
    server: str
    # Alternate FortiAnalyzer.
    alt_server: str
    # Enable/disable this FortiGate unit to fallback to the primary FortiAnalyzer when
    fallback_to_primary: Literal["enable", "disable"]
    # Enable/disable identity verification of FortiAnalyzer by use of certificate.
    certificate_verification: Literal["enable", "disable"]
    # Serial numbers of the FortiAnalyzer.
    serial: list[OverrideSettingSerialObject]  # Table field - list of typed objects
    # Mandatory CA on FortiGate in certificate chain of server.
    server_cert_ca: str
    # Preshared-key used for auto-authorization on FortiAnalyzer.
    preshared_key: str
    # Enable/disable FortiAnalyzer access to configuration and data.
    access_config: Literal["enable", "disable"]
    # OFTP login hash algorithm.
    hmac_algorithm: Literal["sha256"]
    # Configure the level of SSL protection for secure communication with FortiAnalyze
    enc_algorithm: Literal["high-medium", "high", "low"]
    # Minimum supported protocol version for SSL/TLS connections
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # FortiAnalyzer connection time-out in seconds (for status and log buffer).
    conn_timeout: int
    # Time between OFTP keepalives in seconds (for status and log buffer).
    monitor_keepalive_period: int
    # Time between FortiAnalyzer connection retries in seconds
    monitor_failure_retry_period: int
    # Certificate used to communicate with FortiAnalyzer.
    certificate: str
    # Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.
    source_ip: str
    # Enable/disable logging to hard disk and then uploading to FortiAnalyzer.
    upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"]
    # Frequency to upload log files to FortiAnalyzer.
    upload_interval: Literal["daily", "weekly", "monthly"]
    # Day of week (month) to upload logs.
    upload_day: str
    # Time to upload logs (hh:mm).
    upload_time: str
    # Enable/disable reliable logging to FortiAnalyzer.
    reliable: Literal["enable", "disable"]
    # Set log transmission priority.
    priority: Literal["default", "low"]
    # FortiAnalyzer maximum log rate in MBps (0 = unlimited).
    max_log_rate: int
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OverrideSettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class OverrideSetting:
    """
    Override FortiAnalyzer settings.
    
    Path: log/fortianalyzer/override_setting
    Category: cmdb
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
    ) -> OverrideSettingObject: ...
    
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
    ) -> OverrideSettingObject: ...
    
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
    ) -> OverrideSettingResponse: ...
    
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
    ) -> OverrideSettingResponse: ...
    
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
    ) -> OverrideSettingResponse: ...
    
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
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
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
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
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
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
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
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
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
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_ca: str | None = ...,
        preshared_key: str | None = ...,
        access_config: Literal["enable", "disable"] | None = ...,
        hmac_algorithm: Literal["sha256"] | None = ...,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        conn_timeout: int | None = ...,
        monitor_keepalive_period: int | None = ...,
        monitor_failure_retry_period: int | None = ...,
        certificate: str | None = ...,
        source_ip: str | None = ...,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = ...,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = ...,
        upload_day: str | None = ...,
        upload_time: str | None = ...,
        reliable: Literal["enable", "disable"] | None = ...,
        priority: Literal["default", "low"] | None = ...,
        max_log_rate: int | None = ...,
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