from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SettingPayload(TypedDict, total=False):
    """
    Type hints for authentication/setting payload fields.
    
    Configure authentication setting.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.authentication.scheme.SchemeEndpoint` (via: active-auth-scheme, sso-auth-scheme)
        - :class:`~.firewall.address.AddressEndpoint` (via: captive-portal, cert-captive-portal)
        - :class:`~.firewall.address6.Address6Endpoint` (via: captive-portal6)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    active_auth_scheme: NotRequired[str]  # Active authentication method (scheme name).
    sso_auth_scheme: NotRequired[str]  # Single-Sign-On authentication method (scheme name).
    update_time: NotRequired[str]  # Time of the last update.
    persistent_cookie: NotRequired[Literal["enable", "disable"]]  # Enable/disable persistent cookie on web portal authenticatio
    ip_auth_cookie: NotRequired[Literal["enable", "disable"]]  # Enable/disable persistent cookie on IP based web portal auth
    cookie_max_age: NotRequired[int]  # Persistent web portal cookie maximum age in minutes
    cookie_refresh_div: NotRequired[int]  # Refresh rate divider of persistent web portal cookie
    captive_portal_type: NotRequired[Literal["fqdn", "ip"]]  # Captive portal type.
    captive_portal_ip: NotRequired[str]  # Captive portal IP address.
    captive_portal_ip6: NotRequired[str]  # Captive portal IPv6 address.
    captive_portal: NotRequired[str]  # Captive portal host name.
    captive_portal6: NotRequired[str]  # IPv6 captive portal host name.
    cert_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable redirecting certificate authentication to HTT
    cert_captive_portal: NotRequired[str]  # Certificate captive portal host name.
    cert_captive_portal_ip: NotRequired[str]  # Certificate captive portal IP address.
    cert_captive_portal_port: NotRequired[int]  # Certificate captive portal port number
    captive_portal_port: NotRequired[int]  # Captive portal port number (1 - 65535, default = 7830).
    auth_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable redirecting HTTP user authentication to HTTPS
    captive_portal_ssl_port: NotRequired[int]  # Captive portal SSL port number (1 - 65535, default = 7831).
    user_cert_ca: NotRequired[list[dict[str, Any]]]  # CA certificate used for client certificate verification.
    dev_range: NotRequired[list[dict[str, Any]]]  # Address range for the IP based device query.

# Nested classes for table field children

@final
class SettingUsercertcaObject:
    """Typed object for user-cert-ca table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CA certificate list.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SettingDevrangeObject:
    """Typed object for dev-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for authentication/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    active_auth_scheme: str
    sso_auth_scheme: str
    update_time: str
    persistent_cookie: Literal["enable", "disable"]
    ip_auth_cookie: Literal["enable", "disable"]
    cookie_max_age: int
    cookie_refresh_div: int
    captive_portal_type: Literal["fqdn", "ip"]
    captive_portal_ip: str
    captive_portal_ip6: str
    captive_portal: str
    captive_portal6: str
    cert_auth: Literal["enable", "disable"]
    cert_captive_portal: str
    cert_captive_portal_ip: str
    cert_captive_portal_port: int
    captive_portal_port: int
    auth_https: Literal["enable", "disable"]
    captive_portal_ssl_port: int
    user_cert_ca: list[dict[str, Any]]
    dev_range: list[dict[str, Any]]


@final
class SettingObject:
    """Typed FortiObject for authentication/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Active authentication method (scheme name).
    active_auth_scheme: str
    # Single-Sign-On authentication method (scheme name).
    sso_auth_scheme: str
    # Time of the last update.
    update_time: str
    # Enable/disable persistent cookie on web portal authentication (default = enable)
    persistent_cookie: Literal["enable", "disable"]
    # Enable/disable persistent cookie on IP based web portal authentication
    ip_auth_cookie: Literal["enable", "disable"]
    # Persistent web portal cookie maximum age in minutes (30 - 10080
    cookie_max_age: int
    # Refresh rate divider of persistent web portal cookie (default = 2). Refresh valu
    cookie_refresh_div: int
    # Captive portal type.
    captive_portal_type: Literal["fqdn", "ip"]
    # Captive portal IP address.
    captive_portal_ip: str
    # Captive portal IPv6 address.
    captive_portal_ip6: str
    # Captive portal host name.
    captive_portal: str
    # IPv6 captive portal host name.
    captive_portal6: str
    # Enable/disable redirecting certificate authentication to HTTPS portal.
    cert_auth: Literal["enable", "disable"]
    # Certificate captive portal host name.
    cert_captive_portal: str
    # Certificate captive portal IP address.
    cert_captive_portal_ip: str
    # Certificate captive portal port number (1 - 65535, default = 7832).
    cert_captive_portal_port: int
    # Captive portal port number (1 - 65535, default = 7830).
    captive_portal_port: int
    # Enable/disable redirecting HTTP user authentication to HTTPS.
    auth_https: Literal["enable", "disable"]
    # Captive portal SSL port number (1 - 65535, default = 7831).
    captive_portal_ssl_port: int
    # CA certificate used for client certificate verification.
    user_cert_ca: list[SettingUsercertcaObject]  # Table field - list of typed objects
    # Address range for the IP based device query.
    dev_range: list[SettingDevrangeObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Setting:
    """
    Configure authentication setting.
    
    Path: authentication/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
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
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
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