from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SettingsPayload(TypedDict, total=False):
    """
    Type hints for dlp/settings payload fields.
    
    Configure settings for DLP.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.storage.StorageEndpoint` (via: storage-device)

    **Usage:**
        payload: SettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    storage_device: NotRequired[str]  # Storage device name.
    size: NotRequired[int]  # Maximum total size of files within the DLP fingerprint datab
    db_mode: NotRequired[Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"]]  # Behavior when the maximum size is reached in the DLP fingerp
    cache_mem_percent: NotRequired[int]  # Maximum percentage of available memory allocated to caching 
    chunk_size: NotRequired[int]  # Maximum fingerprint chunk size. Caution, changing this setti
    config_builder_timeout: NotRequired[int]  # Maximum time allowed for building a single DLP profile (defa


class SettingsObject(FortiObject[SettingsPayload]):
    """Typed FortiObject for dlp/settings with IDE autocomplete support."""
    
    # Storage device name.
    storage_device: str
    # Maximum total size of files within the DLP fingerprint database (MB).
    size: int
    # Behavior when the maximum size is reached in the DLP fingerprint database.
    db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"]
    # Maximum percentage of available memory allocated to caching DLP fingerprints (1 
    cache_mem_percent: int
    # Maximum fingerprint chunk size. Caution, changing this setting will flush the en
    chunk_size: int
    # Maximum time allowed for building a single DLP profile (default 60 seconds).
    config_builder_timeout: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Settings:
    """
    Configure settings for DLP.
    
    Path: dlp/settings
    Category: cmdb
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
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
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
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
    "Settings",
    "SettingsPayload",
    "SettingsObject",
]