from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class CommunityPayload(TypedDict, total=False):
    """
    Type hints for system/snmp/community payload fields.
    
    SNMP community configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.snmp.mib-view.MibViewEndpoint` (via: mib-view)

    **Usage:**
        payload: CommunityPayload = {
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
    events: NotRequired[Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]]  # SNMP trap events.
    mib_view: NotRequired[str]  # SNMP access control MIB view.
    vdoms: NotRequired[list[dict[str, Any]]]  # SNMP access control VDOMs.

# Nested classes for table field children

@final
class CommunityHostsObject:
    """Typed object for hosts table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Host entry ID.
    id: int
    # Source IPv4 address for SNMP traps.
    source_ip: str
    # IPv4 address of the SNMP manager (host).
    ip: str
    # Enable/disable direct management of HA cluster members.
    ha_direct: Literal["enable", "disable"]
    # Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or bot
    host_type: Literal["any", "query", "trap"]
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
class CommunityHosts6Object:
    """Typed object for hosts6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Host6 entry ID.
    id: int
    # Source IPv6 address for SNMP traps.
    source_ipv6: str
    # SNMP manager IPv6 address prefix.
    ipv6: str
    # Enable/disable direct management of HA cluster members.
    ha_direct: Literal["enable", "disable"]
    # Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or bot
    host_type: Literal["any", "query", "trap"]
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
class CommunityVdomsObject:
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
class CommunityResponse(TypedDict):
    """
    Type hints for system/snmp/community API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int
    name: str
    status: Literal["enable", "disable"]
    hosts: list[dict[str, Any]]
    hosts6: list[dict[str, Any]]
    query_v1_status: Literal["enable", "disable"]
    query_v1_port: int
    query_v2c_status: Literal["enable", "disable"]
    query_v2c_port: int
    trap_v1_status: Literal["enable", "disable"]
    trap_v1_lport: int
    trap_v1_rport: int
    trap_v2c_status: Literal["enable", "disable"]
    trap_v2c_lport: int
    trap_v2c_rport: int
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]
    mib_view: str
    vdoms: list[dict[str, Any]]


@final
class CommunityObject:
    """Typed FortiObject for system/snmp/community with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Community ID.
    id: int
    # Community name.
    name: str
    # Enable/disable this SNMP community.
    status: Literal["enable", "disable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: list[CommunityHostsObject]  # Table field - list of typed objects
    # Configure IPv6 SNMP managers.
    hosts6: list[CommunityHosts6Object]  # Table field - list of typed objects
    # Enable/disable SNMP v1 queries.
    query_v1_status: Literal["enable", "disable"]
    # SNMP v1 query port (default = 161).
    query_v1_port: int
    # Enable/disable SNMP v2c queries.
    query_v2c_status: Literal["enable", "disable"]
    # SNMP v2c query port (default = 161).
    query_v2c_port: int
    # Enable/disable SNMP v1 traps.
    trap_v1_status: Literal["enable", "disable"]
    # SNMP v1 trap local port (default = 162).
    trap_v1_lport: int
    # SNMP v1 trap remote port (default = 162).
    trap_v1_rport: int
    # Enable/disable SNMP v2c traps.
    trap_v2c_status: Literal["enable", "disable"]
    # SNMP v2c trap local port (default = 162).
    trap_v2c_lport: int
    # SNMP v2c trap remote port (default = 162).
    trap_v2c_rport: int
    # SNMP trap events.
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]
    # SNMP access control MIB view.
    mib_view: str
    # SNMP access control VDOMs.
    vdoms: list[CommunityVdomsObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CommunityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Community:
    """
    SNMP community configuration.
    
    Path: system/snmp/community
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CommunityObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CommunityObject: ...
    
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
    ) -> list[CommunityObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> CommunityResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> CommunityResponse: ...
    
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
    ) -> list[CommunityResponse]: ...
    
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
    ) -> CommunityObject | list[CommunityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CommunityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CommunityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> CommunityObject: ...
    
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
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Community",
    "CommunityPayload",
    "CommunityObject",
]