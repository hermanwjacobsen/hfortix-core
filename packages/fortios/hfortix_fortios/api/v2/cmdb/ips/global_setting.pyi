from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GlobalSettingPayload(TypedDict, total=False):
    """
    Type hints for ips/global_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GlobalSettingPayload = {
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


class GlobalSetting:
    """
    Configure IPS global parameter.
    
    Path: ips/global_setting
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
        payload_dict: GlobalSettingPayload | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GlobalSettingPayload | None = ...,
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
        payload_dict: GlobalSettingPayload | None = ...,
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