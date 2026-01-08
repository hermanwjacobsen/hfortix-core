from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class PolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/auto_config/policy payload fields.
    
    Policy definitions which can define the behavior on auto configured interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.switch-controller.qos.qos-policy.QosPolicyEndpoint` (via: qos-policy)
        - :class:`~.switch-controller.storm-control-policy.StormControlPolicyEndpoint` (via: storm-control-policy)

    **Usage:**
        payload: PolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Auto-config policy name.
    qos_policy: NotRequired[str]  # Auto-Config QoS policy.
    storm_control_policy: NotRequired[str]  # Auto-Config storm control policy.
    poe_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable PoE status.
    igmp_flood_report: NotRequired[Literal["enable", "disable"]]  # Enable/disable IGMP flood report.
    igmp_flood_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable IGMP flood traffic.


class PolicyObject(FortiObject[PolicyPayload]):
    """Typed FortiObject for switch_controller/auto_config/policy with IDE autocomplete support."""
    
    # Auto-config policy name.
    name: str
    # Auto-Config QoS policy.
    qos_policy: str
    # Auto-Config storm control policy.
    storm_control_policy: str
    # Enable/disable PoE status.
    poe_status: Literal["enable", "disable"]
    # Enable/disable IGMP flood report.
    igmp_flood_report: Literal["enable", "disable"]
    # Enable/disable IGMP flood traffic.
    igmp_flood_traffic: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Policy:
    """
    Policy definitions which can define the behavior on auto configured interfaces.
    
    Path: switch_controller/auto_config/policy
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
    ) -> PolicyObject: ...
    
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
    ) -> list[PolicyObject]: ...
    
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
    ) -> PolicyObject | list[PolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
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
    ) -> PolicyObject: ...
    
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
        payload_dict: PolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
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
    "Policy",
    "PolicyPayload",
    "PolicyObject",
]