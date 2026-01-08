from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class CaPayload(TypedDict, total=False):
    """
    Type hints for certificate/ca payload fields.
    
    CA certificate.
    
    **Usage:**
        payload: CaPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    ca: str  # CA certificate as a PEM file.
    range: NotRequired[Literal["global", "vdom"]]  # Either global or VDOM IP address range for the CA certificat
    source: NotRequired[Literal["factory", "user", "bundle"]]  # CA certificate source type.
    ssl_inspection_trusted: NotRequired[Literal["enable", "disable"]]  # Enable/disable this CA as a trusted CA for SSL inspection.
    scep_url: NotRequired[str]  # URL of the SCEP server.
    est_url: NotRequired[str]  # URL of the EST server.
    auto_update_days: NotRequired[int]  # Number of days to wait before requesting an updated CA certi
    auto_update_days_warning: NotRequired[int]  # Number of days before an expiry-warning message is generated
    source_ip: NotRequired[str]  # Source IP address for communications to the SCEP server.
    ca_identifier: NotRequired[str]  # CA identifier of the SCEP server.
    obsolete: NotRequired[Literal["disable", "enable"]]  # Enable/disable this CA as obsoleted.
    fabric_ca: NotRequired[Literal["disable", "enable"]]  # Enable/disable synchronization of CA across Security Fabric.
    details: NotRequired[str]  # Print CA certificate detailed information.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class CaResponse(TypedDict):
    """
    Type hints for certificate/ca API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    ca: str
    range: Literal["global", "vdom"]
    source: Literal["factory", "user", "bundle"]
    ssl_inspection_trusted: Literal["enable", "disable"]
    scep_url: str
    est_url: str
    auto_update_days: int
    auto_update_days_warning: int
    source_ip: str
    ca_identifier: str
    obsolete: Literal["disable", "enable"]
    fabric_ca: Literal["disable", "enable"]
    details: str


@final
class CaObject:
    """Typed FortiObject for certificate/ca with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # CA certificate as a PEM file.
    ca: str
    # Either global or VDOM IP address range for the CA certificate.
    range: Literal["global", "vdom"]
    # CA certificate source type.
    source: Literal["factory", "user", "bundle"]
    # Enable/disable this CA as a trusted CA for SSL inspection.
    ssl_inspection_trusted: Literal["enable", "disable"]
    # URL of the SCEP server.
    scep_url: str
    # URL of the EST server.
    est_url: str
    # Number of days to wait before requesting an updated CA certificate
    auto_update_days: int
    # Number of days before an expiry-warning message is generated
    auto_update_days_warning: int
    # Source IP address for communications to the SCEP server.
    source_ip: str
    # CA identifier of the SCEP server.
    ca_identifier: str
    # Enable/disable this CA as obsoleted.
    obsolete: Literal["disable", "enable"]
    # Enable/disable synchronization of CA across Security Fabric.
    fabric_ca: Literal["disable", "enable"]
    # Print CA certificate detailed information.
    details: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CaPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ca:
    """
    CA certificate.
    
    Path: certificate/ca
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CaObject: ...
    
    # Single object (mkey/name provided as keyword arg)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CaObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[CaObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> CaResponse: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> CaResponse: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[CaResponse]: ...
    
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
    ) -> CaObject | list[CaObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CaObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
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
        payload_dict: CaPayload | None = ...,
        name: str | None = ...,
        ca: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        ssl_inspection_trusted: Literal["enable", "disable"] | None = ...,
        scep_url: str | None = ...,
        est_url: str | None = ...,
        auto_update_days: int | None = ...,
        auto_update_days_warning: int | None = ...,
        source_ip: str | None = ...,
        ca_identifier: str | None = ...,
        obsolete: Literal["disable", "enable"] | None = ...,
        fabric_ca: Literal["disable", "enable"] | None = ...,
        details: str | None = ...,
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
    "Ca",
    "CaPayload",
    "CaObject",
]