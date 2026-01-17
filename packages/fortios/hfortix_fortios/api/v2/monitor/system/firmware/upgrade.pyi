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
class UpgradePayload(TypedDict, total=False):
    """
    Type hints for system/firmware/upgrade payload fields.
    
    Upgrade firmware image on this device.
    
    **Usage:**
        payload: UpgradePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    source: str  # source
    url: str  # url
    passphrase: str  # passphrase
    force: bool  # force
    filename: str  # filename
    format_partition: bool  # format_partition
    ignore_invalid_signature: bool  # ignore_invalid_signature
    file_id: str  # file_id
    ignore_admin_lockout_upon_downgrade: bool  # ignore_admin_lockout_upon_downgrade
    file_content: str  # file_content

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class UpgradeResponse(TypedDict):
    """
    Type hints for system/firmware/upgrade API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    source: str
    url: str
    passphrase: str
    force: bool
    filename: str
    format_partition: bool
    ignore_invalid_signature: bool
    file_id: str
    ignore_admin_lockout_upon_downgrade: bool
    file_content: str


@final
class UpgradeObject:
    """Typed FortiObject for system/firmware/upgrade with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # source
    source: str
    # url
    url: str
    # passphrase
    passphrase: str
    # force
    force: bool
    # filename
    filename: str
    # format_partition
    format_partition: bool
    # ignore_invalid_signature
    ignore_invalid_signature: bool
    # file_id
    file_id: str
    # ignore_admin_lockout_upon_downgrade
    ignore_admin_lockout_upon_downgrade: bool
    # file_content
    file_content: str
    
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
    def to_dict(self) -> UpgradePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Upgrade:
    """
    Upgrade firmware image on this device.
    
    Path: system/firmware/upgrade
    Category: monitor
    """
    
    def __init__(self, client: Any) -> None:
        """Initialize endpoint with HTTP client.
        
        Args:
            client: HTTP client instance for API communication
        """
        ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject: ...
    
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
    ) -> UpgradeObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UpgradeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UpgradeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: UpgradePayload | None = ...,
        source: str | None = ...,
        url: str | None = ...,
        passphrase: str | None = ...,
        force: str | None = ...,
        filename: str | None = ...,
        format_partition: str | None = ...,
        ignore_invalid_signature: str | None = ...,
        file_id: str | None = ...,
        ignore_admin_lockout_upon_downgrade: str | None = ...,
        file_content: str | None = ...,
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
    "Upgrade",
    "UpgradePayload",
    "UpgradeResponse",
    "UpgradeObject",
]