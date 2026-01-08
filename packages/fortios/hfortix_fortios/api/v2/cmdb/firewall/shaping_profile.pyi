from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ShapingProfilePayload(TypedDict, total=False):
    """
    Type hints for firewall/shaping_profile payload fields.
    
    Configure shaping profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: default-class-id)

    **Usage:**
        payload: ShapingProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    profile_name: str  # Shaping profile name.
    comment: NotRequired[str]  # Comment.
    type: NotRequired[Literal["policing", "queuing"]]  # Select shaping profile type: policing / queuing.
    npu_offloading: NotRequired[Literal["disable", "enable"]]  # Enable/disable NPU offloading.
    default_class_id: int  # Default class ID to handle unclassified packets
    shaping_entries: NotRequired[list[dict[str, Any]]]  # Define shaping entries of this shaping profile.

# Nested classes for table field children

@final
class ShapingProfileShapingentriesObject:
    """Typed object for shaping-entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID number.
    id: int
    # Class ID.
    class_id: int
    # Priority.
    priority: Literal["top", "critical", "high", "medium", "low"]
    # Guaranteed bandwidth in percentage.
    guaranteed_bandwidth_percentage: int
    # Maximum bandwidth in percentage.
    maximum_bandwidth_percentage: int
    # Hard limit on the real queue size in packets.
    limit: int
    # Number of bytes that can be burst at maximum-bandwidth speed. Formula: burst = m
    burst_in_msec: int
    # Number of bytes that can be burst as fast as the interface can transmit. Formula
    cburst_in_msec: int
    # Maximum probability (in percentage) for RED marking.
    red_probability: int
    # Average queue size in packets at which RED drop becomes a possibility.
    min: int
    # Average queue size in packets at which RED drop probability is maximal.
    max: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ShapingProfileResponse(TypedDict):
    """
    Type hints for firewall/shaping_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    profile_name: str
    comment: str
    type: Literal["policing", "queuing"]
    npu_offloading: Literal["disable", "enable"]
    default_class_id: int
    shaping_entries: list[dict[str, Any]]


@final
class ShapingProfileObject:
    """Typed FortiObject for firewall/shaping_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Shaping profile name.
    profile_name: str
    # Comment.
    comment: str
    # Select shaping profile type: policing / queuing.
    type: Literal["policing", "queuing"]
    # Enable/disable NPU offloading.
    npu_offloading: Literal["disable", "enable"]
    # Default class ID to handle unclassified packets (including all local traffic).
    default_class_id: int
    # Define shaping entries of this shaping profile.
    shaping_entries: list[ShapingProfileShapingentriesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ShapingProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ShapingProfile:
    """
    Configure shaping profiles.
    
    Path: firewall/shaping_profile
    Category: cmdb
    Primary Key: profile-name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        profile_name: str,
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
    ) -> ShapingProfileObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        profile_name: str,
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
    ) -> ShapingProfileObject: ...
    
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
    ) -> list[ShapingProfileObject]: ...
    
    @overload
    def get(
        self,
        profile_name: str | None = ...,
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
        profile_name: str,
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
    ) -> ShapingProfileResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        profile_name: str,
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
    ) -> ShapingProfileResponse: ...
    
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
    ) -> list[ShapingProfileResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        profile_name: str | None = ...,
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
        profile_name: str | None = ...,
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
    ) -> ShapingProfileObject | list[ShapingProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ShapingProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ShapingProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ShapingProfileObject: ...
    
    @overload
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        profile_name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ShapingProfile",
    "ShapingProfilePayload",
    "ShapingProfileObject",
]