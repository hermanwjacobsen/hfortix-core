from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class RulePayload(TypedDict, total=False):
    """
    Type hints for authentication/rule payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Rule:
    """
    Configure Authentication Rules.
    
    Path: authentication/rule
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
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
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
        payload_dict: RulePayload | None = ...,
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