from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AffinityPacketRedistributionPayload(TypedDict, total=False):
    """
    Type hints for system/affinity_packet_redistribution payload fields.
    
    Configure packet redistribution.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: AffinityPacketRedistributionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID of the packet redistribution setting.
    interface: str  # Physical interface name on which to perform packet redistrib
    rxqid: int  # ID of the receive queue
    round_robin: Literal["enable", "disable"]  # Enable/disable round-robin redistribution to multiple CPUs.
    affinity_cpumask: NotRequired[str]  # Hexadecimal cpumask, empty value means all CPUs.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class AffinityPacketRedistributionResponse(TypedDict):
    """
    Type hints for system/affinity_packet_redistribution API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int
    interface: str
    rxqid: int
    round_robin: Literal["enable", "disable"]
    affinity_cpumask: str


@final
class AffinityPacketRedistributionObject:
    """Typed FortiObject for system/affinity_packet_redistribution with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ID of the packet redistribution setting.
    id: int
    # Physical interface name on which to perform packet redistribution.
    interface: str
    # ID of the receive queue (when the interface has multiple queues) on which to per
    rxqid: int
    # Enable/disable round-robin redistribution to multiple CPUs.
    round_robin: Literal["enable", "disable"]
    # Hexadecimal cpumask, empty value means all CPUs.
    affinity_cpumask: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AffinityPacketRedistributionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AffinityPacketRedistribution:
    """
    Configure packet redistribution.
    
    Path: system/affinity_packet_redistribution
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        id: int,
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
    ) -> AffinityPacketRedistributionObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> AffinityPacketRedistributionObject: ...
    
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
    ) -> list[AffinityPacketRedistributionObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
    ) -> AffinityPacketRedistributionResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> AffinityPacketRedistributionResponse: ...
    
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
    ) -> list[AffinityPacketRedistributionResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        id: int | None = ...,
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
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        id: int | None = ...,
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
    ) -> AffinityPacketRedistributionObject | list[AffinityPacketRedistributionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AffinityPacketRedistributionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AffinityPacketRedistributionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AffinityPacketRedistributionObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AffinityPacketRedistributionPayload | None = ...,
        id: int | None = ...,
        interface: str | None = ...,
        rxqid: int | None = ...,
        round_robin: Literal["enable", "disable"] | None = ...,
        affinity_cpumask: str | None = ...,
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
    "AffinityPacketRedistribution",
    "AffinityPacketRedistributionPayload",
    "AffinityPacketRedistributionObject",
]