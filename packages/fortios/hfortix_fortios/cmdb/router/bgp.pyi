from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class BgpPayload(TypedDict, total=False):
    """
    Type hints for router/bgp payload fields.
    
    Configure BGP.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.route-map.RouteMapEndpoint` (via: dampening-route-map)

    **Usage:**
        payload: BgpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    asn: str  # Router AS number, asplain/asdot/asdot+ format, 0 to disable 
    router_id: NotRequired[str]  # Router ID.
    keepalive_timer: NotRequired[int]  # Frequency to send keep alive requests.
    holdtime_timer: NotRequired[int]  # Number of seconds to mark peer as dead.
    always_compare_med: NotRequired[Literal["enable", "disable"]]  # Enable/disable always compare MED.
    bestpath_as_path_ignore: NotRequired[Literal["enable", "disable"]]  # Enable/disable ignore AS path.
    bestpath_cmp_confed_aspath: NotRequired[Literal["enable", "disable"]]  # Enable/disable compare federation AS path length.
    bestpath_cmp_routerid: NotRequired[Literal["enable", "disable"]]  # Enable/disable compare router ID for identical EBGP paths.
    bestpath_med_confed: NotRequired[Literal["enable", "disable"]]  # Enable/disable compare MED among confederation paths.
    bestpath_med_missing_as_worst: NotRequired[Literal["enable", "disable"]]  # Enable/disable treat missing MED as least preferred.
    client_to_client_reflection: NotRequired[Literal["enable", "disable"]]  # Enable/disable client-to-client route reflection.
    dampening: NotRequired[Literal["enable", "disable"]]  # Enable/disable route-flap dampening.
    deterministic_med: NotRequired[Literal["enable", "disable"]]  # Enable/disable enforce deterministic comparison of MED.
    ebgp_multipath: NotRequired[Literal["enable", "disable"]]  # Enable/disable EBGP multi-path.
    ibgp_multipath: NotRequired[Literal["enable", "disable"]]  # Enable/disable IBGP multi-path.
    enforce_first_as: NotRequired[Literal["enable", "disable"]]  # Enable/disable enforce first AS for EBGP routes.
    fast_external_failover: NotRequired[Literal["enable", "disable"]]  # Enable/disable reset peer BGP session if link goes down.
    log_neighbour_changes: NotRequired[Literal["enable", "disable"]]  # Log BGP neighbor changes.
    network_import_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable ensure BGP network route exists in IGP.
    ignore_optional_capability: NotRequired[Literal["enable", "disable"]]  # Do not send unknown optional capability notification message
    additional_path: NotRequired[Literal["enable", "disable"]]  # Enable/disable selection of BGP IPv4 additional paths.
    additional_path6: NotRequired[Literal["enable", "disable"]]  # Enable/disable selection of BGP IPv6 additional paths.
    additional_path_vpnv4: NotRequired[Literal["enable", "disable"]]  # Enable/disable selection of BGP VPNv4 additional paths.
    additional_path_vpnv6: NotRequired[Literal["enable", "disable"]]  # Enable/disable selection of BGP VPNv6 additional paths.
    multipath_recursive_distance: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of recursive distance to select multipath
    recursive_next_hop: NotRequired[Literal["enable", "disable"]]  # Enable/disable recursive resolution of next-hop using BGP ro
    recursive_inherit_priority: NotRequired[Literal["enable", "disable"]]  # Enable/disable priority inheritance for recursive resolution
    tag_resolve_mode: NotRequired[Literal["disable", "preferred", "merge", "merge-all"]]  # Configure tag-match mode. Resolves BGP routes with other rou
    cluster_id: NotRequired[str]  # Route reflector cluster ID.
    confederation_identifier: NotRequired[int]  # Confederation identifier.
    confederation_peers: NotRequired[list[dict[str, Any]]]  # Confederation peers.
    dampening_route_map: NotRequired[str]  # Criteria for dampening.
    dampening_reachability_half_life: NotRequired[int]  # Reachability half-life time for penalty (min).
    dampening_reuse: NotRequired[int]  # Threshold to reuse routes.
    dampening_suppress: NotRequired[int]  # Threshold to suppress routes.
    dampening_max_suppress_time: NotRequired[int]  # Maximum minutes a route can be suppressed.
    dampening_unreachability_half_life: NotRequired[int]  # Unreachability half-life time for penalty (min).
    default_local_preference: NotRequired[int]  # Default local preference.
    scan_time: NotRequired[int]  # Background scanner interval (sec), 0 to disable it.
    distance_external: NotRequired[int]  # Distance for routes external to the AS.
    distance_internal: NotRequired[int]  # Distance for routes internal to the AS.
    distance_local: NotRequired[int]  # Distance for routes local to the AS.
    synchronization: NotRequired[Literal["enable", "disable"]]  # Enable/disable only advertise routes from iBGP if routes pre
    graceful_restart: NotRequired[Literal["enable", "disable"]]  # Enable/disable BGP graceful restart capabilities.
    graceful_restart_time: NotRequired[int]  # Time needed for neighbors to restart (sec).
    graceful_stalepath_time: NotRequired[int]  # Time to hold stale paths of restarting neighbor (sec).
    graceful_update_delay: NotRequired[int]  # Route advertisement/selection delay after restart (sec).
    graceful_end_on_timer: NotRequired[Literal["enable", "disable"]]  # Enable/disable to exit graceful restart on timer only.
    additional_path_select: NotRequired[int]  # Number of additional paths to be selected for each IPv4 NLRI
    additional_path_select6: NotRequired[int]  # Number of additional paths to be selected for each IPv6 NLRI
    additional_path_select_vpnv4: NotRequired[int]  # Number of additional paths to be selected for each VPNv4 NLR
    additional_path_select_vpnv6: NotRequired[int]  # Number of additional paths to be selected for each VPNv6 NLR
    cross_family_conditional_adv: NotRequired[Literal["enable", "disable"]]  # Enable/disable cross address family conditional advertisemen
    aggregate_address: NotRequired[list[dict[str, Any]]]  # BGP aggregate address table.
    aggregate_address6: NotRequired[list[dict[str, Any]]]  # BGP IPv6 aggregate address table.
    neighbor: NotRequired[list[dict[str, Any]]]  # BGP neighbor table.
    neighbor_group: NotRequired[list[dict[str, Any]]]  # BGP neighbor group table.
    neighbor_range: NotRequired[list[dict[str, Any]]]  # BGP neighbor range table.
    neighbor_range6: NotRequired[list[dict[str, Any]]]  # BGP IPv6 neighbor range table.
    network: NotRequired[list[dict[str, Any]]]  # BGP network table.
    network6: NotRequired[list[dict[str, Any]]]  # BGP IPv6 network table.
    redistribute: NotRequired[list[dict[str, Any]]]  # BGP IPv4 redistribute table.
    redistribute6: NotRequired[list[dict[str, Any]]]  # BGP IPv6 redistribute table.
    admin_distance: NotRequired[list[dict[str, Any]]]  # Administrative distance modifications.
    vrf: NotRequired[list[dict[str, Any]]]  # BGP VRF leaking table.
    vrf6: NotRequired[list[dict[str, Any]]]  # BGP IPv6 VRF leaking table.


class BgpObject(FortiObject[BgpPayload]):
    """Typed FortiObject for router/bgp with IDE autocomplete support."""
    
    # Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP.
    asn: str
    # Router ID.
    router_id: str
    # Frequency to send keep alive requests.
    keepalive_timer: int
    # Number of seconds to mark peer as dead.
    holdtime_timer: int
    # Enable/disable always compare MED.
    always_compare_med: Literal["enable", "disable"]
    # Enable/disable ignore AS path.
    bestpath_as_path_ignore: Literal["enable", "disable"]
    # Enable/disable compare federation AS path length.
    bestpath_cmp_confed_aspath: Literal["enable", "disable"]
    # Enable/disable compare router ID for identical EBGP paths.
    bestpath_cmp_routerid: Literal["enable", "disable"]
    # Enable/disable compare MED among confederation paths.
    bestpath_med_confed: Literal["enable", "disable"]
    # Enable/disable treat missing MED as least preferred.
    bestpath_med_missing_as_worst: Literal["enable", "disable"]
    # Enable/disable client-to-client route reflection.
    client_to_client_reflection: Literal["enable", "disable"]
    # Enable/disable route-flap dampening.
    dampening: Literal["enable", "disable"]
    # Enable/disable enforce deterministic comparison of MED.
    deterministic_med: Literal["enable", "disable"]
    # Enable/disable EBGP multi-path.
    ebgp_multipath: Literal["enable", "disable"]
    # Enable/disable IBGP multi-path.
    ibgp_multipath: Literal["enable", "disable"]
    # Enable/disable enforce first AS for EBGP routes.
    enforce_first_as: Literal["enable", "disable"]
    # Enable/disable reset peer BGP session if link goes down.
    fast_external_failover: Literal["enable", "disable"]
    # Log BGP neighbor changes.
    log_neighbour_changes: Literal["enable", "disable"]
    # Enable/disable ensure BGP network route exists in IGP.
    network_import_check: Literal["enable", "disable"]
    # Do not send unknown optional capability notification message.
    ignore_optional_capability: Literal["enable", "disable"]
    # Enable/disable selection of BGP IPv4 additional paths.
    additional_path: Literal["enable", "disable"]
    # Enable/disable selection of BGP IPv6 additional paths.
    additional_path6: Literal["enable", "disable"]
    # Enable/disable selection of BGP VPNv4 additional paths.
    additional_path_vpnv4: Literal["enable", "disable"]
    # Enable/disable selection of BGP VPNv6 additional paths.
    additional_path_vpnv6: Literal["enable", "disable"]
    # Enable/disable use of recursive distance to select multipath.
    multipath_recursive_distance: Literal["enable", "disable"]
    # Enable/disable recursive resolution of next-hop using BGP route.
    recursive_next_hop: Literal["enable", "disable"]
    # Enable/disable priority inheritance for recursive resolution.
    recursive_inherit_priority: Literal["enable", "disable"]
    # Configure tag-match mode. Resolves BGP routes with other routes containing the s
    tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"]
    # Route reflector cluster ID.
    cluster_id: str
    # Confederation identifier.
    confederation_identifier: int
    # Confederation peers.
    confederation_peers: list[str]  # Auto-flattened from member_table
    # Criteria for dampening.
    dampening_route_map: str
    # Reachability half-life time for penalty (min).
    dampening_reachability_half_life: int
    # Threshold to reuse routes.
    dampening_reuse: int
    # Threshold to suppress routes.
    dampening_suppress: int
    # Maximum minutes a route can be suppressed.
    dampening_max_suppress_time: int
    # Unreachability half-life time for penalty (min).
    dampening_unreachability_half_life: int
    # Default local preference.
    default_local_preference: int
    # Background scanner interval (sec), 0 to disable it.
    scan_time: int
    # Distance for routes external to the AS.
    distance_external: int
    # Distance for routes internal to the AS.
    distance_internal: int
    # Distance for routes local to the AS.
    distance_local: int
    # Enable/disable only advertise routes from iBGP if routes present in an IGP.
    synchronization: Literal["enable", "disable"]
    # Enable/disable BGP graceful restart capabilities.
    graceful_restart: Literal["enable", "disable"]
    # Time needed for neighbors to restart (sec).
    graceful_restart_time: int
    # Time to hold stale paths of restarting neighbor (sec).
    graceful_stalepath_time: int
    # Route advertisement/selection delay after restart (sec).
    graceful_update_delay: int
    # Enable/disable to exit graceful restart on timer only.
    graceful_end_on_timer: Literal["enable", "disable"]
    # Number of additional paths to be selected for each IPv4 NLRI.
    additional_path_select: int
    # Number of additional paths to be selected for each IPv6 NLRI.
    additional_path_select6: int
    # Number of additional paths to be selected for each VPNv4 NLRI.
    additional_path_select_vpnv4: int
    # Number of additional paths to be selected for each VPNv6 NLRI.
    additional_path_select_vpnv6: int
    # Enable/disable cross address family conditional advertisement.
    cross_family_conditional_adv: Literal["enable", "disable"]
    # BGP aggregate address table.
    aggregate_address: list[str]  # Auto-flattened from member_table
    # BGP IPv6 aggregate address table.
    aggregate_address6: list[str]  # Auto-flattened from member_table
    # BGP neighbor table.
    neighbor: list[str]  # Auto-flattened from member_table
    # BGP neighbor group table.
    neighbor_group: list[str]  # Auto-flattened from member_table
    # BGP neighbor range table.
    neighbor_range: list[str]  # Auto-flattened from member_table
    # BGP IPv6 neighbor range table.
    neighbor_range6: list[str]  # Auto-flattened from member_table
    # BGP network table.
    network: list[str]  # Auto-flattened from member_table
    # BGP IPv6 network table.
    network6: list[str]  # Auto-flattened from member_table
    # BGP IPv4 redistribute table.
    redistribute: list[str]  # Auto-flattened from member_table
    # BGP IPv6 redistribute table.
    redistribute6: list[str]  # Auto-flattened from member_table
    # Administrative distance modifications.
    admin_distance: list[str]  # Auto-flattened from member_table
    # BGP VRF leaking table.
    vrf: list[str]  # Auto-flattened from member_table
    # BGP IPv6 VRF leaking table.
    vrf6: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> BgpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Bgp:
    """
    Configure BGP.
    
    Path: router/bgp
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
    ) -> BgpObject: ...
    
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
    ) -> BgpObject: ...
    
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
    ) -> BgpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Bgp",
    "BgpPayload",
    "BgpObject",
]