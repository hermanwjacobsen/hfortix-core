from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class AuthPortalGroupsItem(TypedDict, total=False):
    """Type hints for groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: AuthPortalGroupsItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Group name. | MaxLen: 79


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AuthPortalPayload(TypedDict, total=False):
    """
    Type hints for firewall/auth_portal payload fields.
    
    Configure firewall authentication portals.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.identity-based-route.IdentityBasedRouteEndpoint` (via: identity-based-route)

    **Usage:**
        payload: AuthPortalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    groups: list[AuthPortalGroupsItem]  # Firewall user groups permitted to authenticate thr
    portal_addr: str  # Address (or FQDN) of the authentication portal. | MaxLen: 63
    portal_addr6: str  # IPv6 address (or FQDN) of authentication portal. | MaxLen: 63
    identity_based_route: str  # Name of the identity-based route that applies to t | MaxLen: 35
    proxy_auth: Literal["enable", "disable"]  # Enable/disable authentication by proxy daemon | Default: disable

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class AuthPortalGroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name. | MaxLen: 79
    name: str
    
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
class AuthPortalResponse(TypedDict):
    """
    Type hints for firewall/auth_portal API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    groups: list[AuthPortalGroupsItem]  # Firewall user groups permitted to authenticate thr
    portal_addr: str  # Address (or FQDN) of the authentication portal. | MaxLen: 63
    portal_addr6: str  # IPv6 address (or FQDN) of authentication portal. | MaxLen: 63
    identity_based_route: str  # Name of the identity-based route that applies to t | MaxLen: 35
    proxy_auth: Literal["enable", "disable"]  # Enable/disable authentication by proxy daemon | Default: disable


@final
class AuthPortalObject:
    """Typed FortiObject for firewall/auth_portal with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Firewall user groups permitted to authenticate through this
    groups: list[AuthPortalGroupsObject]
    # Address (or FQDN) of the authentication portal. | MaxLen: 63
    portal_addr: str
    # IPv6 address (or FQDN) of authentication portal. | MaxLen: 63
    portal_addr6: str
    # Name of the identity-based route that applies to this portal | MaxLen: 35
    identity_based_route: str
    # Enable/disable authentication by proxy daemon | Default: disable
    proxy_auth: Literal["enable", "disable"]
    
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
    def to_dict(self) -> AuthPortalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AuthPortal:
    """
    Configure firewall authentication portals.
    
    Path: firewall/auth_portal
    Category: cmdb
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject: ...
    
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
    ) -> AuthPortalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AuthPortalPayload | None = ...,
        groups: str | list[str] | list[AuthPortalGroupsItem] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AuthPortalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AuthPortalPayload | None = ...,
        groups: str | list[str] | list[AuthPortalGroupsItem] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AuthPortalPayload | None = ...,
        groups: str | list[str] | list[AuthPortalGroupsItem] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AuthPortalPayload | None = ...,
        groups: str | list[str] | list[AuthPortalGroupsItem] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AuthPortalPayload | None = ...,
        groups: str | list[str] | list[AuthPortalGroupsItem] | None = ...,
        portal_addr: str | None = ...,
        portal_addr6: str | None = ...,
        identity_based_route: str | None = ...,
        proxy_auth: Literal["enable", "disable"] | None = ...,
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
    "AuthPortal",
    "AuthPortalPayload",
    "AuthPortalResponse",
    "AuthPortalObject",
]