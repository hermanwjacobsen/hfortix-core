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
class IpsUrlfilterDnsPayload(TypedDict, total=False):
    """
    Type hints for system/ips_urlfilter_dns payload fields.
    
    Configure IPS URL filter DNS servers.
    
    **Usage:**
        payload: IpsUrlfilterDnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    address: str  # DNS server IP address. | Default: 0.0.0.0
    status: Literal["enable", "disable"]  # Enable/disable using this DNS server for IPS URL f | Default: enable
    ipv6_capability: Literal["enable", "disable"]  # Enable/disable this server for IPv6 queries. | Default: disable

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class IpsUrlfilterDnsResponse(TypedDict):
    """
    Type hints for system/ips_urlfilter_dns API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    address: str  # DNS server IP address. | Default: 0.0.0.0
    status: Literal["enable", "disable"]  # Enable/disable using this DNS server for IPS URL f | Default: enable
    ipv6_capability: Literal["enable", "disable"]  # Enable/disable this server for IPv6 queries. | Default: disable


@final
class IpsUrlfilterDnsObject:
    """Typed FortiObject for system/ips_urlfilter_dns with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # DNS server IP address. | Default: 0.0.0.0
    address: str
    # Enable/disable using this DNS server for IPS URL filter DNS | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable this server for IPv6 queries. | Default: disable
    ipv6_capability: Literal["enable", "disable"]
    
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
    def to_dict(self) -> IpsUrlfilterDnsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class IpsUrlfilterDns:
    """
    Configure IPS URL filter DNS servers.
    
    Path: system/ips_urlfilter_dns
    Category: cmdb
    Primary Key: address
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
        address: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        address: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        address: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> FortiObjectList[IpsUrlfilterDnsObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        address: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        address: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
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
    ) -> FortiObjectList[IpsUrlfilterDnsObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        address: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        address: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
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
    ) -> FortiObjectList[IpsUrlfilterDnsObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        address: str | None = ...,
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
        address: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
    ) -> IpsUrlfilterDnsObject | list[IpsUrlfilterDnsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        address: str | None = ...,
    ) -> IpsUrlfilterDnsObject: ...
    
    @overload
    def delete(
        self,
        address: str | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        address: str | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        address: str | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        address: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
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
    "IpsUrlfilterDns",
    "IpsUrlfilterDnsPayload",
    "IpsUrlfilterDnsResponse",
    "IpsUrlfilterDnsObject",
]