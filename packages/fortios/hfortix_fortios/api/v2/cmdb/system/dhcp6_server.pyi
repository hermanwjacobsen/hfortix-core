from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Dhcp6ServerPayload(TypedDict, total=False):
    """
    Type hints for system/dhcp6_server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Dhcp6ServerPayload = {
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


class Dhcp6Server:
    """
    Configure DHCPv6 servers.
    
    Path: system/dhcp6_server
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: Dhcp6ServerPayload | None = ...,
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
        options: list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Dhcp6ServerPayload | None = ...,
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
        options: list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: Dhcp6ServerPayload | None = ...,
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