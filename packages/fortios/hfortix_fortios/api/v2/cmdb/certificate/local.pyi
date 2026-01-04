from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LocalPayload(TypedDict, total=False):
    """
    Type hints for certificate/local payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LocalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name.
    password: NotRequired[str]  # Password as a PEM file.
    comments: NotRequired[str]  # Comment.
    private_key: str  # PEM format key encrypted with a password.
    certificate: NotRequired[str]  # PEM format certificate.
    csr: NotRequired[str]  # Certificate Signing Request.
    state: NotRequired[str]  # Certificate Signing Request State.
    scep_url: NotRequired[str]  # SCEP server URL.
    range: NotRequired[Literal["global", "vdom"]]  # Either a global or VDOM IP address range for the certificate
    source: NotRequired[Literal["factory", "user", "bundle"]]  # Certificate source type.
    auto_regenerate_days: NotRequired[int]  # Number of days to wait before expiry of an updated local cer
    auto_regenerate_days_warning: NotRequired[int]  # Number of days to wait before an expiry warning message is g
    scep_password: NotRequired[str]  # SCEP server challenge password for auto-regeneration.
    ca_identifier: NotRequired[str]  # CA identifier of the CA server for signing via SCEP.
    name_encoding: NotRequired[Literal["printable", "utf8"]]  # Name encoding method for auto-regeneration.
    source_ip: NotRequired[str]  # Source IP address for communications to the SCEP server.
    ike_localid: NotRequired[str]  # Local ID the FortiGate uses for authentication as a VPN clie
    ike_localid_type: NotRequired[Literal["asn1dn", "fqdn"]]  # IKE local ID type.
    enroll_protocol: NotRequired[Literal["none", "scep", "cmpv2", "acme2", "est"]]  # Certificate enrollment protocol.
    private_key_retain: NotRequired[Literal["enable", "disable"]]  # Enable/disable retention of private key during SCEP renewal 
    cmp_server: NotRequired[str]  # Address and port for CMP server (format = address:port).
    cmp_path: NotRequired[str]  # Path location inside CMP server.
    cmp_server_cert: NotRequired[str]  # CMP server certificate.
    cmp_regeneration_method: NotRequired[Literal["keyupate", "renewal"]]  # CMP auto-regeneration method.
    acme_ca_url: str  # The URL for the ACME CA server (Let's Encrypt is the default
    acme_domain: str  # A valid domain that resolves to this FortiGate unit.
    acme_email: str  # Contact email address that is required by some CAs like Lets
    acme_eab_key_id: NotRequired[str]  # External Account Binding Key ID (optional setting).
    acme_eab_key_hmac: NotRequired[str]  # External Account Binding HMAC Key (URL-encoded base64).
    acme_rsa_key_size: NotRequired[int]  # Length of the RSA private key of the generated cert (Minimum
    acme_renew_window: NotRequired[int]  # Beginning of the renewal window (in days before certificate 
    est_server: NotRequired[str]  # Address and port for EST server (e.g. https://example.com:12
    est_ca_id: NotRequired[str]  # CA identifier of the CA server for signing via EST.
    est_http_username: NotRequired[str]  # HTTP Authentication username for signing via EST.
    est_http_password: NotRequired[str]  # HTTP Authentication password for signing via EST.
    est_client_cert: NotRequired[str]  # Certificate used to authenticate this FortiGate to EST serve
    est_server_cert: NotRequired[str]  # EST server's certificate must be verifiable by this certific
    est_srp_username: NotRequired[str]  # EST SRP authentication username.
    est_srp_password: NotRequired[str]  # EST SRP authentication password.
    est_regeneration_method: NotRequired[Literal["create-new-key", "use-existing-key"]]  # EST behavioral options during re-enrollment.
    details: NotRequired[str]  # Print local certificate detailed information.


class Local:
    """
    Local keys and certificates.
    
    Path: certificate/local
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
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
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
        payload_dict: LocalPayload | None = ...,
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