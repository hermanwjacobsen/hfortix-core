from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class MpskProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/mpsk_profile payload fields.
    
    Configure MPSK profile.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.radius.RadiusEndpoint` (via: mpsk-external-server)

    **Usage:**
        payload: MpskProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # MPSK profile name.
    mpsk_concurrent_clients: NotRequired[int]  # Maximum number of concurrent clients that connect using the 
    mpsk_external_server_auth: NotRequired[Literal["enable", "disable"]]  # Enable/Disable MPSK external server authentication (default 
    mpsk_external_server: NotRequired[str]  # RADIUS server to be used to authenticate MPSK users.
    mpsk_type: NotRequired[Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"]]  # Select the security type of keys for this profile.
    mpsk_group: NotRequired[list[dict[str, Any]]]  # List of multiple PSK groups.


class MpskProfileObject(FortiObject[MpskProfilePayload]):
    """Typed FortiObject for wireless_controller/mpsk_profile with IDE autocomplete support."""
    
    # MPSK profile name.
    name: str
    # Maximum number of concurrent clients that connect using the same passphrase in m
    mpsk_concurrent_clients: int
    # Enable/Disable MPSK external server authentication (default = disable).
    mpsk_external_server_auth: Literal["enable", "disable"]
    # RADIUS server to be used to authenticate MPSK users.
    mpsk_external_server: str
    # Select the security type of keys for this profile.
    mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"]
    # List of multiple PSK groups.
    mpsk_group: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> MpskProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class MpskProfile:
    """
    Configure MPSK profile.
    
    Path: wireless_controller/mpsk_profile
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
    ) -> MpskProfileObject: ...
    
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
    ) -> list[MpskProfileObject]: ...
    
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
    ) -> MpskProfileObject | list[MpskProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MpskProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MpskProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> MpskProfileObject: ...
    
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
        payload_dict: MpskProfilePayload | None = ...,
        name: str | None = ...,
        mpsk_concurrent_clients: int | None = ...,
        mpsk_external_server_auth: Literal["enable", "disable"] | None = ...,
        mpsk_external_server: str | None = ...,
        mpsk_type: Literal["wpa2-personal", "wpa3-sae", "wpa3-sae-transition"] | None = ...,
        mpsk_group: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "MpskProfile",
    "MpskProfilePayload",
    "MpskProfileObject",
]