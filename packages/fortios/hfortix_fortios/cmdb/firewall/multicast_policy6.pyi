from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class MulticastPolicy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/multicast_policy6 payload fields.
    
    Configure IPv6 multicast NAT policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.ips.sensor.SensorEndpoint` (via: ips-sensor)
        - :class:`~.system.interface.InterfaceEndpoint` (via: dstintf, srcintf)
        - :class:`~.system.sdwan.zone.ZoneEndpoint` (via: dstintf, srcintf)
        - :class:`~.system.zone.ZoneEndpoint` (via: dstintf, srcintf)

    **Usage:**
        payload: MulticastPolicy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Policy ID (0 - 4294967294).
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this policy.
    name: NotRequired[str]  # Policy name.
    srcintf: str  # IPv6 source interface name.
    dstintf: str  # IPv6 destination interface name.
    srcaddr: list[dict[str, Any]]  # IPv6 source address name.
    dstaddr: list[dict[str, Any]]  # IPv6 destination address name.
    action: NotRequired[Literal["accept", "deny"]]  # Accept or deny traffic matching the policy.
    protocol: NotRequired[int]  # Integer value for the protocol type as defined by IANA (0 - 
    start_port: NotRequired[int]  # Integer value for starting TCP/UDP/SCTP destination port in 
    end_port: NotRequired[int]  # Integer value for ending TCP/UDP/SCTP destination port in ra
    utm_status: NotRequired[Literal["enable", "disable"]]  # Enable to add an IPS security profile to the policy.
    ips_sensor: NotRequired[str]  # Name of an existing IPS sensor.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Enable or disable logging. Log all sessions or security prof
    auto_asic_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable offloading policy traffic for hardware accele
    comments: NotRequired[str]  # Comment.


class MulticastPolicy6Object(FortiObject[MulticastPolicy6Payload]):
    """Typed FortiObject for firewall/multicast_policy6 with IDE autocomplete support."""
    
    # Policy ID (0 - 4294967294).
    id: int
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Enable/disable this policy.
    status: Literal["enable", "disable"]
    # Policy name.
    name: str
    # IPv6 source interface name.
    srcintf: str
    # IPv6 destination interface name.
    dstintf: str
    # IPv6 source address name.
    srcaddr: list[str]  # Auto-flattened from member_table
    # IPv6 destination address name.
    dstaddr: list[str]  # Auto-flattened from member_table
    # Accept or deny traffic matching the policy.
    action: Literal["accept", "deny"]
    # Integer value for the protocol type as defined by IANA (0 - 255, default = 0).
    protocol: int
    # Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, de
    start_port: int
    # Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, defa
    end_port: int
    # Enable to add an IPS security profile to the policy.
    utm_status: Literal["enable", "disable"]
    # Name of an existing IPS sensor.
    ips_sensor: str
    # Enable or disable logging. Log all sessions or security profile sessions.
    logtraffic: Literal["all", "utm", "disable"]
    # Enable/disable offloading policy traffic for hardware acceleration.
    auto_asic_offload: Literal["enable", "disable"]
    # Comment.
    comments: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> MulticastPolicy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class MulticastPolicy6:
    """
    Configure IPv6 multicast NAT policies.
    
    Path: firewall/multicast_policy6
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
    ) -> MulticastPolicy6Object: ...
    
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
    ) -> list[MulticastPolicy6Object]: ...
    
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
    ) -> MulticastPolicy6Object | list[MulticastPolicy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MulticastPolicy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
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
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MulticastPolicy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
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
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MulticastPolicy6Object: ...
    
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
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
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
    "MulticastPolicy6",
    "MulticastPolicy6Payload",
    "MulticastPolicy6Object",
]