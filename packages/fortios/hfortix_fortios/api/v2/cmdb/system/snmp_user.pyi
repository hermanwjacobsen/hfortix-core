from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SnmpUserPayload(TypedDict, total=False):
    """
    Type hints for system/snmp_user payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SnmpUserPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # SNMP user name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this SNMP user.
    trap_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable traps for this SNMP user.
    trap_lport: NotRequired[int]  # SNMPv3 local trap port (default = 162).
    trap_rport: NotRequired[int]  # SNMPv3 trap remote port (default = 162).
    queries: NotRequired[Literal["enable", "disable"]]  # Enable/disable SNMP queries for this user.
    query_port: NotRequired[int]  # SNMPv3 query port (default = 161).
    notify_hosts: NotRequired[str]  # SNMP managers to send notifications (traps) to.
    notify_hosts6: NotRequired[str]  # IPv6 SNMP managers to send notifications (traps) to.
    source_ip: NotRequired[str]  # Source IP for SNMP trap.
    source_ipv6: NotRequired[str]  # Source IPv6 for SNMP trap.
    ha_direct: NotRequired[Literal["enable", "disable"]]  # Enable/disable direct management of HA cluster members.
    events: NotRequired[Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change"]]  # SNMP notifications (traps) to send.
    mib_view: NotRequired[str]  # SNMP access control MIB view.
    vdoms: NotRequired[list[dict[str, Any]]]  # SNMP access control VDOMs.
    security_level: NotRequired[Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]]  # Security level for message authentication and encryption.
    auth_proto: NotRequired[Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"]]  # Authentication protocol.
    auth_pwd: str  # Password for authentication protocol.
    priv_proto: NotRequired[Literal["aes", "des", "aes256", "aes256cisco"]]  # Privacy (encryption) protocol.
    priv_pwd: str  # Password for privacy (encryption) protocol.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class SnmpUser:
    """
    SNMP user configuration.
    
    Path: system/snmp_user
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
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
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | None = ...,
        notify_hosts6: str | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change"] | None = ...,
        mib_view: str | None = ...,
        vdoms: list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SnmpUserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | None = ...,
        notify_hosts6: str | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change"] | None = ...,
        mib_view: str | None = ...,
        vdoms: list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: SnmpUserPayload | None = ...,
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