from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class PtpPayload(TypedDict, total=False):
    """
    Type hints for system/ptp payload fields.
    
    Configure system PTP information.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: PtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting the FortiGate system time by synchron
    mode: NotRequired[Literal["multicast", "hybrid"]]  # Multicast transmission or hybrid transmission.
    delay_mechanism: NotRequired[Literal["E2E", "P2P"]]  # End to end delay detection or peer to peer delay detection.
    request_interval: NotRequired[int]  # The delay request value is the logarithmic mean interval in 
    interface: str  # PTP client will reply through this interface.
    server_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGate PTP server mode. Your FortiGate bec
    server_interface: NotRequired[list[dict[str, Any]]]  # FortiGate interface(s) with PTP server mode enabled. Devices


class PtpObject(FortiObject[PtpPayload]):
    """Typed FortiObject for system/ptp with IDE autocomplete support."""
    
    # Enable/disable setting the FortiGate system time by synchronizing with an PTP Se
    status: Literal["enable", "disable"]
    # Multicast transmission or hybrid transmission.
    mode: Literal["multicast", "hybrid"]
    # End to end delay detection or peer to peer delay detection.
    delay_mechanism: Literal["E2E", "P2P"]
    # The delay request value is the logarithmic mean interval in seconds between the 
    request_interval: int
    # PTP client will reply through this interface.
    interface: str
    # Enable/disable FortiGate PTP server mode. Your FortiGate becomes an PTP server f
    server_mode: Literal["enable", "disable"]
    # FortiGate interface(s) with PTP server mode enabled. Devices on your network can
    server_interface: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PtpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ptp:
    """
    Configure system PTP information.
    
    Path: system/ptp
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PtpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ptp",
    "PtpPayload",
    "PtpObject",
]