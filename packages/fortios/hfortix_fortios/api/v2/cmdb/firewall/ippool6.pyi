from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Ippool6Payload(TypedDict, total=False):
    """
    Type hints for firewall/ippool6 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Ippool6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IPv6 IP pool name.
    type: NotRequired[Literal["overload", "nptv6"]]  # Configure IPv6 pool type (overload or NPTv6).
    startip: str  # First IPv6 address (inclusive) in the range for the address 
    endip: str  # Final IPv6 address (inclusive) in the range for the address 
    internal_prefix: str  # Internal NPTv6 prefix length (32 - 64).
    external_prefix: str  # External NPTv6 prefix length (32 - 64).
    comments: NotRequired[str]  # Comment.
    nat46: NotRequired[Literal["disable", "enable"]]  # Enable/disable NAT46.
    add_nat46_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable adding NAT46 route.


class Ippool6:
    """
    Configure IPv6 IP pools.
    
    Path: firewall/ippool6
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
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Ippool6Payload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "nptv6"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        internal_prefix: str | None = ...,
        external_prefix: str | None = ...,
        comments: str | None = ...,
        nat46: Literal["disable", "enable"] | None = ...,
        add_nat46_route: Literal["disable", "enable"] | None = ...,
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
        payload_dict: Ippool6Payload | None = ...,
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