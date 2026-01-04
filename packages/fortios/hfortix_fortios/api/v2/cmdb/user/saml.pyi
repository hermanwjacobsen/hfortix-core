from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SamlPayload(TypedDict, total=False):
    """
    Type hints for user/saml payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SamlPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # SAML server entry name.
    cert: NotRequired[str]  # Certificate to sign SAML messages.
    entity_id: str  # SP entity ID.
    single_sign_on_url: str  # SP single sign-on URL.
    single_logout_url: NotRequired[str]  # SP single logout URL.
    idp_entity_id: str  # IDP entity ID.
    idp_single_sign_on_url: str  # IDP single sign-on URL.
    idp_single_logout_url: NotRequired[str]  # IDP single logout url.
    idp_cert: str  # IDP Certificate name.
    scim_client: NotRequired[str]  # SCIM client name.
    scim_user_attr_type: NotRequired[Literal["user-name", "display-name", "external-id"]]  # User attribute type used to match SCIM users (default = user
    scim_group_attr_type: NotRequired[Literal["display-name", "external-id"]]  # Group attribute type used to match SCIM groups (default = di
    user_name: NotRequired[str]  # User name in assertion statement.
    group_name: NotRequired[str]  # Group name in assertion statement.
    digest_method: NotRequired[Literal["sha1", "sha256"]]  # Digest method algorithm.
    limit_relaystate: NotRequired[Literal["enable", "disable"]]  # Enable/disable limiting of relay-state parameter when it exc
    clock_tolerance: NotRequired[int]  # Clock skew tolerance in seconds (0 - 300, default = 15, 0 = 
    adfs_claim: NotRequired[Literal["enable", "disable"]]  # Enable/disable ADFS Claim for user/group attribute in assert
    user_claim_type: NotRequired[Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]]  # User name claim in assertion statement.
    group_claim_type: NotRequired[Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]]  # Group claim in assertion statement.
    reauth: NotRequired[Literal["enable", "disable"]]  # Enable/disable signalling of IDP to force user re-authentica


class Saml:
    """
    SAML server entry configuration.
    
    Path: user/saml
    Category: cmdb
    Primary Key: name
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
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SamlPayload | None = ...,
        name: str | None = ...,
        cert: str | None = ...,
        entity_id: str | None = ...,
        single_sign_on_url: str | None = ...,
        single_logout_url: str | None = ...,
        idp_entity_id: str | None = ...,
        idp_single_sign_on_url: str | None = ...,
        idp_single_logout_url: str | None = ...,
        idp_cert: str | None = ...,
        scim_client: str | None = ...,
        scim_user_attr_type: Literal["user-name", "display-name", "external-id"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
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


__all__ = [
    "Saml",
    "SamlPayload",
]