from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Address6Payload(TypedDict, total=False):
    """
    Type hints for firewall/address6 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Address6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Address name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    type: NotRequired[Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"]]  # Type of IPv6 address object (default = ipprefix).
    route_tag: NotRequired[int]  # route-tag address.
    macaddr: NotRequired[list[dict[str, Any]]]  # Multiple MAC address ranges.
    sdn: NotRequired[str]  # SDN.
    ip6: NotRequired[str]  # IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:x
    wildcard: NotRequired[str]  # IPv6 address and wildcard netmask.
    start_ip: NotRequired[str]  # First IP address (inclusive) in the range for the address (f
    end_ip: NotRequired[str]  # Final IP address (inclusive) in the range for the address (f
    fqdn: NotRequired[str]  # Fully qualified domain name.
    country: NotRequired[str]  # IPv6 addresses associated to a specific country.
    cache_ttl: NotRequired[int]  # Minimal TTL of individual IPv6 addresses in FQDN cache.
    color: NotRequired[int]  # Integer value to determine the color of the icon in the GUI 
    obj_id: NotRequired[str]  # Object ID for NSX.
    tagging: NotRequired[list[dict[str, Any]]]  # Config object tagging.
    comment: NotRequired[str]  # Comment.
    template: str  # IPv6 address template.
    subnet_segment: NotRequired[list[dict[str, Any]]]  # IPv6 subnet segments.
    host_type: NotRequired[Literal["any", "specific"]]  # Host type.
    host: NotRequired[str]  # Host Address.
    tenant: NotRequired[str]  # Tenant.
    epg_name: NotRequired[str]  # Endpoint group name.
    sdn_tag: NotRequired[str]  # SDN Tag.
    filter: str  # Match criteria filter.
    list: NotRequired[list[dict[str, Any]]]  # IP address list.
    sdn_addr_type: NotRequired[Literal["private", "public", "all"]]  # Type of addresses to collect.
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class Address6:
    """
    Configure IPv6 firewall addresses.
    
    Path: firewall/address6
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
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
        payload_dict: Address6Payload | None = ...,
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
    "Address6",
    "Address6Payload",
]