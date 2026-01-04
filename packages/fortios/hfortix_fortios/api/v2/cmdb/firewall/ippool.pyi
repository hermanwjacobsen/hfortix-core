from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IppoolPayload(TypedDict, total=False):
    """
    Type hints for firewall/ippool payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    port_per_user: int  # Number of port for each user (32 - 60416, default = 0, which
    num_blocks_per_user: int  # Number of addresses blocks that can be used by a user (1 to 
    pba_timeout: NotRequired[int]  # Port block allocation timeout (seconds).
    pba_interim_log: NotRequired[int]  # Port block allocation interim logging interval (600 - 86400 
    permit_any_host: NotRequired[Literal["disable", "enable"]]  # Enable/disable full cone NAT.
    arp_reply: NotRequired[Literal["disable", "enable"]]  # Enable/disable replying to ARP requests when an IP Pool is a
    arp_intf: NotRequired[str]  # Select an interface from available options that will reply t
    associated_interface: NotRequired[str]  # Associated interface name.
    comments: NotRequired[str]  # Comment.
    nat64: NotRequired[Literal["disable", "enable"]]  # Enable/disable NAT64.
    add_nat64_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable adding NAT64 route.
    source_prefix6: str  # Source IPv6 network to be translated (format = xxxx:xxxx:xxx
    client_prefix_length: int  # Subnet length of a single deterministic NAT64 client (1 - 12
    tcp_session_quota: NotRequired[int]  # Maximum number of concurrent TCP sessions allowed per client
    udp_session_quota: NotRequired[int]  # Maximum number of concurrent UDP sessions allowed per client
    icmp_session_quota: NotRequired[int]  # Maximum number of concurrent ICMP sessions allowed per clien
    privileged_port_use_pba: NotRequired[Literal["disable", "enable"]]  # Enable/disable selection of the external port from the port 
    subnet_broadcast_in_ippool: NotRequired[Literal["disable"]]  # Enable/disable inclusion of the subnetwork address and broad


class Ippool:
    """
    Configure IPv4 IP pools.
    
    Path: firewall/ippool
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: IppoolPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
]