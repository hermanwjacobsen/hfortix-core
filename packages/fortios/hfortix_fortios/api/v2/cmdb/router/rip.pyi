from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class RipPayload(TypedDict, total=False):
    """
    Type hints for router/rip payload fields.
    
    Configure RIP.
    
    **Usage:**
        payload: RipPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    default_information_originate: NotRequired[Literal["enable", "disable"]]  # Enable/disable generation of default route.
    default_metric: NotRequired[int]  # Default metric.
    max_out_metric: NotRequired[int]  # Maximum metric allowed to output(0 means 'not set').
    distance: NotRequired[list[dict[str, Any]]]  # Distance.
    distribute_list: NotRequired[list[dict[str, Any]]]  # Distribute list.
    neighbor: NotRequired[list[dict[str, Any]]]  # Neighbor.
    network: NotRequired[list[dict[str, Any]]]  # Network.
    offset_list: NotRequired[list[dict[str, Any]]]  # Offset list.
    passive_interface: NotRequired[list[dict[str, Any]]]  # Passive interface configuration.
    redistribute: NotRequired[list[dict[str, Any]]]  # Redistribute configuration.
    update_timer: NotRequired[int]  # Update timer in seconds.
    timeout_timer: NotRequired[int]  # Timeout timer in seconds.
    garbage_timer: NotRequired[int]  # Garbage timer in seconds.
    version: NotRequired[Literal["1", "2"]]  # RIP version.
    interface: NotRequired[list[dict[str, Any]]]  # RIP interface configuration.

# Nested classes for table field children

@final
class RipDistanceObject:
    """Typed object for distance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distance ID.
    id: int
    # Distance prefix.
    prefix: str
    # Distance (1 - 255).
    distance: int
    # Access list for route destination.
    access_list: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipDistributelistObject:
    """Typed object for distribute-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list ID.
    id: int
    # Status.
    status: Literal["enable", "disable"]
    # Distribute list direction.
    direction: Literal["in", "out"]
    # Distribute access/prefix list name.
    listname: str
    # Distribute list interface name.
    interface: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor entry ID.
    id: int
    # IP address.
    ip: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID.
    id: int
    # Network prefix.
    prefix: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipOffsetlistObject:
    """Typed object for offset-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Offset-list ID.
    id: int
    # Status.
    status: Literal["enable", "disable"]
    # Offset list direction.
    direction: Literal["in", "out"]
    # Access list name.
    access_list: str
    # Offset.
    offset: int
    # Interface name.
    interface: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipPassiveinterfaceObject:
    """Typed object for passive-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Passive interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Redistribute name.
    name: str
    # Status.
    status: Literal["enable", "disable"]
    # Redistribute metric setting.
    metric: int
    # Route map name.
    routemap: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RipInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    # Authentication key-chain name.
    auth_keychain: str
    # Authentication mode.
    auth_mode: Literal["none", "text", "md5"]
    # Authentication string/password.
    auth_string: str
    # Receive version.
    receive_version: Literal["1", "2"]
    # Send version.
    send_version: Literal["1", "2"]
    # Enable/disable broadcast version 1 compatible packets.
    send_version2_broadcast: Literal["disable", "enable"]
    # Enable/disable split horizon.
    split_horizon_status: Literal["enable", "disable"]
    # Enable/disable split horizon.
    split_horizon: Literal["poisoned", "regular"]
    # Flags.
    flags: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class RipResponse(TypedDict):
    """
    Type hints for router/rip API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    default_information_originate: Literal["enable", "disable"]
    default_metric: int
    max_out_metric: int
    distance: list[dict[str, Any]]
    distribute_list: list[dict[str, Any]]
    neighbor: list[dict[str, Any]]
    network: list[dict[str, Any]]
    offset_list: list[dict[str, Any]]
    passive_interface: list[dict[str, Any]]
    redistribute: list[dict[str, Any]]
    update_timer: int
    timeout_timer: int
    garbage_timer: int
    version: Literal["1", "2"]
    interface: list[dict[str, Any]]


@final
class RipObject:
    """Typed FortiObject for router/rip with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable generation of default route.
    default_information_originate: Literal["enable", "disable"]
    # Default metric.
    default_metric: int
    # Maximum metric allowed to output(0 means 'not set').
    max_out_metric: int
    # Distance.
    distance: list[RipDistanceObject]  # Table field - list of typed objects
    # Distribute list.
    distribute_list: list[RipDistributelistObject]  # Table field - list of typed objects
    # Neighbor.
    neighbor: list[RipNeighborObject]  # Table field - list of typed objects
    # Network.
    network: list[RipNetworkObject]  # Table field - list of typed objects
    # Offset list.
    offset_list: list[RipOffsetlistObject]  # Table field - list of typed objects
    # Passive interface configuration.
    passive_interface: list[RipPassiveinterfaceObject]  # Table field - list of typed objects
    # Redistribute configuration.
    redistribute: list[RipRedistributeObject]  # Table field - list of typed objects
    # Update timer in seconds.
    update_timer: int
    # Timeout timer in seconds.
    timeout_timer: int
    # Garbage timer in seconds.
    garbage_timer: int
    # RIP version.
    version: Literal["1", "2"]
    # RIP interface configuration.
    interface: list[RipInterfaceObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RipPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Rip:
    """
    Configure RIP.
    
    Path: router/rip
    Category: cmdb
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
    ) -> RipObject: ...
    
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
    ) -> RipObject: ...
    
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
    ) -> RipObject: ...
    
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
    ) -> RipResponse: ...
    
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
    ) -> RipResponse: ...
    
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
    ) -> RipResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> RipObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RipObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Rip",
    "RipPayload",
    "RipObject",
]