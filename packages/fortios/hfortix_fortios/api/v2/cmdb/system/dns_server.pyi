from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DnsServerPayload(TypedDict, total=False):
    """
    Type hints for system/dns_server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DnsServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # DNS server name.
    mode: NotRequired[Literal["recursive", "non-recursive", "forward-only", "resolver"]]  # DNS server mode.
    dnsfilter_profile: NotRequired[str]  # DNS filter profile.
    doh: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS over HTTPS/443 (default = disable).
    doh3: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS over QUIC/HTTP3/443 (default = disable).
    doq: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS over QUIC/853 (default = disable).


class DnsServer:
    """
    Configure DNS servers.
    
    Path: system/dns_server
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
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
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
        payload_dict: DnsServerPayload | None = ...,
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