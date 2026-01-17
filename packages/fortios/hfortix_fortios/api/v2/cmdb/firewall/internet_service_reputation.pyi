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
class InternetServiceReputationPayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service_reputation payload fields.
    
    Show Internet Service reputation.
    
    **Usage:**
        payload: InternetServiceReputationPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Internet Service Reputation ID. | Default: 0 | Min: 0 | Max: 4294967295
    description: str  # Description. | MaxLen: 127

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class InternetServiceReputationResponse(TypedDict):
    """
    Type hints for firewall/internet_service_reputation API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # Internet Service Reputation ID. | Default: 0 | Min: 0 | Max: 4294967295
    description: str  # Description. | MaxLen: 127


@final
class InternetServiceReputationObject:
    """Typed FortiObject for firewall/internet_service_reputation with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Internet Service Reputation ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Description. | MaxLen: 127
    description: str
    
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
    def to_dict(self) -> InternetServiceReputationPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class InternetServiceReputation:
    """
    Show Internet Service reputation.
    
    Path: firewall/internet_service_reputation
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
    ) -> InternetServiceReputationObject: ...
    
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
    ) -> InternetServiceReputationObject: ...
    
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
    ) -> FortiObjectList[InternetServiceReputationObject]: ...
    
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
    ) -> InternetServiceReputationObject: ...
    
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
    ) -> InternetServiceReputationObject: ...
    
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
    ) -> FortiObjectList[InternetServiceReputationObject]: ...
    
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
    ) -> InternetServiceReputationObject: ...
    
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
    ) -> InternetServiceReputationObject: ...
    
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
    ) -> FortiObjectList[InternetServiceReputationObject]: ...
    
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
    ) -> InternetServiceReputationObject | list[InternetServiceReputationObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> InternetServiceReputationObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> InternetServiceReputationObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
    ) -> InternetServiceReputationObject: ...
    
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
        payload_dict: InternetServiceReputationPayload | None = ...,
        id: int | None = ...,
        description: str | None = ...,
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
    "InternetServiceReputation",
    "InternetServiceReputationPayload",
    "InternetServiceReputationResponse",
    "InternetServiceReputationObject",
]