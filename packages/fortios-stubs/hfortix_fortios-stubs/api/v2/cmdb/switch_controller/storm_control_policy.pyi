from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class StormControlPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/storm_control_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: StormControlPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Storm control policy name.
    description: NotRequired[str]  # Description of the storm control policy.
    storm_control_mode: NotRequired[Literal[{"description": "Apply Global or switch level storm control configuration", "help": "Apply Global or switch level storm control configuration.", "label": "Global", "name": "global"}, {"description": "Override global and switch level storm control to use port level configuration", "help": "Override global and switch level storm control to use port level configuration.", "label": "Override", "name": "override"}, {"description": "Disable storm control on the port entirely overriding global and switch level storm control", "help": "Disable storm control on the port entirely overriding global and switch level storm control.", "label": "Disabled", "name": "disabled"}]]  # Set Storm control mode.
    rate: NotRequired[int]  # Threshold rate in packets per second at which storm traffic 
    burst_size_level: NotRequired[int]  # Increase level to handle bursty traffic (0 - 4, default = 0)
    unknown_unicast: NotRequired[Literal[{"description": "Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for unknown unicast traffic to allow all packets", "help": "Disable storm control for unknown unicast traffic to allow all packets.", "label": "Disable", "name": "disable"}]]  # Enable/disable storm control to drop/allow unknown unicast t
    unknown_multicast: NotRequired[Literal[{"description": "Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for unknown multicast traffic to allow all packets", "help": "Disable storm control for unknown multicast traffic to allow all packets.", "label": "Disable", "name": "disable"}]]  # Enable/disable storm control to drop/allow unknown multicast
    broadcast: NotRequired[Literal[{"description": "Enable storm control for broadcast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for broadcast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for broadcast traffic to allow all packets", "help": "Disable storm control for broadcast traffic to allow all packets.", "label": "Disable", "name": "disable"}]]  # Enable/disable storm control to drop/allow broadcast traffic


class StormControlPolicy:
    """
    Configure FortiSwitch storm control policy to be applied on managed-switch ports.
    
    Path: switch_controller/storm_control_policy
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
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal[{"description": "Apply Global or switch level storm control configuration", "help": "Apply Global or switch level storm control configuration.", "label": "Global", "name": "global"}, {"description": "Override global and switch level storm control to use port level configuration", "help": "Override global and switch level storm control to use port level configuration.", "label": "Override", "name": "override"}, {"description": "Disable storm control on the port entirely overriding global and switch level storm control", "help": "Disable storm control on the port entirely overriding global and switch level storm control.", "label": "Disabled", "name": "disabled"}] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal[{"description": "Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for unknown unicast traffic to allow all packets", "help": "Disable storm control for unknown unicast traffic to allow all packets.", "label": "Disable", "name": "disable"}] | None = ...,
        unknown_multicast: Literal[{"description": "Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for unknown multicast traffic to allow all packets", "help": "Disable storm control for unknown multicast traffic to allow all packets.", "label": "Disable", "name": "disable"}] | None = ...,
        broadcast: Literal[{"description": "Enable storm control for broadcast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for broadcast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for broadcast traffic to allow all packets", "help": "Disable storm control for broadcast traffic to allow all packets.", "label": "Disable", "name": "disable"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: StormControlPolicyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        storm_control_mode: Literal[{"description": "Apply Global or switch level storm control configuration", "help": "Apply Global or switch level storm control configuration.", "label": "Global", "name": "global"}, {"description": "Override global and switch level storm control to use port level configuration", "help": "Override global and switch level storm control to use port level configuration.", "label": "Override", "name": "override"}, {"description": "Disable storm control on the port entirely overriding global and switch level storm control", "help": "Disable storm control on the port entirely overriding global and switch level storm control.", "label": "Disabled", "name": "disabled"}] | None = ...,
        rate: int | None = ...,
        burst_size_level: int | None = ...,
        unknown_unicast: Literal[{"description": "Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for unknown unicast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for unknown unicast traffic to allow all packets", "help": "Disable storm control for unknown unicast traffic to allow all packets.", "label": "Disable", "name": "disable"}] | None = ...,
        unknown_multicast: Literal[{"description": "Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for unknown multicast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for unknown multicast traffic to allow all packets", "help": "Disable storm control for unknown multicast traffic to allow all packets.", "label": "Disable", "name": "disable"}] | None = ...,
        broadcast: Literal[{"description": "Enable storm control for broadcast traffic to drop packets which exceed configured rate limits", "help": "Enable storm control for broadcast traffic to drop packets which exceed configured rate limits.", "label": "Enable", "name": "enable"}, {"description": "Disable storm control for broadcast traffic to allow all packets", "help": "Disable storm control for broadcast traffic to allow all packets.", "label": "Disable", "name": "disable"}] | None = ...,
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
        payload_dict: StormControlPolicyPayload | None = ...,
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


__all__ = [
    "StormControlPolicy",
    "StormControlPolicyPayload",
]