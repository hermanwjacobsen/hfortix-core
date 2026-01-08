from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class CustomPayload(TypedDict, total=False):
    """
    Type hints for firewall/service/custom payload fields.
    
    Configure custom services.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.service.category.CategoryEndpoint` (via: category)

    **Usage:**
        payload: CustomPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Custom service name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable web proxy service.
    category: NotRequired[str]  # Service category.
    protocol: NotRequired[Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"]]  # Protocol type based on IANA numbers.
    helper: NotRequired[Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"]]  # Helper name.
    iprange: NotRequired[str]  # Start and end of the IP range associated with service.
    fqdn: NotRequired[str]  # Fully qualified domain name.
    protocol_number: NotRequired[int]  # IP protocol number.
    icmptype: NotRequired[int]  # ICMP type.
    icmpcode: NotRequired[int]  # ICMP code.
    tcp_portrange: NotRequired[str]  # Multiple TCP port ranges.
    udp_portrange: NotRequired[str]  # Multiple UDP port ranges.
    udplite_portrange: NotRequired[str]  # Multiple UDP-Lite port ranges.
    sctp_portrange: NotRequired[str]  # Multiple SCTP port ranges.
    tcp_halfclose_timer: NotRequired[int]  # Wait time to close a TCP session waiting for an unanswered F
    tcp_halfopen_timer: NotRequired[int]  # Wait time to close a TCP session waiting for an unanswered o
    tcp_timewait_timer: NotRequired[int]  # Set the length of the TCP TIME-WAIT state in seconds (1 - 30
    tcp_rst_timer: NotRequired[int]  # Set the length of the TCP CLOSE state in seconds (5 - 300 se
    udp_idle_timer: NotRequired[int]  # Number of seconds before an idle UDP/UDP-Lite connection tim
    session_ttl: NotRequired[str]  # Session TTL (300 - 2764800, 0 = default).
    check_reset_range: NotRequired[Literal["disable", "strict", "default"]]  # Configure the type of ICMP error message verification.
    comment: NotRequired[str]  # Comment.
    color: NotRequired[int]  # Color of icon on the GUI.
    app_service_type: NotRequired[Literal["disable", "app-id", "app-category"]]  # Application service type.
    app_category: NotRequired[list[dict[str, Any]]]  # Application category ID.
    application: NotRequired[list[dict[str, Any]]]  # Application ID.
    fabric_object: NotRequired[Literal["enable", "disable"]]  # Security Fabric global object setting.


class CustomObject(FortiObject[CustomPayload]):
    """Typed FortiObject for firewall/service/custom with IDE autocomplete support."""
    
    # Custom service name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Enable/disable web proxy service.
    proxy: Literal["enable", "disable"]
    # Service category.
    category: str
    # Protocol type based on IANA numbers.
    protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"]
    # Helper name.
    helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"]
    # Start and end of the IP range associated with service.
    iprange: str
    # Fully qualified domain name.
    fqdn: str
    # IP protocol number.
    protocol_number: int
    # ICMP type.
    icmptype: int
    # ICMP code.
    icmpcode: int
    # Multiple TCP port ranges.
    tcp_portrange: str
    # Multiple UDP port ranges.
    udp_portrange: str
    # Multiple UDP-Lite port ranges.
    udplite_portrange: str
    # Multiple SCTP port ranges.
    sctp_portrange: str
    # Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400
    tcp_halfclose_timer: int
    # Wait time to close a TCP session waiting for an unanswered open session packet (
    tcp_halfopen_timer: int
    # Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default).
    tcp_timewait_timer: int
    # Set the length of the TCP CLOSE state in seconds (5 - 300 sec, 0 = default).
    tcp_rst_timer: int
    # Number of seconds before an idle UDP/UDP-Lite connection times out (0 - 86400 se
    udp_idle_timer: int
    # Session TTL (300 - 2764800, 0 = default).
    session_ttl: str
    # Configure the type of ICMP error message verification.
    check_reset_range: Literal["disable", "strict", "default"]
    # Comment.
    comment: str
    # Color of icon on the GUI.
    color: int
    # Application service type.
    app_service_type: Literal["disable", "app-id", "app-category"]
    # Application category ID.
    app_category: list[str]  # Auto-flattened from member_table
    # Application ID.
    application: list[str]  # Auto-flattened from member_table
    # Security Fabric global object setting.
    fabric_object: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CustomPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Custom:
    """
    Configure custom services.
    
    Path: firewall/service/custom
    Category: cmdb
    Primary Key: name
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
    ) -> CustomObject: ...
    
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
    ) -> list[CustomObject]: ...
    
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
    ) -> CustomObject | list[CustomObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CustomObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CustomObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    ) -> CustomObject: ...
    
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
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Custom",
    "CustomPayload",
    "CustomObject",
]