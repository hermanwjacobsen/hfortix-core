from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for virtual_patch/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    comment: NotRequired[str]  # Comment.
    severity: NotRequired[Literal[{"description": "info    low:low    medium:medium    high:high    critical:critical", "help": "info", "label": "Info", "name": "info"}, {"help": "low", "label": "Low", "name": "low"}, {"help": "medium", "label": "Medium", "name": "medium"}, {"help": "high", "label": "High", "name": "high"}, {"help": "critical", "label": "Critical", "name": "critical"}]]  # Relative severity of the signature (low, medium, high, criti
    action: NotRequired[Literal[{"description": "Allows session that match the profile", "help": "Allows session that match the profile.", "label": "Pass", "name": "pass"}, {"description": "Blocks sessions that match the profile", "help": "Blocks sessions that match the profile.", "label": "Block", "name": "block"}]]  # Action (pass/block).
    log: NotRequired[Literal[{"description": "Enable logging", "help": "Enable logging.", "label": "Enable", "name": "enable"}, {"description": "Disable logging", "help": "Disable logging.", "label": "Disable", "name": "disable"}]]  # Enable/disable logging of detection.
    exemption: NotRequired[list[dict[str, Any]]]  # Exempt devices or rules.


class Profile:
    """
    Configure virtual-patch profile.
    
    Path: virtual_patch/profile
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
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        severity: Literal[{"description": "info    low:low    medium:medium    high:high    critical:critical", "help": "info", "label": "Info", "name": "info"}, {"help": "low", "label": "Low", "name": "low"}, {"help": "medium", "label": "Medium", "name": "medium"}, {"help": "high", "label": "High", "name": "high"}, {"help": "critical", "label": "Critical", "name": "critical"}] | None = ...,
        action: Literal[{"description": "Allows session that match the profile", "help": "Allows session that match the profile.", "label": "Pass", "name": "pass"}, {"description": "Blocks sessions that match the profile", "help": "Blocks sessions that match the profile.", "label": "Block", "name": "block"}] | None = ...,
        log: Literal[{"description": "Enable logging", "help": "Enable logging.", "label": "Enable", "name": "enable"}, {"description": "Disable logging", "help": "Disable logging.", "label": "Disable", "name": "disable"}] | None = ...,
        exemption: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        severity: Literal[{"description": "info    low:low    medium:medium    high:high    critical:critical", "help": "info", "label": "Info", "name": "info"}, {"help": "low", "label": "Low", "name": "low"}, {"help": "medium", "label": "Medium", "name": "medium"}, {"help": "high", "label": "High", "name": "high"}, {"help": "critical", "label": "Critical", "name": "critical"}] | None = ...,
        action: Literal[{"description": "Allows session that match the profile", "help": "Allows session that match the profile.", "label": "Pass", "name": "pass"}, {"description": "Blocks sessions that match the profile", "help": "Blocks sessions that match the profile.", "label": "Block", "name": "block"}] | None = ...,
        log: Literal[{"description": "Enable logging", "help": "Enable logging.", "label": "Enable", "name": "enable"}, {"description": "Disable logging", "help": "Disable logging.", "label": "Disable", "name": "disable"}] | None = ...,
        exemption: list[dict[str, Any]] | None = ...,
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
        payload_dict: ProfilePayload | None = ...,
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
    "Profile",
    "ProfilePayload",
]