from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class HostKeyPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssh/host_key payload fields.
    
    SSH proxy host public keys.
    
    **Usage:**
        payload: HostKeyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SSH public key name.
    status: NotRequired[Literal["trusted", "revoked"]]  # Set the trust status of the public key.
    type: NotRequired[Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]]  # Set the type of the public key.
    nid: NotRequired[Literal["256", "384", "521"]]  # Set the nid of the ECDSA key.
    usage: NotRequired[Literal["transparent-proxy", "access-proxy"]]  # Usage for this public key.
    ip: NotRequired[str]  # IP address of the SSH server.
    port: NotRequired[int]  # Port of the SSH server.
    hostname: NotRequired[str]  # Hostname of the SSH server to match SSH certificate principa
    public_key: NotRequired[str]  # SSH public key.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class HostKeyResponse(TypedDict):
    """
    Type hints for firewall/ssh/host_key API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["trusted", "revoked"]
    type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]
    nid: Literal["256", "384", "521"]
    usage: Literal["transparent-proxy", "access-proxy"]
    ip: str
    port: int
    hostname: str
    public_key: str


@final
class HostKeyObject:
    """Typed FortiObject for firewall/ssh/host_key with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SSH public key name.
    name: str
    # Set the trust status of the public key.
    status: Literal["trusted", "revoked"]
    # Set the type of the public key.
    type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"]
    # Set the nid of the ECDSA key.
    nid: Literal["256", "384", "521"]
    # Usage for this public key.
    usage: Literal["transparent-proxy", "access-proxy"]
    # IP address of the SSH server.
    ip: str
    # Port of the SSH server.
    port: int
    # Hostname of the SSH server to match SSH certificate principals.
    hostname: str
    # SSH public key.
    public_key: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> HostKeyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class HostKey:
    """
    SSH proxy host public keys.
    
    Path: firewall/ssh/host_key
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
    ) -> HostKeyObject: ...
    
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
    ) -> HostKeyObject: ...
    
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
    ) -> list[HostKeyObject]: ...
    
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
    ) -> HostKeyResponse: ...
    
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
    ) -> HostKeyResponse: ...
    
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
    ) -> list[HostKeyResponse]: ...
    
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
    ) -> HostKeyObject | list[HostKeyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HostKeyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> HostKeyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
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
    ) -> HostKeyObject: ...
    
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
        payload_dict: HostKeyPayload | None = ...,
        name: str | None = ...,
        status: Literal["trusted", "revoked"] | None = ...,
        type: Literal["RSA", "DSA", "ECDSA", "ED25519", "RSA-CA", "DSA-CA", "ECDSA-CA", "ED25519-CA"] | None = ...,
        nid: Literal["256", "384", "521"] | None = ...,
        usage: Literal["transparent-proxy", "access-proxy"] | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        hostname: str | None = ...,
        public_key: str | None = ...,
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
    "HostKey",
    "HostKeyPayload",
    "HostKeyObject",
]