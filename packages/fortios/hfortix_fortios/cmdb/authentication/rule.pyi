from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class RulePayload(TypedDict, total=False):
    """
    Type hints for authentication/rule payload fields.
    
    Configure Authentication Rules.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.authentication.scheme.SchemeEndpoint` (via: active-auth-method, sso-auth-method)

    **Usage:**
        payload: RulePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Authentication rule name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this authentication rule.
    protocol: NotRequired[Literal["http", "ftp", "socks", "ssh", "ztna-portal"]]  # Authentication is required for the selected protocol (defaul
    srcintf: NotRequired[list[dict[str, Any]]]  # Incoming (ingress) interface.
    srcaddr: NotRequired[list[dict[str, Any]]]  # Authentication is required for the selected IPv4 source addr
    dstaddr: NotRequired[list[dict[str, Any]]]  # Select an IPv4 destination address from available options. R
    srcaddr6: NotRequired[list[dict[str, Any]]]  # Authentication is required for the selected IPv6 source addr
    dstaddr6: NotRequired[list[dict[str, Any]]]  # Select an IPv6 destination address from available options. R
    ip_based: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP-based authentication. When enabled, previo
    active_auth_method: NotRequired[str]  # Select an active authentication method.
    sso_auth_method: NotRequired[str]  # Select a single-sign on (SSO) authentication method.
    web_auth_cookie: NotRequired[Literal["enable", "disable"]]  # Enable/disable Web authentication cookies (default = disable
    cors_stateful: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowance of CORS access (default = disable).
    cors_depth: NotRequired[int]  # Depth to allow CORS access (default = 3).
    cert_auth_cookie: NotRequired[Literal["enable", "disable"]]  # Enable/disable to use device certificate as authentication c
    transaction_based: NotRequired[Literal["enable", "disable"]]  # Enable/disable transaction based authentication (default = d
    web_portal: NotRequired[Literal["enable", "disable"]]  # Enable/disable web portal for proxy transparent policy (defa
    comments: NotRequired[str]  # Comment.
    session_logout: NotRequired[Literal["enable", "disable"]]  # Enable/disable logout of a user from the current session.


class RuleObject(FortiObject[RulePayload]):
    """Typed FortiObject for authentication/rule with IDE autocomplete support."""
    
    # Authentication rule name.
    name: str
    # Enable/disable this authentication rule.
    status: Literal["enable", "disable"]
    # Authentication is required for the selected protocol (default = HTTP).
    protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"]
    # Incoming (ingress) interface.
    srcintf: list[str]  # Auto-flattened from member_table
    # Authentication is required for the selected IPv4 source address.
    srcaddr: list[str]  # Auto-flattened from member_table
    # Select an IPv4 destination address from available options. Required for web prox
    dstaddr: list[str]  # Auto-flattened from member_table
    # Authentication is required for the selected IPv6 source address.
    srcaddr6: list[str]  # Auto-flattened from member_table
    # Select an IPv6 destination address from available options. Required for web prox
    dstaddr6: list[str]  # Auto-flattened from member_table
    # Enable/disable IP-based authentication. When enabled, previously authenticated u
    ip_based: Literal["enable", "disable"]
    # Select an active authentication method.
    active_auth_method: str
    # Select a single-sign on (SSO) authentication method.
    sso_auth_method: str
    # Enable/disable Web authentication cookies (default = disable).
    web_auth_cookie: Literal["enable", "disable"]
    # Enable/disable allowance of CORS access (default = disable).
    cors_stateful: Literal["enable", "disable"]
    # Depth to allow CORS access (default = 3).
    cors_depth: int
    # Enable/disable to use device certificate as authentication cookie (default = ena
    cert_auth_cookie: Literal["enable", "disable"]
    # Enable/disable transaction based authentication (default = disable).
    transaction_based: Literal["enable", "disable"]
    # Enable/disable web portal for proxy transparent policy (default = enable).
    web_portal: Literal["enable", "disable"]
    # Comment.
    comments: str
    # Enable/disable logout of a user from the current session.
    session_logout: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RulePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Rule:
    """
    Configure Authentication Rules.
    
    Path: authentication/rule
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
    ) -> RuleObject: ...
    
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
    ) -> list[RuleObject]: ...
    
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
    ) -> RuleObject | list[RuleObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RuleObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RuleObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
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
    ) -> RuleObject: ...
    
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
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
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
    "Rule",
    "RulePayload",
    "RuleObject",
]