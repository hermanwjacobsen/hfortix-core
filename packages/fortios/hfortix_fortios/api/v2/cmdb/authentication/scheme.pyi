from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SchemePayload(TypedDict, total=False):
    """
    Type hints for authentication/scheme payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SchemePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Authentication scheme name.
    method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"]  # Authentication methods (default = basic).
    negotiate_ntlm: NotRequired[Literal["enable", "disable"]]  # Enable/disable negotiate authentication for NTLM (default = 
    kerberos_keytab: NotRequired[str]  # Kerberos keytab setting.
    domain_controller: NotRequired[str]  # Domain controller setting.
    saml_server: NotRequired[str]  # SAML configuration.
    saml_timeout: NotRequired[int]  # SAML authentication timeout in seconds.
    fsso_agent_for_ntlm: NotRequired[str]  # FSSO agent to use for NTLM authentication.
    require_tfa: NotRequired[Literal["enable", "disable"]]  # Enable/disable two-factor authentication (default = disable)
    fsso_guest: NotRequired[Literal["enable", "disable"]]  # Enable/disable user fsso-guest authentication (default = dis
    user_cert: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication with user certificate (default
    user_database: NotRequired[list[dict[str, Any]]]  # Authentication server to contain user information; "local-us
    ssh_ca: NotRequired[str]  # SSH CA name.
    external_idp: NotRequired[str]  # External identity provider configuration.
    group_attr_type: NotRequired[Literal["display-name", "external-id"]]  # Group attribute type used to match SCIM groups (default = di
    digest_algo: NotRequired[Literal["md5", "sha-256"]]  # Digest Authentication Algorithms.
    digest_rfc2069: NotRequired[Literal["enable", "disable"]]  # Enable/disable support for the deprecated RFC2069 Digest Cli


class Scheme:
    """
    Configure Authentication Schemes.
    
    Path: authentication/scheme
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
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        user_database: list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SchemePayload | None = ...,
        name: str | None = ...,
        method: Literal["ntlm", "basic", "digest", "form", "negotiate", "fsso", "rsso", "ssh-publickey", "cert", "saml", "entra-sso"] | None = ...,
        negotiate_ntlm: Literal["enable", "disable"] | None = ...,
        kerberos_keytab: str | None = ...,
        domain_controller: str | None = ...,
        saml_server: str | None = ...,
        saml_timeout: int | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        require_tfa: Literal["enable", "disable"] | None = ...,
        fsso_guest: Literal["enable", "disable"] | None = ...,
        user_cert: Literal["enable", "disable"] | None = ...,
        user_database: list[dict[str, Any]] | None = ...,
        ssh_ca: str | None = ...,
        external_idp: str | None = ...,
        group_attr_type: Literal["display-name", "external-id"] | None = ...,
        digest_algo: Literal["md5", "sha-256"] | None = ...,
        digest_rfc2069: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SchemePayload | None = ...,
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