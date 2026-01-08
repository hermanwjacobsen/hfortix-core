from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class FtmPushPayload(TypedDict, total=False):
    """
    Type hints for system/ftm_push payload fields.
    
    Configure FortiToken Mobile push services.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: server-cert)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: FtmPushPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable communication to the proxy server in FortiGua
    interface: NotRequired[str]  # Interface of FortiToken Mobile push services server.
    server: NotRequired[str]  # IPv4 address or domain name of FortiToken Mobile push servic
    server_port: NotRequired[int]  # Port to communicate with FortiToken Mobile push services ser
    server_cert: NotRequired[str]  # Name of the server certificate to be used for SSL.
    server_ip: NotRequired[str]  # IPv4 address of FortiToken Mobile push services server (form
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the use of FortiToken Mobile push services.


class FtmPushObject(FortiObject[FtmPushPayload]):
    """Typed FortiObject for system/ftm_push with IDE autocomplete support."""
    
    # Enable/disable communication to the proxy server in FortiGuard configuration.
    proxy: Literal["enable", "disable"]
    # Interface of FortiToken Mobile push services server.
    interface: str
    # IPv4 address or domain name of FortiToken Mobile push services server.
    server: str
    # Port to communicate with FortiToken Mobile push services server (1 - 65535, defa
    server_port: int
    # Name of the server certificate to be used for SSL.
    server_cert: str
    # IPv4 address of FortiToken Mobile push services server (format: xxx.xxx.xxx.xxx)
    server_ip: str
    # Enable/disable the use of FortiToken Mobile push services.
    status: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FtmPushPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FtmPush:
    """
    Configure FortiToken Mobile push services.
    
    Path: system/ftm_push
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FtmPushObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
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
    "FtmPush",
    "FtmPushPayload",
    "FtmPushObject",
]