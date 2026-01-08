from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class NtpPayload(TypedDict, total=False):
    """
    Type hints for system/ntp payload fields.
    
    Configure system NTP information.
    
    **Usage:**
        payload: NtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ntpsync: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting the FortiGate system time by synchron
    type: NotRequired[Literal["fortiguard", "custom"]]  # Use the FortiGuard NTP server or any other available NTP Ser
    syncinterval: NotRequired[int]  # NTP synchronization interval (1 - 1440 min).
    ntpserver: NotRequired[list[dict[str, Any]]]  # Configure the FortiGate to connect to any available third-pa
    source_ip: NotRequired[str]  # Source IP address for communication to the NTP server.
    source_ip6: NotRequired[str]  # Source IPv6 address for communication to the NTP server.
    server_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGate NTP Server Mode. Your FortiGate bec
    authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication.
    key_type: NotRequired[Literal["MD5", "SHA1", "SHA256"]]  # Key type for authentication (MD5, SHA1, SHA256).
    key: str  # Key for authentication.
    key_id: int  # Key ID for authentication.
    interface: NotRequired[list[dict[str, Any]]]  # FortiGate interface(s) with NTP server mode enabled. Devices

# Nested classes for table field children

@final
class NtpNtpserverObject:
    """Typed object for ntpserver table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # NTP server ID.
    id: int
    # IP address or hostname of the NTP Server.
    server: str
    # Enable to use NTPv3 instead of NTPv4.
    ntpv3: Literal["enable", "disable"]
    # Enable/disable authentication.
    authentication: Literal["enable", "disable"]
    # Select NTP authentication type.
    key_type: Literal["MD5", "SHA1", "SHA256"]
    # Key for MD5(NTPv3)/SHA1(NTPv4)/SHA256(NTPv4) authentication.
    key: str
    # Key ID for authentication.
    key_id: int
    # Choose to connect to IPv4 or/and IPv6 NTP server.
    ip_type: Literal["IPv6", "IPv4", "Both"]
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class NtpInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    interface_name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class NtpResponse(TypedDict):
    """
    Type hints for system/ntp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ntpsync: Literal["enable", "disable"]
    type: Literal["fortiguard", "custom"]
    syncinterval: int
    ntpserver: list[dict[str, Any]]
    source_ip: str
    source_ip6: str
    server_mode: Literal["enable", "disable"]
    authentication: Literal["enable", "disable"]
    key_type: Literal["MD5", "SHA1", "SHA256"]
    key: str
    key_id: int
    interface: list[dict[str, Any]]


@final
class NtpObject:
    """Typed FortiObject for system/ntp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable setting the FortiGate system time by synchronizing with an NTP Se
    ntpsync: Literal["enable", "disable"]
    # Use the FortiGuard NTP server or any other available NTP Server.
    type: Literal["fortiguard", "custom"]
    # NTP synchronization interval (1 - 1440 min).
    syncinterval: int
    # Configure the FortiGate to connect to any available third-party NTP server.
    ntpserver: list[NtpNtpserverObject]  # Table field - list of typed objects
    # Source IP address for communication to the NTP server.
    source_ip: str
    # Source IPv6 address for communication to the NTP server.
    source_ip6: str
    # Enable/disable FortiGate NTP Server Mode. Your FortiGate becomes an NTP server f
    server_mode: Literal["enable", "disable"]
    # Enable/disable authentication.
    authentication: Literal["enable", "disable"]
    # Key type for authentication (MD5, SHA1, SHA256).
    key_type: Literal["MD5", "SHA1", "SHA256"]
    # Key for authentication.
    key: str
    # Key ID for authentication.
    key_id: int
    # FortiGate interface(s) with NTP server mode enabled. Devices on your network can
    interface: list[NtpInterfaceObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> NtpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ntp:
    """
    Configure system NTP information.
    
    Path: system/ntp
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpObject: ...
    
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
    ) -> NtpResponse: ...
    
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
    ) -> NtpResponse: ...
    
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
    ) -> NtpResponse: ...
    
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
    ) -> NtpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> NtpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: NtpPayload | None = ...,
        ntpsync: Literal["enable", "disable"] | None = ...,
        type: Literal["fortiguard", "custom"] | None = ...,
        syncinterval: int | None = ...,
        ntpserver: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        key_type: Literal["MD5", "SHA1", "SHA256"] | None = ...,
        key: str | None = ...,
        key_id: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ntp",
    "NtpPayload",
    "NtpObject",
]