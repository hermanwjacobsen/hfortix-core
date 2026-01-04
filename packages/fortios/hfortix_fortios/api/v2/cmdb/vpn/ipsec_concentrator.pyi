from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpsecConcentratorPayload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec_concentrator payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpsecConcentratorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Concentrator ID (1 - 65535).
    name: NotRequired[str]  # Concentrator name.
    src_check: NotRequired[Literal["disable", "enable"]]  # Enable to check source address of phase 2 selector. Disable 
    member: NotRequired[list[dict[str, Any]]]  # Names of up to 3 VPN tunnels to add to the concentrator.


class IpsecConcentrator:
    """
    Concentrator configuration.
    
    Path: vpn/ipsec_concentrator
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
        payload_dict: IpsecConcentratorPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        src_check: Literal["disable", "enable"] | None = ...,
        member: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpsecConcentratorPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        src_check: Literal["disable", "enable"] | None = ...,
        member: list[dict[str, Any]] | None = ...,
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
        payload_dict: IpsecConcentratorPayload | None = ...,
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