from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class DnsPayload(TypedDict, total=False):
    """
    Type hints for system/dns payload fields.
    
    Configure DNS.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: ssl-certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)

    **Usage:**
        payload: DnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    primary: str  # Primary DNS server IP address.
    secondary: NotRequired[str]  # Secondary DNS server IP address.
    protocol: NotRequired[Literal["cleartext", "dot", "doh"]]  # DNS transport protocols.
    ssl_certificate: NotRequired[str]  # Name of local certificate for SSL connections.
    server_hostname: NotRequired[list[dict[str, Any]]]  # DNS server host name list.
    domain: NotRequired[list[dict[str, Any]]]  # Search suffix list for hostname lookup.
    ip6_primary: NotRequired[str]  # Primary DNS server IPv6 address.
    ip6_secondary: NotRequired[str]  # Secondary DNS server IPv6 address.
    timeout: NotRequired[int]  # DNS query timeout interval in seconds (1 - 10).
    retry: NotRequired[int]  # Number of times to retry (0 - 5).
    dns_cache_limit: NotRequired[int]  # Maximum number of records in the DNS cache.
    dns_cache_ttl: NotRequired[int]  # Duration in seconds that the DNS cache retains information.
    cache_notfound_responses: NotRequired[Literal["disable", "enable"]]  # Enable/disable response from the DNS server when a record is
    source_ip: NotRequired[str]  # IP address used by the DNS server as its source IP.
    source_ip_interface: NotRequired[str]  # IP address of the specified interface as the source IP addre
    root_servers: NotRequired[list[dict[str, Any]]]  # Configure up to two preferred servers that serve the DNS roo
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    server_select_method: NotRequired[Literal["least-rtt", "failover"]]  # Specify how configured servers are prioritized.
    alt_primary: NotRequired[str]  # Alternate primary DNS server. This is not used as a failover
    alt_secondary: NotRequired[str]  # Alternate secondary DNS server. This is not used as a failov
    log: NotRequired[Literal["disable", "error", "all"]]  # Local DNS log setting.
    fqdn_cache_ttl: NotRequired[int]  # FQDN cache time to live in seconds (0 - 86400, default = 0).
    fqdn_max_refresh: NotRequired[int]  # FQDN cache maximum refresh time in seconds (3600 - 86400, de
    fqdn_min_refresh: NotRequired[int]  # FQDN cache minimum refresh time in seconds (10 - 3600, defau
    hostname_ttl: NotRequired[int]  # TTL of hostname table entries (60 - 86400).
    hostname_limit: NotRequired[int]  # Limit of the number of hostname table entries (0 - 50000).


class DnsObject(FortiObject[DnsPayload]):
    """Typed FortiObject for system/dns with IDE autocomplete support."""
    
    # Primary DNS server IP address.
    primary: str
    # Secondary DNS server IP address.
    secondary: str
    # DNS transport protocols.
    protocol: Literal["cleartext", "dot", "doh"]
    # Name of local certificate for SSL connections.
    ssl_certificate: str
    # DNS server host name list.
    server_hostname: list[str]  # Auto-flattened from member_table
    # Search suffix list for hostname lookup.
    domain: list[str]  # Auto-flattened from member_table
    # Primary DNS server IPv6 address.
    ip6_primary: str
    # Secondary DNS server IPv6 address.
    ip6_secondary: str
    # DNS query timeout interval in seconds (1 - 10).
    timeout: int
    # Number of times to retry (0 - 5).
    retry: int
    # Maximum number of records in the DNS cache.
    dns_cache_limit: int
    # Duration in seconds that the DNS cache retains information.
    dns_cache_ttl: int
    # Enable/disable response from the DNS server when a record is not in cache.
    cache_notfound_responses: Literal["disable", "enable"]
    # IP address used by the DNS server as its source IP.
    source_ip: str
    # IP address of the specified interface as the source IP address.
    source_ip_interface: str
    # Configure up to two preferred servers that serve the DNS root zone (default uses
    root_servers: list[str]  # Auto-flattened from member_table
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
    # Local DNS log setting.
    log: Literal["disable", "error", "all"]
    # FQDN cache time to live in seconds (0 - 86400, default = 0).
    fqdn_cache_ttl: int
    # FQDN cache maximum refresh time in seconds (3600 - 86400, default = 3600).
    fqdn_max_refresh: int
    # FQDN cache minimum refresh time in seconds (10 - 3600, default = 60).
    fqdn_min_refresh: int
    # TTL of hostname table entries (60 - 86400).
    hostname_ttl: int
    # Limit of the number of hostname table entries (0 - 50000).
    hostname_limit: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DnsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Dns:
    """
    Configure DNS.
    
    Path: system/dns
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DnsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
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
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
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
    "Dns",
    "DnsPayload",
    "DnsObject",
]