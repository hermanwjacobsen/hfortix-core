from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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


class FabricVpnObject(FortiObject[FabricVpnPayload]):
    """Typed FortiObject for system/fabric_vpn with IDE autocomplete support."""
    
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
    overlays: list[str]  # Auto-flattened from member_table
    # Local advertised subnets.
    advertised_subnets: list[str]  # Auto-flattened from member_table
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
    health_checks: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FabricVpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FabricVpn:
    """
    Setup for self orchestrated fabric auto discovery VPN.
    
    Path: system/fabric_vpn
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
    ) -> FabricVpnObject: ...
    
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
        health_checks: str | list[str] | list[dict[str, Any]] | None = ...,
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
        health_checks: str | list[str] | list[dict[str, Any]] | None = ...,
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
        health_checks: str | list[str] | list[dict[str, Any]] | None = ...,
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
        health_checks: str | list[str] | list[dict[str, Any]] | None = ...,
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
        health_checks: str | list[str] | list[dict[str, Any]] | None = ...,
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