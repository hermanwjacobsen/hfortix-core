from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpsUrlfilterDnsPayload(TypedDict, total=False):
    """
    Type hints for system/ips_urlfilter_dns payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpsUrlfilterDnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    address: NotRequired[str]  # DNS server IP address.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable using this DNS server for IPS URL filter DNS 
    ipv6_capability: NotRequired[Literal["enable", "disable"]]  # Enable/disable this server for IPv6 queries.


class IpsUrlfilterDns:
    """
    Configure IPS URL filter DNS servers.
    
    Path: system/ips_urlfilter_dns
    Category: cmdb
    Primary Key: address
    """
    
    def get(
        self,
        address: str | None = ...,
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
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
        address: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        ipv6_capability: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        address: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        address: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: IpsUrlfilterDnsPayload | None = ...,
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