from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SnmpPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/snmp payload fields.
    
    Configure SNMP.
    
    **Usage:**
        payload: SnmpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    engine_id: NotRequired[str]  # AC SNMP engineID string (maximum 24 characters).
    contact_info: NotRequired[str]  # Contact Information.
    trap_high_cpu_threshold: NotRequired[int]  # CPU usage when trap is sent.
    trap_high_mem_threshold: NotRequired[int]  # Memory usage when trap is sent.
    community: NotRequired[list[dict[str, Any]]]  # SNMP Community Configuration.
    user: NotRequired[list[dict[str, Any]]]  # SNMP User Configuration.

# Nested classes for table field children

@final
class SnmpCommunityObject:
    """Typed object for community table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Community ID.
    id: int
    # Community name.
    name: str
    # Enable/disable this SNMP community.
    status: Literal["enable", "disable"]
    # Enable/disable SNMP v1 queries.
    query_v1_status: Literal["enable", "disable"]
    # Enable/disable SNMP v2c queries.
    query_v2c_status: Literal["enable", "disable"]
    # Enable/disable SNMP v1 traps.
    trap_v1_status: Literal["enable", "disable"]
    # Enable/disable SNMP v2c traps.
    trap_v2c_status: Literal["enable", "disable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: str
    # Configure IPv6 SNMP managers (hosts).
    hosts6: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SnmpUserObject:
    """Typed object for user table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SNMP user name.
    name: str
    # SNMP user enable.
    status: Literal["enable", "disable"]
    # Enable/disable SNMP queries for this user.
    queries: Literal["enable", "disable"]
    # Enable/disable traps for this SNMP user.
    trap_status: Literal["enable", "disable"]
    # Security level for message authentication and encryption.
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]
    # Authentication protocol.
    auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"]
    # Password for authentication protocol.
    auth_pwd: str
    # Privacy (encryption) protocol.
    priv_proto: Literal["aes", "des", "aes256", "aes256cisco"]
    # Password for privacy (encryption) protocol.
    priv_pwd: str
    # Configure SNMP User Notify Hosts.
    notify_hosts: str
    # Configure IPv6 SNMP User Notify Hosts.
    notify_hosts6: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SnmpResponse(TypedDict):
    """
    Type hints for wireless_controller/snmp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    engine_id: str
    contact_info: str
    trap_high_cpu_threshold: int
    trap_high_mem_threshold: int
    community: list[dict[str, Any]]
    user: list[dict[str, Any]]


@final
class SnmpObject:
    """Typed FortiObject for wireless_controller/snmp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # AC SNMP engineID string (maximum 24 characters).
    engine_id: str
    # Contact Information.
    contact_info: str
    # CPU usage when trap is sent.
    trap_high_cpu_threshold: int
    # Memory usage when trap is sent.
    trap_high_mem_threshold: int
    # SNMP Community Configuration.
    community: list[SnmpCommunityObject]  # Table field - list of typed objects
    # SNMP User Configuration.
    user: list[SnmpUserObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SnmpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Snmp:
    """
    Configure SNMP.
    
    Path: wireless_controller/snmp
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpObject: ...
    
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
    ) -> SnmpResponse: ...
    
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
    ) -> SnmpResponse: ...
    
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
    ) -> SnmpResponse: ...
    
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
    ) -> SnmpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnmpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: SnmpPayload | None = ...,
        engine_id: str | None = ...,
        contact_info: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_high_mem_threshold: int | None = ...,
        community: str | list[str] | list[dict[str, Any]] | None = ...,
        user: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Snmp",
    "SnmpPayload",
    "SnmpObject",
]