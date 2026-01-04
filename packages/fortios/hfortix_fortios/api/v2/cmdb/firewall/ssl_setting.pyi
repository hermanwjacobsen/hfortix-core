from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SslSettingPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SslSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    proxy_connect_timeout: int  # Time limit to make an internal connection to the appropriate
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ssl_send_empty_frags: Literal["enable", "disable"]  # Enable/disable sending empty fragments to avoid attack on CB
    no_matching_cipher_action: Literal["bypass", "drop"]  # Bypass or drop the connection when no matching cipher is fou
    cert_manager_cache_timeout: int  # Time limit for certificate manager to keep FortiGate re-sign
    resigned_short_lived_certificate: Literal["enable", "disable"]  # Enable/disable short-lived certificate.
    cert_cache_capacity: int  # Maximum capacity of the host certificate cache (0 - 500, def
    cert_cache_timeout: int  # Time limit to keep certificate cache (1 - 120 min, default =
    session_cache_capacity: int  # Capacity of the SSL session cache (--Obsolete--) (1 - 1000, 
    session_cache_timeout: int  # Time limit to keep SSL session state (1 - 60 min, default = 
    abbreviate_handshake: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of SSL abbreviated handshake.


class SslSetting:
    """
    SSL proxy settings.
    
    Path: firewall/ssl_setting
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
        payload_dict: SslSettingPayload | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SslSettingPayload | None = ...,
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
        payload_dict: SslSettingPayload | None = ...,
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