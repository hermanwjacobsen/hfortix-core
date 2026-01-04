from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Fortianalyzer2SettingPayload(TypedDict, total=False):
    """
    Type hints for log/fortianalyzer2_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Fortianalyzer2SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
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
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    conn_timeout: NotRequired[int]  # FortiAnalyzer connection time-out in seconds (for status and
    monitor_keepalive_period: NotRequired[int]  # Time between OFTP keepalives in seconds (for status and log 
    monitor_failure_retry_period: NotRequired[int]  # Time between FortiAnalyzer connection retries in seconds (fo
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


class Fortianalyzer2Setting:
    """
    Global FortiAnalyzer settings.
    
    Path: log/fortianalyzer2_setting
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
        payload_dict: Fortianalyzer2SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Fortianalyzer2SettingPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ips_archive: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        alt_server: str | None = ...,
        fallback_to_primary: Literal["enable", "disable"] | None = ...,
        certificate_verification: Literal["enable", "disable"] | None = ...,
        serial: list[dict[str, Any]] | None = ...,
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
        payload_dict: Fortianalyzer2SettingPayload | None = ...,
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