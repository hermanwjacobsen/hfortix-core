from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class AccessProxySshClientCertPayload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy_ssh_client_cert payload fields.
    
    Configure Access Proxy SSH client certificate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.ssh.local-ca.LocalCaEndpoint` (via: auth-ca)

    **Usage:**
        payload: AccessProxySshClientCertPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SSH client certificate name.
    source_address: NotRequired[Literal["enable", "disable"]]  # Enable/disable appending source-address certificate critical
    permit_x11_forwarding: NotRequired[Literal["enable", "disable"]]  # Enable/disable appending permit-x11-forwarding certificate e
    permit_agent_forwarding: NotRequired[Literal["enable", "disable"]]  # Enable/disable appending permit-agent-forwarding certificate
    permit_port_forwarding: NotRequired[Literal["enable", "disable"]]  # Enable/disable appending permit-port-forwarding certificate 
    permit_pty: NotRequired[Literal["enable", "disable"]]  # Enable/disable appending permit-pty certificate extension.
    permit_user_rc: NotRequired[Literal["enable", "disable"]]  # Enable/disable appending permit-user-rc certificate extensio
    cert_extension: NotRequired[list[dict[str, Any]]]  # Configure certificate extension for user certificate.
    auth_ca: str  # Name of the SSH server public key authentication CA.


class AccessProxySshClientCertObject(FortiObject[AccessProxySshClientCertPayload]):
    """Typed FortiObject for firewall/access_proxy_ssh_client_cert with IDE autocomplete support."""
    
    # SSH client certificate name.
    name: str
    # Enable/disable appending source-address certificate critical option. This option
    source_address: Literal["enable", "disable"]
    # Enable/disable appending permit-x11-forwarding certificate extension.
    permit_x11_forwarding: Literal["enable", "disable"]
    # Enable/disable appending permit-agent-forwarding certificate extension.
    permit_agent_forwarding: Literal["enable", "disable"]
    # Enable/disable appending permit-port-forwarding certificate extension.
    permit_port_forwarding: Literal["enable", "disable"]
    # Enable/disable appending permit-pty certificate extension.
    permit_pty: Literal["enable", "disable"]
    # Enable/disable appending permit-user-rc certificate extension.
    permit_user_rc: Literal["enable", "disable"]
    # Configure certificate extension for user certificate.
    cert_extension: list[str]  # Auto-flattened from member_table
    # Name of the SSH server public key authentication CA.
    auth_ca: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AccessProxySshClientCertPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AccessProxySshClientCert:
    """
    Configure Access Proxy SSH client certificate.
    
    Path: firewall/access_proxy_ssh_client_cert
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> list[AccessProxySshClientCertObject]: ...
    
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
    ) -> AccessProxySshClientCertObject | list[AccessProxySshClientCertObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxySshClientCertObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccessProxySshClientCertObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
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
    ) -> AccessProxySshClientCertObject: ...
    
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
        payload_dict: AccessProxySshClientCertPayload | None = ...,
        name: str | None = ...,
        source_address: Literal["enable", "disable"] | None = ...,
        permit_x11_forwarding: Literal["enable", "disable"] | None = ...,
        permit_agent_forwarding: Literal["enable", "disable"] | None = ...,
        permit_port_forwarding: Literal["enable", "disable"] | None = ...,
        permit_pty: Literal["enable", "disable"] | None = ...,
        permit_user_rc: Literal["enable", "disable"] | None = ...,
        cert_extension: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ca: str | None = ...,
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
    "AccessProxySshClientCert",
    "AccessProxySshClientCertPayload",
    "AccessProxySshClientCertObject",
]