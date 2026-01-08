from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class EmailServerPayload(TypedDict, total=False):
    """
    Type hints for system/email_server payload fields.
    
    Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: EmailServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    type: NotRequired[Literal["custom"]]  # Use FortiGuard Message service or custom email server.
    server: NotRequired[str]  # SMTP server IP address or hostname.
    port: NotRequired[int]  # SMTP server port.
    source_ip: NotRequired[str]  # SMTP server IPv4 source IP.
    source_ip6: NotRequired[str]  # SMTP server IPv6 source IP.
    authenticate: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication.
    validate_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable validation of server certificate.
    username: NotRequired[str]  # SMTP server user name for authentication.
    password: NotRequired[str]  # SMTP server user password for authentication.
    security: NotRequired[Literal["none", "starttls", "smtps"]]  # Connection security used by the email server.
    ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class EmailServerObject(FortiObject[EmailServerPayload]):
    """Typed FortiObject for system/email_server with IDE autocomplete support."""
    
    # Use FortiGuard Message service or custom email server.
    type: Literal["custom"]
    # SMTP server IP address or hostname.
    server: str
    # SMTP server port.
    port: int
    # SMTP server IPv4 source IP.
    source_ip: str
    # SMTP server IPv6 source IP.
    source_ip6: str
    # Enable/disable authentication.
    authenticate: Literal["enable", "disable"]
    # Enable/disable validation of server certificate.
    validate_server: Literal["enable", "disable"]
    # SMTP server user name for authentication.
    username: str
    # SMTP server user password for authentication.
    password: str
    # Connection security used by the email server.
    security: Literal["none", "starttls", "smtps"]
    # Minimum supported protocol version for SSL/TLS connections (default is to follow
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> EmailServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class EmailServer:
    """
    Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
    
    Path: system/email_server
    Category: cmdb
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> EmailServerObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> EmailServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "EmailServer",
    "EmailServerPayload",
    "EmailServerObject",
]