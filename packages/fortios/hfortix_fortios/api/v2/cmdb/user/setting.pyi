from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for user/setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Setting:
    """
    Configure user authentication setting.
    
    Path: user/setting
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
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | None = ...,
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
        auth_ports: list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | None = ...,
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
        auth_ports: list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
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
        payload_dict: SettingPayload | None = ...,
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