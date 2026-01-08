from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for ips/global_ payload fields.
    
    Configure IPS global parameter.
    
    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    fail_open: NotRequired[Literal["enable", "disable"]]  # Enable to allow traffic if the IPS buffer is full. Default i
    database: NotRequired[Literal["regular", "extended"]]  # Regular or extended IPS database. Regular protects against t
    traffic_submit: NotRequired[Literal["enable", "disable"]]  # Enable/disable submitting attack data found by this FortiGat
    anomaly_mode: NotRequired[Literal["periodical", "continuous"]]  # Global blocking mode for rate-based anomalies.
    session_limit_mode: NotRequired[Literal["accurate", "heuristic"]]  # Method of counting concurrent sessions used by session limit
    socket_size: NotRequired[int]  # IPS socket buffer size. Max and default value depend on avai
    engine_count: NotRequired[int]  # Number of IPS engines running. If set to the default value o
    sync_session_ttl: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of kernel session TTL for IPS sessions.
    deep_app_insp_timeout: NotRequired[int]  # Timeout for Deep application inspection (1 - 2147483647 sec.
    deep_app_insp_db_limit: NotRequired[int]  # Limit on number of entries in deep application inspection da
    exclude_signatures: NotRequired[Literal["none", "ot"]]  # Excluded signatures.
    packet_log_queue_depth: NotRequired[int]  # Packet/pcap log queue depth per IPS engine.
    ngfw_max_scan_range: NotRequired[int]  # NGFW policy-mode app detection threshold.
    av_mem_limit: NotRequired[int]  # Maximum percentage of system memory allowed for use on AV sc
    machine_learning_detection: NotRequired[Literal["enable", "disable"]]  # Enable/disable machine learning detection.
    tls_active_probe: NotRequired[str]  # TLS active probe configuration.


class GlobalObject(FortiObject[GlobalPayload]):
    """Typed FortiObject for ips/global_ with IDE autocomplete support."""
    
    # Enable to allow traffic if the IPS buffer is full. Default is disable and IPS tr
    fail_open: Literal["enable", "disable"]
    # Regular or extended IPS database. Regular protects against the latest common and
    database: Literal["regular", "extended"]
    # Enable/disable submitting attack data found by this FortiGate to FortiGuard.
    traffic_submit: Literal["enable", "disable"]
    # Global blocking mode for rate-based anomalies.
    anomaly_mode: Literal["periodical", "continuous"]
    # Method of counting concurrent sessions used by session limit anomalies. Choose b
    session_limit_mode: Literal["accurate", "heuristic"]
    # IPS socket buffer size. Max and default value depend on available memory. Can be
    socket_size: int
    # Number of IPS engines running. If set to the default value of 0, FortiOS sets th
    engine_count: int
    # Enable/disable use of kernel session TTL for IPS sessions.
    sync_session_ttl: Literal["enable", "disable"]
    # Timeout for Deep application inspection (1 - 2147483647 sec., 0 = use recommende
    deep_app_insp_timeout: int
    # Limit on number of entries in deep application inspection database (1 - 21474836
    deep_app_insp_db_limit: int
    # Excluded signatures.
    exclude_signatures: Literal["none", "ot"]
    # Packet/pcap log queue depth per IPS engine.
    packet_log_queue_depth: int
    # NGFW policy-mode app detection threshold.
    ngfw_max_scan_range: int
    # Maximum percentage of system memory allowed for use on AV scanning (10 - 50, def
    av_mem_limit: int
    # Enable/disable machine learning detection.
    machine_learning_detection: Literal["enable", "disable"]
    # TLS active probe configuration.
    tls_active_probe: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure IPS global parameter.
    
    Path: ips/global_
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
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
        payload_dict: GlobalPayload | None = ...,
        fail_open: Literal["enable", "disable"] | None = ...,
        database: Literal["regular", "extended"] | None = ...,
        traffic_submit: Literal["enable", "disable"] | None = ...,
        anomaly_mode: Literal["periodical", "continuous"] | None = ...,
        session_limit_mode: Literal["accurate", "heuristic"] | None = ...,
        socket_size: int | None = ...,
        engine_count: int | None = ...,
        sync_session_ttl: Literal["enable", "disable"] | None = ...,
        deep_app_insp_timeout: int | None = ...,
        deep_app_insp_db_limit: int | None = ...,
        exclude_signatures: Literal["none", "ot"] | None = ...,
        packet_log_queue_depth: int | None = ...,
        ngfw_max_scan_range: int | None = ...,
        av_mem_limit: int | None = ...,
        machine_learning_detection: Literal["enable", "disable"] | None = ...,
        tls_active_probe: str | None = ...,
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
    "Global",
    "GlobalPayload",
    "GlobalObject",
]