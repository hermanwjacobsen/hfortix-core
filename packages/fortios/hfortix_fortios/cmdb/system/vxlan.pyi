from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class VxlanPayload(TypedDict, total=False):
    """
    Type hints for system/vxlan payload fields.
    
    Configure VXLAN devices.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.evpn.EvpnEndpoint` (via: evpn-id)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: VxlanPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # VXLAN device or interface name. Must be a unique interface n
    interface: str  # Outgoing interface for VXLAN encapsulated traffic.
    vni: int  # VXLAN network ID.
    ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"]  # IP version to use for the VXLAN interface and so for communi
    remote_ip: NotRequired[list[dict[str, Any]]]  # IPv4 address of the VXLAN interface on the device at the rem
    local_ip: NotRequired[str]  # IPv4 address to use as the source address for egress VXLAN p
    remote_ip6: list[dict[str, Any]]  # IPv6 IP address of the VXLAN interface on the device at the 
    local_ip6: NotRequired[str]  # IPv6 address to use as the source address for egress VXLAN p
    dstport: NotRequired[int]  # VXLAN destination port (1 - 65535, default = 4789).
    multicast_ttl: int  # VXLAN multicast TTL (1-255, default = 0).
    evpn_id: NotRequired[int]  # EVPN instance.
    learn_from_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable VXLAN MAC learning from traffic.


class VxlanObject(FortiObject[VxlanPayload]):
    """Typed FortiObject for system/vxlan with IDE autocomplete support."""
    
    # VXLAN device or interface name. Must be a unique interface name.
    name: str
    # Outgoing interface for VXLAN encapsulated traffic.
    interface: str
    # VXLAN network ID.
    vni: int
    # IP version to use for the VXLAN interface and so for communication over the VXLA
    ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"]
    # IPv4 address of the VXLAN interface on the device at the remote end of the VXLAN
    remote_ip: list[str]  # Auto-flattened from member_table
    # IPv4 address to use as the source address for egress VXLAN packets.
    local_ip: str
    # IPv6 IP address of the VXLAN interface on the device at the remote end of the VX
    remote_ip6: list[str]  # Auto-flattened from member_table
    # IPv6 address to use as the source address for egress VXLAN packets.
    local_ip6: str
    # VXLAN destination port (1 - 65535, default = 4789).
    dstport: int
    # VXLAN multicast TTL (1-255, default = 0).
    multicast_ttl: int
    # EVPN instance.
    evpn_id: int
    # Enable/disable VXLAN MAC learning from traffic.
    learn_from_traffic: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VxlanPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Vxlan:
    """
    Configure VXLAN devices.
    
    Path: system/vxlan
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
    ) -> VxlanObject: ...
    
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
    ) -> list[VxlanObject]: ...
    
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
    ) -> VxlanObject | list[VxlanObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VxlanObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VxlanObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
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
    ) -> VxlanObject: ...
    
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
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
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
    "Vxlan",
    "VxlanPayload",
    "VxlanObject",
]