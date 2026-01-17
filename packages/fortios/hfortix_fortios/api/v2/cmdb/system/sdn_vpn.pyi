from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SdnVpnPayload(TypedDict, total=False):
    """
    Type hints for system/sdn_vpn payload fields.
    
    Configure public cloud VPN service.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: internal-interface, tunnel-interface)
        - :class:`~.system.sdn-connector.SdnConnectorEndpoint` (via: sdn)

    **Usage:**
        payload: SdnVpnPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Public cloud VPN name. | MaxLen: 35
    sdn: str  # SDN connector name. | MaxLen: 35
    remote_type: Literal["vgw", "tgw"]  # Type of remote device. | Default: vgw
    routing_type: Literal["static", "dynamic"]  # Type of routing. | Default: dynamic
    vgw_id: str  # Virtual private gateway id. | MaxLen: 63
    tgw_id: str  # Transit gateway id. | MaxLen: 63
    subnet_id: str  # AWS subnet id for TGW route propagation. | MaxLen: 63
    bgp_as: int  # BGP Router AS number. | Default: 65000 | Min: 1 | Max: 4294967295
    cgw_gateway: str  # Public IP address of the customer gateway. | Default: 0.0.0.0
    nat_traversal: Literal["disable", "enable"]  # Enable/disable use for NAT traversal. Please enabl | Default: enable
    tunnel_interface: str  # Tunnel interface with public IP. | MaxLen: 15
    internal_interface: str  # Internal interface with local subnet. | MaxLen: 15
    local_cidr: str  # Local subnet address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    remote_cidr: str  # Remote subnet address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    cgw_name: str  # AWS customer gateway name to be created. | MaxLen: 35
    psksecret: str  # Pre-shared secret for PSK authentication. Auto-gen
    type: int  # SDN VPN type. | Default: 0 | Min: 0 | Max: 65535
    status: int  # SDN VPN status. | Default: 0 | Min: 0 | Max: 255
    code: int  # SDN VPN error code. | Default: 0 | Min: 0 | Max: 255

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class SdnVpnResponse(TypedDict):
    """
    Type hints for system/sdn_vpn API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Public cloud VPN name. | MaxLen: 35
    sdn: str  # SDN connector name. | MaxLen: 35
    remote_type: Literal["vgw", "tgw"]  # Type of remote device. | Default: vgw
    routing_type: Literal["static", "dynamic"]  # Type of routing. | Default: dynamic
    vgw_id: str  # Virtual private gateway id. | MaxLen: 63
    tgw_id: str  # Transit gateway id. | MaxLen: 63
    subnet_id: str  # AWS subnet id for TGW route propagation. | MaxLen: 63
    bgp_as: int  # BGP Router AS number. | Default: 65000 | Min: 1 | Max: 4294967295
    cgw_gateway: str  # Public IP address of the customer gateway. | Default: 0.0.0.0
    nat_traversal: Literal["disable", "enable"]  # Enable/disable use for NAT traversal. Please enabl | Default: enable
    tunnel_interface: str  # Tunnel interface with public IP. | MaxLen: 15
    internal_interface: str  # Internal interface with local subnet. | MaxLen: 15
    local_cidr: str  # Local subnet address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    remote_cidr: str  # Remote subnet address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    cgw_name: str  # AWS customer gateway name to be created. | MaxLen: 35
    psksecret: str  # Pre-shared secret for PSK authentication. Auto-gen
    type: int  # SDN VPN type. | Default: 0 | Min: 0 | Max: 65535
    status: int  # SDN VPN status. | Default: 0 | Min: 0 | Max: 255
    code: int  # SDN VPN error code. | Default: 0 | Min: 0 | Max: 255


@final
class SdnVpnObject:
    """Typed FortiObject for system/sdn_vpn with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Public cloud VPN name. | MaxLen: 35
    name: str
    # SDN connector name. | MaxLen: 35
    sdn: str
    # Type of remote device. | Default: vgw
    remote_type: Literal["vgw", "tgw"]
    # Type of routing. | Default: dynamic
    routing_type: Literal["static", "dynamic"]
    # Virtual private gateway id. | MaxLen: 63
    vgw_id: str
    # Transit gateway id. | MaxLen: 63
    tgw_id: str
    # AWS subnet id for TGW route propagation. | MaxLen: 63
    subnet_id: str
    # BGP Router AS number. | Default: 65000 | Min: 1 | Max: 4294967295
    bgp_as: int
    # Public IP address of the customer gateway. | Default: 0.0.0.0
    cgw_gateway: str
    # Enable/disable use for NAT traversal. Please enable if your | Default: enable
    nat_traversal: Literal["disable", "enable"]
    # Tunnel interface with public IP. | MaxLen: 15
    tunnel_interface: str
    # Internal interface with local subnet. | MaxLen: 15
    internal_interface: str
    # Local subnet address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    local_cidr: str
    # Remote subnet address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    remote_cidr: str
    # AWS customer gateway name to be created. | MaxLen: 35
    cgw_name: str
    # Pre-shared secret for PSK authentication. Auto-generated if
    psksecret: str
    # SDN VPN type. | Default: 0 | Min: 0 | Max: 65535
    type: int
    # SDN VPN status. | Default: 0 | Min: 0 | Max: 255
    status: int
    # SDN VPN error code. | Default: 0 | Min: 0 | Max: 255
    code: int
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SdnVpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SdnVpn:
    """
    Configure public cloud VPN service.
    
    Path: system/sdn_vpn
    Category: cmdb
    Primary Key: name
    """
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client.
        
        Args:
            client: HTTP client instance for API communication
        """
        ...
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
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
    ) -> SdnVpnObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
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
    ) -> SdnVpnObject: ...
    
    # Without mkey -> returns list of FortiObjects
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
    ) -> FortiObjectList[SdnVpnObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
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
    ) -> SdnVpnObject: ...
    
    # With mkey as keyword arg -> returns single object
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
    ) -> SdnVpnObject: ...
    
    # With no mkey -> returns list of objects
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
    ) -> FortiObjectList[SdnVpnObject]: ...
    
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
    ) -> SdnVpnObject: ...
    
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
    ) -> SdnVpnObject: ...
    
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
    ) -> FortiObjectList[SdnVpnObject]: ...
    
    # Fallback overload for all other cases
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
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
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
    ) -> SdnVpnObject | list[SdnVpnObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> SdnVpnObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> SdnVpnObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
    ) -> SdnVpnObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SdnVpnPayload | None = ...,
        name: str | None = ...,
        sdn: str | None = ...,
        remote_type: Literal["vgw", "tgw"] | None = ...,
        routing_type: Literal["static", "dynamic"] | None = ...,
        vgw_id: str | None = ...,
        tgw_id: str | None = ...,
        subnet_id: str | None = ...,
        bgp_as: int | None = ...,
        cgw_gateway: str | None = ...,
        nat_traversal: Literal["disable", "enable"] | None = ...,
        tunnel_interface: str | None = ...,
        internal_interface: str | None = ...,
        local_cidr: str | None = ...,
        remote_cidr: str | None = ...,
        cgw_name: str | None = ...,
        psksecret: str | None = ...,
        type: int | None = ...,
        status: int | None = ...,
        code: int | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "SdnVpn",
    "SdnVpnPayload",
    "SdnVpnResponse",
    "SdnVpnObject",
]