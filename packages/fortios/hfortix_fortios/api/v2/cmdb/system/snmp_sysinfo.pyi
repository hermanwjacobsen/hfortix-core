from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnmpSysinfoPayload(TypedDict, total=False):
    """
    Type hints for system/snmp_sysinfo payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SnmpSysinfoPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP.
    engine_id_type: NotRequired[Literal["text", "hex", "mac"]]  # Local SNMP engineID type (text/hex/mac).
    engine_id: NotRequired[str]  # Local SNMP engineID string (maximum 27 characters).
    description: NotRequired[str]  # System description.
    contact_info: NotRequired[str]  # Contact information.
    location: NotRequired[str]  # System location.
    trap_high_cpu_threshold: NotRequired[int]  # CPU usage when trap is sent.
    trap_low_memory_threshold: NotRequired[int]  # Memory usage when trap is sent.
    trap_log_full_threshold: NotRequired[int]  # Log disk usage when trap is sent.
    trap_free_memory_threshold: NotRequired[int]  # Free memory usage when trap is sent.
    trap_freeable_memory_threshold: NotRequired[int]  # Freeable memory usage when trap is sent.
    append_index: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowance of appending vdom or interface inde
    non_mgmt_vdom_query: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowance of SNMPv3 query from non-management


class SnmpSysinfo:
    """
    SNMP system info configuration.
    
    Path: system/snmp_sysinfo
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
        payload_dict: SnmpSysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SnmpSysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SnmpSysinfoPayload | None = ...,
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