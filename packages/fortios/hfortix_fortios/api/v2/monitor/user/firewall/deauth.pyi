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
class DeauthPayload(TypedDict, total=False):
    """
    Type hints for user/firewall/deauth payload fields.
    
    Deauthenticate single, multiple, or all firewall users.
    
    **Usage:**
        payload: DeauthPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    user_type: str  # user_type
    id: int  # id
    ip: str  # ip
    ip_version: str  # ip_version
    method: str  # method
    all: bool  # all
    users: str  # users

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class DeauthResponse(TypedDict):
    """
    Type hints for user/firewall/deauth API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    user_type: str
    id: int
    ip: str
    ip_version: str
    method: str
    all: bool
    users: str


@final
class DeauthObject:
    """Typed FortiObject for user/firewall/deauth with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # user_type
    user_type: str
    # id
    id: int
    # ip
    ip: str
    # ip_version
    ip_version: str
    # method
    method: str
    # all
    all: bool
    # users
    users: str
    
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
    def to_dict(self) -> DeauthPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Deauth:
    """
    Deauthenticate single, multiple, or all firewall users.
    
    Path: user/firewall/deauth
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject: ...
    
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
    ) -> DeauthObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DeauthObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DeauthObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DeauthPayload | None = ...,
        user_type: str | None = ...,
        id: int | None = ...,
        ip: str | None = ...,
        ip_version: str | None = ...,
        method: str | None = ...,
        all: str | None = ...,
        users: str | None = ...,
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
    "Deauth",
    "DeauthPayload",
    "DeauthResponse",
    "DeauthObject",
]