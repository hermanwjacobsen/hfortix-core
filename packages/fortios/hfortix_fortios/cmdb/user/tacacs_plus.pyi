from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class TacacsPlusPayload(TypedDict, total=False):
    """
    Type hints for user/tacacs_plus payload fields.
    
    Configure TACACS+ server entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: TacacsPlusPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # TACACS+ server entry name.
    server: str  # Primary TACACS+ server CN domain name or IP address.
    secondary_server: NotRequired[str]  # Secondary TACACS+ server CN domain name or IP address.
    tertiary_server: NotRequired[str]  # Tertiary TACACS+ server CN domain name or IP address.
    port: NotRequired[int]  # Port number of the TACACS+ server.
    key: NotRequired[str]  # Key to access the primary server.
    secondary_key: NotRequired[str]  # Key to access the secondary server.
    tertiary_key: NotRequired[str]  # Key to access the tertiary server.
    status_ttl: NotRequired[int]  # Time for which server reachability is cached so that when a 
    authen_type: NotRequired[Literal["mschap", "chap", "pap", "ascii", "auto"]]  # Allowed authentication protocols/methods.
    authorization: NotRequired[Literal["enable", "disable"]]  # Enable/disable TACACS+ authorization.
    source_ip: NotRequired[str]  # Source IP address for communications to TACACS+ server.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class TacacsPlusObject(FortiObject[TacacsPlusPayload]):
    """Typed FortiObject for user/tacacs_plus with IDE autocomplete support."""
    
    # TACACS+ server entry name.
    name: str
    # Primary TACACS+ server CN domain name or IP address.
    server: str
    # Secondary TACACS+ server CN domain name or IP address.
    secondary_server: str
    # Tertiary TACACS+ server CN domain name or IP address.
    tertiary_server: str
    # Port number of the TACACS+ server.
    port: int
    # Key to access the primary server.
    key: str
    # Key to access the secondary server.
    secondary_key: str
    # Key to access the tertiary server.
    tertiary_key: str
    # Time for which server reachability is cached so that when a server is unreachabl
    status_ttl: int
    # Allowed authentication protocols/methods.
    authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"]
    # Enable/disable TACACS+ authorization.
    authorization: Literal["enable", "disable"]
    # Source IP address for communications to TACACS+ server.
    source_ip: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> TacacsPlusPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TacacsPlus:
    """
    Configure TACACS+ server entries.
    
    Path: user/tacacs_plus
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
    ) -> TacacsPlusObject: ...
    
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
    ) -> list[TacacsPlusObject]: ...
    
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
    ) -> TacacsPlusObject | list[TacacsPlusObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TacacsPlusObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TacacsPlusObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TacacsPlusObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: TacacsPlusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secondary_server: str | None = ...,
        tertiary_server: str | None = ...,
        port: int | None = ...,
        key: str | None = ...,
        secondary_key: str | None = ...,
        tertiary_key: str | None = ...,
        status_ttl: int | None = ...,
        authen_type: Literal["mschap", "chap", "pap", "ascii", "auto"] | None = ...,
        authorization: Literal["enable", "disable"] | None = ...,
        source_ip: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "TacacsPlus",
    "TacacsPlusPayload",
    "TacacsPlusObject",
]