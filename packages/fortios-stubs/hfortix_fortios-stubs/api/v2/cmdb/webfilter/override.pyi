from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class OverridePayload(TypedDict, total=False):
    """
    Type hints for webfilter/override payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: OverridePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Override rule ID.
    status: NotRequired[Literal[{"description": "Enable override rule", "help": "Enable override rule.", "label": "Enable", "name": "enable"}, {"description": "Disable override rule", "help": "Disable override rule.", "label": "Disable", "name": "disable"}]]  # Enable/disable override rule.
    scope: NotRequired[Literal[{"description": "Override the specified user", "help": "Override the specified user.", "label": "User", "name": "user"}, {"description": "Override the specified user group", "help": "Override the specified user group.", "label": "User Group", "name": "user-group"}, {"description": "Override the specified IP address", "help": "Override the specified IP address.", "label": "Ip", "name": "ip"}, {"description": "Override the specified IPv6 address", "help": "Override the specified IPv6 address.", "label": "Ip6", "name": "ip6"}]]  # Override either the specific user, user group, IPv4 address,
    ip: str  # IPv4 address which the override applies.
    user: str  # Name of the user which the override applies.
    user_group: str  # Specify the user group for which the override applies.
    old_profile: str  # Name of the web filter profile which the override applies.
    new_profile: str  # Name of the new web filter profile used by the override.
    ip6: str  # IPv6 address which the override applies.
    expires: str  # Override expiration date and time, from 5 minutes to 365 fro
    initiator: NotRequired[str]  # Initiating user of override (read-only setting).


class Override:
    """
    Configure FortiGuard Web Filter administrative overrides.
    
    Path: webfilter/override
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal[{"description": "Enable override rule", "help": "Enable override rule.", "label": "Enable", "name": "enable"}, {"description": "Disable override rule", "help": "Disable override rule.", "label": "Disable", "name": "disable"}] | None = ...,
        scope: Literal[{"description": "Override the specified user", "help": "Override the specified user.", "label": "User", "name": "user"}, {"description": "Override the specified user group", "help": "Override the specified user group.", "label": "User Group", "name": "user-group"}, {"description": "Override the specified IP address", "help": "Override the specified IP address.", "label": "Ip", "name": "ip"}, {"description": "Override the specified IPv6 address", "help": "Override the specified IPv6 address.", "label": "Ip6", "name": "ip6"}] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: OverridePayload | None = ...,
        id: int | None = ...,
        status: Literal[{"description": "Enable override rule", "help": "Enable override rule.", "label": "Enable", "name": "enable"}, {"description": "Disable override rule", "help": "Disable override rule.", "label": "Disable", "name": "disable"}] | None = ...,
        scope: Literal[{"description": "Override the specified user", "help": "Override the specified user.", "label": "User", "name": "user"}, {"description": "Override the specified user group", "help": "Override the specified user group.", "label": "User Group", "name": "user-group"}, {"description": "Override the specified IP address", "help": "Override the specified IP address.", "label": "Ip", "name": "ip"}, {"description": "Override the specified IPv6 address", "help": "Override the specified IPv6 address.", "label": "Ip6", "name": "ip6"}] | None = ...,
        ip: str | None = ...,
        user: str | None = ...,
        user_group: str | None = ...,
        old_profile: str | None = ...,
        new_profile: str | None = ...,
        ip6: str | None = ...,
        expires: str | None = ...,
        initiator: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: OverridePayload | None = ...,
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
    "Override",
    "OverridePayload",
]