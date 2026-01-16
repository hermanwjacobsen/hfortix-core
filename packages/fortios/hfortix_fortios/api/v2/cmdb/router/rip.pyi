from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class RipDistanceItem(TypedDict, total=False):
    """Type hints for distance table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - prefix: str
        - distance: int
        - access_list: str
    
    **Example:**
        entry: RipDistanceItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Distance ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Distance prefix. | Default: 0.0.0.0 0.0.0.0
    distance: int  # Distance (1 - 255). | Default: 0 | Min: 1 | Max: 255
    access_list: str  # Access list for route destination. | MaxLen: 35


class RipDistributelistItem(TypedDict, total=False):
    """Type hints for distribute-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - status: "enable" | "disable"
        - direction: "in" | "out"
        - listname: str
        - interface: str
    
    **Example:**
        entry: RipDistributelistItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Distribute list ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Status. | Default: disable
    direction: Literal["in", "out"]  # Distribute list direction. | Default: out
    listname: str  # Distribute access/prefix list name. | MaxLen: 35
    interface: str  # Distribute list interface name. | MaxLen: 15


class RipNeighborItem(TypedDict, total=False):
    """Type hints for neighbor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - ip: str
    
    **Example:**
        entry: RipNeighborItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Neighbor entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    ip: str  # IP address. | Default: 0.0.0.0


class RipNetworkItem(TypedDict, total=False):
    """Type hints for network table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - prefix: str
    
    **Example:**
        entry: RipNetworkItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Network prefix. | Default: 0.0.0.0 0.0.0.0


class RipOffsetlistItem(TypedDict, total=False):
    """Type hints for offset-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - status: "enable" | "disable"
        - direction: "in" | "out"
        - access_list: str
        - offset: int
        - interface: str
    
    **Example:**
        entry: RipOffsetlistItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Offset-list ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Status. | Default: enable
    direction: Literal["in", "out"]  # Offset list direction. | Default: out
    access_list: str  # Access list name. | MaxLen: 35
    offset: int  # Offset. | Default: 0 | Min: 1 | Max: 16
    interface: str  # Interface name. | MaxLen: 15


class RipPassiveinterfaceItem(TypedDict, total=False):
    """Type hints for passive-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: RipPassiveinterfaceItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Passive interface name. | MaxLen: 79


