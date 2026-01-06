from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SwitchProfilePayload(TypedDict, total=False):
    """
    Type hints for switch_controller/switch_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SwitchProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiSwitch Profile name.
    login_passwd_override: NotRequired[Literal[{"description": "Override a managed FortiSwitch\u0027s admin administrator password", "help": "Override a managed FortiSwitch\u0027s admin administrator password.", "label": "Enable", "name": "enable"}, {"description": "Use the managed FortiSwitch admin administrator account password", "help": "Use the managed FortiSwitch admin administrator account password.", "label": "Disable", "name": "disable"}]]  # Enable/disable overriding the admin administrator password f
    login_passwd: NotRequired[str]  # Login password of managed FortiSwitch.
    login: NotRequired[Literal[{"description": "Enable FortiSwitch serial console", "help": "Enable FortiSwitch serial console.", "label": "Enable", "name": "enable"}, {"description": "Disable FortiSwitch serial console", "help": "Disable FortiSwitch serial console.", "label": "Disable", "name": "disable"}]]  # Enable/disable FortiSwitch serial console.
    revision_backup_on_logout: NotRequired[Literal[{"description": "Enable automatic revision backup upon logout from FortiSwitch", "help": "Enable automatic revision backup upon logout from FortiSwitch.", "label": "Enable", "name": "enable"}, {"description": "Disable automatic revision backup upon logout from FortiSwitch", "help": "Disable automatic revision backup upon logout from FortiSwitch.", "label": "Disable", "name": "disable"}]]  # Enable/disable automatic revision backup upon logout from Fo
    revision_backup_on_upgrade: NotRequired[Literal[{"description": "Enable automatic revision backup upon FortiSwitch image upgrade", "help": "Enable automatic revision backup upon FortiSwitch image upgrade.", "label": "Enable", "name": "enable"}, {"description": "Disable automatic revision backup upon FortiSwitch image upgrade", "help": "Disable automatic revision backup upon FortiSwitch image upgrade.", "label": "Disable", "name": "disable"}]]  # Enable/disable automatic revision backup upon FortiSwitch im


class SwitchProfile:
    """
    Configure FortiSwitch switch profile.
    
    Path: switch_controller/switch_profile
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
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal[{"description": "Override a managed FortiSwitch\u0027s admin administrator password", "help": "Override a managed FortiSwitch\u0027s admin administrator password.", "label": "Enable", "name": "enable"}, {"description": "Use the managed FortiSwitch admin administrator account password", "help": "Use the managed FortiSwitch admin administrator account password.", "label": "Disable", "name": "disable"}] | None = ...,
        login_passwd: str | None = ...,
        login: Literal[{"description": "Enable FortiSwitch serial console", "help": "Enable FortiSwitch serial console.", "label": "Enable", "name": "enable"}, {"description": "Disable FortiSwitch serial console", "help": "Disable FortiSwitch serial console.", "label": "Disable", "name": "disable"}] | None = ...,
        revision_backup_on_logout: Literal[{"description": "Enable automatic revision backup upon logout from FortiSwitch", "help": "Enable automatic revision backup upon logout from FortiSwitch.", "label": "Enable", "name": "enable"}, {"description": "Disable automatic revision backup upon logout from FortiSwitch", "help": "Disable automatic revision backup upon logout from FortiSwitch.", "label": "Disable", "name": "disable"}] | None = ...,
        revision_backup_on_upgrade: Literal[{"description": "Enable automatic revision backup upon FortiSwitch image upgrade", "help": "Enable automatic revision backup upon FortiSwitch image upgrade.", "label": "Enable", "name": "enable"}, {"description": "Disable automatic revision backup upon FortiSwitch image upgrade", "help": "Disable automatic revision backup upon FortiSwitch image upgrade.", "label": "Disable", "name": "disable"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SwitchProfilePayload | None = ...,
        name: str | None = ...,
        login_passwd_override: Literal[{"description": "Override a managed FortiSwitch\u0027s admin administrator password", "help": "Override a managed FortiSwitch\u0027s admin administrator password.", "label": "Enable", "name": "enable"}, {"description": "Use the managed FortiSwitch admin administrator account password", "help": "Use the managed FortiSwitch admin administrator account password.", "label": "Disable", "name": "disable"}] | None = ...,
        login_passwd: str | None = ...,
        login: Literal[{"description": "Enable FortiSwitch serial console", "help": "Enable FortiSwitch serial console.", "label": "Enable", "name": "enable"}, {"description": "Disable FortiSwitch serial console", "help": "Disable FortiSwitch serial console.", "label": "Disable", "name": "disable"}] | None = ...,
        revision_backup_on_logout: Literal[{"description": "Enable automatic revision backup upon logout from FortiSwitch", "help": "Enable automatic revision backup upon logout from FortiSwitch.", "label": "Enable", "name": "enable"}, {"description": "Disable automatic revision backup upon logout from FortiSwitch", "help": "Disable automatic revision backup upon logout from FortiSwitch.", "label": "Disable", "name": "disable"}] | None = ...,
        revision_backup_on_upgrade: Literal[{"description": "Enable automatic revision backup upon FortiSwitch image upgrade", "help": "Enable automatic revision backup upon FortiSwitch image upgrade.", "label": "Enable", "name": "enable"}, {"description": "Disable automatic revision backup upon FortiSwitch image upgrade", "help": "Disable automatic revision backup upon FortiSwitch image upgrade.", "label": "Disable", "name": "disable"}] | None = ...,
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
        payload_dict: SwitchProfilePayload | None = ...,
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
    "SwitchProfile",
    "SwitchProfilePayload",
]