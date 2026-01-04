from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LinkMonitorPayload(TypedDict, total=False):
    """
    Type hints for system/link_monitor payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class LinkMonitor:
    """
    Configure Link Health Monitor.
    
    Path: system/link_monitor
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
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
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
        payload_dict: LinkMonitorPayload | None = ...,
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