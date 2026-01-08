from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ServerPayload(TypedDict, total=False):
    """
    Type hints for system/dhcp6/server payload fields.
    
    Configure DHCPv6 servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, upstream-interface)

    **Usage:**
        payload: ServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable this DHCPv6 configuration.
    rapid_commit: NotRequired[Literal["disable", "enable"]]  # Enable/disable allow/disallow rapid commit.
    lease_time: NotRequired[int]  # Lease time in seconds, 0 means unlimited.
    dns_service: NotRequired[Literal["delegated", "default", "specify"]]  # Options for assigning DNS servers to DHCPv6 clients.
    dns_search_list: NotRequired[Literal["delegated", "specify"]]  # DNS search list options.
    dns_server1: NotRequired[str]  # DNS server 1.
    dns_server2: NotRequired[str]  # DNS server 2.
    dns_server3: NotRequired[str]  # DNS server 3.
    dns_server4: NotRequired[str]  # DNS server 4.
    domain: NotRequired[str]  # Domain name suffix for the IP addresses that the DHCP server
    subnet: str  # Subnet or subnet-id if the IP mode is delegated.
    interface: str  # DHCP server can assign IP configurations to clients connecte
    delegated_prefix_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable automatically adding of routing for delegated
    options: NotRequired[list[dict[str, Any]]]  # DHCPv6 options.
    upstream_interface: str  # Interface name from where delegated information is provided.
    delegated_prefix_iaid: int  # IAID of obtained delegated-prefix from the upstream interfac
    ip_mode: NotRequired[Literal["range", "delegated"]]  # Method used to assign client IP.
    prefix_mode: NotRequired[Literal["dhcp6", "ra"]]  # Assigning a prefix from a DHCPv6 client or RA.
    prefix_range: NotRequired[list[dict[str, Any]]]  # DHCP prefix configuration.
    ip_range: NotRequired[list[dict[str, Any]]]  # DHCP IP range configuration.


class ServerObject(FortiObject[ServerPayload]):
    """Typed FortiObject for system/dhcp6/server with IDE autocomplete support."""
    
    # ID.
    id: int
    # Enable/disable this DHCPv6 configuration.
    status: Literal["disable", "enable"]
    # Enable/disable allow/disallow rapid commit.
    rapid_commit: Literal["disable", "enable"]
    # Lease time in seconds, 0 means unlimited.
    lease_time: int
    # Options for assigning DNS servers to DHCPv6 clients.
    dns_service: Literal["delegated", "default", "specify"]
    # DNS search list options.
    dns_search_list: Literal["delegated", "specify"]
    # DNS server 1.
    dns_server1: str
    # DNS server 2.
    dns_server2: str
    # DNS server 3.
    dns_server3: str
    # DNS server 4.
    dns_server4: str
    # Domain name suffix for the IP addresses that the DHCP server assigns to clients.
    domain: str
    # Subnet or subnet-id if the IP mode is delegated.
    subnet: str
    # DHCP server can assign IP configurations to clients connected to this interface.
    interface: str
    # Enable/disable automatically adding of routing for delegated prefix.
    delegated_prefix_route: Literal["disable", "enable"]
    # DHCPv6 options.
    options: list[str]  # Auto-flattened from member_table
    # Interface name from where delegated information is provided.
    upstream_interface: str
    # IAID of obtained delegated-prefix from the upstream interface.
    delegated_prefix_iaid: int
    # Method used to assign client IP.
    ip_mode: Literal["range", "delegated"]
    # Assigning a prefix from a DHCPv6 client or RA.
    prefix_mode: Literal["dhcp6", "ra"]
    # DHCP prefix configuration.
    prefix_range: list[str]  # Auto-flattened from member_table
    # DHCP IP range configuration.
    ip_range: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Server:
    """
    Configure DHCPv6 servers.
    
    Path: system/dhcp6/server
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        id: int,
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
    ) -> ServerObject: ...
    
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
    ) -> list[ServerObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
        id: None = None,
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
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> ServerObject | list[ServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Server",
    "ServerPayload",
    "ServerObject",
]