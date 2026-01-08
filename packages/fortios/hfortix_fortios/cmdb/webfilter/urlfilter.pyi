from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class UrlfilterPayload(TypedDict, total=False):
    """
    Type hints for webfilter/urlfilter payload fields.
    
    Configure URL filter lists.
    
    **Usage:**
        payload: UrlfilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID.
    name: str  # Name of URL filter list.
    comment: NotRequired[str]  # Optional comments.
    one_arm_ips_urlfilter: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS resolver for one-arm IPS URL filter opera
    ip_addr_block: NotRequired[Literal["enable", "disable"]]  # Enable/disable blocking URLs when the hostname appears as an
    ip4_mapped_ip6: NotRequired[Literal["enable", "disable"]]  # Enable/disable matching of IPv4 mapped IPv6 URLs.
    include_subdomains: NotRequired[Literal["enable", "disable"]]  # Enable/disable matching subdomains. Applies only to simple t
    entries: list[dict[str, Any]]  # URL filter entries.


class UrlfilterObject(FortiObject[UrlfilterPayload]):
    """Typed FortiObject for webfilter/urlfilter with IDE autocomplete support."""
    
    # ID.
    id: int
    # Name of URL filter list.
    name: str
    # Optional comments.
    comment: str
    # Enable/disable DNS resolver for one-arm IPS URL filter operation.
    one_arm_ips_urlfilter: Literal["enable", "disable"]
    # Enable/disable blocking URLs when the hostname appears as an IP address.
    ip_addr_block: Literal["enable", "disable"]
    # Enable/disable matching of IPv4 mapped IPv6 URLs.
    ip4_mapped_ip6: Literal["enable", "disable"]
    # Enable/disable matching subdomains. Applies only to simple type (default = enabl
    include_subdomains: Literal["enable", "disable"]
    # URL filter entries.
    entries: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> UrlfilterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Urlfilter:
    """
    Configure URL filter lists.
    
    Path: webfilter/urlfilter
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        id: int,
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
    ) -> UrlfilterObject: ...
    
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
    ) -> list[UrlfilterObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
        id: None = None,
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
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> UrlfilterObject | list[UrlfilterObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UrlfilterObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UrlfilterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UrlfilterObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Urlfilter",
    "UrlfilterPayload",
    "UrlfilterObject",
]