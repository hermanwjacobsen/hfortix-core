from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class VdomDnsPayload(TypedDict, total=False):
    """
    Type hints for system/vdom_dns payload fields.
    
    Configure DNS servers for a non-management VDOM.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: ssl-certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)

    **Usage:**
        payload: VdomDnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    vdom_dns: NotRequired[Literal["enable", "disable"]]  # Enable/disable configuring DNS servers for the current VDOM.
    primary: str  # Primary DNS server IP address for the VDOM.
    secondary: NotRequired[str]  # Secondary DNS server IP address for the VDOM.
    protocol: NotRequired[Literal["cleartext", "dot", "doh"]]  # DNS transport protocols.
    ssl_certificate: NotRequired[str]  # Name of local certificate for SSL connections.
    server_hostname: NotRequired[list[dict[str, Any]]]  # DNS server host name list.
    ip6_primary: NotRequired[str]  # Primary IPv6 DNS server IP address for the VDOM.
    ip6_secondary: NotRequired[str]  # Secondary IPv6 DNS server IP address for the VDOM.
    source_ip: NotRequired[str]  # Source IP for communications with the DNS server.
    source_ip_interface: NotRequired[str]  # IP address of the specified interface as the source IP addre
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    server_select_method: NotRequired[Literal["least-rtt", "failover"]]  # Specify how configured servers are prioritized.
    alt_primary: NotRequired[str]  # Alternate primary DNS server. This is not used as a failover
    alt_secondary: NotRequired[str]  # Alternate secondary DNS server. This is not used as a failov


class VdomDnsObject(FortiObject[VdomDnsPayload]):
    """Typed FortiObject for system/vdom_dns with IDE autocomplete support."""
    
    # Enable/disable configuring DNS servers for the current VDOM.
    vdom_dns: Literal["enable", "disable"]
    # Primary DNS server IP address for the VDOM.
    primary: str
    # Secondary DNS server IP address for the VDOM.
    secondary: str
    # DNS transport protocols.
    protocol: Literal["cleartext", "dot", "doh"]
    # Name of local certificate for SSL connections.
    ssl_certificate: str
    # DNS server host name list.
    server_hostname: list[str]  # Auto-flattened from member_table
    # Primary IPv6 DNS server IP address for the VDOM.
    ip6_primary: str
    # Secondary IPv6 DNS server IP address for the VDOM.
    ip6_secondary: str
    # Source IP for communications with the DNS server.
    source_ip: str
    # IP address of the specified interface as the source IP address.
    source_ip_interface: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    # Specify how configured servers are prioritized.
    server_select_method: Literal["least-rtt", "failover"]
    # Alternate primary DNS server. This is not used as a failover DNS server.
    alt_primary: str
    # Alternate secondary DNS server. This is not used as a failover DNS server.
    alt_secondary: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VdomDnsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class VdomDns:
    """
    Configure DNS servers for a non-management VDOM.
    
    Path: system/vdom_dns
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
    ) -> VdomDnsObject: ...
    
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
    ) -> VdomDnsObject: ...
    
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
    ) -> VdomDnsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VdomDnsPayload | None = ...,
        vdom_dns: Literal["enable", "disable"] | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VdomDnsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomDnsPayload | None = ...,
        vdom_dns: Literal["enable", "disable"] | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomDnsPayload | None = ...,
        vdom_dns: Literal["enable", "disable"] | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VdomDnsPayload | None = ...,
        vdom_dns: Literal["enable", "disable"] | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
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
        payload_dict: VdomDnsPayload | None = ...,
        vdom_dns: Literal["enable", "disable"] | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
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
    "VdomDns",
    "VdomDnsPayload",
    "VdomDnsObject",
]