class RipRedistributeItem(TypedDict, total=False):
    """Type hints for redistribute table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
        - status: "enable" | "disable"
        - metric: int
        - routemap: str
    
    **Example:**
        entry: RipRedistributeItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Redistribute name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    metric: int  # Redistribute metric setting. | Default: 0 | Min: 1 | Max: 16
    routemap: str  # Route map name. | MaxLen: 35


class RipInterfaceItem(TypedDict, total=False):
    """Type hints for interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
        - auth_keychain: str
        - auth_mode: "none" | "text" | "md5"
        - auth_string: str
        - receive_version: "1" | "2"
        - send_version: "1" | "2"
        - send_version2_broadcast: "disable" | "enable"
        - split_horizon_status: "enable" | "disable"
        - split_horizon: "poisoned" | "regular"
        - flags: int
    
    **Example:**
        entry: RipInterfaceItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Interface name. | MaxLen: 35
    auth_keychain: str  # Authentication key-chain name. | MaxLen: 35
    auth_mode: Literal["none", "text", "md5"]  # Authentication mode. | Default: none
    auth_string: str  # Authentication string/password. | MaxLen: 16
    receive_version: Literal["1", "2"]  # Receive version.
    send_version: Literal["1", "2"]  # Send version.
    send_version2_broadcast: Literal["disable", "enable"]  # Enable/disable broadcast version 1 compatible pack | Default: disable
    split_horizon_status: Literal["enable", "disable"]  # Enable/disable split horizon. | Default: enable
    split_horizon: Literal["poisoned", "regular"]  # Enable/disable split horizon. | Default: poisoned
    flags: int  # Flags. | Default: 8 | Min: 0 | Max: 255


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RipPayload(TypedDict, total=False):
    """
    Type hints for router/rip payload fields.
    
    Configure RIP.
    
    **Usage:**
        payload: RipPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    default_information_originate: Literal["enable", "disable"]  # Enable/disable generation of default route. | Default: disable
    default_metric: int  # Default metric. | Default: 1 | Min: 1 | Max: 16
    max_out_metric: int  # Maximum metric allowed to output | Default: 0 | Min: 0 | Max: 15
    distance: list[RipDistanceItem]  # Distance.
    distribute_list: list[RipDistributelistItem]  # Distribute list.
    neighbor: list[RipNeighborItem]  # Neighbor.
    network: list[RipNetworkItem]  # Network.
    offset_list: list[RipOffsetlistItem]  # Offset list.
    passive_interface: list[RipPassiveinterfaceItem]  # Passive interface configuration.
    redistribute: list[RipRedistributeItem]  # Redistribute configuration.
    update_timer: int  # Update timer in seconds. | Default: 30 | Min: 1 | Max: 2147483647
    timeout_timer: int  # Timeout timer in seconds. | Default: 180 | Min: 5 | Max: 2147483647
    garbage_timer: int  # Garbage timer in seconds. | Default: 120 | Min: 5 | Max: 2147483647
    version: Literal["1", "2"]  # RIP version. | Default: 2
    interface: list[RipInterfaceItem]  # RIP interface configuration.

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class RipDistanceObject:
    """Typed object for distance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distance ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Distance prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Distance (1 - 255). | Default: 0 | Min: 1 | Max: 255
    distance: int
    # Access list for route destination. | MaxLen: 35
    access_list: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipDistributelistObject:
    """Typed object for distribute-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Distribute list direction. | Default: out
    direction: Literal["in", "out"]
    # Distribute access/prefix list name. | MaxLen: 35
    listname: str
    # Distribute list interface name. | MaxLen: 15
    interface: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IP address. | Default: 0.0.0.0
    ip: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Network prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipOffsetlistObject:
    """Typed object for offset-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Offset-list ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Status. | Default: enable
    status: Literal["enable", "disable"]
    # Offset list direction. | Default: out
    direction: Literal["in", "out"]
    # Access list name. | MaxLen: 35
    access_list: str
    # Offset. | Default: 0 | Min: 1 | Max: 16
    offset: int
    # Interface name. | MaxLen: 15
    interface: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipPassiveinterfaceObject:
    """Typed object for passive-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Passive interface name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Redistribute name. | MaxLen: 35
    name: str
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Redistribute metric setting. | Default: 0 | Min: 1 | Max: 16
    metric: int
    # Route map name. | MaxLen: 35
    routemap: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class RipInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 35
    name: str
    # Authentication key-chain name. | MaxLen: 35
    auth_keychain: str
    # Authentication mode. | Default: none
    auth_mode: Literal["none", "text", "md5"]
    # Authentication string/password. | MaxLen: 16
    auth_string: str
    # Receive version.
    receive_version: Literal["1", "2"]
    # Send version.
    send_version: Literal["1", "2"]
    # Enable/disable broadcast version 1 compatible packets. | Default: disable
    send_version2_broadcast: Literal["disable", "enable"]
    # Enable/disable split horizon. | Default: enable
    split_horizon_status: Literal["enable", "disable"]
    # Enable/disable split horizon. | Default: poisoned
    split_horizon: Literal["poisoned", "regular"]
    # Flags. | Default: 8 | Min: 0 | Max: 255
    flags: int
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...




# Response TypedDict for GET returns (all fields present in API response)
class RipResponse(TypedDict):
    """
    Type hints for router/rip API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    default_information_originate: Literal["enable", "disable"]  # Enable/disable generation of default route. | Default: disable
    default_metric: int  # Default metric. | Default: 1 | Min: 1 | Max: 16
    max_out_metric: int  # Maximum metric allowed to output | Default: 0 | Min: 0 | Max: 15
    distance: list[RipDistanceItem]  # Distance.
    distribute_list: list[RipDistributelistItem]  # Distribute list.
    neighbor: list[RipNeighborItem]  # Neighbor.
    network: list[RipNetworkItem]  # Network.
    offset_list: list[RipOffsetlistItem]  # Offset list.
    passive_interface: list[RipPassiveinterfaceItem]  # Passive interface configuration.
    redistribute: list[RipRedistributeItem]  # Redistribute configuration.
    update_timer: int  # Update timer in seconds. | Default: 30 | Min: 1 | Max: 2147483647
    timeout_timer: int  # Timeout timer in seconds. | Default: 180 | Min: 5 | Max: 2147483647
    garbage_timer: int  # Garbage timer in seconds. | Default: 120 | Min: 5 | Max: 2147483647
    version: Literal["1", "2"]  # RIP version. | Default: 2
    interface: list[RipInterfaceItem]  # RIP interface configuration.


