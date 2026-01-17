from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class AcmeInterfaceItem(TypedDict, total=False):
    """Type hints for interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - interface_name: str
    
    **Example:**
        entry: AcmeInterfaceItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    interface_name: str  # Interface name. | MaxLen: 79


class AcmeAccountsItem(TypedDict, total=False):
    """Type hints for accounts table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: str
        - status: str
        - url: str
        - ca_url: str
        - email: str
        - eab_key_id: str
        - eab_key_hmac: str
        - privatekey: str
    
    **Example:**
        entry: AcmeAccountsItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: str  # Account id. | MaxLen: 255
    status: str  # Account status. | MaxLen: 127
    url: str  # Account url. | MaxLen: 511
    ca_url: str  # Account ca_url. | MaxLen: 255
    email: str  # Account email. | MaxLen: 255
    eab_key_id: str  # External Acccount Binding Key ID. | MaxLen: 255
    eab_key_hmac: str  # External Acccount Binding Key HMAC. | MaxLen: 128
    privatekey: str  # Account Private Key. | MaxLen: 8191


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AcmePayload(TypedDict, total=False):
    """
    Type hints for system/acme payload fields.
    
    Configure ACME client.
    
    **Usage:**
        payload: AcmePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    interface: list[AcmeInterfaceItem]  # Interface(s) on which the ACME client will listen
    use_ha_direct: Literal["enable", "disable"]  # Enable the use of 'ha-mgmt' interface to connect t | Default: disable
    source_ip: str  # Source IPv4 address used to connect to the ACME se | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address used to connect to the ACME se | Default: ::
    accounts: list[AcmeAccountsItem]  # ACME accounts list.
    acc_details: str  # Print Account information and decrypted key.
    status: str  # Print information about the current status of the

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class AcmeInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    interface_name: str
    
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


@final
class AcmeAccountsObject:
    """Typed object for accounts table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Account id. | MaxLen: 255
    id: str
    # Account status. | MaxLen: 127
    status: str
    # Account url. | MaxLen: 511
    url: str
    # Account ca_url. | MaxLen: 255
    ca_url: str
    # Account email. | MaxLen: 255
    email: str
    # External Acccount Binding Key ID. | MaxLen: 255
    eab_key_id: str
    # External Acccount Binding Key HMAC. | MaxLen: 128
    eab_key_hmac: str
    # Account Private Key. | MaxLen: 8191
    privatekey: str
    
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
class AcmeResponse(TypedDict):
    """
    Type hints for system/acme API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    interface: list[AcmeInterfaceItem]  # Interface(s) on which the ACME client will listen
    use_ha_direct: Literal["enable", "disable"]  # Enable the use of 'ha-mgmt' interface to connect t | Default: disable
    source_ip: str  # Source IPv4 address used to connect to the ACME se | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address used to connect to the ACME se | Default: ::
    accounts: list[AcmeAccountsItem]  # ACME accounts list.
    acc_details: str  # Print Account information and decrypted key.
    status: str  # Print information about the current status of the


@final
class AcmeObject:
    """Typed FortiObject for system/acme with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Interface(s) on which the ACME client will listen for challe
    interface: list[AcmeInterfaceObject]
    # Enable the use of 'ha-mgmt' interface to connect to the ACME | Default: disable
    use_ha_direct: Literal["enable", "disable"]
    # Source IPv4 address used to connect to the ACME server. | Default: 0.0.0.0
    source_ip: str
    # Source IPv6 address used to connect to the ACME server. | Default: ::
    source_ip6: str
    # ACME accounts list.
    accounts: list[AcmeAccountsObject]
    # Print Account information and decrypted key.
    acc_details: str
    # Print information about the current status of the acme clien
    status: str
    
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
    def to_dict(self) -> AcmePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Acme:
    """
    Configure ACME client.
    
    Path: system/acme
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject: ...
    
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
    ) -> AcmeObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[AcmeInterfaceItem] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[AcmeAccountsItem] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
    ) -> AcmeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[AcmeInterfaceItem] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[AcmeAccountsItem] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[AcmeInterfaceItem] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[AcmeAccountsItem] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[AcmeInterfaceItem] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[AcmeAccountsItem] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AcmePayload | None = ...,
        interface: str | list[str] | list[AcmeInterfaceItem] | None = ...,
        use_ha_direct: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        accounts: str | list[str] | list[AcmeAccountsItem] | None = ...,
        acc_details: str | None = ...,
        status: str | None = ...,
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
    "Acme",
    "AcmePayload",
    "AcmeResponse",
    "AcmeObject",
]