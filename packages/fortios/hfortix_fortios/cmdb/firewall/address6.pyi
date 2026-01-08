from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class Address6Payload(TypedDict, total=False):
    """
    Type hints for firewall/address6 payload fields.
    
    Configure IPv6 firewall addresses.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address6-template.Address6TemplateEndpoint` (via: template)
        - :class:`~.system.sdn-connector.SdnConnectorEndpoint` (via: sdn)

    **Usage:**
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
    passive_fqdn_learning: NotRequired[Literal["disable", "enable"]]  # Enable/disable passive learning of FQDNs.  When enabled, the
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class Address6Object(FortiObject[Address6Payload]):
    """Typed FortiObject for firewall/address6 with IDE autocomplete support."""
    
    # Address name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Type of IPv6 address object (default = ipprefix).
    type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"]
    # route-tag address.
    route_tag: int
    # Multiple MAC address ranges.
    macaddr: list[str]  # Auto-flattened from member_table
    # SDN.
    sdn: str
    # IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx).
    ip6: str
    # IPv6 address and wildcard netmask.
    wildcard: str
    # First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxx
    start_ip: str
    # Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxx
    end_ip: str
    # Fully qualified domain name.
    fqdn: str
    # IPv6 addresses associated to a specific country.
    country: str
    # Minimal TTL of individual IPv6 addresses in FQDN cache.
    cache_ttl: int
    # Integer value to determine the color of the icon in the GUI (range 1 to 32, defa
    color: int
    # Object ID for NSX.
    obj_id: str
    # Config object tagging.
    tagging: list[str]  # Auto-flattened from member_table
    # Comment.
    comment: str
    # IPv6 address template.
    template: str
    # IPv6 subnet segments.
    subnet_segment: list[str]  # Auto-flattened from member_table
    # Host type.
    host_type: Literal["any", "specific"]
    # Host Address.
    host: str
    # Tenant.
    tenant: str
    # Endpoint group name.
    epg_name: str
    # SDN Tag.
    sdn_tag: str
    # Match criteria filter.
    filter: str
    # IP address list.
    list: list[str]  # Auto-flattened from member_table
    # Type of addresses to collect.
    sdn_addr_type: Literal["private", "public", "all"]
    # Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, t
    passive_fqdn_learning: Literal["disable", "enable"]
    # Security Fabric global object setting.
    fabric_object: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Address6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Address6:
    """
    Configure IPv6 firewall addresses.
    
    Path: firewall/address6
    Category: cmdb
    Primary Key: name
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
    ) -> Address6Object: ...
    
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
    ) -> list[Address6Object]: ...
    
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
    ) -> Address6Object | list[Address6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Address6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Address6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    ) -> Address6Object: ...
    
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
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
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
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Address6",
    "Address6Payload",
    "Address6Object",
]