from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SettingPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl/setting payload fields.
    
    SSL proxy settings.
    
    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    proxy_connect_timeout: int  # Time limit to make an internal connection to the appropriate
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ssl_send_empty_frags: Literal["enable", "disable"]  # Enable/disable sending empty fragments to avoid attack on CB
    no_matching_cipher_action: Literal["bypass", "drop"]  # Bypass or drop the connection when no matching cipher is fou
    cert_manager_cache_timeout: int  # Time limit for certificate manager to keep FortiGate re-sign
    resigned_short_lived_certificate: Literal["enable", "disable"]  # Enable/disable short-lived certificate.
    cert_cache_capacity: int  # Maximum capacity of the host certificate cache
    cert_cache_timeout: int  # Time limit to keep certificate cache
    session_cache_capacity: int  # Capacity of the SSL session cache (--Obsolete--)
    session_cache_timeout: int  # Time limit to keep SSL session state
    abbreviate_handshake: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of SSL abbreviated handshake.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for firewall/ssl/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    proxy_connect_timeout: int
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    ssl_send_empty_frags: Literal["enable", "disable"]
    no_matching_cipher_action: Literal["bypass", "drop"]
    cert_manager_cache_timeout: int
    resigned_short_lived_certificate: Literal["enable", "disable"]
    cert_cache_capacity: int
    cert_cache_timeout: int
    session_cache_capacity: int
    session_cache_timeout: int
    abbreviate_handshake: Literal["enable", "disable"]


@final
class SettingObject:
    """Typed FortiObject for firewall/ssl/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Time limit to make an internal connection to the appropriate proxy process
    proxy_connect_timeout: int
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Enable/disable sending empty fragments to avoid attack on CBC IV
    ssl_send_empty_frags: Literal["enable", "disable"]
    # Bypass or drop the connection when no matching cipher is found.
    no_matching_cipher_action: Literal["bypass", "drop"]
    # Time limit for certificate manager to keep FortiGate re-signed server certificat
    cert_manager_cache_timeout: int
    # Enable/disable short-lived certificate.
    resigned_short_lived_certificate: Literal["enable", "disable"]
    # Maximum capacity of the host certificate cache (0 - 500, default = 200).
    cert_cache_capacity: int
    # Time limit to keep certificate cache (1 - 120 min, default = 10).
    cert_cache_timeout: int
    # Capacity of the SSL session cache (--Obsolete--) (1 - 1000, default = 500).
    session_cache_capacity: int
    # Time limit to keep SSL session state (1 - 60 min, default = 20).
    session_cache_timeout: int
    # Enable/disable use of SSL abbreviated handshake.
    abbreviate_handshake: Literal["enable", "disable"]
    
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
    SSL proxy settings.
    
    Path: firewall/ssl/setting
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
        proxy_connect_timeout: int | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        no_matching_cipher_action: Literal["bypass", "drop"] | None = ...,
        cert_manager_cache_timeout: int | None = ...,
        resigned_short_lived_certificate: Literal["enable", "disable"] | None = ...,
        cert_cache_capacity: int | None = ...,
        cert_cache_timeout: int | None = ...,
        session_cache_capacity: int | None = ...,
        session_cache_timeout: int | None = ...,
        abbreviate_handshake: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        proxy_connect_timeout: int | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        no_matching_cipher_action: Literal["bypass", "drop"] | None = ...,
        cert_manager_cache_timeout: int | None = ...,
        resigned_short_lived_certificate: Literal["enable", "disable"] | None = ...,
        cert_cache_capacity: int | None = ...,
        cert_cache_timeout: int | None = ...,
        session_cache_capacity: int | None = ...,
        session_cache_timeout: int | None = ...,
        abbreviate_handshake: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        proxy_connect_timeout: int | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        no_matching_cipher_action: Literal["bypass", "drop"] | None = ...,
        cert_manager_cache_timeout: int | None = ...,
        resigned_short_lived_certificate: Literal["enable", "disable"] | None = ...,
        cert_cache_capacity: int | None = ...,
        cert_cache_timeout: int | None = ...,
        session_cache_capacity: int | None = ...,
        session_cache_timeout: int | None = ...,
        abbreviate_handshake: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        proxy_connect_timeout: int | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        no_matching_cipher_action: Literal["bypass", "drop"] | None = ...,
        cert_manager_cache_timeout: int | None = ...,
        resigned_short_lived_certificate: Literal["enable", "disable"] | None = ...,
        cert_cache_capacity: int | None = ...,
        cert_cache_timeout: int | None = ...,
        session_cache_capacity: int | None = ...,
        session_cache_timeout: int | None = ...,
        abbreviate_handshake: Literal["enable", "disable"] | None = ...,
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
        proxy_connect_timeout: int | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        no_matching_cipher_action: Literal["bypass", "drop"] | None = ...,
        cert_manager_cache_timeout: int | None = ...,
        resigned_short_lived_certificate: Literal["enable", "disable"] | None = ...,
        cert_cache_capacity: int | None = ...,
        cert_cache_timeout: int | None = ...,
        session_cache_capacity: int | None = ...,
        session_cache_timeout: int | None = ...,
        abbreviate_handshake: Literal["enable", "disable"] | None = ...,
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