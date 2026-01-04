from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DnsDatabasePayload(TypedDict, total=False):
    """
    Type hints for system/dns_database payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DnsDatabasePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Zone name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this DNS zone.
    domain: str  # Domain name.
    allow_transfer: NotRequired[str]  # DNS zone transfer IP address list.
    type: Literal["primary", "secondary"]  # Zone type (primary to manage entries directly, secondary to 
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]  # Zone view (public to serve public clients, shadow to serve i
    ip_primary: NotRequired[str]  # IP address of primary DNS server. Entries in this primary DN
    primary_name: NotRequired[str]  # Domain name of the default DNS server for this zone.
    contact: NotRequired[str]  # Email address of the administrator for this zone. You can sp
    ttl: int  # Default time-to-live value for the entries of this DNS zone 
    authoritative: Literal["enable", "disable"]  # Enable/disable authoritative zone.
    forwarder: NotRequired[str]  # DNS zone forwarder IP address list.
    forwarder6: NotRequired[str]  # Forwarder IPv6 address.
    source_ip: NotRequired[str]  # Source IP for forwarding to DNS server.
    source_ip6: NotRequired[str]  # IPv6 source IP address for forwarding to DNS server.
    source_ip_interface: NotRequired[str]  # IP address of the specified interface as the source IP addre
    rr_max: NotRequired[int]  # Maximum number of resource records (10 - 65536, 0 means infi
    dns_entry: list[dict[str, Any]]  # DNS entry.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class DnsDatabase:
    """
    Configure DNS databases.
    
    Path: system/dns_database
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
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
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
        payload_dict: DnsDatabasePayload | None = ...,
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