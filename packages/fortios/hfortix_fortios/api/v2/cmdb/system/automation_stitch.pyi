from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class AutomationStitchConditionItem(TypedDict, total=False):
    """Type hints for condition table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: AutomationStitchConditionItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Condition name. | MaxLen: 79


class AutomationStitchActionsItem(TypedDict, total=False):
    """Type hints for actions table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - id: int
        - action: str
        - delay: int
        - required: "enable" | "disable"
    
    **Example:**
        entry: AutomationStitchActionsItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    action: str  # Action name. | MaxLen: 64
    delay: int  # Delay before execution (in seconds). | Default: 0 | Min: 0 | Max: 3600
    required: Literal["enable", "disable"]  # Required in action chain. | Default: disable


class AutomationStitchDestinationItem(TypedDict, total=False):
    """Type hints for destination table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: AutomationStitchDestinationItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Destination name. | MaxLen: 79


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AutomationStitchPayload(TypedDict, total=False):
    """
    Type hints for system/automation_stitch payload fields.
    
    Automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.automation-trigger.AutomationTriggerEndpoint` (via: trigger)

    **Usage:**
        payload: AutomationStitchPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    description: str  # Description. | MaxLen: 255
    status: Literal["enable", "disable"]  # Enable/disable this stitch. | Default: enable
    trigger: str  # Trigger name. | MaxLen: 35
    condition: list[AutomationStitchConditionItem]  # Automation conditions.
    condition_logic: Literal["and", "or"]  # Apply AND/OR logic to the specified automation con | Default: and
    actions: list[AutomationStitchActionsItem]  # Configure stitch actions.
    destination: list[AutomationStitchDestinationItem]  # Serial number/HA group-name of destination devices

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class AutomationStitchConditionObject:
    """Typed object for condition table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Condition name. | MaxLen: 79
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


@final
class AutomationStitchActionsObject:
    """Typed object for actions table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Action name. | MaxLen: 64
    action: str
    # Delay before execution (in seconds). | Default: 0 | Min: 0 | Max: 3600
    delay: int
    # Required in action chain. | Default: disable
    required: Literal["enable", "disable"]
    
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
class AutomationStitchDestinationObject:
    """Typed object for destination table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Destination name. | MaxLen: 79
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
class AutomationStitchResponse(TypedDict):
    """
    Type hints for system/automation_stitch API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    description: str  # Description. | MaxLen: 255
    status: Literal["enable", "disable"]  # Enable/disable this stitch. | Default: enable
    trigger: str  # Trigger name. | MaxLen: 35
    condition: list[AutomationStitchConditionItem]  # Automation conditions.
    condition_logic: Literal["and", "or"]  # Apply AND/OR logic to the specified automation con | Default: and
    actions: list[AutomationStitchActionsItem]  # Configure stitch actions.
    destination: list[AutomationStitchDestinationItem]  # Serial number/HA group-name of destination devices


@final
class AutomationStitchObject:
    """Typed FortiObject for system/automation_stitch with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Description. | MaxLen: 255
    description: str
    # Enable/disable this stitch. | Default: enable
    status: Literal["enable", "disable"]
    # Trigger name. | MaxLen: 35
    trigger: str
    # Automation conditions.
    condition: list[AutomationStitchConditionObject]
    # Apply AND/OR logic to the specified automation conditions. | Default: and
    condition_logic: Literal["and", "or"]
    # Configure stitch actions.
    actions: list[AutomationStitchActionsObject]
    # Serial number/HA group-name of destination devices.
    destination: list[AutomationStitchDestinationObject]
    
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
    def to_dict(self) -> AutomationStitchPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutomationStitch:
    """
    Automation stitches.
    
    Path: system/automation_stitch
    Category: cmdb
    Primary Key: name
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> FortiObjectList[AutomationStitchObject]: ...
    
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> FortiObjectList[AutomationStitchObject]: ...
    
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> FortiObjectList[AutomationStitchObject]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
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
    ) -> AutomationStitchObject | list[AutomationStitchObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> AutomationStitchObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> AutomationStitchObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
    ) -> AutomationStitchObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[AutomationStitchConditionItem] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[AutomationStitchActionsItem] | None = ...,
        destination: str | list[str] | list[AutomationStitchDestinationItem] | None = ...,
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
    "AutomationStitch",
    "AutomationStitchPayload",
    "AutomationStitchResponse",
    "AutomationStitchObject",
]