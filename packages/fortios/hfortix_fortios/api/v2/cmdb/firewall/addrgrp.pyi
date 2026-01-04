from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AddrgrpPayload(TypedDict, total=False):
    """
    Type hints for firewall/addrgrp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AddrgrpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Address group name.
    type: NotRequired[Literal["default", "folder"]]  # Address group type.
    category: NotRequired[Literal["default", "ztna-ems-tag", "ztna-geo-tag"]]  # Address group category.
    allow_routing: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of this group in routing configurations.
    member: NotRequired[list[dict[str, Any]]]  # Address objects contained within the group.
    comment: NotRequired[str]  # Comment.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    exclude: NotRequired[Literal["enable", "disable"]]  # Enable/disable address exclusion.
    exclude_member: list[dict[str, Any]]  # Address exclusion member.
    color: NotRequired[int]  # Color of icon on the GUI.
    tagging: NotRequired[list[dict[str, Any]]]  # Config object tagging.
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class Addrgrp:
    """
    Configure IPv4 address groups.
    
    Path: firewall/addrgrp
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
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
        payload_dict: AddrgrpPayload | None = ...,
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