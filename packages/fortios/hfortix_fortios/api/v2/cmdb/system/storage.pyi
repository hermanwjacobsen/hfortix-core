from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class StoragePayload(TypedDict, total=False):
    """
    Type hints for system/storage payload fields.
    
    Configure logical storage.
    
    **Usage:**
        payload: StoragePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Storage name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable storage.
    media_status: NotRequired[Literal["enable", "disable", "fail"]]  # The physical status of current media.
    order: NotRequired[int]  # Set storage order.
    partition: NotRequired[str]  # Label of underlying partition.
    device: NotRequired[str]  # Partition device.
    size: NotRequired[int]  # Partition size.
    usage: NotRequired[Literal["log", "wanopt"]]  # Use hard disk for logging or WAN Optimization
    wanopt_mode: NotRequired[Literal["mix", "wanopt", "webcache"]]  # WAN Optimization mode (default = mix).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class StorageResponse(TypedDict):
    """
    Type hints for system/storage API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["enable", "disable"]
    media_status: Literal["enable", "disable", "fail"]
    order: int
    partition: str
    device: str
    size: int
    usage: Literal["log", "wanopt"]
    wanopt_mode: Literal["mix", "wanopt", "webcache"]


@final
class StorageObject:
    """Typed FortiObject for system/storage with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Storage name.
    name: str
    # Enable/disable storage.
    status: Literal["enable", "disable"]
    # The physical status of current media.
    media_status: Literal["enable", "disable", "fail"]
    # Set storage order.
    order: int
    # Label of underlying partition.
    partition: str
    # Partition device.
    device: str
    # Partition size.
    size: int
    # Use hard disk for logging or WAN Optimization (default = log).
    usage: Literal["log", "wanopt"]
    # WAN Optimization mode (default = mix).
    wanopt_mode: Literal["mix", "wanopt", "webcache"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> StoragePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Storage:
    """
    Configure logical storage.
    
    Path: system/storage
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
    ) -> StorageObject: ...
    
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
    ) -> StorageObject: ...
    
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
    ) -> list[StorageObject]: ...
    
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
    ) -> StorageResponse: ...
    
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
    ) -> StorageResponse: ...
    
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
    ) -> list[StorageResponse]: ...
    
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
    ) -> StorageObject | list[StorageObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StorageObject: ...
    
    @overload
    def post(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> StorageObject: ...
    
    @overload
    def put(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
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
    ) -> StorageObject: ...
    
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
        payload_dict: StoragePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        media_status: Literal["enable", "disable", "fail"] | None = ...,
        order: int | None = ...,
        partition: str | None = ...,
        device: str | None = ...,
        size: int | None = ...,
        usage: Literal["log", "wanopt"] | None = ...,
        wanopt_mode: Literal["mix", "wanopt", "webcache"] | None = ...,
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
    "Storage",
    "StoragePayload",
    "StorageObject",
]