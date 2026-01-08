from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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

# Nested classes for table field children

@final
class BgpConfederationpeersObject:
    """Typed object for confederation-peers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Peer ID.
    peer: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpAggregateaddressObject:
    """Typed object for aggregate-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Aggregate prefix.
    prefix: str
    # Enable/disable generate AS set path information.
    as_set: Literal["enable", "disable"]
    # Enable/disable filter more specific routes from updates.
    summary_only: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpAggregateaddress6Object:
    """Typed object for aggregate-address6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Aggregate IPv6 prefix.
    prefix6: str
    # Enable/disable generate AS set path information.
    as_set: Literal["enable", "disable"]
    # Enable/disable filter more specific routes from updates.
    summary_only: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP/IPv6 address of neighbor.
    ip: str
    # Minimum interval (sec) between sending updates.
    advertisement_interval: int
    # Enable/disable IPv4 Enable to allow my AS in AS path.
    allowas_in_enable: Literal["enable", "disable"]
    # Enable/disable IPv6 Enable to allow my AS in AS path.
    allowas_in_enable6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for VPNv4 route.
    allowas_in_enable_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of my AS in AS path for VPNv6 route.
    allowas_in_enable_vpnv6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for L2VPN EVPN route.
    allowas_in_enable_evpn: Literal["enable", "disable"]
    # IPv4 The maximum number of occurrence of my AS number allowed.
    allowas_in: int
    # IPv6 The maximum number of occurrence of my AS number allowed.
    allowas_in6: int
    # The maximum number of occurrence of my AS number allowed for VPNv4 route.
    allowas_in_vpnv4: int
    # The maximum number of occurrence of my AS number allowed for VPNv6 route.
    allowas_in_vpnv6: int
    # The maximum number of occurrence of my AS number allowed for L2VPN EVPN route.
    allowas_in_evpn: int
    # IPv4 List of attributes that should be unchanged.
    attribute_unchanged: Literal["as-path", "med", "next-hop"]
    # IPv6 List of attributes that should be unchanged.
    attribute_unchanged6: Literal["as-path", "med", "next-hop"]
    # List of attributes that should be unchanged for VPNv4 route.
    attribute_unchanged_vpnv4: Literal["as-path", "med", "next-hop"]
    # List of attributes that should not be changed for VPNv6 route.
    attribute_unchanged_vpnv6: Literal["as-path", "med", "next-hop"]
    # Enable/disable address family IPv4 for this neighbor.
    activate: Literal["enable", "disable"]
    # Enable/disable address family IPv6 for this neighbor.
    activate6: Literal["enable", "disable"]
    # Enable/disable address family VPNv4 for this neighbor.
    activate_vpnv4: Literal["enable", "disable"]
    # Enable/disable address family VPNv6 for this neighbor.
    activate_vpnv6: Literal["enable", "disable"]
    # Enable/disable address family L2VPN EVPN for this neighbor.
    activate_evpn: Literal["enable", "disable"]
    # Enable/disable BFD for this neighbor.
    bfd: Literal["enable", "disable"]
    # Enable/disable advertise dynamic capability to this neighbor.
    capability_dynamic: Literal["enable", "disable"]
    # Accept/Send IPv4 ORF lists to/from this neighbor.
    capability_orf: Literal["none", "receive", "send", "both"]
    # Accept/Send IPv6 ORF lists to/from this neighbor.
    capability_orf6: Literal["none", "receive", "send", "both"]
    # Enable/disable advertise IPv4 graceful restart capability to this neighbor.
    capability_graceful_restart: Literal["enable", "disable"]
    # Enable/disable advertise IPv6 graceful restart capability to this neighbor.
    capability_graceful_restart6: Literal["enable", "disable"]
    # Enable/disable advertise VPNv4 graceful restart capability to this neighbor.
    capability_graceful_restart_vpnv4: Literal["enable", "disable"]
    # Enable/disable advertisement of VPNv6 graceful restart capability to this neighb
    capability_graceful_restart_vpnv6: Literal["enable", "disable"]
    # Enable/disable advertisement of L2VPN EVPN graceful restart capability to this n
    capability_graceful_restart_evpn: Literal["enable", "disable"]
    # Enable/disable advertise route refresh capability to this neighbor.
    capability_route_refresh: Literal["enable", "disable"]
    # Enable/disable advertise default IPv4 route to this neighbor.
    capability_default_originate: Literal["enable", "disable"]
    # Enable/disable advertise default IPv6 route to this neighbor.
    capability_default_originate6: Literal["enable", "disable"]
    # Do not negotiate capabilities with this neighbor.
    dont_capability_negotiate: Literal["enable", "disable"]
    # Enable/disable allow multi-hop EBGP neighbors.
    ebgp_enforce_multihop: Literal["enable", "disable"]
    # Enable/disable failover upon link down.
    link_down_failover: Literal["enable", "disable"]
    # Enable/disable stale route after neighbor down.
    stale_route: Literal["enable", "disable"]
    # Enable/disable IPv4 next-hop calculation for this neighbor.
    next_hop_self: Literal["enable", "disable"]
    # Enable/disable IPv6 next-hop calculation for this neighbor.
    next_hop_self6: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv4 address for route-r
    next_hop_self_rr: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv6 address for route-r
    next_hop_self_rr6: Literal["enable", "disable"]
    # Enable/disable setting VPNv4 next-hop to interface's IP address for this neighbo
    next_hop_self_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of outgoing interface's IP address as VPNv6 next-hop for this
    next_hop_self_vpnv6: Literal["enable", "disable"]
    # Enable/disable override result of capability negotiation.
    override_capability: Literal["enable", "disable"]
    # Enable/disable sending of open messages to this neighbor.
    passive: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv4 outbound updates.
    remove_private_as: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv6 outbound updates.
    remove_private_as6: Literal["enable", "disable"]
    # Enable/disable remove private AS number from VPNv4 outbound updates.
    remove_private_as_vpnv4: Literal["enable", "disable"]
    # Enable/disable to remove private AS number from VPNv6 outbound updates.
    remove_private_as_vpnv6: Literal["enable", "disable"]
    # Enable/disable removing private AS number from L2VPN EVPN outbound updates.
    remove_private_as_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route reflector client.
    route_reflector_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route reflector client.
    route_reflector_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route reflector client for this neighbor.
    route_reflector_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route reflector client for this neighbor.
    route_reflector_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route reflector client for this neighbor.
    route_reflector_client_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route server client.
    route_server_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route server client.
    route_server_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route server client for this neighbor.
    route_server_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route server client for this neighbor.
    route_server_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route server client for this neighbor.
    route_server_client_evpn: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to IPv4 rout
    rr_attr_allow_change: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to IPv6 rout
    rr_attr_allow_change6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to VPNv4 rou
    rr_attr_allow_change_vpnv4: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to VPNv6 rou
    rr_attr_allow_change_vpnv6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to L2VPN EVP
    rr_attr_allow_change_evpn: Literal["enable", "disable"]
    # Enable/disable shutdown this neighbor.
    shutdown: Literal["enable", "disable"]
    # Enable/disable allow IPv4 inbound soft reconfiguration.
    soft_reconfiguration: Literal["enable", "disable"]
    # Enable/disable allow IPv6 inbound soft reconfiguration.
    soft_reconfiguration6: Literal["enable", "disable"]
    # Enable/disable allow VPNv4 inbound soft reconfiguration.
    soft_reconfiguration_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 inbound soft reconfiguration.
    soft_reconfiguration_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN inbound soft reconfiguration.
    soft_reconfiguration_evpn: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv4.
    as_override: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv6.
    as_override6: Literal["enable", "disable"]
    # Enable/disable strict capability matching.
    strict_capability_match: Literal["enable", "disable"]
    # Route map to specify criteria to originate IPv4 default.
    default_originate_routemap: str
    # Route map to specify criteria to originate IPv6 default.
    default_originate_routemap6: str
    # Description.
    description: str
    # Filter for IPv4 updates from this neighbor.
    distribute_list_in: str
    # Filter for IPv6 updates from this neighbor.
    distribute_list_in6: str
    # Filter for VPNv4 updates from this neighbor.
    distribute_list_in_vpnv4: str
    # Filter for VPNv6 updates from this neighbor.
    distribute_list_in_vpnv6: str
    # Filter for IPv4 updates to this neighbor.
    distribute_list_out: str
    # Filter for IPv6 updates to this neighbor.
    distribute_list_out6: str
    # Filter for VPNv4 updates to this neighbor.
    distribute_list_out_vpnv4: str
    # Filter for VPNv6 updates to this neighbor.
    distribute_list_out_vpnv6: str
    # EBGP multihop TTL for this peer.
    ebgp_multihop_ttl: int
    # BGP filter for IPv4 inbound routes.
    filter_list_in: str
    # BGP filter for IPv6 inbound routes.
    filter_list_in6: str
    # BGP filter for VPNv4 inbound routes.
    filter_list_in_vpnv4: str
    # BGP filter for VPNv6 inbound routes.
    filter_list_in_vpnv6: str
    # BGP filter for IPv4 outbound routes.
    filter_list_out: str
    # BGP filter for IPv6 outbound routes.
    filter_list_out6: str
    # BGP filter for VPNv4 outbound routes.
    filter_list_out_vpnv4: str
    # BGP filter for VPNv6 outbound routes.
    filter_list_out_vpnv6: str
    # Specify outgoing interface for peer connection. For IPv6 peer, the interface sho
    interface: str
    # Maximum number of IPv4 prefixes to accept from this peer.
    maximum_prefix: int
    # Maximum number of IPv6 prefixes to accept from this peer.
    maximum_prefix6: int
    # Maximum number of VPNv4 prefixes to accept from this peer.
    maximum_prefix_vpnv4: int
    # Maximum number of VPNv6 prefixes to accept from this peer.
    maximum_prefix_vpnv6: int
    # Maximum number of L2VPN EVPN prefixes to accept from this peer.
    maximum_prefix_evpn: int
    # Maximum IPv4 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold: int
    # Maximum IPv6 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold6: int
    # Maximum VPNv4 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold_vpnv4: int
    # Maximum VPNv6 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold_vpnv6: int
    # Maximum L2VPN EVPN prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold_evpn: int
    # Enable/disable IPv4 Only give warning message when limit is exceeded.
    maximum_prefix_warning_only: Literal["enable", "disable"]
    # Enable/disable IPv6 Only give warning message when limit is exceeded.
    maximum_prefix_warning_only6: Literal["enable", "disable"]
    # Enable/disable only giving warning message when limit is exceeded for VPNv4 rout
    maximum_prefix_warning_only_vpnv4: Literal["enable", "disable"]
    # Enable/disable warning message when limit is exceeded for VPNv6 routes.
    maximum_prefix_warning_only_vpnv6: Literal["enable", "disable"]
    # Enable/disable only sending warning message when exceeding limit of L2VPN EVPN r
    maximum_prefix_warning_only_evpn: Literal["enable", "disable"]
    # IPv4 Inbound filter for updates from this neighbor.
    prefix_list_in: str
    # IPv6 Inbound filter for updates from this neighbor.
    prefix_list_in6: str
    # Inbound filter for VPNv4 updates from this neighbor.
    prefix_list_in_vpnv4: str
    # Inbound filter for VPNv6 updates from this neighbor.
    prefix_list_in_vpnv6: str
    # IPv4 Outbound filter for updates to this neighbor.
    prefix_list_out: str
    # IPv6 Outbound filter for updates to this neighbor.
    prefix_list_out6: str
    # Outbound filter for VPNv4 updates to this neighbor.
    prefix_list_out_vpnv4: str
    # Outbound filter for VPNv6 updates to this neighbor.
    prefix_list_out_vpnv6: str
    # AS number of neighbor.
    remote_as: str
    # Local AS number of neighbor.
    local_as: str
    # Do not prepend local-as to incoming updates.
    local_as_no_prepend: Literal["enable", "disable"]
    # Replace real AS with local-as in outgoing updates.
    local_as_replace_as: Literal["enable", "disable"]
    # Time to retain stale routes.
    retain_stale_time: int
    # IPv4 Inbound route map filter.
    route_map_in: str
    # IPv6 Inbound route map filter.
    route_map_in6: str
    # VPNv4 inbound route map filter.
    route_map_in_vpnv4: str
    # VPNv6 inbound route map filter.
    route_map_in_vpnv6: str
    # L2VPN EVPN inbound route map filter.
    route_map_in_evpn: str
    # IPv4 outbound route map filter.
    route_map_out: str
    # IPv4 outbound route map filter if the peer is preferred.
    route_map_out_preferable: str
    # IPv6 Outbound route map filter.
    route_map_out6: str
    # IPv6 outbound route map filter if the peer is preferred.
    route_map_out6_preferable: str
    # VPNv4 outbound route map filter.
    route_map_out_vpnv4: str
    # VPNv6 outbound route map filter.
    route_map_out_vpnv6: str
    # VPNv4 outbound route map filter if the peer is preferred.
    route_map_out_vpnv4_preferable: str
    # VPNv6 outbound route map filter if this neighbor is preferred.
    route_map_out_vpnv6_preferable: str
    # L2VPN EVPN outbound route map filter.
    route_map_out_evpn: str
    # IPv4 Send community attribute to neighbor.
    send_community: Literal["standard", "extended", "both", "disable"]
    # IPv6 Send community attribute to neighbor.
    send_community6: Literal["standard", "extended", "both", "disable"]
    # Send community attribute to neighbor for VPNv4 address family.
    send_community_vpnv4: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to this neighbor for VPNv6 address fa
    send_community_vpnv6: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to neighbor for L2VPN EVPN address fa
    send_community_evpn: Literal["standard", "extended", "both", "disable"]
    # Keep alive timer interval (sec).
    keep_alive_timer: int
    # Interval (sec) before peer considered dead.
    holdtime_timer: int
    # Interval (sec) for connect timer.
    connect_timer: int
    # IPv4 Route map to selectively unsuppress suppressed routes.
    unsuppress_map: str
    # IPv6 Route map to selectively unsuppress suppressed routes.
    unsuppress_map6: str
    # Interface to use as source IP/IPv6 address of TCP connections.
    update_source: str
    # Neighbor weight.
    weight: int
    # Graceful restart delay time (sec, 0 = global default).
    restart_time: int
    # Enable/disable IPv4 additional-path capability.
    additional_path: Literal["send", "receive", "both", "disable"]
    # Enable/disable IPv6 additional-path capability.
    additional_path6: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv4 additional-path capability.
    additional_path_vpnv4: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv6 additional-path capability.
    additional_path_vpnv6: Literal["send", "receive", "both", "disable"]
    # Number of IPv4 additional paths that can be advertised to this neighbor.
    adv_additional_path: int
    # Number of IPv6 additional paths that can be advertised to this neighbor.
    adv_additional_path6: int
    # Number of VPNv4 additional paths that can be advertised to this neighbor.
    adv_additional_path_vpnv4: int
    # Number of VPNv6 additional paths that can be advertised to this neighbor.
    adv_additional_path_vpnv6: int
    # Password used in MD5 authentication.
    password: str
    # Key-chain name for TCP authentication options.
    auth_options: str
    # Conditional advertisement.
    conditional_advertise: str
    # IPv6 conditional advertisement.
    conditional_advertise6: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpNeighborgroupObject:
    """Typed object for neighbor-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor group name.
    name: str
    # Minimum interval (sec) between sending updates.
    advertisement_interval: int
    # Enable/disable IPv4 Enable to allow my AS in AS path.
    allowas_in_enable: Literal["enable", "disable"]
    # Enable/disable IPv6 Enable to allow my AS in AS path.
    allowas_in_enable6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for VPNv4 route.
    allowas_in_enable_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of my AS in AS path for VPNv6 route.
    allowas_in_enable_vpnv6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for L2VPN EVPN route.
    allowas_in_enable_evpn: Literal["enable", "disable"]
    # IPv4 The maximum number of occurrence of my AS number allowed.
    allowas_in: int
    # IPv6 The maximum number of occurrence of my AS number allowed.
    allowas_in6: int
    # The maximum number of occurrence of my AS number allowed for VPNv4 route.
    allowas_in_vpnv4: int
    # The maximum number of occurrence of my AS number allowed for VPNv6 route.
    allowas_in_vpnv6: int
    # The maximum number of occurrence of my AS number allowed for L2VPN EVPN route.
    allowas_in_evpn: int
    # IPv4 List of attributes that should be unchanged.
    attribute_unchanged: Literal["as-path", "med", "next-hop"]
    # IPv6 List of attributes that should be unchanged.
    attribute_unchanged6: Literal["as-path", "med", "next-hop"]
    # List of attributes that should be unchanged for VPNv4 route.
    attribute_unchanged_vpnv4: Literal["as-path", "med", "next-hop"]
    # List of attributes that should not be changed for VPNv6 route.
    attribute_unchanged_vpnv6: Literal["as-path", "med", "next-hop"]
    # Enable/disable address family IPv4 for this neighbor.
    activate: Literal["enable", "disable"]
    # Enable/disable address family IPv6 for this neighbor.
    activate6: Literal["enable", "disable"]
    # Enable/disable address family VPNv4 for this neighbor.
    activate_vpnv4: Literal["enable", "disable"]
    # Enable/disable address family VPNv6 for this neighbor.
    activate_vpnv6: Literal["enable", "disable"]
    # Enable/disable address family L2VPN EVPN for this neighbor.
    activate_evpn: Literal["enable", "disable"]
    # Enable/disable BFD for this neighbor.
    bfd: Literal["enable", "disable"]
    # Enable/disable advertise dynamic capability to this neighbor.
    capability_dynamic: Literal["enable", "disable"]
    # Accept/Send IPv4 ORF lists to/from this neighbor.
    capability_orf: Literal["none", "receive", "send", "both"]
    # Accept/Send IPv6 ORF lists to/from this neighbor.
    capability_orf6: Literal["none", "receive", "send", "both"]
    # Enable/disable advertise IPv4 graceful restart capability to this neighbor.
    capability_graceful_restart: Literal["enable", "disable"]
    # Enable/disable advertise IPv6 graceful restart capability to this neighbor.
    capability_graceful_restart6: Literal["enable", "disable"]
    # Enable/disable advertise VPNv4 graceful restart capability to this neighbor.
    capability_graceful_restart_vpnv4: Literal["enable", "disable"]
    # Enable/disable advertisement of VPNv6 graceful restart capability to this neighb
    capability_graceful_restart_vpnv6: Literal["enable", "disable"]
    # Enable/disable advertisement of L2VPN EVPN graceful restart capability to this n
    capability_graceful_restart_evpn: Literal["enable", "disable"]
    # Enable/disable advertise route refresh capability to this neighbor.
    capability_route_refresh: Literal["enable", "disable"]
    # Enable/disable advertise default IPv4 route to this neighbor.
    capability_default_originate: Literal["enable", "disable"]
    # Enable/disable advertise default IPv6 route to this neighbor.
    capability_default_originate6: Literal["enable", "disable"]
    # Do not negotiate capabilities with this neighbor.
    dont_capability_negotiate: Literal["enable", "disable"]
    # Enable/disable allow multi-hop EBGP neighbors.
    ebgp_enforce_multihop: Literal["enable", "disable"]
    # Enable/disable failover upon link down.
    link_down_failover: Literal["enable", "disable"]
    # Enable/disable stale route after neighbor down.
    stale_route: Literal["enable", "disable"]
    # Enable/disable IPv4 next-hop calculation for this neighbor.
    next_hop_self: Literal["enable", "disable"]
    # Enable/disable IPv6 next-hop calculation for this neighbor.
    next_hop_self6: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv4 address for route-r
    next_hop_self_rr: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv6 address for route-r
    next_hop_self_rr6: Literal["enable", "disable"]
    # Enable/disable setting VPNv4 next-hop to interface's IP address for this neighbo
    next_hop_self_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of outgoing interface's IP address as VPNv6 next-hop for this
    next_hop_self_vpnv6: Literal["enable", "disable"]
    # Enable/disable override result of capability negotiation.
    override_capability: Literal["enable", "disable"]
    # Enable/disable sending of open messages to this neighbor.
    passive: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv4 outbound updates.
    remove_private_as: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv6 outbound updates.
    remove_private_as6: Literal["enable", "disable"]
    # Enable/disable remove private AS number from VPNv4 outbound updates.
    remove_private_as_vpnv4: Literal["enable", "disable"]
    # Enable/disable to remove private AS number from VPNv6 outbound updates.
    remove_private_as_vpnv6: Literal["enable", "disable"]
    # Enable/disable removing private AS number from L2VPN EVPN outbound updates.
    remove_private_as_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route reflector client.
    route_reflector_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route reflector client.
    route_reflector_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route reflector client for this neighbor.
    route_reflector_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route reflector client for this neighbor.
    route_reflector_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route reflector client for this neighbor.
    route_reflector_client_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route server client.
    route_server_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route server client.
    route_server_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route server client for this neighbor.
    route_server_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route server client for this neighbor.
    route_server_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route server client for this neighbor.
    route_server_client_evpn: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to IPv4 rout
    rr_attr_allow_change: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to IPv6 rout
    rr_attr_allow_change6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to VPNv4 rou
    rr_attr_allow_change_vpnv4: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to VPNv6 rou
    rr_attr_allow_change_vpnv6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when advertising to L2VPN EVP
    rr_attr_allow_change_evpn: Literal["enable", "disable"]
    # Enable/disable shutdown this neighbor.
    shutdown: Literal["enable", "disable"]
    # Enable/disable allow IPv4 inbound soft reconfiguration.
    soft_reconfiguration: Literal["enable", "disable"]
    # Enable/disable allow IPv6 inbound soft reconfiguration.
    soft_reconfiguration6: Literal["enable", "disable"]
    # Enable/disable allow VPNv4 inbound soft reconfiguration.
    soft_reconfiguration_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 inbound soft reconfiguration.
    soft_reconfiguration_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN inbound soft reconfiguration.
    soft_reconfiguration_evpn: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv4.
    as_override: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv6.
    as_override6: Literal["enable", "disable"]
    # Enable/disable strict capability matching.
    strict_capability_match: Literal["enable", "disable"]
    # Route map to specify criteria to originate IPv4 default.
    default_originate_routemap: str
    # Route map to specify criteria to originate IPv6 default.
    default_originate_routemap6: str
    # Description.
    description: str
    # Filter for IPv4 updates from this neighbor.
    distribute_list_in: str
    # Filter for IPv6 updates from this neighbor.
    distribute_list_in6: str
    # Filter for VPNv4 updates from this neighbor.
    distribute_list_in_vpnv4: str
    # Filter for VPNv6 updates from this neighbor.
    distribute_list_in_vpnv6: str
    # Filter for IPv4 updates to this neighbor.
    distribute_list_out: str
    # Filter for IPv6 updates to this neighbor.
    distribute_list_out6: str
    # Filter for VPNv4 updates to this neighbor.
    distribute_list_out_vpnv4: str
    # Filter for VPNv6 updates to this neighbor.
    distribute_list_out_vpnv6: str
    # EBGP multihop TTL for this peer.
    ebgp_multihop_ttl: int
    # BGP filter for IPv4 inbound routes.
    filter_list_in: str
    # BGP filter for IPv6 inbound routes.
    filter_list_in6: str
    # BGP filter for VPNv4 inbound routes.
    filter_list_in_vpnv4: str
    # BGP filter for VPNv6 inbound routes.
    filter_list_in_vpnv6: str
    # BGP filter for IPv4 outbound routes.
    filter_list_out: str
    # BGP filter for IPv6 outbound routes.
    filter_list_out6: str
    # BGP filter for VPNv4 outbound routes.
    filter_list_out_vpnv4: str
    # BGP filter for VPNv6 outbound routes.
    filter_list_out_vpnv6: str
    # Specify outgoing interface for peer connection. For IPv6 peer, the interface sho
    interface: str
    # Maximum number of IPv4 prefixes to accept from this peer.
    maximum_prefix: int
    # Maximum number of IPv6 prefixes to accept from this peer.
    maximum_prefix6: int
    # Maximum number of VPNv4 prefixes to accept from this peer.
    maximum_prefix_vpnv4: int
    # Maximum number of VPNv6 prefixes to accept from this peer.
    maximum_prefix_vpnv6: int
    # Maximum number of L2VPN EVPN prefixes to accept from this peer.
    maximum_prefix_evpn: int
    # Maximum IPv4 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold: int
    # Maximum IPv6 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold6: int
    # Maximum VPNv4 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold_vpnv4: int
    # Maximum VPNv6 prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold_vpnv6: int
    # Maximum L2VPN EVPN prefix threshold value (1 - 100 percent).
    maximum_prefix_threshold_evpn: int
    # Enable/disable IPv4 Only give warning message when limit is exceeded.
    maximum_prefix_warning_only: Literal["enable", "disable"]
    # Enable/disable IPv6 Only give warning message when limit is exceeded.
    maximum_prefix_warning_only6: Literal["enable", "disable"]
    # Enable/disable only giving warning message when limit is exceeded for VPNv4 rout
    maximum_prefix_warning_only_vpnv4: Literal["enable", "disable"]
    # Enable/disable warning message when limit is exceeded for VPNv6 routes.
    maximum_prefix_warning_only_vpnv6: Literal["enable", "disable"]
    # Enable/disable only sending warning message when exceeding limit of L2VPN EVPN r
    maximum_prefix_warning_only_evpn: Literal["enable", "disable"]
    # IPv4 Inbound filter for updates from this neighbor.
    prefix_list_in: str
    # IPv6 Inbound filter for updates from this neighbor.
    prefix_list_in6: str
    # Inbound filter for VPNv4 updates from this neighbor.
    prefix_list_in_vpnv4: str
    # Inbound filter for VPNv6 updates from this neighbor.
    prefix_list_in_vpnv6: str
    # IPv4 Outbound filter for updates to this neighbor.
    prefix_list_out: str
    # IPv6 Outbound filter for updates to this neighbor.
    prefix_list_out6: str
    # Outbound filter for VPNv4 updates to this neighbor.
    prefix_list_out_vpnv4: str
    # Outbound filter for VPNv6 updates to this neighbor.
    prefix_list_out_vpnv6: str
    # AS number of neighbor.
    remote_as: str
    # BGP filter for remote AS.
    remote_as_filter: str
    # Local AS number of neighbor.
    local_as: str
    # Do not prepend local-as to incoming updates.
    local_as_no_prepend: Literal["enable", "disable"]
    # Replace real AS with local-as in outgoing updates.
    local_as_replace_as: Literal["enable", "disable"]
    # Time to retain stale routes.
    retain_stale_time: int
    # IPv4 Inbound route map filter.
    route_map_in: str
    # IPv6 Inbound route map filter.
    route_map_in6: str
    # VPNv4 inbound route map filter.
    route_map_in_vpnv4: str
    # VPNv6 inbound route map filter.
    route_map_in_vpnv6: str
    # L2VPN EVPN inbound route map filter.
    route_map_in_evpn: str
    # IPv4 outbound route map filter.
    route_map_out: str
    # IPv4 outbound route map filter if the peer is preferred.
    route_map_out_preferable: str
    # IPv6 Outbound route map filter.
    route_map_out6: str
    # IPv6 outbound route map filter if the peer is preferred.
    route_map_out6_preferable: str
    # VPNv4 outbound route map filter.
    route_map_out_vpnv4: str
    # VPNv6 outbound route map filter.
    route_map_out_vpnv6: str
    # VPNv4 outbound route map filter if the peer is preferred.
    route_map_out_vpnv4_preferable: str
    # VPNv6 outbound route map filter if this neighbor is preferred.
    route_map_out_vpnv6_preferable: str
    # L2VPN EVPN outbound route map filter.
    route_map_out_evpn: str
    # IPv4 Send community attribute to neighbor.
    send_community: Literal["standard", "extended", "both", "disable"]
    # IPv6 Send community attribute to neighbor.
    send_community6: Literal["standard", "extended", "both", "disable"]
    # Send community attribute to neighbor for VPNv4 address family.
    send_community_vpnv4: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to this neighbor for VPNv6 address fa
    send_community_vpnv6: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to neighbor for L2VPN EVPN address fa
    send_community_evpn: Literal["standard", "extended", "both", "disable"]
    # Keep alive timer interval (sec).
    keep_alive_timer: int
    # Interval (sec) before peer considered dead.
    holdtime_timer: int
    # Interval (sec) for connect timer.
    connect_timer: int
    # IPv4 Route map to selectively unsuppress suppressed routes.
    unsuppress_map: str
    # IPv6 Route map to selectively unsuppress suppressed routes.
    unsuppress_map6: str
    # Interface to use as source IP/IPv6 address of TCP connections.
    update_source: str
    # Neighbor weight.
    weight: int
    # Graceful restart delay time (sec, 0 = global default).
    restart_time: int
    # Enable/disable IPv4 additional-path capability.
    additional_path: Literal["send", "receive", "both", "disable"]
    # Enable/disable IPv6 additional-path capability.
    additional_path6: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv4 additional-path capability.
    additional_path_vpnv4: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv6 additional-path capability.
    additional_path_vpnv6: Literal["send", "receive", "both", "disable"]
    # Number of IPv4 additional paths that can be advertised to this neighbor.
    adv_additional_path: int
    # Number of IPv6 additional paths that can be advertised to this neighbor.
    adv_additional_path6: int
    # Number of VPNv4 additional paths that can be advertised to this neighbor.
    adv_additional_path_vpnv4: int
    # Number of VPNv6 additional paths that can be advertised to this neighbor.
    adv_additional_path_vpnv6: int
    # Password used in MD5 authentication.
    password: str
    # Key-chain name for TCP authentication options.
    auth_options: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpNeighborrangeObject:
    """Typed object for neighbor-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor range ID.
    id: int
    # Neighbor range prefix.
    prefix: str
    # Maximum number of neighbors.
    max_neighbor_num: int
    # Neighbor group name.
    neighbor_group: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpNeighborrange6Object:
    """Typed object for neighbor-range6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 neighbor range ID.
    id: int
    # IPv6 prefix.
    prefix6: str
    # Maximum number of neighbors.
    max_neighbor_num: int
    # Neighbor group name.
    neighbor_group: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Network prefix.
    prefix: str
    # Configure insurance of BGP network route existence in IGP.
    network_import_check: Literal["global", "enable", "disable"]
    # Enable/disable route as backdoor.
    backdoor: Literal["enable", "disable"]
    # Route map to modify generated route.
    route_map: str
    # Name of firewall address or address group.
    prefix_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpNetwork6Object:
    """Typed object for network6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Network IPv6 prefix.
    prefix6: str
    # Configure insurance of BGP network route existence in IGP.
    network_import_check: Literal["global", "enable", "disable"]
    # Enable/disable route as backdoor.
    backdoor: Literal["enable", "disable"]
    # Route map to modify generated route.
    route_map: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list entry name.
    name: str
    # Status.
    status: Literal["enable", "disable"]
    # Route map name.
    route_map: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpRedistribute6Object:
    """Typed object for redistribute6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list entry name.
    name: str
    # Status.
    status: Literal["enable", "disable"]
    # Route map name.
    route_map: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpAdmindistanceObject:
    """Typed object for admin-distance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Neighbor address prefix.
    neighbour_prefix: str
    # Access list of routes to apply new distance to.
    route_list: str
    # Administrative distance to apply (1 - 255).
    distance: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpVrfObject:
    """Typed object for vrf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Origin VRF ID <0-511>.
    vrf: str
    # VRF role.
    role: Literal["standalone", "ce", "pe"]
    # Route Distinguisher: AA:NN|A.B.C.D:NN.
    rd: str
    # List of export route target.
    export_rt: str
    # List of import route target.
    import_rt: str
    # Import route map.
    import_route_map: str
    # Target VRF table.
    leak_target: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class BgpVrf6Object:
    """Typed object for vrf6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Origin VRF ID <0-511>.
    vrf: str
    # VRF role.
    role: Literal["standalone", "ce", "pe"]
    # Route Distinguisher: AA:NN|A.B.C.D:NN.
    rd: str
    # List of export route target.
    export_rt: str
    # List of import route target.
    import_rt: str
    # Import route map.
    import_route_map: str
    # Target VRF table.
    leak_target: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class BgpResponse(TypedDict):
    """
    Type hints for router/bgp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    asn: str
    router_id: str
    keepalive_timer: int
    holdtime_timer: int
    always_compare_med: Literal["enable", "disable"]
    bestpath_as_path_ignore: Literal["enable", "disable"]
    bestpath_cmp_confed_aspath: Literal["enable", "disable"]
    bestpath_cmp_routerid: Literal["enable", "disable"]
    bestpath_med_confed: Literal["enable", "disable"]
    bestpath_med_missing_as_worst: Literal["enable", "disable"]
    client_to_client_reflection: Literal["enable", "disable"]
    dampening: Literal["enable", "disable"]
    deterministic_med: Literal["enable", "disable"]
    ebgp_multipath: Literal["enable", "disable"]
    ibgp_multipath: Literal["enable", "disable"]
    enforce_first_as: Literal["enable", "disable"]
    fast_external_failover: Literal["enable", "disable"]
    log_neighbour_changes: Literal["enable", "disable"]
    network_import_check: Literal["enable", "disable"]
    ignore_optional_capability: Literal["enable", "disable"]
    additional_path: Literal["enable", "disable"]
    additional_path6: Literal["enable", "disable"]
    additional_path_vpnv4: Literal["enable", "disable"]
    additional_path_vpnv6: Literal["enable", "disable"]
    multipath_recursive_distance: Literal["enable", "disable"]
    recursive_next_hop: Literal["enable", "disable"]
    recursive_inherit_priority: Literal["enable", "disable"]
    tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"]
    cluster_id: str
    confederation_identifier: int
    confederation_peers: list[dict[str, Any]]
    dampening_route_map: str
    dampening_reachability_half_life: int
    dampening_reuse: int
    dampening_suppress: int
    dampening_max_suppress_time: int
    dampening_unreachability_half_life: int
    default_local_preference: int
    scan_time: int
    distance_external: int
    distance_internal: int
    distance_local: int
    synchronization: Literal["enable", "disable"]
    graceful_restart: Literal["enable", "disable"]
    graceful_restart_time: int
    graceful_stalepath_time: int
    graceful_update_delay: int
    graceful_end_on_timer: Literal["enable", "disable"]
    additional_path_select: int
    additional_path_select6: int
    additional_path_select_vpnv4: int
    additional_path_select_vpnv6: int
    cross_family_conditional_adv: Literal["enable", "disable"]
    aggregate_address: list[dict[str, Any]]
    aggregate_address6: list[dict[str, Any]]
    neighbor: list[dict[str, Any]]
    neighbor_group: list[dict[str, Any]]
    neighbor_range: list[dict[str, Any]]
    neighbor_range6: list[dict[str, Any]]
    network: list[dict[str, Any]]
    network6: list[dict[str, Any]]
    redistribute: list[dict[str, Any]]
    redistribute6: list[dict[str, Any]]
    admin_distance: list[dict[str, Any]]
    vrf: list[dict[str, Any]]
    vrf6: list[dict[str, Any]]


