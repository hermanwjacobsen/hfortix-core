from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProxyAddressPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy_address payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProxyAddressPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Address name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    type: NotRequired[Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"]]  # Proxy address type.
    host: str  # Address object for the host.
    host_regex: NotRequired[str]  # Host name as a regular expression.
    path: NotRequired[str]  # URL path as a regular expression.
    query: NotRequired[str]  # Match the query part of the URL as a regular expression.
    referrer: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of referrer field in the HTTP header to m
    category: NotRequired[list[dict[str, Any]]]  # FortiGuard category ID.
    method: NotRequired[Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"]]  # HTTP request methods to be used.
    ua: NotRequired[Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"]]  # Names of browsers to be used as user agent.
    ua_min_ver: NotRequired[str]  # Minimum version of the user agent specified in dotted notati
    ua_max_ver: NotRequired[str]  # Maximum version of the user agent specified in dotted notati
    header_name: NotRequired[str]  # Name of HTTP header.
    header: NotRequired[str]  # HTTP header name as a regular expression.
    case_sensitivity: NotRequired[Literal["disable", "enable"]]  # Enable to make the pattern case sensitive.
    header_group: NotRequired[list[dict[str, Any]]]  # HTTP header group.
    color: NotRequired[int]  # Integer value to determine the color of the icon in the GUI 
    tagging: NotRequired[list[dict[str, Any]]]  # Config object tagging.
    comment: NotRequired[str]  # Optional comments.
    application: list[dict[str, Any]]  # SaaS application.


class ProxyAddress:
    """
    Configure web proxy address.
    
    Path: firewall/proxy_address
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
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: list[dict[str, Any]] | None = ...,
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
        payload_dict: ProxyAddressPayload | None = ...,
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
    "ProxyAddress",
    "ProxyAddressPayload",
]