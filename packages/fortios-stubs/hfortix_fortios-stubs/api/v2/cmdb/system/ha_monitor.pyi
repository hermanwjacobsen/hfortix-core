from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class HaMonitorPayload(TypedDict, total=False):
    """
    Type hints for system/ha_monitor payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: HaMonitorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    monitor_vlan: NotRequired[Literal[{"description": "Enable monitor VLAN interfaces", "help": "Enable monitor VLAN interfaces.", "label": "Enable", "name": "enable"}, {"description": "Disable monitor VLAN interfaces", "help": "Disable monitor VLAN interfaces.", "label": "Disable", "name": "disable"}]]  # Enable/disable monitor VLAN interfaces.
    vlan_hb_interval: NotRequired[int]  # Configure heartbeat interval (seconds).
    vlan_hb_lost_threshold: NotRequired[int]  # VLAN lost heartbeat threshold (1 - 60).


class HaMonitor:
    """
    Configure HA monitor.
    
    Path: system/ha_monitor
    Category: cmdb
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
        payload_dict: HaMonitorPayload | None = ...,
        monitor_vlan: Literal[{"description": "Enable monitor VLAN interfaces", "help": "Enable monitor VLAN interfaces.", "label": "Enable", "name": "enable"}, {"description": "Disable monitor VLAN interfaces", "help": "Disable monitor VLAN interfaces.", "label": "Disable", "name": "disable"}] | None = ...,
        vlan_hb_interval: int | None = ...,
        vlan_hb_lost_threshold: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: HaMonitorPayload | None = ...,
        monitor_vlan: Literal[{"description": "Enable monitor VLAN interfaces", "help": "Enable monitor VLAN interfaces.", "label": "Enable", "name": "enable"}, {"description": "Disable monitor VLAN interfaces", "help": "Disable monitor VLAN interfaces.", "label": "Disable", "name": "disable"}] | None = ...,
        vlan_hb_interval: int | None = ...,
        vlan_hb_lost_threshold: int | None = ...,
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
        payload_dict: HaMonitorPayload | None = ...,
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
    "HaMonitor",
    "HaMonitorPayload",
]