from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SnmpCommunityPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/snmp_community payload fields.
    
    Configure FortiSwitch SNMP v1/v2c communities globally.
    
    **Usage:**
        payload: SnmpCommunityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # SNMP community ID.
    name: str  # SNMP community name.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable this SNMP community.
    hosts: NotRequired[list[dict[str, Any]]]  # Configure IPv4 SNMP managers (hosts).
    query_v1_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable SNMP v1 queries.
    query_v1_port: NotRequired[int]  # SNMP v1 query port (default = 161).
    query_v2c_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable SNMP v2c queries.
    query_v2c_port: NotRequired[int]  # SNMP v2c query port (default = 161).
    trap_v1_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable SNMP v1 traps.
    trap_v1_lport: NotRequired[int]  # SNMP v2c trap local port (default = 162).
    trap_v1_rport: NotRequired[int]  # SNMP v2c trap remote port (default = 162).
    trap_v2c_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable SNMP v2c traps.
    trap_v2c_lport: NotRequired[int]  # SNMP v2c trap local port (default = 162).
    trap_v2c_rport: NotRequired[int]  # SNMP v2c trap remote port (default = 162).
    events: NotRequired[Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]]  # SNMP notifications (traps) to send.


class SnmpCommunityObject(FortiObject[SnmpCommunityPayload]):
    """Typed FortiObject for switch_controller/snmp_community with IDE autocomplete support."""
    
    # SNMP community ID.
    id: int
    # SNMP community name.
    name: str
    # Enable/disable this SNMP community.
    status: Literal["disable", "enable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: list[str]  # Auto-flattened from member_table
    # Enable/disable SNMP v1 queries.
    query_v1_status: Literal["disable", "enable"]
    # SNMP v1 query port (default = 161).
    query_v1_port: int
    # Enable/disable SNMP v2c queries.
    query_v2c_status: Literal["disable", "enable"]
    # SNMP v2c query port (default = 161).
    query_v2c_port: int
    # Enable/disable SNMP v1 traps.
    trap_v1_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162).
    trap_v1_lport: int
    # SNMP v2c trap remote port (default = 162).
    trap_v1_rport: int
    # Enable/disable SNMP v2c traps.
    trap_v2c_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162).
    trap_v2c_lport: int
    # SNMP v2c trap remote port (default = 162).
    trap_v2c_rport: int
    # SNMP notifications (traps) to send.
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SnmpCommunityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SnmpCommunity:
    """
    Configure FortiSwitch SNMP v1/v2c communities globally.
    
    Path: switch_controller/snmp_community
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
    ) -> SnmpCommunityObject: ...
    
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
    ) -> list[SnmpCommunityObject]: ...
    
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
    ) -> SnmpCommunityObject | list[SnmpCommunityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnmpCommunityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SnmpCommunityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> SnmpCommunityObject: ...
    
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
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | list[dict[str, Any]] | None = ...,
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
    "SnmpCommunity",
    "SnmpCommunityPayload",
    "SnmpCommunityObject",
]