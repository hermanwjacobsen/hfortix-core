from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RestorePayload(TypedDict, total=False):
    """
    Type hints for system/config/restore payload fields.
    
    Restore system configuration from uploaded file or from USB.
    
    **Usage:**
        payload: RestorePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    source: str  # source
    usb_filename: str  # usb_filename
    config_id: str  # config_id
    password: str  # password
    scope: str  # scope
    vdom: str  # vdom
    confirm_password_mask: str  # confirm_password_mask
    file_content: str  # file_content

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class RestoreResponse(TypedDict):
    """
    Type hints for system/config/restore API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    source: str
    usb_filename: str
    config_id: str
    password: str
    scope: str
    vdom: str
    confirm_password_mask: str
    file_content: str


@final
class RestoreObject:
    """Typed FortiObject for system/config/restore with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # source
    source: str
    # usb_filename
    usb_filename: str
    # config_id
    config_id: str
    # password
    password: str
    # scope
    scope: str
    # vdom
    vdom: str
    # confirm_password_mask
    confirm_password_mask: str
    # file_content
    file_content: str
    
    # Common API response fields
    status: str
    http_status: int | None
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
    def to_dict(self) -> RestorePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Restore:
    """
    Restore system configuration from uploaded file or from USB.
    
    Path: system/config/restore
    Category: monitor
    """
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject: ...
    
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
    ) -> RestoreObject | dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RestoreObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RestoreObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
        file_content: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
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
        payload_dict: RestorePayload | None = ...,
        source: str | None = ...,
        usb_filename: str | None = ...,
        config_id: str | None = ...,
        password: str | None = ...,
        scope: str | None = ...,
        confirm_password_mask: str | None = ...,
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
    "Restore",
    "RestorePayload",
    "RestoreResponse",
    "RestoreObject",
]