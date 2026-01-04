from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class UrlfilterPayload(TypedDict, total=False):
    """
    Type hints for webfilter/urlfilter payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Urlfilter:
    """
    Configure URL filter lists.
    
    Path: webfilter/urlfilter
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
        payload_dict: UrlfilterPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        one_arm_ips_urlfilter: Literal["enable", "disable"] | None = ...,
        ip_addr_block: Literal["enable", "disable"] | None = ...,
        ip4_mapped_ip6: Literal["enable", "disable"] | None = ...,
        include_subdomains: Literal["enable", "disable"] | None = ...,
        entries: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        entries: list[dict[str, Any]] | None = ...,
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
        payload_dict: UrlfilterPayload | None = ...,
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