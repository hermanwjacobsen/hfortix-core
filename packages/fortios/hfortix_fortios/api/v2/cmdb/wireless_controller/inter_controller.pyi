from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class InterControllerPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/inter_controller payload fields.
    
    Configure inter wireless controller operation.
    
    **Usage:**
        payload: InterControllerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    inter_controller_mode: NotRequired[Literal["disable", "l2-roaming", "1+1"]]  # Configure inter-controller mode
    l3_roaming: NotRequired[Literal["enable", "disable"]]  # Enable/disable layer 3 roaming (default = disable).
    inter_controller_key: NotRequired[str]  # Secret key for inter-controller communications.
    inter_controller_pri: NotRequired[Literal["primary", "secondary"]]  # Configure inter-controller's priority
    fast_failover_max: NotRequired[int]  # Maximum number of retransmissions for fast failover HA messa
    fast_failover_wait: NotRequired[int]  # Minimum wait time before an AP transitions from secondary co
    inter_controller_peer: NotRequired[list[dict[str, Any]]]  # Fast failover peer wireless controller list.

# Nested classes for table field children

@final
class InterControllerIntercontrollerpeerObject:
    """Typed object for inter-controller-peer table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID.
    id: int
    # Peer wireless controller's IP address.
    peer_ip: str
    # Port used by the wireless controller's for inter-controller communications
    peer_port: int
    # Peer wireless controller's priority (primary or secondary, default = primary).
    peer_priority: Literal["primary", "secondary"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class InterControllerResponse(TypedDict):
    """
    Type hints for wireless_controller/inter_controller API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    inter_controller_mode: Literal["disable", "l2-roaming", "1+1"]
    l3_roaming: Literal["enable", "disable"]
    inter_controller_key: str
    inter_controller_pri: Literal["primary", "secondary"]
    fast_failover_max: int
    fast_failover_wait: int
    inter_controller_peer: list[dict[str, Any]]


@final
class InterControllerObject:
    """Typed FortiObject for wireless_controller/inter_controller with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure inter-controller mode (disable, l2-roaming, 1+1, default = disable).
    inter_controller_mode: Literal["disable", "l2-roaming", "1+1"]
    # Enable/disable layer 3 roaming (default = disable).
    l3_roaming: Literal["enable", "disable"]
    # Secret key for inter-controller communications.
    inter_controller_key: str
    # Configure inter-controller's priority (primary or secondary, default = primary).
    inter_controller_pri: Literal["primary", "secondary"]
    # Maximum number of retransmissions for fast failover HA messages between peer wir
    fast_failover_max: int
    # Minimum wait time before an AP transitions from secondary controller to primary
    fast_failover_wait: int
    # Fast failover peer wireless controller list.
    inter_controller_peer: list[InterControllerIntercontrollerpeerObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> InterControllerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class InterController:
    """
    Configure inter wireless controller operation.
    
    Path: wireless_controller/inter_controller
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerResponse: ...
    
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
    ) -> InterControllerResponse: ...
    
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
    ) -> InterControllerResponse: ...
    
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
    ) -> InterControllerObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InterControllerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "InterController",
    "InterControllerPayload",
    "InterControllerObject",
]