from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ExplicitPayload(TypedDict, total=False):
    """
    Type hints for ftp_proxy/explicit payload fields.
    
    Configure explicit FTP proxy settings.
    
    **Usage:**
        payload: ExplicitPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit FTP proxy.
    incoming_port: NotRequired[str]  # Accept incoming FTP requests on one or more ports.
    incoming_ip: NotRequired[str]  # Accept incoming FTP requests from this IP address. An interf
    outgoing_ip: NotRequired[list[dict[str, Any]]]  # Outgoing FTP requests will leave from this IP address. An in
    sec_default_action: NotRequired[Literal["accept", "deny"]]  # Accept or deny explicit FTP proxy sessions when no FTP proxy
    server_data_mode: NotRequired[Literal["client", "passive"]]  # Determine mode of data session on FTP server side.
    ssl: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit FTPS proxy.
    ssl_cert: NotRequired[list[dict[str, Any]]]  # List of certificate names to use for SSL connections to this
    ssl_dh_bits: NotRequired[Literal["768", "1024", "1536", "2048"]]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ssl_algorithm: NotRequired[Literal["high", "medium", "low"]]  # Relative strength of encryption algorithms accepted in negot


class ExplicitObject(FortiObject[ExplicitPayload]):
    """Typed FortiObject for ftp_proxy/explicit with IDE autocomplete support."""
    
    # Enable/disable the explicit FTP proxy.
    status: Literal["enable", "disable"]
    # Accept incoming FTP requests on one or more ports.
    incoming_port: str
    # Accept incoming FTP requests from this IP address. An interface must have this I
    incoming_ip: str
    # Outgoing FTP requests will leave from this IP address. An interface must have th
    outgoing_ip: list[str]  # Auto-flattened from member_table
    # Accept or deny explicit FTP proxy sessions when no FTP proxy firewall policy exi
    sec_default_action: Literal["accept", "deny"]
    # Determine mode of data session on FTP server side.
    server_data_mode: Literal["client", "passive"]
    # Enable/disable the explicit FTPS proxy.
    ssl: Literal["enable", "disable"]
    # List of certificate names to use for SSL connections to this server.
    ssl_cert: list[str]  # Auto-flattened from member_table
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 204
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Relative strength of encryption algorithms accepted in negotiation.
    ssl_algorithm: Literal["high", "medium", "low"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExplicitPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Explicit:
    """
    Configure explicit FTP proxy settings.
    
    Path: ftp_proxy/explicit
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
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
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
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
    "Explicit",
    "ExplicitPayload",
    "ExplicitObject",
]