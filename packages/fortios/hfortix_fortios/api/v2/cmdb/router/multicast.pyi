from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class MulticastPayload(TypedDict, total=False):
    """
    Type hints for router/multicast payload fields.
    
    Configure router multicast.
    
    **Usage:**
        payload: MulticastPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    route_threshold: NotRequired[int]  # Generate warnings when the number of multicast routes exceed
    route_limit: NotRequired[int]  # Maximum number of multicast routes.
    multicast_routing: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP multicast routing.
    pim_sm_global: NotRequired[str]  # PIM sparse-mode global settings.
    pim_sm_global_vrf: NotRequired[list[dict[str, Any]]]  # per-VRF PIM sparse-mode global settings.
    interface: NotRequired[list[dict[str, Any]]]  # PIM interfaces.

# Nested classes for table field children

@final
class MulticastPimsmglobalvrfObject:
    """Typed object for pim-sm-global-vrf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VRF ID.
    vrf: int
    # Enable/disable allowing this router to become a bootstrap router (BSR).
    bsr_candidate: Literal["enable", "disable"]
    # Interface to advertise as candidate BSR.
    bsr_interface: str
    # BSR priority (0 - 255, default = 0).
    bsr_priority: int
    # BSR hash length (0 - 32, default = 10).
    bsr_hash: int
    # Enable/disable accept BSR quick refresh packets from neighbors.
    bsr_allow_quick_refresh: Literal["enable", "disable"]
    # Enable/disable making candidate RP compatible with old Cisco IOS.
    cisco_crp_prefix: Literal["enable", "disable"]
    # Statically configure RP addresses.
    rp_address: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class MulticastInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    # Minimum TTL of multicast packets that will be forwarded
    ttl_threshold: int
    # PIM operation mode.
    pim_mode: Literal["sparse-mode", "dense-mode"]
    # Enable/disable listening to IGMP but not participating in PIM.
    passive: Literal["enable", "disable"]
    # Enable/disable Protocol Independent Multicast (PIM) Bidirectional Forwarding Det
    bfd: Literal["enable", "disable"]
    # Routers acknowledged as neighbor routers.
    neighbour_filter: str
    # Interval between sending PIM hello messages (0 - 65535 sec, default = 30).
    hello_interval: int
    # Time before old neighbor information expires (0 - 65535 sec, default = 105).
    hello_holdtime: int
    # Exclude GenID from hello packets (compatibility with old Cisco IOS).
    cisco_exclude_genid: Literal["enable", "disable"]
    # DR election priority.
    dr_priority: int
    # Delay flooding packets on this interface (100 - 5000 msec, default = 500).
    propagation_delay: int
    # Interval between sending state-refresh packets (1 - 100 sec, default = 60).
    state_refresh_interval: int
    # Enable/disable compete to become RP in elections.
    rp_candidate: Literal["enable", "disable"]
    # Multicast groups managed by this RP.
    rp_candidate_group: str
    # Router's priority as RP.
    rp_candidate_priority: int
    # RP candidate advertisement interval (1 - 16383 sec, default = 60).
    rp_candidate_interval: int
    # Acceptable source for multicast group.
    multicast_flow: str
    # Statically set multicast groups to forward out.
    static_group: str
    # Enable/disable fail back for RPF neighbor query.
    rpf_nbr_fail_back: Literal["enable", "disable"]
    # Filter for fail back RPF neighbors.
    rpf_nbr_fail_back_filter: str
    # Join multicast groups.
    join_group: str
    # IGMP configuration options.
    igmp: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class MulticastResponse(TypedDict):
    """
    Type hints for router/multicast API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    route_threshold: int
    route_limit: int
    multicast_routing: Literal["enable", "disable"]
    pim_sm_global: str
    pim_sm_global_vrf: list[dict[str, Any]]
    interface: list[dict[str, Any]]


@final
class MulticastObject:
    """Typed FortiObject for router/multicast with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Generate warnings when the number of multicast routes exceeds this number, must
    route_threshold: int
    # Maximum number of multicast routes.
    route_limit: int
    # Enable/disable IP multicast routing.
    multicast_routing: Literal["enable", "disable"]
    # PIM sparse-mode global settings.
    pim_sm_global: str
    # per-VRF PIM sparse-mode global settings.
    pim_sm_global_vrf: list[MulticastPimsmglobalvrfObject]  # Table field - list of typed objects
    # PIM interfaces.
    interface: list[MulticastInterfaceObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> MulticastPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Multicast:
    """
    Configure router multicast.
    
    Path: router/multicast
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastResponse: ...
    
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
    ) -> MulticastResponse: ...
    
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
    ) -> MulticastResponse: ...
    
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
    ) -> MulticastObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MulticastObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Multicast",
    "MulticastPayload",
    "MulticastObject",
]