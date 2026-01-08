from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class CentralSnatMapPayload(TypedDict, total=False):
    """
    Type hints for firewall/central_snat_map payload fields.
    
    Configure IPv4 and IPv6 central SNAT policies.
    
    **Usage:**
        payload: CentralSnatMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the active status of this policy.
    type: NotRequired[Literal["ipv4", "ipv6"]]  # IPv4/IPv6 source NAT.
    srcintf: list[dict[str, Any]]  # Source interface name from available interfaces.
    dstintf: list[dict[str, Any]]  # Destination interface name from available interfaces.
    orig_addr: list[dict[str, Any]]  # IPv4 Original address.
    orig_addr6: list[dict[str, Any]]  # IPv6 Original address.
    dst_addr: list[dict[str, Any]]  # IPv4 Destination address.
    dst_addr6: list[dict[str, Any]]  # IPv6 Destination address.
    protocol: NotRequired[int]  # Integer value for the protocol type (0 - 255).
    orig_port: NotRequired[str]  # Original TCP port (1 to 65535, 0 means any port).
    nat: NotRequired[Literal["disable", "enable"]]  # Enable/disable source NAT.
    nat46: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46.
    nat64: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT64.
    nat_ippool: NotRequired[list[dict[str, Any]]]  # Name of the IP pools to be used to translate addresses from 
    nat_ippool6: NotRequired[list[dict[str, Any]]]  # IPv6 pools to be used for source NAT.
    port_preserve: NotRequired[Literal["enable", "disable"]]  # Enable/disable preservation of the original source port from
    port_random: NotRequired[Literal["enable", "disable"]]  # Enable/disable random source port selection for source NAT.
    nat_port: NotRequired[str]  # Translated port or port range (1 to 65535, 0 means any port)
    dst_port: NotRequired[str]  # Destination port or port range (1 to 65535, 0 means any port
    comments: NotRequired[str]  # Comment.


class CentralSnatMapObject(FortiObject[CentralSnatMapPayload]):
    """Typed FortiObject for firewall/central_snat_map with IDE autocomplete support."""
    
    # Policy ID.
    policyid: int
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Enable/disable the active status of this policy.
    status: Literal["enable", "disable"]
    # IPv4/IPv6 source NAT.
    type: Literal["ipv4", "ipv6"]
    # Source interface name from available interfaces.
    srcintf: list[str]  # Auto-flattened from member_table
    # Destination interface name from available interfaces.
    dstintf: list[str]  # Auto-flattened from member_table
    # IPv4 Original address.
    orig_addr: list[str]  # Auto-flattened from member_table
    # IPv6 Original address.
    orig_addr6: list[str]  # Auto-flattened from member_table
    # IPv4 Destination address.
    dst_addr: list[str]  # Auto-flattened from member_table
    # IPv6 Destination address.
    dst_addr6: list[str]  # Auto-flattened from member_table
    # Integer value for the protocol type (0 - 255).
    protocol: int
    # Original TCP port (1 to 65535, 0 means any port).
    orig_port: str
    # Enable/disable source NAT.
    nat: Literal["disable", "enable"]
    # Enable/disable NAT46.
    nat46: Literal["enable", "disable"]
    # Enable/disable NAT64.
    nat64: Literal["enable", "disable"]
    # Name of the IP pools to be used to translate addresses from available IP Pools.
    nat_ippool: list[str]  # Auto-flattened from member_table
    # IPv6 pools to be used for source NAT.
    nat_ippool6: list[str]  # Auto-flattened from member_table
    # Enable/disable preservation of the original source port from source NAT if it ha
    port_preserve: Literal["enable", "disable"]
    # Enable/disable random source port selection for source NAT.
    port_random: Literal["enable", "disable"]
    # Translated port or port range (1 to 65535, 0 means any port).
    nat_port: str
    # Destination port or port range (1 to 65535, 0 means any port).
    dst_port: str
    # Comment.
    comments: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CentralSnatMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class CentralSnatMap:
    """
    Configure IPv4 and IPv6 central SNAT policies.
    
    Path: firewall/central_snat_map
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> CentralSnatMapObject: ...
    
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
    ) -> list[CentralSnatMapObject]: ...
    
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int,
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
        policyid: None = None,
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
        policyid: int | None = ...,
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
        policyid: int | None = ...,
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
    ) -> CentralSnatMapObject | list[CentralSnatMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
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
    "CentralSnatMap",
    "CentralSnatMapPayload",
    "CentralSnatMapObject",
]