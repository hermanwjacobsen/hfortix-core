from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for waf/profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # WAF Profile name.
    external: NotRequired[Literal["disable", "enable"]]  # Disable/Enable external HTTP Inspection.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging.
    signature: NotRequired[str]  # WAF signatures.
    constraint: NotRequired[str]  # WAF HTTP protocol restrictions.
    method: NotRequired[str]  # Method restriction.
    address_list: NotRequired[str]  # Address block and allow lists.
    url_access: NotRequired[list[dict[str, Any]]]  # URL access list.
    comment: NotRequired[str]  # Comment.


class Profile:
    """
    Configure Web application firewall configuration.
    
    Path: waf/profile
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
        external: Literal["disable", "enable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        signature: str | None = ...,
        constraint: str | None = ...,
        method: str | None = ...,
        address_list: str | None = ...,
        url_access: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        external: Literal["disable", "enable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        signature: str | None = ...,
        constraint: str | None = ...,
        method: str | None = ...,
        address_list: str | None = ...,
        url_access: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
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