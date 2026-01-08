from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ScimPayload(TypedDict, total=False):
    """
    Type hints for user/scim payload fields.
    
    Configure SCIM client entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: certificate)
        - :class:`~.certificate.remote.RemoteEndpoint` (via: certificate)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: certificate)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: token-certificate)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: certificate, token-certificate)

    **Usage:**
        payload: ScimPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SCIM client name.
    id: NotRequired[int]  # SCIM client ID.
    status: Literal["enable", "disable"]  # Enable/disable System for Cross-domain Identity Management
    base_url: NotRequired[str]  # Server URL to receive SCIM create, read, update, delete
    auth_method: NotRequired[Literal["token", "base"]]  # TLS client authentication methods (default = bearer token).
    token_certificate: NotRequired[str]  # Certificate for token verification.
    secret: NotRequired[str]  # Secret for token verification or base authentication.
    certificate: NotRequired[str]  # Certificate for client verification during TLS handshake.
    client_identity_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable client identity check.
    cascade: NotRequired[Literal["disable", "enable"]]  # Enable/disable to follow SCIM users/groups changes in IDP.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ScimResponse(TypedDict):
    """
    Type hints for user/scim API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    id: int
    status: Literal["enable", "disable"]
    base_url: str
    auth_method: Literal["token", "base"]
    token_certificate: str
    secret: str
    certificate: str
    client_identity_check: Literal["enable", "disable"]
    cascade: Literal["disable", "enable"]


@final
class ScimObject:
    """Typed FortiObject for user/scim with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SCIM client name.
    name: str
    # SCIM client ID.
    id: int
    # Enable/disable System for Cross-domain Identity Management (SCIM).
    status: Literal["enable", "disable"]
    # Server URL to receive SCIM create, read, update, delete (CRUD) requests.
    base_url: str
    # TLS client authentication methods (default = bearer token).
    auth_method: Literal["token", "base"]
    # Certificate for token verification.
    token_certificate: str
    # Secret for token verification or base authentication.
    secret: str
    # Certificate for client verification during TLS handshake.
    certificate: str
    # Enable/disable client identity check.
    client_identity_check: Literal["enable", "disable"]
    # Enable/disable to follow SCIM users/groups changes in IDP.
    cascade: Literal["disable", "enable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ScimPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Scim:
    """
    Configure SCIM client entries.
    
    Path: user/scim
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
    ) -> ScimObject: ...
    
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
    ) -> ScimObject: ...
    
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
    ) -> list[ScimObject]: ...
    
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
    ) -> ScimResponse: ...
    
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
    ) -> ScimResponse: ...
    
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
    ) -> list[ScimResponse]: ...
    
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
    ) -> ScimObject | list[ScimObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ScimObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ScimObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
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
    ) -> ScimObject: ...
    
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
        payload_dict: ScimPayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        base_url: str | None = ...,
        auth_method: Literal["token", "base"] | None = ...,
        token_certificate: str | None = ...,
        secret: str | None = ...,
        certificate: str | None = ...,
        client_identity_check: Literal["enable", "disable"] | None = ...,
        cascade: Literal["disable", "enable"] | None = ...,
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
    "Scim",
    "ScimPayload",
    "ScimObject",
]