@final
class RipObject:
    """Typed FortiObject for router/rip with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable generation of default route. | Default: disable
    default_information_originate: Literal["enable", "disable"]
    # Default metric. | Default: 1 | Min: 1 | Max: 16
    default_metric: int
    # Maximum metric allowed to output(0 means 'not set'). | Default: 0 | Min: 0 | Max: 15
    max_out_metric: int
    # Distance.
    distance: list[RipDistanceObject]
    # Distribute list.
    distribute_list: list[RipDistributelistObject]
    # Neighbor.
    neighbor: list[RipNeighborObject]
    # Network.
    network: list[RipNetworkObject]
    # Offset list.
    offset_list: list[RipOffsetlistObject]
    # Passive interface configuration.
    passive_interface: list[RipPassiveinterfaceObject]
    # Redistribute configuration.
    redistribute: list[RipRedistributeObject]
    # Update timer in seconds. | Default: 30 | Min: 1 | Max: 2147483647
    update_timer: int
    # Timeout timer in seconds. | Default: 180 | Min: 5 | Max: 2147483647
    timeout_timer: int
    # Garbage timer in seconds. | Default: 120 | Min: 5 | Max: 2147483647
    garbage_timer: int
    # RIP version. | Default: 2
    version: Literal["1", "2"]
    # RIP interface configuration.
    interface: list[RipInterfaceObject]
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RipPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Rip:
    """
    Configure RIP.
    
    Path: router/rip
    Category: cmdb
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
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
    ) -> RipObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
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
    ) -> RipObject: ...
    
    # Without mkey -> returns list of FortiObjects
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
    ) -> RipObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
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
    ) -> RipObject: ...
    
    # With mkey as keyword arg -> returns single object
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
    ) -> RipObject: ...
    
    # With no mkey -> returns list of objects
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
    ) -> RipObject: ...
    
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
    ) -> RipObject: ...
    
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
    ) -> RipObject: ...
    
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
    ) -> RipObject: ...
    
    # Fallback overload for all other cases
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> RipObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[RipDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[RipDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[RipNeighborItem] | None = ...,
        network: str | list[str] | list[RipNetworkItem] | None = ...,
        offset_list: str | list[str] | list[RipOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[RipPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[RipRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[RipInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RipObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[RipDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[RipDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[RipNeighborItem] | None = ...,
        network: str | list[str] | list[RipNetworkItem] | None = ...,
        offset_list: str | list[str] | list[RipOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[RipPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[RipRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[RipInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[RipDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[RipDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[RipNeighborItem] | None = ...,
        network: str | list[str] | list[RipNetworkItem] | None = ...,
        offset_list: str | list[str] | list[RipOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[RipPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[RipRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[RipInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: RipPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[RipDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[RipDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[RipNeighborItem] | None = ...,
        network: str | list[str] | list[RipNetworkItem] | None = ...,
        offset_list: str | list[str] | list[RipOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[RipPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[RipRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[RipInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
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
        distance: str | list[str] | list[RipDistanceItem] | None = ...,
        distribute_list: str | list[str] | list[RipDistributelistItem] | None = ...,
        neighbor: str | list[str] | list[RipNeighborItem] | None = ...,
        network: str | list[str] | list[RipNetworkItem] | None = ...,
        offset_list: str | list[str] | list[RipOffsetlistItem] | None = ...,
        passive_interface: str | list[str] | list[RipPassiveinterfaceItem] | None = ...,
        redistribute: str | list[str] | list[RipRedistributeItem] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        version: Literal["1", "2"] | None = ...,
        interface: str | list[str] | list[RipInterfaceItem] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Rip",
    "RipPayload",
    "RipResponse",
    "RipObject",
]