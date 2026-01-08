from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LocalPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/local payload fields.
    
    Local keys and certificates.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: cmp-server-cert, est-server-cert)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: est-client-cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: cmp-server-cert, est-server-cert)

    **Usage:**
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


class LocalObject(FortiObject[LocalPayload]):
    """Typed FortiObject for vpn/certificate/local with IDE autocomplete support."""
    
    # Name.
    name: str
    # Password as a PEM file.
    password: str
    # Comment.
    comments: str
    # PEM format key encrypted with a password.
    private_key: str
    # PEM format certificate.
    certificate: str
    # Certificate Signing Request.
    csr: str
    # Certificate Signing Request State.
    state: str
    # SCEP server URL.
    scep_url: str
    # Either a global or VDOM IP address range for the certificate.
    range: Literal["global", "vdom"]
    # Certificate source type.
    source: Literal["factory", "user", "bundle"]
    # Number of days to wait before expiry of an updated local certificate is requeste
    auto_regenerate_days: int
    # Number of days to wait before an expiry warning message is generated (0 = disabl
    auto_regenerate_days_warning: int
    # SCEP server challenge password for auto-regeneration.
    scep_password: str
    # CA identifier of the CA server for signing via SCEP.
    ca_identifier: str
    # Name encoding method for auto-regeneration.
    name_encoding: Literal["printable", "utf8"]
    # Source IP address for communications to the SCEP server.
    source_ip: str
    # Local ID the FortiGate uses for authentication as a VPN client.
    ike_localid: str
    # IKE local ID type.
    ike_localid_type: Literal["asn1dn", "fqdn"]
    # Certificate enrollment protocol.
    enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"]
    # Enable/disable retention of private key during SCEP renewal (default = disable).
    private_key_retain: Literal["enable", "disable"]
    # Address and port for CMP server (format = address:port).
    cmp_server: str
    # Path location inside CMP server.
    cmp_path: str
    # CMP server certificate.
    cmp_server_cert: str
    # CMP auto-regeneration method.
    cmp_regeneration_method: Literal["keyupate", "renewal"]
    # The URL for the ACME CA server (Let's Encrypt is the default provider).
    acme_ca_url: str
    # A valid domain that resolves to this FortiGate unit.
    acme_domain: str
    # Contact email address that is required by some CAs like LetsEncrypt.
    acme_email: str
    # External Account Binding Key ID (optional setting).
    acme_eab_key_id: str
    # External Account Binding HMAC Key (URL-encoded base64).
    acme_eab_key_hmac: str
    # Length of the RSA private key of the generated cert (Minimum 2048 bits).
    acme_rsa_key_size: int
    # Beginning of the renewal window (in days before certificate expiration, 30 by de
    acme_renew_window: int
    # Address and port for EST server (e.g. https://example.com:1234).
    est_server: str
    # CA identifier of the CA server for signing via EST.
    est_ca_id: str
    # HTTP Authentication username for signing via EST.
    est_http_username: str
    # HTTP Authentication password for signing via EST.
    est_http_password: str
    # Certificate used to authenticate this FortiGate to EST server.
    est_client_cert: str
    # EST server's certificate must be verifiable by this certificate to be authentica
    est_server_cert: str
    # EST SRP authentication username.
    est_srp_username: str
    # EST SRP authentication password.
    est_srp_password: str
    # EST behavioral options during re-enrollment.
    est_regeneration_method: Literal["create-new-key", "use-existing-key"]
    # Print local certificate detailed information.
    details: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LocalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Local:
    """
    Local keys and certificates.
    
    Path: vpn/certificate/local
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
    ) -> LocalObject: ...
    
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
    ) -> list[LocalObject]: ...
    
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
    ) -> LocalObject | list[LocalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalObject: ...
    
    @overload
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
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
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
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
    "Local",
    "LocalPayload",
    "LocalObject",
]