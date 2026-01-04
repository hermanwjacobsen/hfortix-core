from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnmpCommunityPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/snmp_community payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class SnmpCommunity:
    """
    Configure FortiSwitch SNMP v1/v2c communities globally.
    
    Path: switch_controller/snmp_community
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
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