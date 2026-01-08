from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class TrafficPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/traffic_policy payload fields.
    
    Configure FortiSwitch traffic policy.
    
    **Usage:**
        payload: TrafficPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Traffic policy name.
    description: NotRequired[str]  # Description of the traffic policy.
    policer_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable policer config on the traffic policy.
    guaranteed_bandwidth: NotRequired[int]  # Guaranteed bandwidth in kbps (max value = 524287000).
    guaranteed_burst: NotRequired[int]  # Guaranteed burst size in bytes (max value = 4294967295).
    maximum_burst: NotRequired[int]  # Maximum burst size in bytes (max value = 4294967295).
    type: NotRequired[Literal["ingress", "egress"]]  # Configure type of policy(ingress/egress).
    cos_queue: NotRequired[int]  # COS queue(0 - 7), or unset to disable.


class TrafficPolicyObject(FortiObject[TrafficPolicyPayload]):
    """Typed FortiObject for switch_controller/traffic_policy with IDE autocomplete support."""
    
    # Traffic policy name.
    name: str
    # Description of the traffic policy.
    description: str
    # Enable/disable policer config on the traffic policy.
    policer_status: Literal["enable", "disable"]
    # Guaranteed bandwidth in kbps (max value = 524287000).
    guaranteed_bandwidth: int
    # Guaranteed burst size in bytes (max value = 4294967295).
    guaranteed_burst: int
    # Maximum burst size in bytes (max value = 4294967295).
    maximum_burst: int
    # Configure type of policy(ingress/egress).
    type: Literal["ingress", "egress"]
    # COS queue(0 - 7), or unset to disable.
    cos_queue: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> TrafficPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TrafficPolicy:
    """
    Configure FortiSwitch traffic policy.
    
    Path: switch_controller/traffic_policy
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> TrafficPolicyObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[TrafficPolicyObject]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    ) -> TrafficPolicyObject | list[TrafficPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TrafficPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TrafficPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
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
    ) -> TrafficPolicyObject: ...
    
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
        payload_dict: TrafficPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        policer_status: Literal["enable", "disable"] | None = ...,
        guaranteed_bandwidth: int | None = ...,
        guaranteed_burst: int | None = ...,
        maximum_burst: int | None = ...,
        type: Literal["ingress", "egress"] | None = ...,
        cos_queue: int | None = ...,
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
    "TrafficPolicy",
    "TrafficPolicyPayload",
    "TrafficPolicyObject",
]