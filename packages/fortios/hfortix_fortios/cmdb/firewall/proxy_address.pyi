from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ProxyAddressPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy_address payload fields.
    
    Configure web proxy address.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: host)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: host)
        - :class:`~.firewall.proxy-address.ProxyAddressEndpoint` (via: host)
        - :class:`~.firewall.vip.VipEndpoint` (via: host)
        - :class:`~.firewall.vipgrp.VipgrpEndpoint` (via: host)

    **Usage:**
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


class ProxyAddressObject(FortiObject[ProxyAddressPayload]):
    """Typed FortiObject for firewall/proxy_address with IDE autocomplete support."""
    
    # Address name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Proxy address type.
    type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"]
    # Address object for the host.
    host: str
    # Host name as a regular expression.
    host_regex: str
    # URL path as a regular expression.
    path: str
    # Match the query part of the URL as a regular expression.
    query: str
    # Enable/disable use of referrer field in the HTTP header to match the address.
    referrer: Literal["enable", "disable"]
    # FortiGuard category ID.
    category: list[str]  # Auto-flattened from member_table
    # HTTP request methods to be used.
    method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"]
    # Names of browsers to be used as user agent.
    ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"]
    # Minimum version of the user agent specified in dotted notation. For example, use
    ua_min_ver: str
    # Maximum version of the user agent specified in dotted notation. For example, use
    ua_max_ver: str
    # Name of HTTP header.
    header_name: str
    # HTTP header name as a regular expression.
    header: str
    # Enable to make the pattern case sensitive.
    case_sensitivity: Literal["disable", "enable"]
    # HTTP header group.
    header_group: list[str]  # Auto-flattened from member_table
    # Integer value to determine the color of the icon in the GUI (1 - 32, default = 0
    color: int
    # Config object tagging.
    tagging: list[str]  # Auto-flattened from member_table
    # Optional comments.
    comment: str
    # SaaS application.
    application: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProxyAddressPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ProxyAddress:
    """
    Configure web proxy address.
    
    Path: firewall/proxy_address
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> list[ProxyAddressObject]: ...
    
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
    ) -> ProxyAddressObject | list[ProxyAddressObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProxyAddressObject: ...
    
    @overload
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ProxyAddressObject: ...
    
    @overload
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ProxyAddressObject: ...
    
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
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | list[dict[str, Any]] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ProxyAddress",
    "ProxyAddressPayload",
    "ProxyAddressObject",
]