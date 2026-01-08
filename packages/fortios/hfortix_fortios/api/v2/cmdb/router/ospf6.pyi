from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class Ospf6Payload(TypedDict, total=False):
    """
    Type hints for router/ospf6 payload fields.
    
    Configure IPv6 OSPF.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.route-map.RouteMapEndpoint` (via: default-information-route-map)

    **Usage:**
        payload: Ospf6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: NotRequired[Literal["cisco", "ibm", "standard"]]  # Area border router type.
    auto_cost_ref_bandwidth: NotRequired[int]  # Reference bandwidth in terms of megabits per second.
    default_information_originate: NotRequired[Literal["enable", "always", "disable"]]  # Enable/disable generation of default route.
    log_neighbour_changes: NotRequired[Literal["enable", "disable"]]  # Log OSPFv3 neighbor changes.
    default_information_metric: NotRequired[int]  # Default information metric.
    default_information_metric_type: NotRequired[Literal["1", "2"]]  # Default information metric type.
    default_information_route_map: NotRequired[str]  # Default information route map.
    default_metric: NotRequired[int]  # Default metric of redistribute routes.
    router_id: str  # A.B.C.D, in IPv4 address format.
    spf_timers: NotRequired[str]  # SPF calculation frequency.
    bfd: NotRequired[Literal["enable", "disable"]]  # Enable/disable Bidirectional Forwarding Detection (BFD).
    restart_mode: NotRequired[Literal["none", "graceful-restart"]]  # OSPFv3 restart mode (graceful or none).
    restart_period: NotRequired[int]  # Graceful restart period in seconds.
    restart_on_topology_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable continuing graceful restart upon topology cha
    area: NotRequired[list[dict[str, Any]]]  # OSPF6 area configuration.
    ospf6_interface: NotRequired[list[dict[str, Any]]]  # OSPF6 interface configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    summary_address: NotRequired[list[dict[str, Any]]]  # IPv6 address summary configuration.

# Nested classes for table field children

@final
class Ospf6AreaObject:
    """Typed object for area table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Area entry IP address.
    id: str
    # Summary default cost of stub or NSSA area.
    default_cost: int
    # NSSA translator role type.
    nssa_translator_role: Literal["candidate", "never", "always"]
    # Stub summary setting.
    stub_type: Literal["no-summary", "summary"]
    # Area type setting.
    type: Literal["regular", "nssa", "stub"]
    # Enable/disable originate type 7 default into NSSA area.
    nssa_default_information_originate: Literal["enable", "disable"]
    # OSPFv3 default metric.
    nssa_default_information_originate_metric: int
    # OSPFv3 metric type for default routes.
    nssa_default_information_originate_metric_type: Literal["1", "2"]
    # Enable/disable redistribute into NSSA area.
    nssa_redistribution: Literal["enable", "disable"]
    # Authentication mode.
    authentication: Literal["none", "ah", "esp"]
    # Key roll-over interval.
    key_rollover_interval: int
    # Authentication algorithm.
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]
    # Encryption algorithm.
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]
    # IPsec authentication and encryption keys.
    ipsec_keys: str
    # OSPF6 area range configuration.
    range: str
    # OSPF6 virtual link configuration.
    virtual_link: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class Ospf6Ospf6interfaceObject:
    """Typed object for ospf6-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface entry name.
    name: str
    # A.B.C.D, in IPv4 address format.
    area_id: str
    # Configuration interface name.
    interface: str
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
    # Enable/disable OSPF6 routing on this interface.
    status: Literal["disable", "enable"]
    # Network type.
    network_type: Literal["broadcast", "point-to-point", "non-broadcast", "point-to-multipoint", "point-to-multipoint-non-broadcast"]
    # Enable/disable Bidirectional Forwarding Detection (BFD).
    bfd: Literal["global", "enable", "disable"]
    # MTU for OSPFv3 packets.
    mtu: int
    # Enable/disable ignoring MTU field in DBD packets.
    mtu_ignore: Literal["enable", "disable"]
    # Authentication mode.
    authentication: Literal["none", "ah", "esp", "area"]
    # Key roll-over interval.
    key_rollover_interval: int
    # Authentication algorithm.
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]
    # Encryption algorithm.
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]
    # IPsec authentication and encryption keys.
    ipsec_keys: str
    # OSPFv3 neighbors are used when OSPFv3 runs on non-broadcast media.
    neighbor: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class Ospf6RedistributeObject:
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
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class Ospf6PassiveinterfaceObject:
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
class Ospf6SummaryaddressObject:
    """Typed object for summary-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Summary address entry ID.
    id: int
    # IPv6 prefix.
    prefix6: str
    # Enable/disable advertise status.
    advertise: Literal["disable", "enable"]
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
class Ospf6Response(TypedDict):
    """
    Type hints for router/ospf6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    abr_type: Literal["cisco", "ibm", "standard"]
    auto_cost_ref_bandwidth: int
    default_information_originate: Literal["enable", "always", "disable"]
    log_neighbour_changes: Literal["enable", "disable"]
    default_information_metric: int
    default_information_metric_type: Literal["1", "2"]
    default_information_route_map: str
    default_metric: int
    router_id: str
    spf_timers: str
    bfd: Literal["enable", "disable"]
    restart_mode: Literal["none", "graceful-restart"]
    restart_period: int
    restart_on_topology_change: Literal["enable", "disable"]
    area: list[dict[str, Any]]
    ospf6_interface: list[dict[str, Any]]
    redistribute: list[dict[str, Any]]
    passive_interface: list[dict[str, Any]]
    summary_address: list[dict[str, Any]]


@final
class Ospf6Object:
    """Typed FortiObject for router/ospf6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Area border router type.
    abr_type: Literal["cisco", "ibm", "standard"]
    # Reference bandwidth in terms of megabits per second.
    auto_cost_ref_bandwidth: int
    # Enable/disable generation of default route.
    default_information_originate: Literal["enable", "always", "disable"]
    # Log OSPFv3 neighbor changes.
    log_neighbour_changes: Literal["enable", "disable"]
    # Default information metric.
    default_information_metric: int
    # Default information metric type.
    default_information_metric_type: Literal["1", "2"]
    # Default information route map.
    default_information_route_map: str
    # Default metric of redistribute routes.
    default_metric: int
    # A.B.C.D, in IPv4 address format.
    router_id: str
    # SPF calculation frequency.
    spf_timers: str
    # Enable/disable Bidirectional Forwarding Detection (BFD).
    bfd: Literal["enable", "disable"]
    # OSPFv3 restart mode (graceful or none).
    restart_mode: Literal["none", "graceful-restart"]
    # Graceful restart period in seconds.
    restart_period: int
    # Enable/disable continuing graceful restart upon topology change.
    restart_on_topology_change: Literal["enable", "disable"]
    # OSPF6 area configuration.
    area: list[Ospf6AreaObject]  # Table field - list of typed objects
    # OSPF6 interface configuration.
    ospf6_interface: list[Ospf6Ospf6interfaceObject]  # Table field - list of typed objects
    # Redistribute configuration.
    redistribute: list[Ospf6RedistributeObject]  # Table field - list of typed objects
    # Passive interface configuration.
    passive_interface: list[Ospf6PassiveinterfaceObject]  # Table field - list of typed objects
    # IPv6 address summary configuration.
    summary_address: list[Ospf6SummaryaddressObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Ospf6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ospf6:
    """
    Configure IPv6 OSPF.
    
    Path: router/ospf6
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Response: ...
    
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
    ) -> Ospf6Response: ...
    
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
    ) -> Ospf6Response: ...
    
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
    ) -> Ospf6Object | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Ospf6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ospf6",
    "Ospf6Payload",
    "Ospf6Object",
]