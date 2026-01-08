from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class DedicatedMgmtPayload(TypedDict, total=False):
    """
    Type hints for system/dedicated_mgmt payload fields.
    
    Configure dedicated management.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: DedicatedMgmtPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable dedicated management.
    interface: NotRequired[str]  # Dedicated management interface.
    default_gateway: NotRequired[str]  # Default gateway for dedicated management interface.
    dhcp_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP server on management interface.
    dhcp_netmask: NotRequired[str]  # DHCP netmask.
    dhcp_start_ip: NotRequired[str]  # DHCP start IP for dedicated management.
    dhcp_end_ip: NotRequired[str]  # DHCP end IP for dedicated management.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class DedicatedMgmtResponse(TypedDict):
    """
    Type hints for system/dedicated_mgmt API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    interface: str
    default_gateway: str
    dhcp_server: Literal["enable", "disable"]
    dhcp_netmask: str
    dhcp_start_ip: str
    dhcp_end_ip: str


@final
class DedicatedMgmtObject:
    """Typed FortiObject for system/dedicated_mgmt with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable dedicated management.
    status: Literal["enable", "disable"]
    # Dedicated management interface.
    interface: str
    # Default gateway for dedicated management interface.
    default_gateway: str
    # Enable/disable DHCP server on management interface.
    dhcp_server: Literal["enable", "disable"]
    # DHCP netmask.
    dhcp_netmask: str
    # DHCP start IP for dedicated management.
    dhcp_start_ip: str
    # DHCP end IP for dedicated management.
    dhcp_end_ip: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DedicatedMgmtPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class DedicatedMgmt:
    """
    Configure dedicated management.
    
    Path: system/dedicated_mgmt
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtObject: ...
    
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
    ) -> DedicatedMgmtResponse: ...
    
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
    ) -> DedicatedMgmtResponse: ...
    
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
    ) -> DedicatedMgmtResponse: ...
    
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
    ) -> DedicatedMgmtObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DedicatedMgmtObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
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
        payload_dict: DedicatedMgmtPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        default_gateway: str | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        dhcp_netmask: str | None = ...,
        dhcp_start_ip: str | None = ...,
        dhcp_end_ip: str | None = ...,
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
    "DedicatedMgmt",
    "DedicatedMgmtPayload",
    "DedicatedMgmtObject",
]