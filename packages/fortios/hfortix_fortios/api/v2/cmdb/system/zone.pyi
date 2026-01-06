from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ZonePayload(TypedDict, total=False):
    """
    Type hints for system/zone payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ZonePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Zone name.
    tagging: NotRequired[list[dict[str, Any]]]  # Config object tagging.
    description: NotRequired[str]  # Description.
    intrazone: NotRequired[Literal[{"description": "Allow traffic between interfaces in the zone", "help": "Allow traffic between interfaces in the zone.", "label": "Allow", "name": "allow"}, {"description": "Deny traffic between interfaces in the zone", "help": "Deny traffic between interfaces in the zone.", "label": "Deny", "name": "deny"}]]  # Allow or deny traffic routing between different interfaces i
    interface: NotRequired[list[dict[str, Any]]]  # Add interfaces to this zone. Interfaces must not be assigned


class Zone:
    """
    Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead of individual interfaces in the zone.
    
    Path: system/zone
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
        payload_dict: ZonePayload | None = ...,
        name: str | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        description: str | None = ...,
        intrazone: Literal[{"description": "Allow traffic between interfaces in the zone", "help": "Allow traffic between interfaces in the zone.", "label": "Allow", "name": "allow"}, {"description": "Deny traffic between interfaces in the zone", "help": "Deny traffic between interfaces in the zone.", "label": "Deny", "name": "deny"}] | None = ...,
        interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ZonePayload | None = ...,
        name: str | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        description: str | None = ...,
        intrazone: Literal[{"description": "Allow traffic between interfaces in the zone", "help": "Allow traffic between interfaces in the zone.", "label": "Allow", "name": "allow"}, {"description": "Deny traffic between interfaces in the zone", "help": "Deny traffic between interfaces in the zone.", "label": "Deny", "name": "deny"}] | None = ...,
        interface: list[dict[str, Any]] | None = ...,
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
        payload_dict: ZonePayload | None = ...,
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
    "Zone",
    "ZonePayload",
]