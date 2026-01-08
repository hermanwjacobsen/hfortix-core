from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class NetflowPayload(TypedDict, total=False):
    """
    Type hints for system/netflow payload fields.
    
    Configure NetFlow.
    
    **Usage:**
        payload: NetflowPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    active_flow_timeout: NotRequired[int]  # Timeout to report active flows
    inactive_flow_timeout: NotRequired[int]  # Timeout for periodic report of finished flows
    template_tx_timeout: NotRequired[int]  # Timeout for periodic template flowset transmission
    template_tx_counter: NotRequired[int]  # Counter of flowset records before resending a template flows
    session_cache_size: NotRequired[Literal["min", "default", "max"]]  # Maximum RAM usage allowed for Netflow session cache.
    exclusion_filters: NotRequired[list[dict[str, Any]]]  # Exclusion filters
    collectors: NotRequired[list[dict[str, Any]]]  # Netflow collectors.

# Nested classes for table field children

@final
class NetflowExclusionfiltersObject:
    """Typed object for exclusion-filters table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Filter ID.
    id: int
    # Session source address.
    source_ip: str
    # Session destination address.
    destination_ip: str
    # Session source port number or range.
    source_port: str
    # Session destination port number or range.
    destination_port: str
    # Session IP protocol (0 - 255, default = 255, meaning any).
    protocol: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class NetflowCollectorsObject:
    """Typed object for collectors table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Collector IP.
    collector_ip: str
    # NetFlow collector port number.
    collector_port: int
    # Source IP address for communication with the NetFlow agent.
    source_ip: str
    # Name of the interface used to determine the source IP for exporting packets.
    source_ip_interface: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class NetflowResponse(TypedDict):
    """
    Type hints for system/netflow API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    active_flow_timeout: int
    inactive_flow_timeout: int
    template_tx_timeout: int
    template_tx_counter: int
    session_cache_size: Literal["min", "default", "max"]
    exclusion_filters: list[dict[str, Any]]
    collectors: list[dict[str, Any]]


@final
class NetflowObject:
    """Typed FortiObject for system/netflow with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Timeout to report active flows (60 - 3600 sec, default = 1800).
    active_flow_timeout: int
    # Timeout for periodic report of finished flows (10 - 600 sec, default = 15).
    inactive_flow_timeout: int
    # Timeout for periodic template flowset transmission
    template_tx_timeout: int
    # Counter of flowset records before resending a template flowset record.
    template_tx_counter: int
    # Maximum RAM usage allowed for Netflow session cache.
    session_cache_size: Literal["min", "default", "max"]
    # Exclusion filters
    exclusion_filters: list[NetflowExclusionfiltersObject]  # Table field - list of typed objects
    # Netflow collectors.
    collectors: list[NetflowCollectorsObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> NetflowPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Netflow:
    """
    Configure NetFlow.
    
    Path: system/netflow
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowObject: ...
    
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
    ) -> NetflowResponse: ...
    
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
    ) -> NetflowResponse: ...
    
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
    ) -> NetflowResponse: ...
    
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
    ) -> NetflowObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NetflowObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: NetflowPayload | None = ...,
        active_flow_timeout: int | None = ...,
        inactive_flow_timeout: int | None = ...,
        template_tx_timeout: int | None = ...,
        template_tx_counter: int | None = ...,
        session_cache_size: Literal["min", "default", "max"] | None = ...,
        exclusion_filters: str | list[str] | list[dict[str, Any]] | None = ...,
        collectors: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Netflow",
    "NetflowPayload",
    "NetflowObject",
]