from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class DnsDatabasePayload(TypedDict, total=False):
    """
    Type hints for system/dns_database payload fields.
    
    Configure DNS databases.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)

    **Usage:**
        payload: DnsDatabasePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Zone name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this DNS zone.
    domain: str  # Domain name.
    allow_transfer: NotRequired[list[dict[str, Any]]]  # DNS zone transfer IP address list.
    type: Literal["primary", "secondary"]  # Zone type
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]  # Zone view
    ip_primary: NotRequired[str]  # IP address of primary DNS server. Entries in this primary DN
    primary_name: NotRequired[str]  # Domain name of the default DNS server for this zone.
    contact: NotRequired[str]  # Email address of the administrator for this zone. You can sp
    ttl: int  # Default time-to-live value for the entries of this DNS zone
    authoritative: Literal["enable", "disable"]  # Enable/disable authoritative zone.
    forwarder: NotRequired[list[dict[str, Any]]]  # DNS zone forwarder IP address list.
    forwarder6: NotRequired[str]  # Forwarder IPv6 address.
    source_ip: NotRequired[str]  # Source IP for forwarding to DNS server.
    source_ip6: NotRequired[str]  # IPv6 source IP address for forwarding to DNS server.
    source_ip_interface: NotRequired[str]  # IP address of the specified interface as the source IP addre
    rr_max: NotRequired[int]  # Maximum number of resource records
    dns_entry: list[dict[str, Any]]  # DNS entry.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.

# Nested classes for table field children

@final
class DnsDatabaseDnsentryObject:
    """Typed object for dns-entry table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DNS entry ID.
    id: int
    # Enable/disable resource record status.
    status: Literal["enable", "disable"]
    # Resource record type.
    type: Literal["A", "NS", "CNAME", "MX", "AAAA", "PTR", "PTR_V6"]
    # Time-to-live for this entry (0 to 2147483647 sec, default = 0).
    ttl: int
    # DNS entry preference (0 - 65535, highest preference = 0, default = 10).
    preference: int
    # IPv4 address of the host.
    ip: str
    # IPv6 address of the host.
    ipv6: str
    # Name of the host.
    hostname: str
    # Canonical name of the host.
    canonical_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class DnsDatabaseResponse(TypedDict):
    """
    Type hints for system/dns_database API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["enable", "disable"]
    domain: str
    allow_transfer: list[dict[str, Any]]
    type: Literal["primary", "secondary"]
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]
    ip_primary: str
    primary_name: str
    contact: str
    ttl: int
    authoritative: Literal["enable", "disable"]
    forwarder: list[dict[str, Any]]
    forwarder6: str
    source_ip: str
    source_ip6: str
    source_ip_interface: str
    rr_max: int
    dns_entry: list[dict[str, Any]]
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int


@final
class DnsDatabaseObject:
    """Typed FortiObject for system/dns_database with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Zone name.
    name: str
    # Enable/disable this DNS zone.
    status: Literal["enable", "disable"]
    # Domain name.
    domain: str
    # DNS zone transfer IP address list.
    allow_transfer: list[dict[str, Any]]  # Multi-value field
    # Zone type
    type: Literal["primary", "secondary"]
    # Zone view (public to serve public clients, shadow to serve internal clients).
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]
    # IP address of primary DNS server. Entries in this primary DNS server and importe
    ip_primary: str
    # Domain name of the default DNS server for this zone.
    primary_name: str
    # Email address of the administrator for this zone. You can specify only the usern
    contact: str
    # Default time-to-live value for the entries of this DNS zone
    ttl: int
    # Enable/disable authoritative zone.
    authoritative: Literal["enable", "disable"]
    # DNS zone forwarder IP address list.
    forwarder: list[dict[str, Any]]  # Multi-value field
    # Forwarder IPv6 address.
    forwarder6: str
    # Source IP for forwarding to DNS server.
    source_ip: str
    # IPv6 source IP address for forwarding to DNS server.
    source_ip6: str
    # IP address of the specified interface as the source IP address.
    source_ip_interface: str
    # Maximum number of resource records (10 - 65536, 0 means infinite).
    rr_max: int
    # DNS entry.
    dns_entry: list[DnsDatabaseDnsentryObject]  # Table field - list of typed objects
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DnsDatabasePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class DnsDatabase:
    """
    Configure DNS databases.
    
    Path: system/dns_database
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> list[DnsDatabaseObject]: ...
    
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
    ) -> DnsDatabaseResponse: ...
    
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
    ) -> DnsDatabaseResponse: ...
    
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
    ) -> list[DnsDatabaseResponse]: ...
    
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
    ) -> DnsDatabaseObject | list[DnsDatabaseObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DnsDatabaseObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DnsDatabaseObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    ) -> DnsDatabaseObject: ...
    
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
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "DnsDatabase",
    "DnsDatabasePayload",
    "DnsDatabaseObject",
]