from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class InternetServiceAdditionEntryItem(TypedDict, total=False):
    """Type hints for entry table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - addr_mode: "ipv4" | "ipv6"
        - protocol: int
        - port_range: str
    
    **Example:**
        entry: InternetServiceAdditionEntryItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Entry ID(1-255). | Default: 0 | Min: 0 | Max: 255
    addr_mode: Literal["ipv4", "ipv6"]  # Address mode (IPv4 or IPv6). | Default: ipv4
    protocol: int  # Integer value for the protocol type as defined by | Default: 0 | Min: 0 | Max: 255
    port_range: str  # Port ranges in the custom entry.


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class InternetServiceAdditionPayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service_addition payload fields.
    
    Configure Internet Services Addition.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.internet-service.InternetServiceEndpoint` (via: id)

    **Usage:**
        payload: InternetServiceAdditionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Internet Service ID in the Internet Service databa | Default: 0 | Min: 0 | Max: 4294967295
    comment: str  # Comment. | MaxLen: 255
    entry: list[InternetServiceAdditionEntryItem]  # Entries added to the Internet Service addition dat

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class InternetServiceAdditionEntryObject:
    """Typed object for entry table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID(1-255). | Default: 0 | Min: 0 | Max: 255
    id: int
    # Address mode (IPv4 or IPv6). | Default: ipv4
    addr_mode: Literal["ipv4", "ipv6"]
    # Integer value for the protocol type as defined by IANA | Default: 0 | Min: 0 | Max: 255
    protocol: int
    # Port ranges in the custom entry.
    port_range: str
    
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
class InternetServiceAdditionResponse(TypedDict):
    """
    Type hints for firewall/internet_service_addition API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # Internet Service ID in the Internet Service databa | Default: 0 | Min: 0 | Max: 4294967295
    comment: str  # Comment. | MaxLen: 255
    entry: list[InternetServiceAdditionEntryItem]  # Entries added to the Internet Service addition dat


@final
class InternetServiceAdditionObject:
    """Typed FortiObject for firewall/internet_service_addition with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Internet Service ID in the Internet Service database. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Comment. | MaxLen: 255
    comment: str
    # Entries added to the Internet Service addition database.
    entry: list[InternetServiceAdditionEntryObject]
    
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
    def to_dict(self) -> InternetServiceAdditionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class InternetServiceAddition:
    """
    Configure Internet Services Addition.
    
    Path: firewall/internet_service_addition
    Category: cmdb
    Primary Key: id
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
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> FortiObjectList[InternetServiceAdditionObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
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
    ) -> FortiObjectList[InternetServiceAdditionObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
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
    ) -> FortiObjectList[InternetServiceAdditionObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
    def get(
        self,
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> InternetServiceAdditionObject | list[InternetServiceAdditionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
    ) -> InternetServiceAdditionObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        id: int | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        id: int,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InternetServiceAdditionPayload | None = ...,
        id: int | None = ...,
        comment: str | None = ...,
        entry: str | list[str] | list[InternetServiceAdditionEntryItem] | None = ...,
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
    "InternetServiceAddition",
    "InternetServiceAdditionPayload",
    "InternetServiceAdditionResponse",
    "InternetServiceAdditionObject",
]