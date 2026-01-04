from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Hotspot20H2qpWanMetricPayload(TypedDict, total=False):
    """
    Type hints for wireless-controller/hotspot20_h2qp_wan_metric payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Hotspot20H2qpWanMetricPayload = {
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


class Hotspot20H2qpWanMetric:
    """
    Configure WAN metrics.
    
    Path: wireless-controller/hotspot20_h2qp_wan_metric
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: Hotspot20H2qpWanMetricPayload | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Hotspot20H2qpWanMetricPayload | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: Hotspot20H2qpWanMetricPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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