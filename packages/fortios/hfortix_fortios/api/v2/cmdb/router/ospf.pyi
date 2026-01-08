from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class OspfPayload(TypedDict, total=False):
    """
    Type hints for router/ospf payload fields.
    
    Configure OSPF.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.access-list.AccessListEndpoint` (via: distribute-list-in)
        - :class:`~.router.prefix-list.PrefixListEndpoint` (via: distribute-list-in)
        - :class:`~.router.route-map.RouteMapEndpoint` (via: default-information-route-map, distribute-route-map-in)

    **Usage:**
        payload: OspfPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: NotRequired[Literal["cisco", "ibm", "shortcut", "standard"]]  # Area border router type.
    auto_cost_ref_bandwidth: NotRequired[int]  # Reference bandwidth in terms of megabits per second.
    distance_external: NotRequired[int]  # Administrative external distance.
    distance_inter_area: NotRequired[int]  # Administrative inter-area distance.
    distance_intra_area: NotRequired[int]  # Administrative intra-area distance.
    database_overflow: NotRequired[Literal["enable", "disable"]]  # Enable/disable database overflow.
    database_overflow_max_lsas: NotRequired[int]  # Database overflow maximum LSAs.
    database_overflow_time_to_recover: NotRequired[int]  # Database overflow time to recover (sec).
    default_information_originate: NotRequired[Literal["enable", "always", "disable"]]  # Enable/disable generation of default route.
    default_information_metric: NotRequired[int]  # Default information metric.
    default_information_metric_type: NotRequired[Literal["1", "2"]]  # Default information metric type.
    default_information_route_map: NotRequired[str]  # Default information route map.
    default_metric: NotRequired[int]  # Default metric of redistribute routes.
    distance: NotRequired[int]  # Distance of the route.
    lsa_refresh_interval: NotRequired[int]  # The minimal OSPF LSA update time interval
    rfc1583_compatible: NotRequired[Literal["enable", "disable"]]  # Enable/disable RFC1583 compatibility.
    router_id: str  # Router ID.
    spf_timers: NotRequired[str]  # SPF calculation frequency.
    bfd: NotRequired[Literal["enable", "disable"]]  # Bidirectional Forwarding Detection (BFD).
    log_neighbour_changes: NotRequired[Literal["enable", "disable"]]  # Log of OSPF neighbor changes.
    distribute_list_in: NotRequired[str]  # Filter incoming routes.
    distribute_route_map_in: NotRequired[str]  # Filter incoming external routes by route-map.
    restart_mode: NotRequired[Literal["none", "lls", "graceful-restart"]]  # OSPF restart mode (graceful or LLS).
    restart_period: NotRequired[int]  # Graceful restart period.
    restart_on_topology_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable continuing graceful restart upon topology cha
    area: NotRequired[list[dict[str, Any]]]  # OSPF area configuration.
    ospf_interface: NotRequired[list[dict[str, Any]]]  # OSPF interface configuration.
    network: NotRequired[list[dict[str, Any]]]  # OSPF network configuration.
    neighbor: NotRequired[list[dict[str, Any]]]  # OSPF neighbor configuration are used when OSPF runs on non-b
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    summary_address: NotRequired[list[dict[str, Any]]]  # IP address summary configuration.
    distribute_list: NotRequired[list[dict[str, Any]]]  # Distribute list configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.

# Nested classes for table field children

@final
class OspfAreaObject:
    """Typed object for area table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Area entry IP address.
    id: str
    # Enable/disable shortcut option.
    shortcut: Literal["disable", "enable", "default"]
    # Authentication type.
    authentication: Literal["none", "text", "message-digest"]
    # Summary default cost of stub or NSSA area.
    default_cost: int
    # NSSA translator role type.
    nssa_translator_role: Literal["candidate", "never", "always"]
    # Stub summary setting.
    stub_type: Literal["no-summary", "summary"]
    # Area type setting.
    type: Literal["regular", "nssa", "stub"]
    # Redistribute, advertise, or do not originate Type-7 default route into NSSA area
    nssa_default_information_originate: Literal["enable", "always", "disable"]
    # OSPF default metric.
    nssa_default_information_originate_metric: int
    # OSPF metric type for default routes.
    nssa_default_information_originate_metric_type: Literal["1", "2"]
    # Enable/disable redistribute into NSSA area.
    nssa_redistribution: Literal["enable", "disable"]
    # Comment.
    comments: str
    # OSPF area range configuration.
    range: str
    # OSPF virtual link configuration.
    virtual_link: str
    # OSPF area filter-list configuration.
    filter_list: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfOspfinterfaceObject:
    """Typed object for ospf-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface entry name.
    name: str
    # Comment.
    comments: str
    # Configuration interface name.
    interface: str
    # IP address.
    ip: str
    # Enable/disable fast link failover.
    linkdown_fast_failover: Literal["enable", "disable"]
    # Authentication type.
    authentication: Literal["none", "text", "message-digest"]
    # Authentication key.
    authentication_key: str
    # Message-digest key-chain name.
    keychain: str
    # Prefix length.
    prefix_length: int
    # Retransmit interval.
    retransmit_interval: int
    # Transmit delay.
    transmit_delay: int
    # Cost of the interface, value range from 0 to 65535, 0 means auto-cost.
    cost: int
    # Priority.
    priority: int
    # Dead interval.
    dead_interval: int
    # Hello interval.
    hello_interval: int
    # Number of hello packets within dead interval.
    hello_multiplier: int
    # Enable/disable control of flooding out LSAs.
    database_filter_out: Literal["enable", "disable"]
    # MTU for database description packets.
    mtu: int
    # Enable/disable ignore MTU.
    mtu_ignore: Literal["enable", "disable"]
    # Network type.
    network_type: Literal["broadcast", "non-broadcast", "point-to-point", "point-to-multipoint", "point-to-multipoint-non-broadcast"]
    # Bidirectional Forwarding Detection (BFD).
    bfd: Literal["global", "enable", "disable"]
    # Enable/disable status.
    status: Literal["disable", "enable"]
    # Graceful restart neighbor resynchronization timeout.
    resync_timeout: int
    # MD5 key.
    md5_keys: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID.
    id: int
    # Prefix.
    prefix: str
    # Attach the network to area.
    area: str
    # Comment.
    comments: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor entry ID.
    id: int
    # Interface IP address of the neighbor.
    ip: str
    # Poll interval time in seconds.
    poll_interval: int
    # Cost of the interface, value range from 0 to 65535, 0 means auto-cost.
    cost: int
    # Priority.
    priority: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfPassiveinterfaceObject:
    """Typed object for passive-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Passive interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfSummaryaddressObject:
    """Typed object for summary-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Summary address entry ID.
    id: int
    # Prefix.
    prefix: str
    # Tag value.
    tag: int
    # Enable/disable advertise status.
    advertise: Literal["disable", "enable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfDistributelistObject:
    """Typed object for distribute-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list entry ID.
    id: int
    # Access list name.
    access_list: str
    # Protocol type.
    protocol: Literal["connected", "static", "rip"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OspfRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Redistribute name.
    name: str
    # Status.
    status: Literal["enable", "disable"]
    # Redistribute metric setting.
    metric: int
    # Route map name.
    routemap: str
    # Metric type.
    metric_type: Literal["1", "2"]
    # Tag value.
    tag: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class OspfResponse(TypedDict):
    """
    Type hints for router/ospf API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    abr_type: Literal["cisco", "ibm", "shortcut", "standard"]
    auto_cost_ref_bandwidth: int
    distance_external: int
    distance_inter_area: int
    distance_intra_area: int
    database_overflow: Literal["enable", "disable"]
    database_overflow_max_lsas: int
    database_overflow_time_to_recover: int
    default_information_originate: Literal["enable", "always", "disable"]
    default_information_metric: int
    default_information_metric_type: Literal["1", "2"]
    default_information_route_map: str
    default_metric: int
    distance: int
    lsa_refresh_interval: int
    rfc1583_compatible: Literal["enable", "disable"]
    router_id: str
    spf_timers: str
    bfd: Literal["enable", "disable"]
    log_neighbour_changes: Literal["enable", "disable"]
    distribute_list_in: str
    distribute_route_map_in: str
    restart_mode: Literal["none", "lls", "graceful-restart"]
    restart_period: int
    restart_on_topology_change: Literal["enable", "disable"]
    area: list[dict[str, Any]]
    ospf_interface: list[dict[str, Any]]
    network: list[dict[str, Any]]
    neighbor: list[dict[str, Any]]
    passive_interface: list[dict[str, Any]]
    summary_address: list[dict[str, Any]]
    distribute_list: list[dict[str, Any]]
    redistribute: list[dict[str, Any]]


@final
class OspfObject:
    """Typed FortiObject for router/ospf with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Area border router type.
    abr_type: Literal["cisco", "ibm", "shortcut", "standard"]
    # Reference bandwidth in terms of megabits per second.
    auto_cost_ref_bandwidth: int
    # Administrative external distance.
    distance_external: int
    # Administrative inter-area distance.
    distance_inter_area: int
    # Administrative intra-area distance.
    distance_intra_area: int
    # Enable/disable database overflow.
    database_overflow: Literal["enable", "disable"]
    # Database overflow maximum LSAs.
    database_overflow_max_lsas: int
    # Database overflow time to recover (sec).
    database_overflow_time_to_recover: int
    # Enable/disable generation of default route.
    default_information_originate: Literal["enable", "always", "disable"]
    # Default information metric.
    default_information_metric: int
    # Default information metric type.
    default_information_metric_type: Literal["1", "2"]
    # Default information route map.
    default_information_route_map: str
    # Default metric of redistribute routes.
    default_metric: int
    # Distance of the route.
    distance: int
    # The minimal OSPF LSA update time interval
    lsa_refresh_interval: int
    # Enable/disable RFC1583 compatibility.
    rfc1583_compatible: Literal["enable", "disable"]
    # Router ID.
    router_id: str
    # SPF calculation frequency.
    spf_timers: str
    # Bidirectional Forwarding Detection (BFD).
    bfd: Literal["enable", "disable"]
    # Log of OSPF neighbor changes.
    log_neighbour_changes: Literal["enable", "disable"]
    # Filter incoming routes.
    distribute_list_in: str
    # Filter incoming external routes by route-map.
    distribute_route_map_in: str
    # OSPF restart mode (graceful or LLS).
    restart_mode: Literal["none", "lls", "graceful-restart"]
    # Graceful restart period.
    restart_period: int
    # Enable/disable continuing graceful restart upon topology change.
    restart_on_topology_change: Literal["enable", "disable"]
    # OSPF area configuration.
    area: list[OspfAreaObject]  # Table field - list of typed objects
    # OSPF interface configuration.
    ospf_interface: list[OspfOspfinterfaceObject]  # Table field - list of typed objects
    # OSPF network configuration.
    network: list[OspfNetworkObject]  # Table field - list of typed objects
    # OSPF neighbor configuration are used when OSPF runs on non-broadcast media.
    neighbor: list[OspfNeighborObject]  # Table field - list of typed objects
    # Passive interface configuration.
    passive_interface: list[OspfPassiveinterfaceObject]  # Table field - list of typed objects
    # IP address summary configuration.
    summary_address: list[OspfSummaryaddressObject]  # Table field - list of typed objects
    # Distribute list configuration.
    distribute_list: list[OspfDistributelistObject]  # Table field - list of typed objects
    # Redistribute configuration.
    redistribute: list[OspfRedistributeObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OspfPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ospf:
    """
    Configure OSPF.
    
    Path: router/ospf
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfResponse: ...
    
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
    ) -> OspfResponse: ...
    
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
    ) -> OspfResponse: ...
    
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
    ) -> OspfObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OspfObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ospf",
    "OspfPayload",
    "OspfObject",
]