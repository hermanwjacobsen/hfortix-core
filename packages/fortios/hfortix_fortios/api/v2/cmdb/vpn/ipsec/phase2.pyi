from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class Phase2Payload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec/phase2 payload fields.
    
    Configure VPN autokey tunnel.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: dst-name, src-name)
        - :class:`~.firewall.address6.Address6Endpoint` (via: dst-name6, src-name6)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: dst-name, src-name)
        - :class:`~.firewall.addrgrp6.Addrgrp6Endpoint` (via: dst-name6, src-name6)
        - :class:`~.vpn.ipsec.phase1.Phase1Endpoint` (via: phase1name)

    **Usage:**
        payload: Phase2Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IPsec tunnel name.
    phase1name: str  # Phase 1 determines the options required for phase 2.
    dhcp_ipsec: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP-IPsec.
    use_natip: NotRequired[Literal["enable", "disable"]]  # Enable to use the FortiGate public IP as the source selector
    selector_match: NotRequired[Literal["exact", "subset", "auto"]]  # Match type to use when comparing selectors.
    proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]  # Phase2 proposal.
    pfs: NotRequired[Literal["enable", "disable"]]  # Enable/disable PFS feature.
    dhgrp: NotRequired[Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]]  # Phase2 DH group.
    addke1: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE1 group.
    addke2: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE2 group.
    addke3: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE3 group.
    addke4: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE4 group.
    addke5: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE5 group.
    addke6: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE6 group.
    addke7: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # phase2 ADDKE7 group.
    replay: NotRequired[Literal["enable", "disable"]]  # Enable/disable replay detection.
    keepalive: NotRequired[Literal["enable", "disable"]]  # Enable/disable keep alive.
    auto_negotiate: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPsec SA auto-negotiation.
    add_route: NotRequired[Literal["phase1", "enable", "disable"]]  # Enable/disable automatic route addition.
    inbound_dscp_copy: NotRequired[Literal["phase1", "enable", "disable"]]  # Enable/disable copying of the DSCP in the ESP header to the
    keylifeseconds: NotRequired[int]  # Phase2 key life in time in seconds (120 - 172800).
    keylifekbs: NotRequired[int]  # Phase2 key life in number of kilobytes of traffic
    keylife_type: NotRequired[Literal["seconds", "kbs", "both"]]  # Keylife type.
    single_source: NotRequired[Literal["enable", "disable"]]  # Enable/disable single source IP restriction.
    route_overlap: NotRequired[Literal["use-old", "use-new", "allow"]]  # Action for overlapping routes.
    encapsulation: NotRequired[Literal["tunnel-mode", "transport-mode"]]  # ESP encapsulation mode.
    l2tp: NotRequired[Literal["enable", "disable"]]  # Enable/disable L2TP over IPsec.
    comments: NotRequired[str]  # Comment.
    initiator_ts_narrow: NotRequired[Literal["enable", "disable"]]  # Enable/disable traffic selector narrowing for IKEv2 initiato
    diffserv: NotRequired[Literal["enable", "disable"]]  # Enable/disable applying DSCP value to the IPsec tunnel outer
    diffservcode: NotRequired[str]  # DSCP value to be applied to the IPsec tunnel outer IP header
    protocol: NotRequired[int]  # Quick mode protocol selector (1 - 255 or 0 for all).
    src_name: str  # Local proxy ID name.
    src_name6: str  # Local proxy ID name.
    src_addr_type: NotRequired[Literal["subnet", "range", "ip", "name"]]  # Local proxy ID type.
    src_start_ip: NotRequired[str]  # Local proxy ID start.
    src_start_ip6: NotRequired[str]  # Local proxy ID IPv6 start.
    src_end_ip: NotRequired[str]  # Local proxy ID end.
    src_end_ip6: NotRequired[str]  # Local proxy ID IPv6 end.
    src_subnet: NotRequired[str]  # Local proxy ID subnet.
    src_subnet6: NotRequired[str]  # Local proxy ID IPv6 subnet.
    src_port: NotRequired[int]  # Quick mode source port (1 - 65535 or 0 for all).
    dst_name: str  # Remote proxy ID name.
    dst_name6: str  # Remote proxy ID name.
    dst_addr_type: NotRequired[Literal["subnet", "range", "ip", "name"]]  # Remote proxy ID type.
    dst_start_ip: NotRequired[str]  # Remote proxy ID IPv4 start.
    dst_start_ip6: NotRequired[str]  # Remote proxy ID IPv6 start.
    dst_end_ip: NotRequired[str]  # Remote proxy ID IPv4 end.
    dst_end_ip6: NotRequired[str]  # Remote proxy ID IPv6 end.
    dst_subnet: NotRequired[str]  # Remote proxy ID IPv4 subnet.
    dst_subnet6: NotRequired[str]  # Remote proxy ID IPv6 subnet.
    dst_port: NotRequired[int]  # Quick mode destination port (1 - 65535 or 0 for all).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class Phase2Response(TypedDict):
    """
    Type hints for vpn/ipsec/phase2 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    phase1name: str
    dhcp_ipsec: Literal["enable", "disable"]
    use_natip: Literal["enable", "disable"]
    selector_match: Literal["exact", "subset", "auto"]
    proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]
    pfs: Literal["enable", "disable"]
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    replay: Literal["enable", "disable"]
    keepalive: Literal["enable", "disable"]
    auto_negotiate: Literal["enable", "disable"]
    add_route: Literal["phase1", "enable", "disable"]
    inbound_dscp_copy: Literal["phase1", "enable", "disable"]
    keylifeseconds: int
    keylifekbs: int
    keylife_type: Literal["seconds", "kbs", "both"]
    single_source: Literal["enable", "disable"]
    route_overlap: Literal["use-old", "use-new", "allow"]
    encapsulation: Literal["tunnel-mode", "transport-mode"]
    l2tp: Literal["enable", "disable"]
    comments: str
    initiator_ts_narrow: Literal["enable", "disable"]
    diffserv: Literal["enable", "disable"]
    diffservcode: str
    protocol: int
    src_name: str
    src_name6: str
    src_addr_type: Literal["subnet", "range", "ip", "name"]
    src_start_ip: str
    src_start_ip6: str
    src_end_ip: str
    src_end_ip6: str
    src_subnet: str
    src_subnet6: str
    src_port: int
    dst_name: str
    dst_name6: str
    dst_addr_type: Literal["subnet", "range", "ip", "name"]
    dst_start_ip: str
    dst_start_ip6: str
    dst_end_ip: str
    dst_end_ip6: str
    dst_subnet: str
    dst_subnet6: str
    dst_port: int


@final
class Phase2Object:
    """Typed FortiObject for vpn/ipsec/phase2 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPsec tunnel name.
    name: str
    # Phase 1 determines the options required for phase 2.
    phase1name: str
    # Enable/disable DHCP-IPsec.
    dhcp_ipsec: Literal["enable", "disable"]
    # Enable to use the FortiGate public IP as the source selector when outbound NAT i
    use_natip: Literal["enable", "disable"]
    # Match type to use when comparing selectors.
    selector_match: Literal["exact", "subset", "auto"]
    # Phase2 proposal.
    proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]
    # Enable/disable PFS feature.
    pfs: Literal["enable", "disable"]
    # Phase2 DH group.
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]
    # phase2 ADDKE1 group.
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE2 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE3 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE4 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE5 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE6 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # phase2 ADDKE7 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # Enable/disable replay detection.
    replay: Literal["enable", "disable"]
    # Enable/disable keep alive.
    keepalive: Literal["enable", "disable"]
    # Enable/disable IPsec SA auto-negotiation.
    auto_negotiate: Literal["enable", "disable"]
    # Enable/disable automatic route addition.
    add_route: Literal["phase1", "enable", "disable"]
    # Enable/disable copying of the DSCP in the ESP header to the inner IP header.
    inbound_dscp_copy: Literal["phase1", "enable", "disable"]
    # Phase2 key life in time in seconds (120 - 172800).
    keylifeseconds: int
    # Phase2 key life in number of kilobytes of traffic (5120 - 4294967295).
    keylifekbs: int
    # Keylife type.
    keylife_type: Literal["seconds", "kbs", "both"]
    # Enable/disable single source IP restriction.
    single_source: Literal["enable", "disable"]
    # Action for overlapping routes.
    route_overlap: Literal["use-old", "use-new", "allow"]
    # ESP encapsulation mode.
    encapsulation: Literal["tunnel-mode", "transport-mode"]
    # Enable/disable L2TP over IPsec.
    l2tp: Literal["enable", "disable"]
    # Comment.
    comments: str
    # Enable/disable traffic selector narrowing for IKEv2 initiator.
    initiator_ts_narrow: Literal["enable", "disable"]
    # Enable/disable applying DSCP value to the IPsec tunnel outer IP header.
    diffserv: Literal["enable", "disable"]
    # DSCP value to be applied to the IPsec tunnel outer IP header.
    diffservcode: str
    # Quick mode protocol selector (1 - 255 or 0 for all).
    protocol: int
    # Local proxy ID name.
    src_name: str
    # Local proxy ID name.
    src_name6: str
    # Local proxy ID type.
    src_addr_type: Literal["subnet", "range", "ip", "name"]
    # Local proxy ID start.
    src_start_ip: str
    # Local proxy ID IPv6 start.
    src_start_ip6: str
    # Local proxy ID end.
    src_end_ip: str
    # Local proxy ID IPv6 end.
    src_end_ip6: str
    # Local proxy ID subnet.
    src_subnet: str
    # Local proxy ID IPv6 subnet.
    src_subnet6: str
    # Quick mode source port (1 - 65535 or 0 for all).
    src_port: int
    # Remote proxy ID name.
    dst_name: str
    # Remote proxy ID name.
    dst_name6: str
    # Remote proxy ID type.
    dst_addr_type: Literal["subnet", "range", "ip", "name"]
    # Remote proxy ID IPv4 start.
    dst_start_ip: str
    # Remote proxy ID IPv6 start.
    dst_start_ip6: str
    # Remote proxy ID IPv4 end.
    dst_end_ip: str
    # Remote proxy ID IPv6 end.
    dst_end_ip6: str
    # Remote proxy ID IPv4 subnet.
    dst_subnet: str
    # Remote proxy ID IPv6 subnet.
    dst_subnet6: str
    # Quick mode destination port (1 - 65535 or 0 for all).
    dst_port: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Phase2Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Phase2:
    """
    Configure VPN autokey tunnel.
    
    Path: vpn/ipsec/phase2
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
    ) -> Phase2Object: ...
    
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
    ) -> Phase2Object: ...
    
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
    ) -> list[Phase2Object]: ...
    
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
    ) -> Phase2Response: ...
    
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
    ) -> Phase2Response: ...
    
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
    ) -> list[Phase2Response]: ...
    
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
    ) -> Phase2Object | list[Phase2Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Phase2Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Phase2Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
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
    ) -> Phase2Object: ...
    
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
        payload_dict: Phase2Payload | None = ...,
        name: str | None = ...,
        phase1name: str | None = ...,
        dhcp_ipsec: Literal["enable", "disable"] | None = ...,
        use_natip: Literal["enable", "disable"] | None = ...,
        selector_match: Literal["exact", "subset", "auto"] | None = ...,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        pfs: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        replay: Literal["enable", "disable"] | None = ...,
        keepalive: Literal["enable", "disable"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        add_route: Literal["phase1", "enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = ...,
        keylifeseconds: int | None = ...,
        keylifekbs: int | None = ...,
        keylife_type: Literal["seconds", "kbs", "both"] | None = ...,
        single_source: Literal["enable", "disable"] | None = ...,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = ...,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = ...,
        l2tp: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        initiator_ts_narrow: Literal["enable", "disable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        protocol: int | None = ...,
        src_name: str | None = ...,
        src_name6: str | None = ...,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        src_start_ip: str | None = ...,
        src_start_ip6: str | None = ...,
        src_end_ip: str | None = ...,
        src_end_ip6: str | None = ...,
        src_subnet: str | None = ...,
        src_subnet6: str | None = ...,
        src_port: int | None = ...,
        dst_name: str | None = ...,
        dst_name6: str | None = ...,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = ...,
        dst_start_ip: str | None = ...,
        dst_start_ip6: str | None = ...,
        dst_end_ip: str | None = ...,
        dst_end_ip6: str | None = ...,
        dst_subnet: str | None = ...,
        dst_subnet6: str | None = ...,
        dst_port: int | None = ...,
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
    "Phase2",
    "Phase2Payload",
    "Phase2Object",
]