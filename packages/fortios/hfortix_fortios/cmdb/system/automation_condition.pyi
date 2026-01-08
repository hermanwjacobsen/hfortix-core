from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class AutomationConditionPayload(TypedDict, total=False):
    """
    Type hints for system/automation_condition payload fields.
    
    Condition for automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: AutomationConditionPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name.
    description: NotRequired[str]  # Description.
    condition_type: NotRequired[Literal["cpu", "memory", "vpn"]]  # Condition type.
    cpu_usage_percent: int  # CPU usage reaches specified percentage.
    mem_usage_percent: int  # Memory usage reaches specified percentage.
    vdom: str  # Virtual domain which the tunnel belongs to.
    vpn_tunnel_name: str  # VPN tunnel name.
    vpn_tunnel_state: NotRequired[Literal["tunnel-up", "tunnel-down"]]  # VPN tunnel state.


class AutomationConditionObject(FortiObject[AutomationConditionPayload]):
    """Typed FortiObject for system/automation_condition with IDE autocomplete support."""
    
    # Name.
    name: str
    # Description.
    description: str
    # Condition type.
    condition_type: Literal["cpu", "memory", "vpn"]
    # CPU usage reaches specified percentage.
    cpu_usage_percent: int
    # Memory usage reaches specified percentage.
    mem_usage_percent: int
    # Virtual domain which the tunnel belongs to.
    vdom: str
    # VPN tunnel name.
    vpn_tunnel_name: str
    # VPN tunnel state.
    vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AutomationConditionPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutomationCondition:
    """
    Condition for automation stitches.
    
    Path: system/automation_condition
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
    ) -> AutomationConditionObject: ...
    
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
    ) -> list[AutomationConditionObject]: ...
    
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
    ) -> AutomationConditionObject | list[AutomationConditionObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationConditionObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationConditionObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
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
    ) -> AutomationConditionObject: ...
    
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
        payload_dict: AutomationConditionPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        condition_type: Literal["cpu", "memory", "vpn"] | None = ...,
        cpu_usage_percent: int | None = ...,
        mem_usage_percent: int | None = ...,
        vpn_tunnel_name: str | None = ...,
        vpn_tunnel_state: Literal["tunnel-up", "tunnel-down"] | None = ...,
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
    "AutomationCondition",
    "AutomationConditionPayload",
    "AutomationConditionObject",
]