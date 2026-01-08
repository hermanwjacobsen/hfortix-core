from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class UserPayload(TypedDict, total=False):
    """
    Type hints for system/snmp/user payload fields.
    
    SNMP user configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.snmp.mib-view.MibViewEndpoint` (via: mib-view)

    **Usage:**
        payload: UserPayload = {
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
    notify_hosts: NotRequired[list[dict[str, Any]]]  # SNMP managers to send notifications (traps) to.
    notify_hosts6: NotRequired[list[dict[str, Any]]]  # IPv6 SNMP managers to send notifications (traps) to.
    source_ip: NotRequired[str]  # Source IP for SNMP trap.
    source_ipv6: NotRequired[str]  # Source IPv6 for SNMP trap.
    ha_direct: NotRequired[Literal["enable", "disable"]]  # Enable/disable direct management of HA cluster members.
    events: NotRequired[Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]]  # SNMP notifications (traps) to send.
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

# Nested classes for table field children

@final
class UserVdomsObject:
    """Typed object for vdoms table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VDOM name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class UserResponse(TypedDict):
    """
    Type hints for system/snmp/user API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["enable", "disable"]
    trap_status: Literal["enable", "disable"]
    trap_lport: int
    trap_rport: int
    queries: Literal["enable", "disable"]
    query_port: int
    notify_hosts: list[dict[str, Any]]
    notify_hosts6: list[dict[str, Any]]
    source_ip: str
    source_ipv6: str
    ha_direct: Literal["enable", "disable"]
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]
    mib_view: str
    vdoms: list[dict[str, Any]]
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]
    auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"]
    auth_pwd: str
    priv_proto: Literal["aes", "des", "aes256", "aes256cisco"]
    priv_pwd: str
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int


@final
class UserObject:
    """Typed FortiObject for system/snmp/user with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SNMP user name.
    name: str
    # Enable/disable this SNMP user.
    status: Literal["enable", "disable"]
    # Enable/disable traps for this SNMP user.
    trap_status: Literal["enable", "disable"]
    # SNMPv3 local trap port (default = 162).
    trap_lport: int
    # SNMPv3 trap remote port (default = 162).
    trap_rport: int
    # Enable/disable SNMP queries for this user.
    queries: Literal["enable", "disable"]
    # SNMPv3 query port (default = 161).
    query_port: int
    # SNMP managers to send notifications (traps) to.
    notify_hosts: list[dict[str, Any]]  # Multi-value field
    # IPv6 SNMP managers to send notifications (traps) to.
    notify_hosts6: list[dict[str, Any]]  # Multi-value field
    # Source IP for SNMP trap.
    source_ip: str
    # Source IPv6 for SNMP trap.
    source_ipv6: str
    # Enable/disable direct management of HA cluster members.
    ha_direct: Literal["enable", "disable"]
    # SNMP notifications (traps) to send.
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]
    # SNMP access control MIB view.
    mib_view: str
    # SNMP access control VDOMs.
    vdoms: list[UserVdomsObject]  # Table field - list of typed objects
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
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> UserPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class User:
    """
    SNMP user configuration.
    
    Path: system/snmp/user
    Category: cmdb
    Primary Key: name
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
    ) -> UserObject: ...
    
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
    ) -> UserObject: ...
    
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
    ) -> list[UserObject]: ...
    
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
    ) -> UserResponse: ...
    
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
    ) -> UserResponse: ...
    
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
    ) -> list[UserResponse]: ...
    
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
    ) -> UserObject | list[UserObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UserObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
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
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
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
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UserObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
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
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
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
    ) -> UserObject: ...
    
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
        payload_dict: UserPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        trap_status: Literal["enable", "disable"] | None = ...,
        trap_lport: int | None = ...,
        trap_rport: int | None = ...,
        queries: Literal["enable", "disable"] | None = ...,
        query_port: int | None = ...,
        notify_hosts: str | list[str] | None = ...,
        notify_hosts6: str | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ipv6: str | None = ...,
        ha_direct: Literal["enable", "disable"] | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = ...,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = ...,
        auth_pwd: str | None = ...,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = ...,
        priv_pwd: str | None = ...,
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
    "User",
    "UserPayload",
    "UserObject",
]