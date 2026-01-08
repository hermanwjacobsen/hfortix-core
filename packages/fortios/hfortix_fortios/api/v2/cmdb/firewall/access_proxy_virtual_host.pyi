from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AccessProxyVirtualHostPayload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy_virtual_host payload fields.
    
    Configure Access Proxy virtual hosts.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: AccessProxyVirtualHostPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Virtual host name.
    ssl_certificate: list[dict[str, Any]]  # SSL certificates for this host.
    host: str  # The host name.
    host_type: Literal["sub-string", "wildcard"]  # Type of host pattern.
    replacemsg_group: NotRequired[str]  # Access-proxy-virtual-host replacement message override group
    empty_cert_action: NotRequired[Literal["accept", "block", "accept-unmanageable"]]  # Action for an empty client certificate.
    user_agent_detect: NotRequired[Literal["disable", "enable"]]  # Enable/disable detecting device type by HTTP user-agent if n
    client_cert: NotRequired[Literal["disable", "enable"]]  # Enable/disable requesting client certificate.

# Nested classes for table field children

@final
class AccessProxyVirtualHostSslcertificateObject:
    """Typed object for ssl-certificate table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate list.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AccessProxyVirtualHostResponse(TypedDict):
    """
    Type hints for firewall/access_proxy_virtual_host API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    ssl_certificate: list[dict[str, Any]]
    host: str
    host_type: Literal["sub-string", "wildcard"]
    replacemsg_group: str
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    user_agent_detect: Literal["disable", "enable"]
    client_cert: Literal["disable", "enable"]


@final
class AccessProxyVirtualHostObject:
    """Typed FortiObject for firewall/access_proxy_virtual_host with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Virtual host name.
    name: str
    # SSL certificates for this host.
    ssl_certificate: list[AccessProxyVirtualHostSslcertificateObject]  # Table field - list of typed objects
    # The host name.
    host: str
    # Type of host pattern.
    host_type: Literal["sub-string", "wildcard"]
    # Access-proxy-virtual-host replacement message override group.
    replacemsg_group: str
    # Action for an empty client certificate.
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"]
    # Enable/disable detecting device type by HTTP user-agent if no client certificate
    user_agent_detect: Literal["disable", "enable"]
    # Enable/disable requesting client certificate.
    client_cert: Literal["disable", "enable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AccessProxyVirtualHostPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AccessProxyVirtualHost:
    """
    Configure Access Proxy virtual hosts.
    
    Path: firewall/access_proxy_virtual_host
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[AccessProxyVirtualHostObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> AccessProxyVirtualHostResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> AccessProxyVirtualHostResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[AccessProxyVirtualHostResponse]: ...
    
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
    ) -> AccessProxyVirtualHostObject | list[AccessProxyVirtualHostObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxyVirtualHostObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
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
    ) -> AccessProxyVirtualHostObject: ...
    
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
        payload_dict: AccessProxyVirtualHostPayload | None = ...,
        name: str | None = ...,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        host: str | None = ...,
        host_type: Literal["sub-string", "wildcard"] | None = ...,
        replacemsg_group: str | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
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
    "AccessProxyVirtualHost",
    "AccessProxyVirtualHostPayload",
    "AccessProxyVirtualHostObject",
]