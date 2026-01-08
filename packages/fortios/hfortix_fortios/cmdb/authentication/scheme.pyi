from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SchemePayload(TypedDict, total=False):
    """
    Type hints for authentication/scheme payload fields.
    
    Configure Authentication Schemes.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.ssh.local-ca.LocalCaEndpoint` (via: ssh-ca)
        - :class:`~.user.domain-controller.DomainControllerEndpoint` (via: domain-controller)
        - :class:`~.user.external-identity-provider.ExternalIdentityProviderEndpoint` (via: external-idp)
        - :class:`~.user.fsso.FssoEndpoint` (via: fsso-agent-for-ntlm)
        - :class:`~.user.krb-keytab.KrbKeytabEndpoint` (via: kerberos-keytab)
        - :class:`~.user.saml.SamlEndpoint` (via: saml-server)

    **Usage:**
        payload: SchemePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Authentication scheme name.
    method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"]  # Authentication methods (default = basic).
    negotiate_ntlm: NotRequired[Literal["enable", "disable"]]  # Enable/disable negotiate authentication for NTLM
    kerberos_keytab: NotRequired[str]  # Kerberos keytab setting.
    domain_controller: NotRequired[str]  # Domain controller setting.
    saml_server: NotRequired[str]  # SAML configuration.
    saml_timeout: NotRequired[int]  # SAML authentication timeout in seconds.
    fsso_agent_for_ntlm: NotRequired[str]  # FSSO agent to use for NTLM authentication.
    require_tfa: NotRequired[Literal["enable", "disable"]]  # Enable/disable two-factor authentication (default = disable)
    fsso_guest: NotRequired[Literal["enable", "disable"]]  # Enable/disable user fsso-guest authentication
    user_cert: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication with user certificate
    cert_http_header: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication with user certificate in Clien
    user_database: NotRequired[list[dict[str, Any]]]  # Authentication server to contain user information; "local-us
    ssh_ca: NotRequired[str]  # SSH CA name.
    external_idp: NotRequired[str]  # External identity provider configuration.
    group_attr_type: NotRequired[Literal["display-name", "external-id"]]  # Group attribute type used to match SCIM groups
    digest_algo: NotRequired[Literal["md5", "sha-256"]]  # Digest Authentication Algorithms.
    digest_rfc2069: NotRequired[Literal["enable", "disable"]]  # Enable/disable support for the deprecated RFC2069 Digest Cli


# Response TypedDict for GET returns (all fields present in API response)
class SchemeResponse(TypedDict):
    """
    Type hints for authentication/scheme API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"]
    negotiate_ntlm: Literal["enable", "disable"]
    kerberos_keytab: str
    domain_controller: str
    saml_server: str
    saml_timeout: int
    fsso_agent_for_ntlm: str
    require_tfa: Literal["enable", "disable"]
    fsso_guest: Literal["enable", "disable"]
    user_cert: Literal["enable", "disable"]
    cert_http_header: Literal["enable", "disable"]
    user_database: list[dict[str, Any]]
    ssh_ca: str
    external_idp: str
    group_attr_type: Literal["display-name", "external-id"]
    digest_algo: Literal["md5", "sha-256"]
    digest_rfc2069: Literal["enable", "disable"]


@final
class SchemeObject:
    """Typed FortiObject for authentication/scheme with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Authentication scheme name.
    name: str
    # Authentication methods (default = basic).
    method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"]
    # Enable/disable negotiate authentication for NTLM (default = disable).
    negotiate_ntlm: Literal["enable", "disable"]
    # Kerberos keytab setting.
    kerberos_keytab: str
    # Domain controller setting.
    domain_controller: str
    # SAML configuration.
    saml_server: str
    # SAML authentication timeout in seconds.
    saml_timeout: int
    # FSSO agent to use for NTLM authentication.
    fsso_agent_for_ntlm: str
    # Enable/disable two-factor authentication (default = disable).
    require_tfa: Literal["enable", "disable"]
    # Enable/disable user fsso-guest authentication (default = disable).
    fsso_guest: Literal["enable", "disable"]
    # Enable/disable authentication with user certificate (default = disable).
    user_cert: Literal["enable", "disable"]
    # Enable/disable authentication with user certificate in Client-Cert HTTP header
    cert_http_header: Literal["enable", "disable"]
    # Authentication server to contain user information; "local-user-db" (default) or
    user_database: list[str]  # Auto-flattened from member_table
    # SSH CA name.
    ssh_ca: str
    # External identity provider configuration.
    external_idp: str
    # Group attribute type used to match SCIM groups (default = display-name).
    group_attr_type: Literal["display-name", "external-id"]
    # Digest Authentication Algorithms.
    digest_algo: Literal["md5", "sha-256"]
    # Enable/disable support for the deprecated RFC2069 Digest Client
    digest_rfc2069: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SchemePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Scheme:
    """
    Configure Authentication Schemes.
    
    Path: authentication/scheme
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
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
    ) -> list[SchemeObject]: ...
    
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
    ) -> SchemeObject: ...
    
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
    ) -> list[SchemeResponse]: ...
    
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
    ) -> SchemeResponse: ...
    
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
    ) -> SchemeObject | list[SchemeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SchemeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SchemeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
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
    ) -> SchemeObject: ...
    
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
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | list[str] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        cert_http_header: Literal["enable", "disable"] | None = ...,
        user_database: str | list[str] | list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | list[str] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
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
    "Scheme",
    "SchemePayload",
    "SchemeObject",
]