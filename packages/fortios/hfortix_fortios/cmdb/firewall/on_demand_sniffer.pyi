from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class OnDemandSnifferPayload(TypedDict, total=False):
    """
    Type hints for firewall/on_demand_sniffer payload fields.
    
    Configure on-demand packet sniffer.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: OnDemandSnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # On-demand packet sniffer name.
    interface: str  # Interface name that on-demand packet sniffer will take place
    max_packet_count: int  # Maximum number of packets to capture per on-demand packet sn
    hosts: NotRequired[list[dict[str, Any]]]  # IPv4 or IPv6 hosts to filter in this traffic sniffer.
    ports: NotRequired[list[dict[str, Any]]]  # Ports to filter for in this traffic sniffer.
    protocols: NotRequired[list[dict[str, Any]]]  # Protocols to filter in this traffic sniffer.
    non_ip_packet: NotRequired[Literal["enable", "disable"]]  # Include non-IP packets.
    advanced_filter: NotRequired[str]  # Advanced freeform filter that will be used over existing fil


class OnDemandSnifferObject(FortiObject[OnDemandSnifferPayload]):
    """Typed FortiObject for firewall/on_demand_sniffer with IDE autocomplete support."""
    
    # On-demand packet sniffer name.
    name: str
    # Interface name that on-demand packet sniffer will take place.
    interface: str
    # Maximum number of packets to capture per on-demand packet sniffer.
    max_packet_count: int
    # IPv4 or IPv6 hosts to filter in this traffic sniffer.
    hosts: list[str]  # Auto-flattened from member_table
    # Ports to filter for in this traffic sniffer.
    ports: list[str]  # Auto-flattened from member_table
    # Protocols to filter in this traffic sniffer.
    protocols: list[str]  # Auto-flattened from member_table
    # Include non-IP packets.
    non_ip_packet: Literal["enable", "disable"]
    # Advanced freeform filter that will be used over existing filter settings if set.
    advanced_filter: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OnDemandSnifferPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class OnDemandSniffer:
    """
    Configure on-demand packet sniffer.
    
    Path: firewall/on_demand_sniffer
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> list[OnDemandSnifferObject]: ...
    
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
    ) -> OnDemandSnifferObject | list[OnDemandSnifferObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OnDemandSnifferObject: ...
    
    @overload
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> OnDemandSnifferObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
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
    ) -> OnDemandSnifferObject: ...
    
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
        payload_dict: OnDemandSnifferPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        max_packet_count: int | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        protocols: str | list[str] | list[dict[str, Any]] | None = ...,
        non_ip_packet: Literal["enable", "disable"] | None = ...,
        advanced_filter: str | None = ...,
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
    "OnDemandSniffer",
    "OnDemandSnifferPayload",
    "OnDemandSnifferObject",
]