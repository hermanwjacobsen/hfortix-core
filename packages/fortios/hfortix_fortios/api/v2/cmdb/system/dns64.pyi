from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Dns64Payload(TypedDict, total=False):
    """
    Type hints for system/dns64 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Dns64Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal[{"description": "Enable DNS64", "help": "Enable DNS64.", "label": "Enable", "name": "enable"}, {"description": "Disable DNS64", "help": "Disable DNS64.", "label": "Disable", "name": "disable"}]]  # Enable/disable DNS64 (default = disable).
    dns64_prefix: str  # DNS64 prefix must be ::/96 (default = 64:ff9b::/96).
    always_synthesize_aaaa_record: NotRequired[Literal[{"description": "Enable AAAA record synthesis", "help": "Enable AAAA record synthesis.", "label": "Enable", "name": "enable"}, {"description": "Disable AAAA record synthesis", "help": "Disable AAAA record synthesis.", "label": "Disable", "name": "disable"}]]  # Enable/disable AAAA record synthesis (default = enable).


class Dns64:
    """
    Configure DNS64.
    
    Path: system/dns64
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
        payload_dict: Dns64Payload | None = ...,
        status: Literal[{"description": "Enable DNS64", "help": "Enable DNS64.", "label": "Enable", "name": "enable"}, {"description": "Disable DNS64", "help": "Disable DNS64.", "label": "Disable", "name": "disable"}] | None = ...,
        dns64_prefix: str | None = ...,
        always_synthesize_aaaa_record: Literal[{"description": "Enable AAAA record synthesis", "help": "Enable AAAA record synthesis.", "label": "Enable", "name": "enable"}, {"description": "Disable AAAA record synthesis", "help": "Disable AAAA record synthesis.", "label": "Disable", "name": "disable"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Dns64Payload | None = ...,
        status: Literal[{"description": "Enable DNS64", "help": "Enable DNS64.", "label": "Enable", "name": "enable"}, {"description": "Disable DNS64", "help": "Disable DNS64.", "label": "Disable", "name": "disable"}] | None = ...,
        dns64_prefix: str | None = ...,
        always_synthesize_aaaa_record: Literal[{"description": "Enable AAAA record synthesis", "help": "Enable AAAA record synthesis.", "label": "Enable", "name": "enable"}, {"description": "Disable AAAA record synthesis", "help": "Disable AAAA record synthesis.", "label": "Disable", "name": "disable"}] | None = ...,
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
        payload_dict: Dns64Payload | None = ...,
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
    "Dns64",
    "Dns64Payload",
]