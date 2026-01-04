from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpmacbindingSettingPayload(TypedDict, total=False):
    """
    Type hints for firewall/ipmacbinding_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpmacbindingSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    bindthroughfw: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IP/MAC binding to filter packets that 
    bindtofw: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IP/MAC binding to filter packets that 
    undefinedhost: Literal["allow", "block"]  # Select action to take on packets with IP/MAC addresses not i


class IpmacbindingSetting:
    """
    Configure IP to MAC binding settings.
    
    Path: firewall/ipmacbinding_setting
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
        payload_dict: IpmacbindingSettingPayload | None = ...,
        bindthroughfw: Literal["enable", "disable"] | None = ...,
        bindtofw: Literal["enable", "disable"] | None = ...,
        undefinedhost: Literal["allow", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpmacbindingSettingPayload | None = ...,
        bindthroughfw: Literal["enable", "disable"] | None = ...,
        bindtofw: Literal["enable", "disable"] | None = ...,
        undefinedhost: Literal["allow", "block"] | None = ...,
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
        payload_dict: IpmacbindingSettingPayload | None = ...,
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