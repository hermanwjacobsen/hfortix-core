from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class H2qpWanMetricPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/h2qp_wan_metric payload fields.
    
    Configure WAN metrics.
    
    **Usage:**
        payload: H2qpWanMetricPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WAN metric name.
    link_status: NotRequired[Literal["up", "down", "in-test"]]  # Link status.
    symmetric_wan_link: NotRequired[Literal["symmetric", "asymmetric"]]  # WAN link symmetry.
    link_at_capacity: NotRequired[Literal["enable", "disable"]]  # Link at capacity.
    uplink_speed: NotRequired[int]  # Uplink speed (in kilobits/s).
    downlink_speed: NotRequired[int]  # Downlink speed (in kilobits/s).
    uplink_load: NotRequired[int]  # Uplink load.
    downlink_load: NotRequired[int]  # Downlink load.
    load_measurement_duration: NotRequired[int]  # Load measurement duration (in tenths of a second).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class H2qpWanMetricResponse(TypedDict):
    """
    Type hints for wireless_controller/hotspot20/h2qp_wan_metric API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    link_status: Literal["up", "down", "in-test"]
    symmetric_wan_link: Literal["symmetric", "asymmetric"]
    link_at_capacity: Literal["enable", "disable"]
    uplink_speed: int
    downlink_speed: int
    uplink_load: int
    downlink_load: int
    load_measurement_duration: int


@final
class H2qpWanMetricObject:
    """Typed FortiObject for wireless_controller/hotspot20/h2qp_wan_metric with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WAN metric name.
    name: str
    # Link status.
    link_status: Literal["up", "down", "in-test"]
    # WAN link symmetry.
    symmetric_wan_link: Literal["symmetric", "asymmetric"]
    # Link at capacity.
    link_at_capacity: Literal["enable", "disable"]
    # Uplink speed (in kilobits/s).
    uplink_speed: int
    # Downlink speed (in kilobits/s).
    downlink_speed: int
    # Uplink load.
    uplink_load: int
    # Downlink load.
    downlink_load: int
    # Load measurement duration (in tenths of a second).
    load_measurement_duration: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> H2qpWanMetricPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class H2qpWanMetric:
    """
    Configure WAN metrics.
    
    Path: wireless_controller/hotspot20/h2qp_wan_metric
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> list[H2qpWanMetricObject]: ...
    
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
    ) -> H2qpWanMetricResponse: ...
    
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
    ) -> H2qpWanMetricResponse: ...
    
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
    ) -> list[H2qpWanMetricResponse]: ...
    
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
    ) -> H2qpWanMetricObject | list[H2qpWanMetricObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> H2qpWanMetricObject: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> H2qpWanMetricObject: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
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
    ) -> H2qpWanMetricObject: ...
    
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
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
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
    "H2qpWanMetric",
    "H2qpWanMetricPayload",
    "H2qpWanMetricObject",
]