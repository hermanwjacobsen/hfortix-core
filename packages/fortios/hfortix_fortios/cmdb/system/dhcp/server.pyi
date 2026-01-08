from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ServerPayload(TypedDict, total=False):
    """
    Type hints for system/dhcp/server payload fields.
    
    Configure DHCP servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.timezone.TimezoneEndpoint` (via: timezone)

    **Usage:**
        payload: ServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable this DHCP configuration.
    lease_time: NotRequired[int]  # Lease time in seconds, 0 means unlimited.
    mac_acl_default_action: NotRequired[Literal["assign", "block"]]  # MAC access control default action (allow or block assigning 
    forticlient_on_net_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable FortiClient-On-Net service for this DHCP serv
    dns_service: NotRequired[Literal["local", "default", "specify"]]  # Options for assigning DNS servers to DHCP clients.
    dns_server1: NotRequired[str]  # DNS server 1.
    dns_server2: NotRequired[str]  # DNS server 2.
    dns_server3: NotRequired[str]  # DNS server 3.
    dns_server4: NotRequired[str]  # DNS server 4.
    wifi_ac_service: NotRequired[Literal["specify", "local"]]  # Options for assigning WiFi access controllers to DHCP client
    wifi_ac1: NotRequired[str]  # WiFi Access Controller 1 IP address (DHCP option 138, RFC 54
    wifi_ac2: NotRequired[str]  # WiFi Access Controller 2 IP address (DHCP option 138, RFC 54
    wifi_ac3: NotRequired[str]  # WiFi Access Controller 3 IP address (DHCP option 138, RFC 54
    ntp_service: NotRequired[Literal["local", "default", "specify"]]  # Options for assigning Network Time Protocol (NTP) servers to
    ntp_server1: NotRequired[str]  # NTP server 1.
    ntp_server2: NotRequired[str]  # NTP server 2.
    ntp_server3: NotRequired[str]  # NTP server 3.
    domain: NotRequired[str]  # Domain name suffix for the IP addresses that the DHCP server
    wins_server1: NotRequired[str]  # WINS server 1.
    wins_server2: NotRequired[str]  # WINS server 2.
    default_gateway: NotRequired[str]  # Default gateway IP address assigned by the DHCP server.
    next_server: NotRequired[str]  # IP address of a server (for example, a TFTP sever) that DHCP
    netmask: str  # Netmask assigned by the DHCP server.
    interface: str  # DHCP server can assign IP configurations to clients connecte
    ip_range: NotRequired[list[dict[str, Any]]]  # DHCP IP range configuration.
    timezone_option: NotRequired[Literal["disable", "default", "specify"]]  # Options for the DHCP server to set the client's time zone.
    timezone: str  # Select the time zone to be assigned to DHCP clients.
    tftp_server: NotRequired[list[dict[str, Any]]]  # One or more hostnames or IP addresses of the TFTP servers in
    filename: NotRequired[str]  # Name of the boot file on the TFTP server.
    options: NotRequired[list[dict[str, Any]]]  # DHCP options.
    server_type: NotRequired[Literal["regular", "ipsec"]]  # DHCP server can be a normal DHCP server or an IPsec DHCP ser
    ip_mode: NotRequired[Literal["range", "usrgrp"]]  # Method used to assign client IP.
    conflicted_ip_timeout: NotRequired[int]  # Time in seconds to wait after a conflicted IP address is rem
    ipsec_lease_hold: NotRequired[int]  # DHCP over IPsec leases expire this many seconds after tunnel
    auto_configuration: NotRequired[Literal["disable", "enable"]]  # Enable/disable auto configuration.
    dhcp_settings_from_fortiipam: NotRequired[Literal["disable", "enable"]]  # Enable/disable populating of DHCP server settings from Forti
    auto_managed_status: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of this DHCP server once this interface h
    ddns_update: NotRequired[Literal["disable", "enable"]]  # Enable/disable DDNS update for DHCP.
    ddns_update_override: NotRequired[Literal["disable", "enable"]]  # Enable/disable DDNS update override for DHCP.
    ddns_server_ip: NotRequired[str]  # DDNS server IP.
    ddns_zone: NotRequired[str]  # Zone of your domain name (ex. DDNS.com).
    ddns_auth: NotRequired[Literal["disable", "tsig"]]  # DDNS authentication mode.
    ddns_keyname: NotRequired[str]  # DDNS update key name.
    ddns_key: NotRequired[str]  # DDNS update key (base 64 encoding).
    ddns_ttl: NotRequired[int]  # TTL.
    vci_match: NotRequired[Literal["disable", "enable"]]  # Enable/disable vendor class identifier (VCI) matching. When 
    vci_string: NotRequired[list[dict[str, Any]]]  # One or more VCI strings in quotes separated by spaces.
    exclude_range: NotRequired[list[dict[str, Any]]]  # Exclude one or more ranges of IP addresses from being assign
    shared_subnet: NotRequired[Literal["disable", "enable"]]  # Enable/disable shared subnet.
    relay_agent: NotRequired[str]  # Relay agent IP.
    reserved_address: NotRequired[list[dict[str, Any]]]  # Options for the DHCP server to assign IP settings to specifi


class ServerObject(FortiObject[ServerPayload]):
    """Typed FortiObject for system/dhcp/server with IDE autocomplete support."""
    
    # ID.
    id: int
    # Enable/disable this DHCP configuration.
    status: Literal["disable", "enable"]
    # Lease time in seconds, 0 means unlimited.
    lease_time: int
    # MAC access control default action (allow or block assigning IP settings).
    mac_acl_default_action: Literal["assign", "block"]
    # Enable/disable FortiClient-On-Net service for this DHCP server.
    forticlient_on_net_status: Literal["disable", "enable"]
    # Options for assigning DNS servers to DHCP clients.
    dns_service: Literal["local", "default", "specify"]
    # DNS server 1.
    dns_server1: str
    # DNS server 2.
    dns_server2: str
    # DNS server 3.
    dns_server3: str
    # DNS server 4.
    dns_server4: str
    # Options for assigning WiFi access controllers to DHCP clients.
    wifi_ac_service: Literal["specify", "local"]
    # WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).
    wifi_ac1: str
    # WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).
    wifi_ac2: str
    # WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).
    wifi_ac3: str
    # Options for assigning Network Time Protocol (NTP) servers to DHCP clients.
    ntp_service: Literal["local", "default", "specify"]
    # NTP server 1.
    ntp_server1: str
    # NTP server 2.
    ntp_server2: str
    # NTP server 3.
    ntp_server3: str
    # Domain name suffix for the IP addresses that the DHCP server assigns to clients.
    domain: str
    # WINS server 1.
    wins_server1: str
    # WINS server 2.
    wins_server2: str
    # Default gateway IP address assigned by the DHCP server.
    default_gateway: str
    # IP address of a server (for example, a TFTP sever) that DHCP clients can downloa
    next_server: str
    # Netmask assigned by the DHCP server.
    netmask: str
    # DHCP server can assign IP configurations to clients connected to this interface.
    interface: str
    # DHCP IP range configuration.
    ip_range: list[str]  # Auto-flattened from member_table
    # Options for the DHCP server to set the client's time zone.
    timezone_option: Literal["disable", "default", "specify"]
    # Select the time zone to be assigned to DHCP clients.
    timezone: str
    # One or more hostnames or IP addresses of the TFTP servers in quotes separated by
    tftp_server: list[str]  # Auto-flattened from member_table
    # Name of the boot file on the TFTP server.
    filename: str
    # DHCP options.
    options: list[str]  # Auto-flattened from member_table
    # DHCP server can be a normal DHCP server or an IPsec DHCP server.
    server_type: Literal["regular", "ipsec"]
    # Method used to assign client IP.
    ip_mode: Literal["range", "usrgrp"]
    # Time in seconds to wait after a conflicted IP address is removed from the DHCP r
    conflicted_ip_timeout: int
    # DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable 
    ipsec_lease_hold: int
    # Enable/disable auto configuration.
    auto_configuration: Literal["disable", "enable"]
    # Enable/disable populating of DHCP server settings from FortiIPAM.
    dhcp_settings_from_fortiipam: Literal["disable", "enable"]
    # Enable/disable use of this DHCP server once this interface has been assigned an 
    auto_managed_status: Literal["disable", "enable"]
    # Enable/disable DDNS update for DHCP.
    ddns_update: Literal["disable", "enable"]
    # Enable/disable DDNS update override for DHCP.
    ddns_update_override: Literal["disable", "enable"]
    # DDNS server IP.
    ddns_server_ip: str
    # Zone of your domain name (ex. DDNS.com).
    ddns_zone: str
    # DDNS authentication mode.
    ddns_auth: Literal["disable", "tsig"]
    # DDNS update key name.
    ddns_keyname: str
    # DDNS update key (base 64 encoding).
    ddns_key: str
    # TTL.
    ddns_ttl: int
    # Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP re
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: list[str]  # Auto-flattened from member_table
    # Exclude one or more ranges of IP addresses from being assigned to clients.
    exclude_range: list[str]  # Auto-flattened from member_table
    # Enable/disable shared subnet.
    shared_subnet: Literal["disable", "enable"]
    # Relay agent IP.
    relay_agent: str
    # Options for the DHCP server to assign IP settings to specific MAC addresses.
    reserved_address: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Server:
    """
    Configure DHCP servers.
    
    Path: system/dhcp/server
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
    ) -> ServerObject: ...
    
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
    ) -> list[ServerObject]: ...
    
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
    ) -> ServerObject | list[ServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ServerObject: ...
    
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
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        mac_acl_default_action: Literal["assign", "block"] | None = ...,
        forticlient_on_net_status: Literal["disable", "enable"] | None = ...,
        dns_service: Literal["local", "default", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        wifi_ac_service: Literal["specify", "local"] | None = ...,
        wifi_ac1: str | None = ...,
        wifi_ac2: str | None = ...,
        wifi_ac3: str | None = ...,
        ntp_service: Literal["local", "default", "specify"] | None = ...,
        ntp_server1: str | None = ...,
        ntp_server2: str | None = ...,
        ntp_server3: str | None = ...,
        domain: str | None = ...,
        wins_server1: str | None = ...,
        wins_server2: str | None = ...,
        default_gateway: str | None = ...,
        next_server: str | None = ...,
        netmask: str | None = ...,
        interface: str | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        timezone_option: Literal["disable", "default", "specify"] | None = ...,
        timezone: str | None = ...,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        filename: str | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        server_type: Literal["regular", "ipsec"] | None = ...,
        ip_mode: Literal["range", "usrgrp"] | None = ...,
        conflicted_ip_timeout: int | None = ...,
        ipsec_lease_hold: int | None = ...,
        auto_configuration: Literal["disable", "enable"] | None = ...,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = ...,
        auto_managed_status: Literal["disable", "enable"] | None = ...,
        ddns_update: Literal["disable", "enable"] | None = ...,
        ddns_update_override: Literal["disable", "enable"] | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_zone: str | None = ...,
        ddns_auth: Literal["disable", "tsig"] | None = ...,
        ddns_keyname: str | None = ...,
        ddns_key: str | None = ...,
        ddns_ttl: int | None = ...,
        vci_match: Literal["disable", "enable"] | None = ...,
        vci_string: str | list[str] | list[dict[str, Any]] | None = ...,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        shared_subnet: Literal["disable", "enable"] | None = ...,
        relay_agent: str | None = ...,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Server",
    "ServerPayload",
    "ServerObject",
]