from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ForwardServerPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/forward_server payload fields.
    
    Configure forward-server addresses.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: ForwardServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Server name.
    addr_type: NotRequired[Literal["ip", "ipv6", "fqdn"]]  # Address type of the forwarding proxy server: IP or FQDN.
    ip: NotRequired[str]  # Forward proxy server IP address.
    ipv6: NotRequired[str]  # Forward proxy server IPv6 address.
    fqdn: NotRequired[str]  # Forward server Fully Qualified Domain Name (FQDN).
    port: NotRequired[int]  # Port number that the forwarding server expects to receive HT
    interface_select_method: NotRequired[Literal["sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    comment: NotRequired[str]  # Comment.
    masquerade: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of the IP address of the outgoing interfa
    healthcheck: NotRequired[Literal["disable", "enable"]]  # Enable/disable forward server health checking. Attempts to c
    monitor: NotRequired[str]  # URL for forward server health check monitoring
    server_down_option: NotRequired[Literal["block", "pass"]]  # Action to take when the forward server is found to be down:
    username: NotRequired[str]  # HTTP authentication user name.
    password: NotRequired[str]  # HTTP authentication password.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ForwardServerResponse(TypedDict):
    """
    Type hints for web_proxy/forward_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    addr_type: Literal["ip", "ipv6", "fqdn"]
    ip: str
    ipv6: str
    fqdn: str
    port: int
    interface_select_method: Literal["sdwan", "specify"]
    interface: str
    vrf_select: int
    comment: str
    masquerade: Literal["enable", "disable"]
    healthcheck: Literal["disable", "enable"]
    monitor: str
    server_down_option: Literal["block", "pass"]
    username: str
    password: str


@final
class ForwardServerObject:
    """Typed FortiObject for web_proxy/forward_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Server name.
    name: str
    # Address type of the forwarding proxy server: IP or FQDN.
    addr_type: Literal["ip", "ipv6", "fqdn"]
    # Forward proxy server IP address.
    ip: str
    # Forward proxy server IPv6 address.
    ipv6: str
    # Forward server Fully Qualified Domain Name (FQDN).
    fqdn: str
    # Port number that the forwarding server expects to receive HTTP sessions on
    port: int
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    # Comment.
    comment: str
    # Enable/disable use of the IP address of the outgoing interface as the client IP
    masquerade: Literal["enable", "disable"]
    # Enable/disable forward server health checking. Attempts to connect through the r
    healthcheck: Literal["disable", "enable"]
    # URL for forward server health check monitoring (default = www.google.com).
    monitor: str
    # Action to take when the forward server is found to be down: block sessions until
    server_down_option: Literal["block", "pass"]
    # HTTP authentication user name.
    username: str
    # HTTP authentication password.
    password: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ForwardServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ForwardServer:
    """
    Configure forward-server addresses.
    
    Path: web_proxy/forward_server
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
    ) -> ForwardServerObject: ...
    
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
    ) -> ForwardServerObject: ...
    
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
    ) -> list[ForwardServerObject]: ...
    
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
    ) -> ForwardServerResponse: ...
    
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
    ) -> ForwardServerResponse: ...
    
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
    ) -> list[ForwardServerResponse]: ...
    
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
    ) -> ForwardServerObject | list[ForwardServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ForwardServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ForwardServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
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
    ) -> ForwardServerObject: ...
    
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
        payload_dict: ForwardServerPayload | None = ...,
        name: str | None = ...,
        addr_type: Literal["ip", "ipv6", "fqdn"] | None = ...,
        ip: str | None = ...,
        ipv6: str | None = ...,
        fqdn: str | None = ...,
        port: int | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        comment: str | None = ...,
        masquerade: Literal["enable", "disable"] | None = ...,
        healthcheck: Literal["disable", "enable"] | None = ...,
        monitor: str | None = ...,
        server_down_option: Literal["block", "pass"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
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
    "ForwardServer",
    "ForwardServerPayload",
    "ForwardServerObject",
]