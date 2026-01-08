from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SamlPayload(TypedDict, total=False):
    """
    Type hints for user/saml payload fields.
    
    SAML server entry configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.scim.ScimEndpoint` (via: scim-client)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: idp-cert)

    **Usage:**
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
    scim_user_attr_type: NotRequired[Literal["user-name", "display-name", "external-id", "email"]]  # User attribute type used to match SCIM users (default = user
    scim_group_attr_type: NotRequired[Literal["display-name", "external-id"]]  # Group attribute type used to match SCIM groups (default = di
    user_name: NotRequired[str]  # User name in assertion statement.
    group_name: NotRequired[str]  # Group name in assertion statement.
    digest_method: NotRequired[Literal["sha1", "sha256"]]  # Digest method algorithm.
    require_signed_resp_and_asrt: NotRequired[Literal["enable", "disable"]]  # Require both response and assertion from IDP to be signed wh
    limit_relaystate: NotRequired[Literal["enable", "disable"]]  # Enable/disable limiting of relay-state parameter when it exc
    clock_tolerance: NotRequired[int]  # Clock skew tolerance in seconds (0 - 300, default = 15, 0 = 
    adfs_claim: NotRequired[Literal["enable", "disable"]]  # Enable/disable ADFS Claim for user/group attribute in assert
    user_claim_type: NotRequired[Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]]  # User name claim in assertion statement.
    group_claim_type: NotRequired[Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]]  # Group claim in assertion statement.
    reauth: NotRequired[Literal["enable", "disable"]]  # Enable/disable signalling of IDP to force user re-authentica


class SamlObject(FortiObject[SamlPayload]):
    """Typed FortiObject for user/saml with IDE autocomplete support."""
    
    # SAML server entry name.
    name: str
    # Certificate to sign SAML messages.
    cert: str
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
    # IDP single logout url.
    idp_single_logout_url: str
    # IDP Certificate name.
    idp_cert: str
    # SCIM client name.
    scim_client: str
    # User attribute type used to match SCIM users (default = user-name).
    scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"]
    # Group attribute type used to match SCIM groups (default = display-name).
    scim_group_attr_type: Literal["display-name", "external-id"]
    # User name in assertion statement.
    user_name: str
    # Group name in assertion statement.
    group_name: str
    # Digest method algorithm.
    digest_method: Literal["sha1", "sha256"]
    # Require both response and assertion from IDP to be signed when FGT acts as SP (d
    require_signed_resp_and_asrt: Literal["enable", "disable"]
    # Enable/disable limiting of relay-state parameter when it exceeds SAML 2.0 specif
    limit_relaystate: Literal["enable", "disable"]
    # Clock skew tolerance in seconds (0 - 300, default = 15, 0 = no tolerance).
    clock_tolerance: int
    # Enable/disable ADFS Claim for user/group attribute in assertion statement (defau
    adfs_claim: Literal["enable", "disable"]
    # User name claim in assertion statement.
    user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]
    # Group claim in assertion statement.
    group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"]
    # Enable/disable signalling of IDP to force user re-authentication (default = disa
    reauth: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SamlPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Saml:
    """
    SAML server entry configuration.
    
    Path: user/saml
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
    ) -> SamlObject: ...
    
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
    ) -> list[SamlObject]: ...
    
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
    ) -> SamlObject | list[SamlObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SamlObject: ...
    
    @overload
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SamlObject: ...
    
    @overload
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
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
    ) -> SamlObject: ...
    
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
        scim_user_attr_type: Literal["user-name", "display-name", "external-id", "email"] | None = ...,
        scim_group_attr_type: Literal["display-name", "external-id"] | None = ...,
        user_name: str | None = ...,
        group_name: str | None = ...,
        digest_method: Literal["sha1", "sha256"] | None = ...,
        require_signed_resp_and_asrt: Literal["enable", "disable"] | None = ...,
        limit_relaystate: Literal["enable", "disable"] | None = ...,
        clock_tolerance: int | None = ...,
        adfs_claim: Literal["enable", "disable"] | None = ...,
        user_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        group_claim_type: Literal["email", "given-name", "name", "upn", "common-name", "email-adfs-1x", "group", "upn-adfs-1x", "role", "sur-name", "ppid", "name-identifier", "authentication-method", "deny-only-group-sid", "deny-only-primary-sid", "deny-only-primary-group-sid", "group-sid", "primary-group-sid", "primary-sid", "windows-account-name"] | None = ...,
        reauth: Literal["enable", "disable"] | None = ...,
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