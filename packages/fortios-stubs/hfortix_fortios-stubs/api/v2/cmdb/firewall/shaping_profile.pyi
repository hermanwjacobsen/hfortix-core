from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ShapingProfilePayload(TypedDict, total=False):
    """
    Type hints for firewall/shaping_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ShapingProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    profile_name: str  # Shaping profile name.
    comment: NotRequired[str]  # Comment.
    type: NotRequired[Literal[{"description": "Enable policing mode", "help": "Enable policing mode.", "label": "Policing", "name": "policing"}, {"description": "Enable queuing mode", "help": "Enable queuing mode.", "label": "Queuing", "name": "queuing"}]]  # Select shaping profile type: policing / queuing.
    npu_offloading: NotRequired[Literal[{"description": "Diable shaper offloading", "help": "Diable shaper offloading.", "label": "Disable", "name": "disable"}, {"description": "Enable shaper offloading", "help": "Enable shaper offloading.", "label": "Enable", "name": "enable"}]]  # Enable/disable NPU offloading.
    default_class_id: int  # Default class ID to handle unclassified packets (including a
    shaping_entries: NotRequired[list[dict[str, Any]]]  # Define shaping entries of this shaping profile.


class ShapingProfile:
    """
    Configure shaping profiles.
    
    Path: firewall/shaping_profile
    Category: cmdb
    Primary Key: profile-name
    """
    
    def get(
        self,
        profile_name: str | None = ...,
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
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal[{"description": "Enable policing mode", "help": "Enable policing mode.", "label": "Policing", "name": "policing"}, {"description": "Enable queuing mode", "help": "Enable queuing mode.", "label": "Queuing", "name": "queuing"}] | None = ...,
        npu_offloading: Literal[{"description": "Diable shaper offloading", "help": "Diable shaper offloading.", "label": "Disable", "name": "disable"}, {"description": "Enable shaper offloading", "help": "Enable shaper offloading.", "label": "Enable", "name": "enable"}] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal[{"description": "Enable policing mode", "help": "Enable policing mode.", "label": "Policing", "name": "policing"}, {"description": "Enable queuing mode", "help": "Enable queuing mode.", "label": "Queuing", "name": "queuing"}] | None = ...,
        npu_offloading: Literal[{"description": "Diable shaper offloading", "help": "Diable shaper offloading.", "label": "Disable", "name": "disable"}, {"description": "Enable shaper offloading", "help": "Enable shaper offloading.", "label": "Enable", "name": "enable"}] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        profile_name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
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
    "ShapingProfile",
    "ShapingProfilePayload",
]