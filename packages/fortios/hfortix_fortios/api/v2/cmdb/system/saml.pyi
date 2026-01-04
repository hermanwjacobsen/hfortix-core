from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SamlPayload(TypedDict, total=False):
    """
    Type hints for system/saml payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    tolerance: NotRequired[int]  # Tolerance to the range of time when the assertion is valid (
    life: NotRequired[int]  # Length of the range of time when the assertion is valid (in 
    service_providers: NotRequired[list[dict[str, Any]]]  # Authorized service providers.


class Saml:
    """
    Global settings for SAML authentication.
    
    Path: system/saml
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
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        tolerance: int | None = ...,
        life: int | None = ...,
        service_providers: list[dict[str, Any]] | None = ...,
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
        payload_dict: SamlPayload | None = ...,
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