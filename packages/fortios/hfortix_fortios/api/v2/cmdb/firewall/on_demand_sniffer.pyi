from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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

# Nested classes for table field children

@final
class OnDemandSnifferHostsObject:
    """Typed object for hosts table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv4 or IPv6 host.
    host: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OnDemandSnifferPortsObject:
    """Typed object for ports table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Port to filter in this traffic sniffer.
    port: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class OnDemandSnifferProtocolsObject:
    """Typed object for protocols table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Integer value for the protocol type as defined by IANA (0 - 255).
    protocol: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class OnDemandSnifferResponse(TypedDict):
    """
    Type hints for firewall/on_demand_sniffer API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    interface: str
    max_packet_count: int
    hosts: list[dict[str, Any]]
    ports: list[dict[str, Any]]
    protocols: list[dict[str, Any]]
    non_ip_packet: Literal["enable", "disable"]
    advanced_filter: str


@final
class OnDemandSnifferObject:
    """Typed FortiObject for firewall/on_demand_sniffer with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # On-demand packet sniffer name.
    name: str
    # Interface name that on-demand packet sniffer will take place.
    interface: str
    # Maximum number of packets to capture per on-demand packet sniffer.
    max_packet_count: int
    # IPv4 or IPv6 hosts to filter in this traffic sniffer.
    hosts: list[OnDemandSnifferHostsObject]  # Table field - list of typed objects
    # Ports to filter for in this traffic sniffer.
    ports: list[OnDemandSnifferPortsObject]  # Table field - list of typed objects
    # Protocols to filter in this traffic sniffer.
    protocols: list[OnDemandSnifferProtocolsObject]  # Table field - list of typed objects
    # Include non-IP packets.
    non_ip_packet: Literal["enable", "disable"]
    # Advanced freeform filter that will be used over existing filter settings if set.
    advanced_filter: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> OnDemandSnifferPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class OnDemandSniffer:
    """
    Configure on-demand packet sniffer.
    
    Path: firewall/on_demand_sniffer
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> OnDemandSnifferObject: ...
    
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
    ) -> OnDemandSnifferResponse: ...
    
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
    ) -> OnDemandSnifferResponse: ...
    
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
    ) -> list[OnDemandSnifferResponse]: ...
    
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