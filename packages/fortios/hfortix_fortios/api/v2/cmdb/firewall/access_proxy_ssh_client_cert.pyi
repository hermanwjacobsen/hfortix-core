from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
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

# Nested classes for table field children

@final
class AccessProxySshClientCertCertextensionObject:
    """Typed object for cert-extension table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name of certificate extension.
    name: str
    # Critical option.
    critical: Literal["no", "yes"]
    # Type of certificate extension.
    type: Literal["fixed", "user"]
    # Data of certificate extension.
    data: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AccessProxySshClientCertResponse(TypedDict):
    """
    Type hints for firewall/access_proxy_ssh_client_cert API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    source_address: Literal["enable", "disable"]
    permit_x11_forwarding: Literal["enable", "disable"]
    permit_agent_forwarding: Literal["enable", "disable"]
    permit_port_forwarding: Literal["enable", "disable"]
    permit_pty: Literal["enable", "disable"]
    permit_user_rc: Literal["enable", "disable"]
    cert_extension: list[dict[str, Any]]
    auth_ca: str


@final
class AccessProxySshClientCertObject:
    """Typed FortiObject for firewall/access_proxy_ssh_client_cert with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
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
    cert_extension: list[AccessProxySshClientCertCertextensionObject]  # Table field - list of typed objects
    # Name of the SSH server public key authentication CA.
    auth_ca: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AccessProxySshClientCertPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AccessProxySshClientCert:
    """
    Configure Access Proxy SSH client certificate.
    
    Path: firewall/access_proxy_ssh_client_cert
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> AccessProxySshClientCertObject: ...
    
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
    ) -> AccessProxySshClientCertResponse: ...
    
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
    ) -> AccessProxySshClientCertResponse: ...
    
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
    ) -> list[AccessProxySshClientCertResponse]: ...
    
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