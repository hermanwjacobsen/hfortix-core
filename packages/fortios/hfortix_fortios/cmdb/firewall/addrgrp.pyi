from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class AddrgrpPayload(TypedDict, total=False):
    """
    Type hints for firewall/addrgrp payload fields.
    
    Configure IPv4 address groups.
    
    **Usage:**
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


class AddrgrpObject(FortiObject[AddrgrpPayload]):
    """Typed FortiObject for firewall/addrgrp with IDE autocomplete support."""
    
    # Address group name.
    name: str
    # Address group type.
    type: Literal["default", "folder"]
    # Address group category.
    category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"]
    # Enable/disable use of this group in routing configurations.
    allow_routing: Literal["enable", "disable"]
    # Address objects contained within the group.
    member: list[str]  # Auto-flattened from member_table
    # Comment.
    comment: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Enable/disable address exclusion.
    exclude: Literal["enable", "disable"]
    # Address exclusion member.
    exclude_member: list[str]  # Auto-flattened from member_table
    # Color of icon on the GUI.
    color: int
    # Config object tagging.
    tagging: list[str]  # Auto-flattened from member_table
    # Security Fabric global object setting.
    fabric_object: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AddrgrpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Addrgrp:
    """
    Configure IPv4 address groups.
    
    Path: firewall/addrgrp
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> AddrgrpObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[AddrgrpObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> AddrgrpObject | list[AddrgrpObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AddrgrpObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AddrgrpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AddrgrpObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AddrgrpPayload | None = ...,
        name: str | None = ...,
        type: Literal["default", "folder"] | None = ...,
        category: Literal["default", "ztna-ems-tag", "ztna-geo-tag"] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        uuid: str | None = ...,
        exclude: Literal["enable", "disable"] | None = ...,
        exclude_member: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "Addrgrp",
    "AddrgrpPayload",
    "AddrgrpObject",
]