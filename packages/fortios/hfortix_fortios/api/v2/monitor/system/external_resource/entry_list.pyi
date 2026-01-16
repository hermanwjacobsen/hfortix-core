from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class EntryListPayload(TypedDict, total=False):
    """
    Type hints for system/external_resource/entry_list payload fields.
    
    Retrieve resource file status with a list of valid/invalid entries for the specific external resource. Empty lines and comment lines are not returned.
    
    **Usage:**
        payload: EntryListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mkey: str  # mkey
    status_only: bool  # status_only
    include_notes: bool  # include_notes
    counts_only: bool  # counts_only
    entry: str  # entry

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class EntryListResponse(TypedDict):
    """
    Type hints for system/external_resource/entry_list API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: str
    error: str
    error_code: int
    http_status_code: int
    conn_attempt_time: int
    resource_file_status: str
    last_content_update_time: int
    last_conn_success_time: int
    entries: str
    invalid_count: int
    valid_count: int
    accepted_count: int
    accepted_limit: int
    overflow: bool
    matched_invalid: int
    matched_valid: int
    notes: str


@final
class EntryListObject:
    """Typed FortiObject for system/external_resource/entry_list with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # status
    status: str
    # error
    error: str
    # error_code
    error_code: int
    # http_status_code
    http_status_code: int
    # conn_attempt_time
    conn_attempt_time: int
    # resource_file_status
    resource_file_status: str
    # last_content_update_time
    last_content_update_time: int
    # last_conn_success_time
    last_conn_success_time: int
    # entries
    entries: str
    # invalid_count
    invalid_count: int
    # valid_count
    valid_count: int
    # accepted_count
    accepted_count: int
    # accepted_limit
    accepted_limit: int
    # overflow
    overflow: bool
    # matched_invalid
    matched_invalid: int
    # matched_valid
    matched_valid: int
    # notes
    notes: str
    
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
    def to_dict(self) -> EntryListPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class EntryList:
    """
    Retrieve resource file status with a list of valid/invalid entries for the specific external resource. Empty lines and comment lines are not returned.
    
    Path: system/external_resource/entry_list
    Category: monitor
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # Service/Monitor endpoint with query parameters
    @overload
    def get(
        self,
        *,
        mkey: str,
        status_only: str | None = ...,
        include_notes: str | None = ...,
        counts_only: str | None = ...,
        entry: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> EntryListObject: ...
    
    
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
    ) -> EntryListObject: ...
    
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
    ) -> EntryListObject: ...
    
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
    ) -> EntryListObject: ...
    
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
    ) -> EntryListObject: ...
    
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
    ) -> EntryListObject: ...
    
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
    ) -> EntryListObject: ...
    
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
    ) -> EntryListObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: EntryListPayload | None = ...,
        mkey: str | None = ...,
        status_only: str | None = ...,
        include_notes: str | None = ...,
        counts_only: str | None = ...,
        entry: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> EntryListObject: ...
    
    @overload
    def put(
        self,
        payload_dict: EntryListPayload | None = ...,
        mkey: str | None = ...,
        status_only: str | None = ...,
        include_notes: str | None = ...,
        counts_only: str | None = ...,
        entry: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: EntryListPayload | None = ...,
        mkey: str | None = ...,
        status_only: str | None = ...,
        include_notes: str | None = ...,
        counts_only: str | None = ...,
        entry: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: EntryListPayload | None = ...,
        mkey: str | None = ...,
        status_only: str | None = ...,
        include_notes: str | None = ...,
        counts_only: str | None = ...,
        entry: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: EntryListPayload | None = ...,
        mkey: str | None = ...,
        status_only: str | None = ...,
        include_notes: str | None = ...,
        counts_only: str | None = ...,
        entry: str | None = ...,
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
    "EntryList",
    "EntryListPayload",
    "EntryListResponse",
    "EntryListObject",
]