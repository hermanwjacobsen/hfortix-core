from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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
    name: NotRequired[str]  # Public cloud VPN name.
    sdn: str  # SDN connector name.
    remote_type: Literal["vgw", "tgw"]  # Type of remote device.
    routing_type: Literal["static", "dynamic"]  # Type of routing.
    vgw_id: str  # Virtual private gateway id.
    tgw_id: str  # Transit gateway id.
    subnet_id: NotRequired[str]  # AWS subnet id for TGW route propagation.
    bgp_as: int  # BGP Router AS number.
    cgw_gateway: str  # Public IP address of the customer gateway.
    nat_traversal: NotRequired[Literal["disable", "enable"]]  # Enable/disable use for NAT traversal. Please enable if your
    tunnel_interface: str  # Tunnel interface with public IP.
    internal_interface: str  # Internal interface with local subnet.
    local_cidr: str  # Local subnet address and subnet mask.
    remote_cidr: str  # Remote subnet address and subnet mask.
    cgw_name: NotRequired[str]  # AWS customer gateway name to be created.
    psksecret: NotRequired[str]  # Pre-shared secret for PSK authentication. Auto-generated if
    type: NotRequired[int]  # SDN VPN type.
    status: NotRequired[int]  # SDN VPN status.
    code: NotRequired[int]  # SDN VPN error code.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SdnVpnResponse(TypedDict):
    """
    Type hints for system/sdn_vpn API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    sdn: str
    remote_type: Literal["vgw", "tgw"]
    routing_type: Literal["static", "dynamic"]
    vgw_id: str
    tgw_id: str
    subnet_id: str
    bgp_as: int
    cgw_gateway: str
    nat_traversal: Literal["disable", "enable"]
    tunnel_interface: str
    internal_interface: str
    local_cidr: str
    remote_cidr: str
    cgw_name: str
    psksecret: str
    type: int
    status: int
    code: int


@final
class SdnVpnObject:
    """Typed FortiObject for system/sdn_vpn with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Public cloud VPN name.
    name: str
    # SDN connector name.
    sdn: str
    # Type of remote device.
    remote_type: Literal["vgw", "tgw"]
    # Type of routing.
    routing_type: Literal["static", "dynamic"]
    # Virtual private gateway id.
    vgw_id: str
    # Transit gateway id.
    tgw_id: str
    # AWS subnet id for TGW route propagation.
    subnet_id: str
    # BGP Router AS number.
    bgp_as: int
    # Public IP address of the customer gateway.
    cgw_gateway: str
    # Enable/disable use for NAT traversal. Please enable if your FortiGate device is
    nat_traversal: Literal["disable", "enable"]
    # Tunnel interface with public IP.
    tunnel_interface: str
    # Internal interface with local subnet.
    internal_interface: str
    # Local subnet address and subnet mask.
    local_cidr: str
    # Remote subnet address and subnet mask.
    remote_cidr: str
    # AWS customer gateway name to be created.
    cgw_name: str
    # Pre-shared secret for PSK authentication. Auto-generated if not specified
    psksecret: str
    # SDN VPN type.
    type: int
    # SDN VPN status.
    status: int
    # SDN VPN error code.
    code: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SdnVpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SdnVpn:
    """
    Configure public cloud VPN service.
    
    Path: system/sdn_vpn
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
    ) -> SdnVpnObject: ...
    
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
    ) -> SdnVpnObject: ...
    
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
    ) -> list[SdnVpnObject]: ...
    
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
    ) -> SdnVpnResponse: ...
    
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
    ) -> SdnVpnResponse: ...
    
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
    ) -> list[SdnVpnResponse]: ...
    
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
    ) -> SdnVpnObject | list[SdnVpnObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
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
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    ) -> SdnVpnObject: ...
    
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
    "SdnVpn",
    "SdnVpnPayload",
    "SdnVpnObject",
]