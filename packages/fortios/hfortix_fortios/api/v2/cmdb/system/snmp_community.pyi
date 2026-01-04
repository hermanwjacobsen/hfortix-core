from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnmpCommunityPayload(TypedDict, total=False):
    """
    Type hints for system/snmp_community payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SnmpCommunityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Community ID.
    name: str  # Community name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this SNMP community.
    hosts: NotRequired[list[dict[str, Any]]]  # Configure IPv4 SNMP managers (hosts).
    hosts6: NotRequired[list[dict[str, Any]]]  # Configure IPv6 SNMP managers.
    query_v1_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP v1 queries.
    query_v1_port: NotRequired[int]  # SNMP v1 query port (default = 161).
    query_v2c_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP v2c queries.
    query_v2c_port: NotRequired[int]  # SNMP v2c query port (default = 161).
    trap_v1_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP v1 traps.
    trap_v1_lport: NotRequired[int]  # SNMP v1 trap local port (default = 162).
    trap_v1_rport: NotRequired[int]  # SNMP v1 trap remote port (default = 162).
    trap_v2c_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP v2c traps.
    trap_v2c_lport: NotRequired[int]  # SNMP v2c trap local port (default = 162).
    trap_v2c_rport: NotRequired[int]  # SNMP v2c trap remote port (default = 162).
    events: NotRequired[Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change"]]  # SNMP trap events.
    mib_view: NotRequired[str]  # SNMP access control MIB view.
    vdoms: NotRequired[list[dict[str, Any]]]  # SNMP access control VDOMs.


class SnmpCommunity:
    """
    SNMP community configuration.
    
    Path: system/snmp_community
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
        status: Literal["enable", "disable"] | None = ...,
        hosts: list[dict[str, Any]] | None = ...,
        hosts6: list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change"] | None = ...,
        mib_view: str | None = ...,
        vdoms: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: list[dict[str, Any]] | None = ...,
        hosts6: list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change"] | None = ...,
        mib_view: str | None = ...,
        vdoms: list[dict[str, Any]] | None = ...,
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