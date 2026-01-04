from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class EmailServerPayload(TypedDict, total=False):
    """
    Type hints for system/email_server payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class EmailServer:
    """
    Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
    
    Path: system/email_server
    Category: cmdb
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: EmailServerPayload | None = ...,
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