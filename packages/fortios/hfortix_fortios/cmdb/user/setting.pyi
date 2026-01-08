from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for user/setting payload fields.
    
    Configure user authentication setting.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.password-policy.PasswordPolicyEndpoint` (via: default-user-password-policy)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: auth-ca-cert, auth-cert)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    auth_type: NotRequired[Literal["http", "https", "ftp", "telnet"]]  # Supported firewall policy authentication protocols/methods.
    auth_cert: NotRequired[str]  # HTTPS server certificate for policy authentication.
    auth_ca_cert: NotRequired[str]  # HTTPS CA certificate for policy authentication.
    auth_secure_http: NotRequired[Literal["enable", "disable"]]  # Enable/disable redirecting HTTP user authentication to more 
    auth_http_basic: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of HTTP basic authentication for identity
    auth_ssl_allow_renegotiation: NotRequired[Literal["enable", "disable"]]  # Allow/forbid SSL re-negotiation for HTTPS authentication.
    auth_src_mac: NotRequired[Literal["enable", "disable"]]  # Enable/disable source MAC for user identity.
    auth_on_demand: NotRequired[Literal["always", "implicitly"]]  # Always/implicitly trigger firewall authentication on demand.
    auth_timeout: NotRequired[int]  # Time in minutes before the firewall user authentication time
    auth_timeout_type: NotRequired[Literal["idle-timeout", "hard-timeout", "new-session"]]  # Control if authenticated users have to login again after a h
    auth_portal_timeout: NotRequired[int]  # Time in minutes before captive portal user have to re-authen
    radius_ses_timeout_act: NotRequired[Literal["hard-timeout", "ignore-timeout"]]  # Set the RADIUS session timeout to a hard timeout or to ignor
    auth_blackout_time: NotRequired[int]  # Time in seconds an IP address is denied access after failing
    auth_invalid_max: NotRequired[int]  # Maximum number of failed authentication attempts before the 
    auth_lockout_threshold: NotRequired[int]  # Maximum number of failed login attempts before login lockout
    auth_lockout_duration: NotRequired[int]  # Lockout period in seconds after too many login failures.
    per_policy_disclaimer: NotRequired[Literal["enable", "disable"]]  # Enable/disable per policy disclaimer.
    auth_ports: NotRequired[list[dict[str, Any]]]  # Set up non-standard ports for authentication with HTTP, HTTP
    auth_ssl_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections (
    auth_ssl_max_proto_version: NotRequired[Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"]]  # Maximum supported protocol version for SSL/TLS connections (
    auth_ssl_sigalgs: NotRequired[Literal["no-rsa-pss", "all"]]  # Set signature algorithms related to HTTPS authentication (af
    default_user_password_policy: NotRequired[str]  # Default password policy to apply to all local users unless o
    cors: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowed origins white list for CORS.
    cors_allowed_origins: NotRequired[list[dict[str, Any]]]  # Allowed origins white list for CORS.


class SettingObject(FortiObject[SettingPayload]):
    """Typed FortiObject for user/setting with IDE autocomplete support."""
    
    # Supported firewall policy authentication protocols/methods.
    auth_type: Literal["http", "https", "ftp", "telnet"]
    # HTTPS server certificate for policy authentication.
    auth_cert: str
    # HTTPS CA certificate for policy authentication.
    auth_ca_cert: str
    # Enable/disable redirecting HTTP user authentication to more secure HTTPS.
    auth_secure_http: Literal["enable", "disable"]
    # Enable/disable use of HTTP basic authentication for identity-based firewall poli
    auth_http_basic: Literal["enable", "disable"]
    # Allow/forbid SSL re-negotiation for HTTPS authentication.
    auth_ssl_allow_renegotiation: Literal["enable", "disable"]
    # Enable/disable source MAC for user identity.
    auth_src_mac: Literal["enable", "disable"]
    # Always/implicitly trigger firewall authentication on demand.
    auth_on_demand: Literal["always", "implicitly"]
    # Time in minutes before the firewall user authentication timeout requires the use
    auth_timeout: int
    # Control if authenticated users have to login again after a hard timeout, after a
    auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"]
    # Time in minutes before captive portal user have to re-authenticate (1 - 30 min, 
    auth_portal_timeout: int
    # Set the RADIUS session timeout to a hard timeout or to ignore RADIUS server sess
    radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"]
    # Time in seconds an IP address is denied access after failing to authenticate fiv
    auth_blackout_time: int
    # Maximum number of failed authentication attempts before the user is blocked.
    auth_invalid_max: int
    # Maximum number of failed login attempts before login lockout is triggered.
    auth_lockout_threshold: int
    # Lockout period in seconds after too many login failures.
    auth_lockout_duration: int
    # Enable/disable per policy disclaimer.
    per_policy_disclaimer: Literal["enable", "disable"]
    # Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and TELNET.
    auth_ports: list[str]  # Auto-flattened from member_table
    # Minimum supported protocol version for SSL/TLS connections (default is to follow
    auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Maximum supported protocol version for SSL/TLS connections (default is no limit)
    auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"]
    # Set signature algorithms related to HTTPS authentication (affects TLS version <=
    auth_ssl_sigalgs: Literal["no-rsa-pss", "all"]
    # Default password policy to apply to all local users unless otherwise specified, 
    default_user_password_policy: str
    # Enable/disable allowed origins white list for CORS.
    cors: Literal["disable", "enable"]
    # Allowed origins white list for CORS.
    cors_allowed_origins: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Setting:
    """
    Configure user authentication setting.
    
    Path: user/setting
    Category: cmdb
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | list[dict[str, Any]] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingObject",
]