from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class GreTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/gre_tunnel payload fields.
    
    Configure GRE tunnel.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: GreTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Tunnel name.
    interface: NotRequired[str]  # Interface name.
    ip_version: NotRequired[Literal["4", "6"]]  # IP version to use for VPN interface.
    remote_gw6: str  # IPv6 address of the remote gateway.
    local_gw6: str  # IPv6 address of the local gateway.
    remote_gw: str  # IP address of the remote gateway.
    local_gw: str  # IP address of the local gateway.
    use_sdwan: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of SD-WAN to reach remote gateway.
    sequence_number_transmission: NotRequired[Literal["disable", "enable"]]  # Enable/disable including of sequence numbers in transmitted
    sequence_number_reception: NotRequired[Literal["disable", "enable"]]  # Enable/disable validating sequence numbers in received GRE p
    checksum_transmission: NotRequired[Literal["disable", "enable"]]  # Enable/disable including checksums in transmitted GRE packet
    checksum_reception: NotRequired[Literal["disable", "enable"]]  # Enable/disable validating checksums in received GRE packets.
    key_outbound: NotRequired[int]  # Include this key in transmitted GRE packets (0 - 4294967295)
    key_inbound: NotRequired[int]  # Require received GRE packets contain this key
    dscp_copying: NotRequired[Literal["disable", "enable"]]  # Enable/disable DSCP copying.
    diffservcode: NotRequired[str]  # DiffServ setting to be applied to GRE tunnel outer IP header
    keepalive_interval: NotRequired[int]  # Keepalive message interval (0 - 32767, 0 = disabled).
    keepalive_failtimes: NotRequired[int]  # Number of consecutive unreturned keepalive messages before a

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class GreTunnelResponse(TypedDict):
    """
    Type hints for system/gre_tunnel API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    interface: str
    ip_version: Literal["4", "6"]
    remote_gw6: str
    local_gw6: str
    remote_gw: str
    local_gw: str
    use_sdwan: Literal["disable", "enable"]
    sequence_number_transmission: Literal["disable", "enable"]
    sequence_number_reception: Literal["disable", "enable"]
    checksum_transmission: Literal["disable", "enable"]
    checksum_reception: Literal["disable", "enable"]
    key_outbound: int
    key_inbound: int
    dscp_copying: Literal["disable", "enable"]
    diffservcode: str
    keepalive_interval: int
    keepalive_failtimes: int


@final
class GreTunnelObject:
    """Typed FortiObject for system/gre_tunnel with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tunnel name.
    name: str
    # Interface name.
    interface: str
    # IP version to use for VPN interface.
    ip_version: Literal["4", "6"]
    # IPv6 address of the remote gateway.
    remote_gw6: str
    # IPv6 address of the local gateway.
    local_gw6: str
    # IP address of the remote gateway.
    remote_gw: str
    # IP address of the local gateway.
    local_gw: str
    # Enable/disable use of SD-WAN to reach remote gateway.
    use_sdwan: Literal["disable", "enable"]
    # Enable/disable including of sequence numbers in transmitted GRE packets.
    sequence_number_transmission: Literal["disable", "enable"]
    # Enable/disable validating sequence numbers in received GRE packets.
    sequence_number_reception: Literal["disable", "enable"]
    # Enable/disable including checksums in transmitted GRE packets.
    checksum_transmission: Literal["disable", "enable"]
    # Enable/disable validating checksums in received GRE packets.
    checksum_reception: Literal["disable", "enable"]
    # Include this key in transmitted GRE packets (0 - 4294967295).
    key_outbound: int
    # Require received GRE packets contain this key (0 - 4294967295).
    key_inbound: int
    # Enable/disable DSCP copying.
    dscp_copying: Literal["disable", "enable"]
    # DiffServ setting to be applied to GRE tunnel outer IP header.
    diffservcode: str
    # Keepalive message interval (0 - 32767, 0 = disabled).
    keepalive_interval: int
    # Number of consecutive unreturned keepalive messages before a GRE connection is c
    keepalive_failtimes: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GreTunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class GreTunnel:
    """
    Configure GRE tunnel.
    
    Path: system/gre_tunnel
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
    ) -> GreTunnelObject: ...
    
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
    ) -> GreTunnelObject: ...
    
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
    ) -> list[GreTunnelObject]: ...
    
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
    ) -> GreTunnelResponse: ...
    
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
    ) -> GreTunnelResponse: ...
    
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
    ) -> list[GreTunnelResponse]: ...
    
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
    ) -> GreTunnelObject | list[GreTunnelObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GreTunnelObject: ...
    
    @overload
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GreTunnelObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
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
    ) -> GreTunnelObject: ...
    
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
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
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
    "GreTunnel",
    "GreTunnelPayload",
    "GreTunnelObject",
]