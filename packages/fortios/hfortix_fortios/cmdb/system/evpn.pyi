from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class EvpnPayload(TypedDict, total=False):
    """
    Type hints for system/evpn payload fields.
    
    Configure EVPN instance.
    
    **Usage:**
        payload: EvpnPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # ID.
    rd: NotRequired[str]  # Route Distinguisher: AA:NN|A.B.C.D:NN.
    import_rt: NotRequired[list[dict[str, Any]]]  # List of import route targets.
    export_rt: NotRequired[list[dict[str, Any]]]  # List of export route targets.
    ip_local_learning: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP address local learning.
    arp_suppression: NotRequired[Literal["enable", "disable"]]  # Enable/disable ARP suppression.


class EvpnObject(FortiObject[EvpnPayload]):
    """Typed FortiObject for system/evpn with IDE autocomplete support."""
    
    # ID.
    id: int
    # Route Distinguisher: AA:NN|A.B.C.D:NN.
    rd: str
    # List of import route targets.
    import_rt: list[str]  # Auto-flattened from member_table
    # List of export route targets.
    export_rt: list[str]  # Auto-flattened from member_table
    # Enable/disable IP address local learning.
    ip_local_learning: Literal["enable", "disable"]
    # Enable/disable ARP suppression.
    arp_suppression: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> EvpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Evpn:
    """
    Configure EVPN instance.
    
    Path: system/evpn
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        id: int,
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
    ) -> EvpnObject: ...
    
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
    ) -> list[EvpnObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
        id: None = None,
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
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> EvpnObject | list[EvpnObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> EvpnObject: ...
    
    @overload
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> EvpnObject: ...
    
    @overload
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> EvpnObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: EvpnPayload | None = ...,
        id: int | None = ...,
        rd: str | None = ...,
        import_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        export_rt: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_local_learning: Literal["enable", "disable"] | None = ...,
        arp_suppression: Literal["enable", "disable"] | None = ...,
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
    "Evpn",
    "EvpnPayload",
    "EvpnObject",
]