from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SystemPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/system payload fields.
    
    Configure system-wide switch controller settings.
    
    **Usage:**
        payload: SystemPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    parallel_process_override: NotRequired[Literal["disable", "enable"]]  # Enable/disable parallel process override.
    parallel_process: NotRequired[int]  # Maximum number of parallel processes.
    data_sync_interval: NotRequired[int]  # Time interval between collection of switch data
    iot_weight_threshold: NotRequired[int]  # MAC entry's confidence value. Value is re-queried when below
    iot_scan_interval: NotRequired[int]  # IoT scan interval
    iot_holdoff: NotRequired[int]  # MAC entry's creation time. Time must be greater than this va
    iot_mac_idle: NotRequired[int]  # MAC entry's idle time. MAC entry is removed after this value
    nac_periodic_interval: NotRequired[int]  # Periodic time interval to run NAC engine
    dynamic_periodic_interval: NotRequired[int]  # Periodic time interval to run Dynamic port policy engine
    tunnel_mode: NotRequired[Literal["compatible", "moderate", "strict"]]  # Compatible/strict tunnel mode.
    caputp_echo_interval: NotRequired[int]  # Echo interval for the caputp echo requests from swtp.
    caputp_max_retransmit: NotRequired[int]  # Maximum retransmission count for the caputp tunnel packets.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SystemResponse(TypedDict):
    """
    Type hints for switch_controller/system API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    parallel_process_override: Literal["disable", "enable"]
    parallel_process: int
    data_sync_interval: int
    iot_weight_threshold: int
    iot_scan_interval: int
    iot_holdoff: int
    iot_mac_idle: int
    nac_periodic_interval: int
    dynamic_periodic_interval: int
    tunnel_mode: Literal["compatible", "moderate", "strict"]
    caputp_echo_interval: int
    caputp_max_retransmit: int


@final
class SystemObject:
    """Typed FortiObject for switch_controller/system with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable parallel process override.
    parallel_process_override: Literal["disable", "enable"]
    # Maximum number of parallel processes.
    parallel_process: int
    # Time interval between collection of switch data
    data_sync_interval: int
    # MAC entry's confidence value. Value is re-queried when below this value
    iot_weight_threshold: int
    # IoT scan interval (2 - 10080 mins, default = 60 mins, 0 = disable).
    iot_scan_interval: int
    # MAC entry's creation time. Time must be greater than this value for an entry to
    iot_holdoff: int
    # MAC entry's idle time. MAC entry is removed after this value
    iot_mac_idle: int
    # Periodic time interval to run NAC engine (5 - 180 sec, default = 60).
    nac_periodic_interval: int
    # Periodic time interval to run Dynamic port policy engine
    dynamic_periodic_interval: int
    # Compatible/strict tunnel mode.
    tunnel_mode: Literal["compatible", "moderate", "strict"]
    # Echo interval for the caputp echo requests from swtp.
    caputp_echo_interval: int
    # Maximum retransmission count for the caputp tunnel packets.
    caputp_max_retransmit: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SystemPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class System:
    """
    Configure system-wide switch controller settings.
    
    Path: switch_controller/system
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemResponse: ...
    
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
    ) -> SystemResponse: ...
    
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
    ) -> SystemResponse: ...
    
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
    ) -> SystemObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SystemObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
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
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
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
    "System",
    "SystemPayload",
    "SystemObject",
]