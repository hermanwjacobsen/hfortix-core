from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SamlPayload(TypedDict, total=False):
    """
    Type hints for system/saml payload fields.
    
    Global settings for SAML authentication.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: cert)
        - :class:`~.certificate.remote.RemoteEndpoint` (via: idp-cert)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: default-profile)

    **Usage:**
        payload: SamlPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SAML authentication (default = disable).
    role: NotRequired[Literal["identity-provider", "service-provider"]]  # SAML role.
    default_login_page: Literal["normal", "sso"]  # Choose default login page.
    default_profile: str  # Default profile for new SSO admin.
    cert: NotRequired[str]  # Certificate to sign SAML messages.
    binding_protocol: NotRequired[Literal["post", "redirect"]]  # IdP Binding protocol.
    portal_url: NotRequired[str]  # SP portal URL.
    entity_id: str  # SP entity ID.
    single_sign_on_url: NotRequired[str]  # SP single sign-on URL.
    single_logout_url: NotRequired[str]  # SP single logout URL.
    idp_entity_id: NotRequired[str]  # IDP entity ID.
    idp_single_sign_on_url: NotRequired[str]  # IDP single sign-on URL.
    idp_single_logout_url: NotRequired[str]  # IDP single logout URL.
    idp_cert: str  # IDP certificate name.
    server_address: str  # Server address.
    require_signed_resp_and_asrt: NotRequired[Literal["enable", "disable"]]  # Require both response and assertion from IDP to be signed wh
    tolerance: NotRequired[int]  # Tolerance to the range of time when the assertion is valid
    life: NotRequired[int]  # Length of the range of time when the assertion is valid
    service_providers: NotRequired[list[dict[str, Any]]]  # Authorized service providers.

# Nested classes for table field children

@final
class SamlServiceprovidersObject:
    """Typed object for service-providers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name.
    name: str
    # Prefix.
    prefix: str
    # SP binding protocol.
    sp_binding_protocol: Literal["post", "redirect"]
    # SP certificate name.
    sp_cert: str
    # SP entity ID.
    sp_entity_id: str
    # SP single sign-on URL.
    sp_single_sign_on_url: str
    # SP single logout URL.
    sp_single_logout_url: str
    # SP portal URL.
    sp_portal_url: str
    # IDP entity ID.
    idp_entity_id: str
    # IDP single sign-on URL.
    idp_single_sign_on_url: str
    # IDP single logout URL.
    idp_single_logout_url: str
    # Customized SAML attributes to send along with assertion.
    assertion_attributes: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SamlResponse(TypedDict):
    """
    Type hints for system/saml API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    role: Literal["identity-provider", "service-provider"]
    default_login_page: Literal["normal", "sso"]
    default_profile: str
    cert: str
    binding_protocol: Literal["post", "redirect"]
    portal_url: str
    entity_id: str
    single_sign_on_url: str
    single_logout_url: str
    idp_entity_id: str
    idp_single_sign_on_url: str
    idp_single_logout_url: str
    idp_cert: str
    server_address: str
    require_signed_resp_and_asrt: Literal["enable", "disable"]
    tolerance: int
    life: int
    service_providers: list[dict[str, Any]]


@final
class SamlObject:
    """Typed FortiObject for system/saml with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable SAML authentication (default = disable).
    status: Literal["enable", "disable"]
    # SAML role.
    role: Literal["identity-provider", "service-provider"]
    # Choose default login page.
    default_login_page: Literal["normal", "sso"]
    # Default profile for new SSO admin.
    default_profile: str
    # Certificate to sign SAML messages.
    cert: str
    # IdP Binding protocol.
    binding_protocol: Literal["post", "redirect"]
    # SP portal URL.
    portal_url: str
    # SP entity ID.
    entity_id: str
    # SP single sign-on URL.
    single_sign_on_url: str
    # SP single logout URL.
    single_logout_url: str
    # IDP entity ID.
    idp_entity_id: str
    # IDP single sign-on URL.
    idp_single_sign_on_url: str
    # IDP single logout URL.
    idp_single_logout_url: str
    # IDP certificate name.
    idp_cert: str
    # Server address.
    server_address: str
    # Require both response and assertion from IDP to be signed when FGT acts as SP
    require_signed_resp_and_asrt: Literal["enable", "disable"]
    # Tolerance to the range of time when the assertion is valid (in minutes).
    tolerance: int
    # Length of the range of time when the assertion is valid (in minutes).
    life: int
    # Authorized service providers.
    service_providers: list[SamlServiceprovidersObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SamlPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Saml:
    """
    Global settings for SAML authentication.
    
    Path: system/saml
    Category: cmdb
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlObject: ...
    
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
    ) -> SamlResponse: ...
    
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
    ) -> SamlResponse: ...
    
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
    ) -> SamlResponse: ...
    
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
    ) -> SamlObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SamlObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: SamlPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        role: Literal["identity-provider", "service-provider"] | None = ...,
        default_login_page: Literal["normal", "sso"] | None = ...,
        default_profile: str | None = ...,
        cert: str | None = ...,
        binding_protocol: Literal["post", "redirect"] | None = ...,
        portal_url: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        server_address: str | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Saml",
    "SamlPayload",
    "SamlObject",
]