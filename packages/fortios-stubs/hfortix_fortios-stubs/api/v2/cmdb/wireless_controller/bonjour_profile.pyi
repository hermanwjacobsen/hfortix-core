from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class BonjourProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/bonjour_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: BonjourProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Bonjour profile name.
    comment: NotRequired[str]  # Comment.
    micro_location: NotRequired[Literal[{"description": "Enable Micro location", "help": "Enable Micro location.", "label": "Enable", "name": "enable"}, {"description": "Disable Micro location", "help": "Disable Micro location.", "label": "Disable", "name": "disable"}]]  # Enable/disable Micro location for Bonjour profile (default =
    policy_list: NotRequired[list[dict[str, Any]]]  # Bonjour policy list.


class BonjourProfile:
    """
    Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
    
    Path: wireless_controller/bonjour_profile
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
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal[{"description": "Enable Micro location", "help": "Enable Micro location.", "label": "Enable", "name": "enable"}, {"description": "Disable Micro location", "help": "Disable Micro location.", "label": "Disable", "name": "disable"}] | None = ...,
        policy_list: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: BonjourProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        micro_location: Literal[{"description": "Enable Micro location", "help": "Enable Micro location.", "label": "Enable", "name": "enable"}, {"description": "Disable Micro location", "help": "Disable Micro location.", "label": "Disable", "name": "disable"}] | None = ...,
        policy_list: list[dict[str, Any]] | None = ...,
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
        payload_dict: BonjourProfilePayload | None = ...,
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
    "BonjourProfile",
    "BonjourProfilePayload",
]