from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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
    usage: NotRequired[Literal["log", "wanopt"]]  # Use hard disk for logging or WAN Optimization (default = log
    wanopt_mode: NotRequired[Literal["mix", "wanopt", "webcache"]]  # WAN Optimization mode (default = mix).


class StorageObject(FortiObject[StoragePayload]):
    """Typed FortiObject for system/storage with IDE autocomplete support."""
    
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
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> StoragePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Storage:
    """
    Configure logical storage.
    
    Path: system/storage
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
    ) -> StorageObject: ...
    
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