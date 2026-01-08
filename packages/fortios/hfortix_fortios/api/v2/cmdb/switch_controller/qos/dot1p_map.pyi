from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class Dot1pMapPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/qos/dot1p_map payload fields.
    
    Configure FortiSwitch QoS 802.1p.
    
    **Usage:**
        payload: Dot1pMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Dot1p map name.
    description: NotRequired[str]  # Description of the 802.1p name.
    egress_pri_tagging: Literal["disable", "enable"]  # Enable/disable egress priority-tag frame.
    priority_0: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_1: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_2: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_3: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_4: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_5: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_6: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.
    priority_7: NotRequired[Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]]  # COS queue mapped to dot1p priority number.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class Dot1pMapResponse(TypedDict):
    """
    Type hints for switch_controller/qos/dot1p_map API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    egress_pri_tagging: Literal["disable", "enable"]
    priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]


@final
class Dot1pMapObject:
    """Typed FortiObject for switch_controller/qos/dot1p_map with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Dot1p map name.
    name: str
    # Description of the 802.1p name.
    description: str
    # Enable/disable egress priority-tag frame.
    egress_pri_tagging: Literal["disable", "enable"]
    # COS queue mapped to dot1p priority number.
    priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    # COS queue mapped to dot1p priority number.
    priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Dot1pMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Dot1pMap:
    """
    Configure FortiSwitch QoS 802.1p.
    
    Path: switch_controller/qos/dot1p_map
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
    ) -> Dot1pMapObject: ...
    
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
    ) -> Dot1pMapObject: ...
    
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
    ) -> list[Dot1pMapObject]: ...
    
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
    ) -> Dot1pMapResponse: ...
    
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
    ) -> Dot1pMapResponse: ...
    
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
    ) -> list[Dot1pMapResponse]: ...
    
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
    ) -> Dot1pMapObject | list[Dot1pMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Dot1pMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Dot1pMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
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
    ) -> Dot1pMapObject: ...
    
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
        payload_dict: Dot1pMapPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        egress_pri_tagging: Literal["disable", "enable"] | None = ...,
        priority_0: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_1: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_2: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_3: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_4: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_5: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_6: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
        priority_7: Literal["queue-0", "queue-1", "queue-2", "queue-3", "queue-4", "queue-5", "queue-6", "queue-7"] | None = ...,
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
    "Dot1pMap",
    "Dot1pMapPayload",
    "Dot1pMapObject",
]