from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AccessControlListPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/access_control_list payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AccessControlListPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # AP access control list name.
    comment: NotRequired[str]  # Description.
    layer3_ipv4_rules: NotRequired[list[dict[str, Any]]]  # AP ACL layer3 ipv4 rule list.
    layer3_ipv6_rules: NotRequired[list[dict[str, Any]]]  # AP ACL layer3 ipv6 rule list.


class AccessControlList:
    """
    Configure WiFi bridge access control list.
    
    Path: wireless_controller/access_control_list
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
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AccessControlListPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        layer3_ipv4_rules: list[dict[str, Any]] | None = ...,
        layer3_ipv6_rules: list[dict[str, Any]] | None = ...,
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
        payload_dict: AccessControlListPayload | None = ...,
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
    "AccessControlList",
    "AccessControlListPayload",
]