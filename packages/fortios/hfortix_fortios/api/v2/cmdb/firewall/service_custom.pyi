from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ServiceCustomPayload(TypedDict, total=False):
    """
    Type hints for firewall/service_custom payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ServiceCustomPayload = {
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


class ServiceCustom:
    """
    Configure custom services.
    
    Path: firewall/service_custom
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
        payload_dict: ServiceCustomPayload | None = ...,
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ServiceCustomPayload | None = ...,
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
        payload_dict: ServiceCustomPayload | None = ...,
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