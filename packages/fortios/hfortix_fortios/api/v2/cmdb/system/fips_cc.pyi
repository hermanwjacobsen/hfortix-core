from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FipsCcPayload(TypedDict, total=False):
    """
    Type hints for system/fips_cc payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FipsCcPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal[{"description": "Enable FIPS-CC mode", "help": "Enable FIPS-CC mode.", "label": "Enable", "name": "enable"}, {"description": "Disable FIPS-CC mode", "help": "Disable FIPS-CC mode.", "label": "Disable", "name": "disable"}]]  # Enable/disable ciphers for FIPS mode of operation.
    self_test_period: NotRequired[int]  # Self test period.
    key_generation_self_test: NotRequired[Literal[{"description": "Enable self tests after key generation", "help": "Enable self tests after key generation.", "label": "Enable", "name": "enable"}, {"description": "Disable self tests after key generation", "help": "Disable self tests after key generation.", "label": "Disable", "name": "disable"}]]  # Enable/disable self tests after key generation.


class FipsCc:
    """
    Configure FIPS-CC mode.
    
    Path: system/fips_cc
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
        payload_dict: FipsCcPayload | None = ...,
        status: Literal[{"description": "Enable FIPS-CC mode", "help": "Enable FIPS-CC mode.", "label": "Enable", "name": "enable"}, {"description": "Disable FIPS-CC mode", "help": "Disable FIPS-CC mode.", "label": "Disable", "name": "disable"}] | None = ...,
        self_test_period: int | None = ...,
        key_generation_self_test: Literal[{"description": "Enable self tests after key generation", "help": "Enable self tests after key generation.", "label": "Enable", "name": "enable"}, {"description": "Disable self tests after key generation", "help": "Disable self tests after key generation.", "label": "Disable", "name": "disable"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FipsCcPayload | None = ...,
        status: Literal[{"description": "Enable FIPS-CC mode", "help": "Enable FIPS-CC mode.", "label": "Enable", "name": "enable"}, {"description": "Disable FIPS-CC mode", "help": "Disable FIPS-CC mode.", "label": "Disable", "name": "disable"}] | None = ...,
        self_test_period: int | None = ...,
        key_generation_self_test: Literal[{"description": "Enable self tests after key generation", "help": "Enable self tests after key generation.", "label": "Enable", "name": "enable"}, {"description": "Disable self tests after key generation", "help": "Disable self tests after key generation.", "label": "Disable", "name": "disable"}] | None = ...,
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
        payload_dict: FipsCcPayload | None = ...,
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
    "FipsCc",
    "FipsCcPayload",
]