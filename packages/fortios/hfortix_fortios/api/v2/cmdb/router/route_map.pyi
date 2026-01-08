from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class RouteMapPayload(TypedDict, total=False):
    """
    Type hints for router/route_map payload fields.
    
    Configure route maps.
    
    **Usage:**
        payload: RouteMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    comments: NotRequired[str]  # Optional comments.
    rule: NotRequired[list[dict[str, Any]]]  # Rule.

# Nested classes for table field children

@final
class RouteMapRuleObject:
    """Typed object for rule table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Rule ID.
    id: int
    # Action.
    action: Literal["permit", "deny"]
    # Match BGP AS path list.
    match_as_path: str
    # Match BGP community list.
    match_community: str
    # Match BGP extended community list.
    match_extcommunity: str
    # Enable/disable exact matching of communities.
    match_community_exact: Literal["enable", "disable"]
    # Enable/disable exact matching of extended communities.
    match_extcommunity_exact: Literal["enable", "disable"]
    # Match BGP origin code.
    match_origin: Literal["none", "egp", "igp", "incomplete"]
    # Match interface configuration.
    match_interface: str
    # Match IP address permitted by access-list or prefix-list.
    match_ip_address: str
    # Match IPv6 address permitted by access-list6 or prefix-list6.
    match_ip6_address: str
    # Match next hop IP address passed by access-list or prefix-list.
    match_ip_nexthop: str
    # Match next hop IPv6 address passed by access-list6 or prefix-list6.
    match_ip6_nexthop: str
    # Match metric for redistribute routes.
    match_metric: int
    # Match route type.
    match_route_type: Literal["external-type1", "external-type2", "none"]
    # Match tag.
    match_tag: int
    # Match VRF ID.
    match_vrf: int
    # Enable/disable matching of suppressed original neighbor.
    match_suppress: Literal["enable", "disable"]
    # BGP aggregator AS.
    set_aggregator_as: int
    # BGP aggregator IP.
    set_aggregator_ip: str
    # Specify preferred action of set-aspath.
    set_aspath_action: Literal["prepend", "replace"]
    # Prepend BGP AS path attribute.
    set_aspath: str
    # Enable/disable BGP atomic aggregate attribute.
    set_atomic_aggregate: Literal["enable", "disable"]
    # Delete communities matching community list.
    set_community_delete: str
    # BGP community attribute.
    set_community: str
    # Enable/disable adding set-community to existing community.
    set_community_additive: Literal["enable", "disable"]
    # Reachability half-life time for the penalty (1 - 45 min, 0 = unset).
    set_dampening_reachability_half_life: int
    # Value to start reusing a route (1 - 20000, 0 = unset).
    set_dampening_reuse: int
    # Value to start suppressing a route (1 - 20000, 0 = unset).
    set_dampening_suppress: int
    # Maximum duration to suppress a route (1 - 255 min, 0 = unset).
    set_dampening_max_suppress: int
    # Unreachability Half-life time for the penalty (1 - 45 min, 0 = unset).
    set_dampening_unreachability_half_life: int
    # Route Target extended community.
    set_extcommunity_rt: str
    # Site-of-Origin extended community.
    set_extcommunity_soo: str
    # IP address of next hop.
    set_ip_nexthop: str
    # IP address of preferred source.
    set_ip_prefsrc: str
    # IP address of VPNv4 next-hop.
    set_vpnv4_nexthop: str
    # IPv6 global address of next hop.
    set_ip6_nexthop: str
    # IPv6 local address of next hop.
    set_ip6_nexthop_local: str
    # IPv6 global address of VPNv6 next-hop.
    set_vpnv6_nexthop: str
    # IPv6 link-local address of VPNv6 next-hop.
    set_vpnv6_nexthop_local: str
    # BGP local preference path attribute.
    set_local_preference: int
    # Metric value.
    set_metric: int
    # Metric type.
    set_metric_type: Literal["external-type1", "external-type2", "none"]
    # BGP originator ID attribute.
    set_originator_id: str
    # BGP origin code.
    set_origin: Literal["none", "egp", "igp", "incomplete"]
    # Tag value.
    set_tag: int
    # BGP weight for routing table.
    set_weight: int
    # Route tag for routing table.
    set_route_tag: int
    # Priority for routing table.
    set_priority: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class RouteMapResponse(TypedDict):
    """
    Type hints for router/route_map API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comments: str
    rule: list[dict[str, Any]]


@final
class RouteMapObject:
    """Typed FortiObject for router/route_map with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # Optional comments.
    comments: str
    # Rule.
    rule: list[RouteMapRuleObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RouteMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class RouteMap:
    """
    Configure route maps.
    
    Path: router/route_map
    Category: cmdb
    Primary Key: name
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
    ) -> RouteMapObject: ...
    
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
    ) -> RouteMapObject: ...
    
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
    ) -> list[RouteMapObject]: ...
    
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
    ) -> RouteMapResponse: ...
    
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
    ) -> RouteMapResponse: ...
    
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
    ) -> list[RouteMapResponse]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
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
    ) -> RouteMapObject | list[RouteMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RouteMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RouteMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RouteMapObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "RouteMap",
    "RouteMapPayload",
    "RouteMapObject",
]