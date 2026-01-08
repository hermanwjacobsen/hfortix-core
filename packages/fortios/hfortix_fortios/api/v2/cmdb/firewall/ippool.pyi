from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class IppoolPayload(TypedDict, total=False):
    """
    Type hints for firewall/ippool payload fields.
    
    Configure IPv4 IP pools.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: arp-intf, associated-interface)

    **Usage:**
        payload: IppoolPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IP pool name.
    type: NotRequired[Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"]]  # IP pool type: overload, one-to-one, fixed-port-range, port-b
    startip: str  # First IPv4 address (inclusive) in the range for the address
    endip: str  # Final IPv4 address (inclusive) in the range for the address
    startport: int  # First port number (inclusive) in the range for the address p
    endport: int  # Final port number (inclusive) in the range for the address p
    source_startip: str  # First IPv4 address (inclusive) in the range of the source ad
    source_endip: str  # Final IPv4 address (inclusive) in the range of the source ad
    block_size: int  # Number of addresses in a block (64 - 4096, default = 128).
    port_per_user: int  # Number of port for each user
    num_blocks_per_user: int  # Number of addresses blocks that can be used by a user
    pba_timeout: NotRequired[int]  # Port block allocation timeout (seconds).
    pba_interim_log: NotRequired[int]  # Port block allocation interim logging interval
    permit_any_host: NotRequired[Literal["disable", "enable"]]  # Enable/disable fullcone NAT. Accept UDP packets from any hos
    arp_reply: NotRequired[Literal["disable", "enable"]]  # Enable/disable replying to ARP requests when an IP Pool is a
    arp_intf: NotRequired[str]  # Select an interface from available options that will reply t
    associated_interface: NotRequired[str]  # Associated interface name.
    comments: NotRequired[str]  # Comment.
    nat64: NotRequired[Literal["disable", "enable"]]  # Enable/disable NAT64.
    add_nat64_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable adding NAT64 route.
    source_prefix6: str  # Source IPv6 network to be translated
    client_prefix_length: int  # Subnet length of a single deterministic NAT64 client
    tcp_session_quota: NotRequired[int]  # Maximum number of concurrent TCP sessions allowed per client
    udp_session_quota: NotRequired[int]  # Maximum number of concurrent UDP sessions allowed per client
    icmp_session_quota: NotRequired[int]  # Maximum number of concurrent ICMP sessions allowed per clien
    privileged_port_use_pba: NotRequired[Literal["disable", "enable"]]  # Enable/disable selection of the external port from the port
    subnet_broadcast_in_ippool: NotRequired[Literal["disable"]]  # Enable/disable inclusion of the subnetwork address and broad

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class IppoolResponse(TypedDict):
    """
    Type hints for firewall/ippool API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"]
    startip: str
    endip: str
    startport: int
    endport: int
    source_startip: str
    source_endip: str
    block_size: int
    port_per_user: int
    num_blocks_per_user: int
    pba_timeout: int
    pba_interim_log: int
    permit_any_host: Literal["disable", "enable"]
    arp_reply: Literal["disable", "enable"]
    arp_intf: str
    associated_interface: str
    comments: str
    nat64: Literal["disable", "enable"]
    add_nat64_route: Literal["disable", "enable"]
    source_prefix6: str
    client_prefix_length: int
    tcp_session_quota: int
    udp_session_quota: int
    icmp_session_quota: int
    privileged_port_use_pba: Literal["disable", "enable"]
    subnet_broadcast_in_ippool: Literal["disable"]


@final
class IppoolObject:
    """Typed FortiObject for firewall/ippool with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IP pool name.
    name: str
    # IP pool type: overload, one-to-one, fixed-port-range, port-block-allocation, cgn
    type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"]
    # First IPv4 address (inclusive) in the range for the address pool
    startip: str
    # Final IPv4 address (inclusive) in the range for the address pool
    endip: str
    # First port number (inclusive) in the range for the address pool
    startport: int
    # Final port number (inclusive) in the range for the address pool
    endport: int
    # First IPv4 address (inclusive) in the range of the source addresses to be transl
    source_startip: str
    # Final IPv4 address (inclusive) in the range of the source addresses to be transl
    source_endip: str
    # Number of addresses in a block (64 - 4096, default = 128).
    block_size: int
    # Number of port for each user (32 - 60416, default = 0, which is auto).
    port_per_user: int
    # Number of addresses blocks that can be used by a user (1 to 128, default = 8).
    num_blocks_per_user: int
    # Port block allocation timeout (seconds).
    pba_timeout: int
    # Port block allocation interim logging interval
    pba_interim_log: int
    # Enable/disable fullcone NAT. Accept UDP packets from any host.
    permit_any_host: Literal["disable", "enable"]
    # Enable/disable replying to ARP requests when an IP Pool is added to a policy
    arp_reply: Literal["disable", "enable"]
    # Select an interface from available options that will reply to ARP requests.
    arp_intf: str
    # Associated interface name.
    associated_interface: str
    # Comment.
    comments: str
    # Enable/disable NAT64.
    nat64: Literal["disable", "enable"]
    # Enable/disable adding NAT64 route.
    add_nat64_route: Literal["disable", "enable"]
    # Source IPv6 network to be translated
    source_prefix6: str
    # Subnet length of a single deterministic NAT64 client (1 - 128, default = 64).
    client_prefix_length: int
    # Maximum number of concurrent TCP sessions allowed per client
    tcp_session_quota: int
    # Maximum number of concurrent UDP sessions allowed per client
    udp_session_quota: int
    # Maximum number of concurrent ICMP sessions allowed per client
    icmp_session_quota: int
    # Enable/disable selection of the external port from the port block allocation for
    privileged_port_use_pba: Literal["disable", "enable"]
    # Enable/disable inclusion of the subnetwork address and broadcast IP address in t
    subnet_broadcast_in_ippool: Literal["disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> IppoolPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ippool:
    """
    Configure IPv4 IP pools.
    
    Path: firewall/ippool
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
    ) -> IppoolObject: ...
    
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
    ) -> IppoolObject: ...
    
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
    ) -> list[IppoolObject]: ...
    
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
    ) -> IppoolResponse: ...
    
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
    ) -> IppoolResponse: ...
    
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
    ) -> list[IppoolResponse]: ...
    
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
    ) -> IppoolObject | list[IppoolObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> IppoolObject: ...
    
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> IppoolObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
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
    ) -> IppoolObject: ...
    
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
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
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
    "Ippool",
    "IppoolPayload",
    "IppoolObject",
]