@final
class BgpObject:
    """Typed FortiObject for router/bgp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
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
    confederation_peers: list[BgpConfederationpeersObject]  # Table field - list of typed objects
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
    aggregate_address: list[BgpAggregateaddressObject]  # Table field - list of typed objects
    # BGP IPv6 aggregate address table.
    aggregate_address6: list[BgpAggregateaddress6Object]  # Table field - list of typed objects
    # BGP neighbor table.
    neighbor: list[BgpNeighborObject]  # Table field - list of typed objects
    # BGP neighbor group table.
    neighbor_group: list[BgpNeighborgroupObject]  # Table field - list of typed objects
    # BGP neighbor range table.
    neighbor_range: list[BgpNeighborrangeObject]  # Table field - list of typed objects
    # BGP IPv6 neighbor range table.
    neighbor_range6: list[BgpNeighborrange6Object]  # Table field - list of typed objects
    # BGP network table.
    network: list[BgpNetworkObject]  # Table field - list of typed objects
    # BGP IPv6 network table.
    network6: list[BgpNetwork6Object]  # Table field - list of typed objects
    # BGP IPv4 redistribute table.
    redistribute: list[BgpRedistributeObject]  # Table field - list of typed objects
    # BGP IPv6 redistribute table.
    redistribute6: list[BgpRedistribute6Object]  # Table field - list of typed objects
    # Administrative distance modifications.
    admin_distance: list[BgpAdmindistanceObject]  # Table field - list of typed objects
    # BGP VRF leaking table.
    vrf: list[BgpVrfObject]  # Table field - list of typed objects
    # BGP IPv6 VRF leaking table.
    vrf6: list[BgpVrf6Object]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> BgpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Bgp:
    """
    Configure BGP.
    
    Path: router/bgp
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
    ) -> BgpObject: ...
    
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
    ) -> BgpObject: ...
    
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
    ) -> BgpResponse: ...
    
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
    ) -> BgpResponse: ...
    
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
    ) -> BgpResponse: ...
    
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