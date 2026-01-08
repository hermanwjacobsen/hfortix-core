from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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
    name: NotRequired[str]  # Name.
    description: NotRequired[str]  # Description.
    status: Literal["enable", "disable"]  # Enable/disable this stitch.
    trigger: str  # Trigger name.
    condition: NotRequired[list[dict[str, Any]]]  # Automation conditions.
    condition_logic: Literal["and", "or"]  # Apply AND/OR logic to the specified automation conditions.
    actions: NotRequired[list[dict[str, Any]]]  # Configure stitch actions.
    destination: NotRequired[list[dict[str, Any]]]  # Serial number/HA group-name of destination devices.

# Nested classes for table field children

@final
class AutomationStitchConditionObject:
    """Typed object for condition table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Condition name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationStitchActionsObject:
    """Typed object for actions table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Action name.
    action: str
    # Delay before execution (in seconds).
    delay: int
    # Required in action chain.
    required: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationStitchDestinationObject:
    """Typed object for destination table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Destination name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AutomationStitchResponse(TypedDict):
    """
    Type hints for system/automation_stitch API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    status: Literal["enable", "disable"]
    trigger: str
    condition: list[dict[str, Any]]
    condition_logic: Literal["and", "or"]
    actions: list[dict[str, Any]]
    destination: list[dict[str, Any]]


@final
class AutomationStitchObject:
    """Typed FortiObject for system/automation_stitch with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # Description.
    description: str
    # Enable/disable this stitch.
    status: Literal["enable", "disable"]
    # Trigger name.
    trigger: str
    # Automation conditions.
    condition: list[AutomationStitchConditionObject]  # Table field - list of typed objects
    # Apply AND/OR logic to the specified automation conditions.
    condition_logic: Literal["and", "or"]
    # Configure stitch actions.
    actions: list[AutomationStitchActionsObject]  # Table field - list of typed objects
    # Serial number/HA group-name of destination devices.
    destination: list[AutomationStitchDestinationObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AutomationStitchPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AutomationStitch:
    """
    Automation stitches.
    
    Path: system/automation_stitch
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> AutomationStitchObject: ...
    
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
    ) -> list[AutomationStitchObject]: ...
    
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
    ) -> AutomationStitchResponse: ...
    
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
    ) -> AutomationStitchResponse: ...
    
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
    ) -> list[AutomationStitchResponse]: ...
    
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
    ) -> AutomationStitchObject | list[AutomationStitchObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationStitchObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationStitchObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationStitchObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AutomationStitchPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trigger: str | None = ...,
        condition: str | list[str] | list[dict[str, Any]] | None = ...,
        condition_logic: Literal["and", "or"] | None = ...,
        actions: str | list[str] | list[dict[str, Any]] | None = ...,
        destination: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "AutomationStitch",
    "AutomationStitchPayload",
    "AutomationStitchObject",
]