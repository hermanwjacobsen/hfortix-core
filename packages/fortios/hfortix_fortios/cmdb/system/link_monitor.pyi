from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LinkMonitorPayload(TypedDict, total=False):
    """
    Type hints for system/link_monitor payload fields.
    
    Configure Link Health Monitor.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: class-id)
        - :class:`~.system.interface.InterfaceEndpoint` (via: srcintf)

    **Usage:**
        payload: LinkMonitorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Link monitor name.
    addr_mode: NotRequired[Literal["ipv4", "ipv6"]]  # Address mode (IPv4 or IPv6).
    srcintf: NotRequired[str]  # Interface that receives the traffic to be monitored.
    server_config: NotRequired[Literal["default", "individual"]]  # Mode of server configuration.
    server_type: NotRequired[Literal["static", "dynamic"]]  # Server type (static or dynamic).
    server: list[dict[str, Any]]  # IP address of the server(s) to be monitored.
    protocol: NotRequired[Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]]  # Protocols used to monitor the server.
    port: NotRequired[int]  # Port number of the traffic to be used to monitor the server.
    gateway_ip: NotRequired[str]  # Gateway IP address used to probe the server.
    gateway_ip6: NotRequired[str]  # Gateway IPv6 address used to probe the server.
    route: NotRequired[list[dict[str, Any]]]  # Subnet to monitor.
    source_ip: NotRequired[str]  # Source IP address used in packet to the server.
    source_ip6: NotRequired[str]  # Source IPv6 address used in packet to the server.
    http_get: str  # If you are monitoring an HTML server you can send an HTTP-GE
    http_agent: NotRequired[str]  # String in the http-agent field in the HTTP header.
    http_match: NotRequired[str]  # String that you expect to see in the HTTP-GET requests of th
    interval: NotRequired[int]  # Detection interval in milliseconds (20 - 3600 * 1000 msec, d
    probe_timeout: NotRequired[int]  # Time to wait before a probe packet is considered lost (20 - 
    failtime: NotRequired[int]  # Number of retry attempts before the server is considered dow
    recoverytime: NotRequired[int]  # Number of successful responses received before server is con
    probe_count: NotRequired[int]  # Number of most recent probes that should be used to calculat
    security_mode: NotRequired[Literal["none", "authentication"]]  # Twamp controller security mode.
    password: NotRequired[str]  # TWAMP controller password in authentication mode.
    packet_size: NotRequired[int]  # Packet size of a TWAMP test session (124/158 - 1024).
    ha_priority: NotRequired[int]  # HA election priority (1 - 50).
    fail_weight: NotRequired[int]  # Threshold weight to trigger link failure alert.
    update_cascade_interface: NotRequired[Literal["enable", "disable"]]  # Enable/disable update cascade interface.
    update_static_route: NotRequired[Literal["enable", "disable"]]  # Enable/disable updating the static route.
    update_policy_route: NotRequired[Literal["enable", "disable"]]  # Enable/disable updating the policy route.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this link monitor.
    diffservcode: NotRequired[str]  # Differentiated services code point (DSCP) in the IP header o
    class_id: NotRequired[int]  # Traffic class ID.
    service_detection: NotRequired[Literal["enable", "disable"]]  # Only use monitor to read quality values. If enabled, static 
    server_list: NotRequired[list[dict[str, Any]]]  # Servers for link-monitor to monitor.


class LinkMonitorObject(FortiObject[LinkMonitorPayload]):
    """Typed FortiObject for system/link_monitor with IDE autocomplete support."""
    
    # Link monitor name.
    name: str
    # Address mode (IPv4 or IPv6).
    addr_mode: Literal["ipv4", "ipv6"]
    # Interface that receives the traffic to be monitored.
    srcintf: str
    # Mode of server configuration.
    server_config: Literal["default", "individual"]
    # Server type (static or dynamic).
    server_type: Literal["static", "dynamic"]
    # IP address of the server(s) to be monitored.
    server: list[str]  # Auto-flattened from member_table
    # Protocols used to monitor the server.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]
    # Port number of the traffic to be used to monitor the server.
    port: int
    # Gateway IP address used to probe the server.
    gateway_ip: str
    # Gateway IPv6 address used to probe the server.
    gateway_ip6: str
    # Subnet to monitor.
    route: list[str]  # Auto-flattened from member_table
    # Source IP address used in packet to the server.
    source_ip: str
    # Source IPv6 address used in packet to the server.
    source_ip6: str
    # If you are monitoring an HTML server you can send an HTTP-GET request with a cus
    http_get: str
    # String in the http-agent field in the HTTP header.
    http_agent: str
    # String that you expect to see in the HTTP-GET requests of the traffic to be moni
    http_match: str
    # Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500).
    interval: int
    # Time to wait before a probe packet is considered lost (20 - 5000 msec, default =
    probe_timeout: int
    # Number of retry attempts before the server is considered down (1 - 3600, default
    failtime: int
    # Number of successful responses received before server is considered recovered (1
    recoverytime: int
    # Number of most recent probes that should be used to calculate latency and jitter
    probe_count: int
    # Twamp controller security mode.
    security_mode: Literal["none", "authentication"]
    # TWAMP controller password in authentication mode.
    password: str
    # Packet size of a TWAMP test session (124/158 - 1024).
    packet_size: int
    # HA election priority (1 - 50).
    ha_priority: int
    # Threshold weight to trigger link failure alert.
    fail_weight: int
    # Enable/disable update cascade interface.
    update_cascade_interface: Literal["enable", "disable"]
    # Enable/disable updating the static route.
    update_static_route: Literal["enable", "disable"]
    # Enable/disable updating the policy route.
    update_policy_route: Literal["enable", "disable"]
    # Enable/disable this link monitor.
    status: Literal["enable", "disable"]
    # Differentiated services code point (DSCP) in the IP header of the probe packet.
    diffservcode: str
    # Traffic class ID.
    class_id: int
    # Only use monitor to read quality values. If enabled, static routes and cascade i
    service_detection: Literal["enable", "disable"]
    # Servers for link-monitor to monitor.
    server_list: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LinkMonitorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LinkMonitor:
    """
    Configure Link Health Monitor.
    
    Path: system/link_monitor
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> list[LinkMonitorObject]: ...
    
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
    ) -> LinkMonitorObject | list[LinkMonitorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LinkMonitorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LinkMonitorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> LinkMonitorObject: ...
    
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
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "LinkMonitor",
    "LinkMonitorPayload",
    "LinkMonitorObject",
]