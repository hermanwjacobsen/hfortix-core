from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AutomationDestinationPayload(TypedDict, total=False):
    """
    Type hints for system/automation_destination payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AutomationDestinationPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name.
    type: NotRequired[Literal[{"description": "FortiGate set as destination", "help": "FortiGate set as destination.", "label": "Fortigate", "name": "fortigate"}, {"description": "HA cluster set as destination", "help": "HA cluster set as destination.", "label": "Ha Cluster", "name": "ha-cluster"}]]  # Destination type.
    destination: NotRequired[list[dict[str, Any]]]  # Destinations.
    ha_group_id: NotRequired[int]  # Cluster group ID set for this destination (default = 0).


class AutomationDestination:
    """
    Automation destinations.
    
    Path: system/automation_destination
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
        payload_dict: AutomationDestinationPayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "FortiGate set as destination", "help": "FortiGate set as destination.", "label": "Fortigate", "name": "fortigate"}, {"description": "HA cluster set as destination", "help": "HA cluster set as destination.", "label": "Ha Cluster", "name": "ha-cluster"}] | None = ...,
        destination: list[dict[str, Any]] | None = ...,
        ha_group_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AutomationDestinationPayload | None = ...,
        name: str | None = ...,
        type: Literal[{"description": "FortiGate set as destination", "help": "FortiGate set as destination.", "label": "Fortigate", "name": "fortigate"}, {"description": "HA cluster set as destination", "help": "HA cluster set as destination.", "label": "Ha Cluster", "name": "ha-cluster"}] | None = ...,
        destination: list[dict[str, Any]] | None = ...,
        ha_group_id: int | None = ...,
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
        payload_dict: AutomationDestinationPayload | None = ...,
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
    "AutomationDestination",
    "AutomationDestinationPayload",
]