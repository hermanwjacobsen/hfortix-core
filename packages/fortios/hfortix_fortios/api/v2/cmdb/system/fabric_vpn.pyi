from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class FabricVpnPayload(TypedDict, total=False):
    """
    Type hints for system/fabric_vpn payload fields.
    
    Setup for self orchestrated fabric auto discovery VPN.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.fabric-vpn.advertised-subnets.AdvertisedSubnetsEndpoint` (via: loopback-advertised-subnet)
        - :class:`~.system.interface.InterfaceEndpoint` (via: loopback-interface)
        - :class:`~.system.sdwan.health-check.HealthCheckEndpoint` (via: health-checks)
        - :class:`~.system.sdwan.zone.ZoneEndpoint` (via: sdwan-zone)

    **Usage:**
        payload: FabricVpnPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable Fabric VPN.
    sync_mode: Literal["enable", "disable"]  # Setting synchronized by fabric or manual.
    branch_name: NotRequired[str]  # Branch name.
    policy_rule: NotRequired[Literal["health-check", "manual", "auto"]]  # Policy creation rule.
    vpn_role: Literal["hub", "spoke"]  # Fabric VPN role.
    overlays: NotRequired[list[dict[str, Any]]]  # Local overlay interfaces table.
    advertised_subnets: NotRequired[list[dict[str, Any]]]  # Local advertised subnets.
    loopback_address_block: str  # IPv4 address and subnet mask for hub's loopback address, syn
    loopback_interface: NotRequired[str]  # Loopback interface.
    loopback_advertised_subnet: NotRequired[int]  # Loopback advertised subnet reference.
    psksecret: str  # Pre-shared secret for ADVPN.
    bgp_as: str  # BGP Router AS number, asplain/asdot/asdot+ format.
    sdwan_zone: NotRequired[str]  # Reference to created SD-WAN zone.
    health_checks: NotRequired[list[dict[str, Any]]]  # Underlying health checks.

# Nested classes for table field children

@final
class FabricVpnOverlaysObject:
    """Typed object for overlays table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Overlay name.
    name: str
    # VPN gateway network ID.
    ipsec_network_id: int
    # IPv4 address and subnet mask for the overlay tunnel , syntax: X.X.X.X/24.
    overlay_tunnel_block: str
    # IP address of the hub gateway (Set by hub).
    remote_gw: str
    # Underlying interface name.
    interface: str
    # Underlying BGP neighbor entry.
    bgp_neighbor: str
    # The overlay policy to allow ADVPN thru traffic.
    overlay_policy: int
    # Underlying BGP network.
    bgp_network: int
    # Underlying router policy.
    route_policy: int
    # Underlying BGP neighbor group entry.
    bgp_neighbor_group: str
    # Underlying BGP neighbor range entry.
    bgp_neighbor_range: int
    # IPsec interface.
    ipsec_phase1: str
    # Reference to SD-WAN member entry.
    sdwan_member: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class FabricVpnAdvertisedsubnetsObject:
    """Typed object for advertised-subnets table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Network prefix.
    prefix: str
    # Access policy direction.
    access: Literal["inbound", "bidirectional"]
    # Underlying BGP network.
    bgp_network: int
    # Underlying firewall address.
    firewall_address: str
    # Underlying policies.
    policies: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class FabricVpnResponse(TypedDict):
    """
    Type hints for system/fabric_vpn API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    sync_mode: Literal["enable", "disable"]
    branch_name: str
    policy_rule: Literal["health-check", "manual", "auto"]
    vpn_role: Literal["hub", "spoke"]
    overlays: list[dict[str, Any]]
    advertised_subnets: list[dict[str, Any]]
    loopback_address_block: str
    loopback_interface: str
    loopback_advertised_subnet: int
    psksecret: str
    bgp_as: str
    sdwan_zone: str
    health_checks: list[dict[str, Any]]


@final
class FabricVpnObject:
    """Typed FortiObject for system/fabric_vpn with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable Fabric VPN.
    status: Literal["enable", "disable"]
    # Setting synchronized by fabric or manual.
    sync_mode: Literal["enable", "disable"]
    # Branch name.
    branch_name: str
    # Policy creation rule.
    policy_rule: Literal["health-check", "manual", "auto"]
    # Fabric VPN role.
    vpn_role: Literal["hub", "spoke"]
    # Local overlay interfaces table.
    overlays: list[FabricVpnOverlaysObject]  # Table field - list of typed objects
    # Local advertised subnets.
    advertised_subnets: list[FabricVpnAdvertisedsubnetsObject]  # Table field - list of typed objects
    # IPv4 address and subnet mask for hub's loopback address, syntax: X.X.X.X/24.
    loopback_address_block: str
    # Loopback interface.
    loopback_interface: str
    # Loopback advertised subnet reference.
    loopback_advertised_subnet: int
    # Pre-shared secret for ADVPN.
    psksecret: str
    # BGP Router AS number, asplain/asdot/asdot+ format.
    bgp_as: str
    # Reference to created SD-WAN zone.
    sdwan_zone: str
    # Underlying health checks.
    health_checks: list[dict[str, Any]]  # Multi-value field
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FabricVpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class FabricVpn:
    """
    Setup for self orchestrated fabric auto discovery VPN.
    
    Path: system/fabric_vpn
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnResponse: ...
    
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
    ) -> FabricVpnResponse: ...
    
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
    ) -> FabricVpnResponse: ...
    
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
    ) -> FabricVpnObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FabricVpnObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
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
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
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
    "FabricVpn",
    "FabricVpnPayload",
    "FabricVpnObject",
]