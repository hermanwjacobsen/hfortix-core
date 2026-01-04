from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExplicitPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/explicit payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExplicitPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the explicit Web proxy for HTTP and HTTPS ses
    secure_web_proxy: NotRequired[Literal["disable", "enable", "secure"]]  # Enable/disable/require the secure web proxy for HTTP and HTT
    ftp_over_http: NotRequired[Literal["enable", "disable"]]  # Enable to proxy FTP-over-HTTP sessions sent from a web brows
    socks: NotRequired[Literal["enable", "disable"]]  # Enable/disable the SOCKS proxy.
    http_incoming_port: NotRequired[str]  # Accept incoming HTTP requests on one or more ports (0 - 6553
    http_connection_mode: NotRequired[Literal["static", "multiplex", "serverpool"]]  # HTTP connection mode (default = static).
    https_incoming_port: NotRequired[str]  # Accept incoming HTTPS requests on one or more ports (0 - 655
    secure_web_proxy_cert: NotRequired[list[dict[str, Any]]]  # Name of certificates for secure web proxy.
    client_cert: NotRequired[Literal["disable", "enable"]]  # Enable/disable to request client certificate.
    user_agent_detect: NotRequired[Literal["disable", "enable"]]  # Enable/disable to detect device type by HTTP user-agent if n
    empty_cert_action: NotRequired[Literal["accept", "block", "accept-unmanageable"]]  # Action of an empty client certificate.
    ssl_dh_bits: NotRequired[Literal["768", "1024", "1536", "2048"]]  # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti
    ftp_incoming_port: NotRequired[str]  # Accept incoming FTP-over-HTTP requests on one or more ports 
    socks_incoming_port: NotRequired[str]  # Accept incoming SOCKS proxy requests on one or more ports (0
    incoming_ip: NotRequired[str]  # Restrict the explicit HTTP proxy to only accept sessions fro
    outgoing_ip: NotRequired[str]  # Outgoing HTTP requests will have this IP address as their so
    interface_select_method: NotRequired[Literal["sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    ipv6_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing an IPv6 web proxy destination in pol
    incoming_ip6: NotRequired[str]  # Restrict the explicit web proxy to only accept sessions from
    outgoing_ip6: NotRequired[str]  # Outgoing HTTP requests will leave this IPv6. Multiple interf
    strict_guest: NotRequired[Literal["enable", "disable"]]  # Enable/disable strict guest user checking by the explicit we
    pref_dns_result: NotRequired[Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"]]  # Prefer resolving addresses using the configured IPv4 or IPv6
    unknown_http_version: NotRequired[Literal["reject", "best-effort"]]  # How to handle HTTP sessions that do not comply with HTTP 0.9
    realm: str  # Authentication realm used to identify the explicit web proxy
    sec_default_action: NotRequired[Literal["accept", "deny"]]  # Accept or deny explicit web proxy sessions when no web proxy
    https_replacement_message: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending the client a replacement message for 
    message_upon_server_error: NotRequired[Literal["enable", "disable"]]  # Enable/disable displaying a replacement message when a serve
    pac_file_server_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable Proxy Auto-Configuration (PAC) for users of t
    pac_file_url: NotRequired[str]  # PAC file access URL.
    pac_file_server_port: NotRequired[str]  # Port number that PAC traffic from client web browsers uses t
    pac_file_through_https: NotRequired[Literal["enable", "disable"]]  # Enable/disable to get Proxy Auto-Configuration (PAC) through
    pac_file_name: str  # Pac file name.
    pac_file_data: NotRequired[str]  # PAC file contents enclosed in quotes (maximum of 256K bytes)
    pac_policy: NotRequired[list[dict[str, Any]]]  # PAC policies.
    ssl_algorithm: NotRequired[Literal["high", "medium", "low"]]  # Relative strength of encryption algorithms accepted in HTTPS
    trace_auth_no_rsp: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging timed-out authentication requests.


class Explicit:
    """
    Configure explicit Web proxy settings.
    
    Path: web_proxy/explicit
    Category: cmdb
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
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        secure_web_proxy: Literal["disable", "enable", "secure"] | None = ...,
        ftp_over_http: Literal["enable", "disable"] | None = ...,
        socks: Literal["enable", "disable"] | None = ...,
        http_incoming_port: str | None = ...,
        http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = ...,
        https_incoming_port: str | None = ...,
        secure_web_proxy_cert: list[dict[str, Any]] | None = ...,
        client_cert: Literal["disable", "enable"] | None = ...,
        user_agent_detect: Literal["disable", "enable"] | None = ...,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ftp_incoming_port: str | None = ...,
        socks_incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | None = ...,
        interface_select_method: Literal["sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        ipv6_status: Literal["enable", "disable"] | None = ...,
        incoming_ip6: str | None = ...,
        outgoing_ip6: str | None = ...,
        strict_guest: Literal["enable", "disable"] | None = ...,
        pref_dns_result: Literal["ipv4", "ipv6", "ipv4-strict", "ipv6-strict"] | None = ...,
        unknown_http_version: Literal["reject", "best-effort"] | None = ...,
        realm: str | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        https_replacement_message: Literal["enable", "disable"] | None = ...,
        message_upon_server_error: Literal["enable", "disable"] | None = ...,
        pac_file_server_status: Literal["enable", "disable"] | None = ...,
        pac_file_url: str | None = ...,
        pac_file_server_port: str | None = ...,
        pac_file_through_https: Literal["enable", "disable"] | None = ...,
        pac_file_name: str | None = ...,
        pac_file_data: str | None = ...,
        pac_policy: list[dict[str, Any]] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        trace_auth_no_rsp: Literal["enable", "disable"] | None = ...,
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
        payload_dict: ExplicitPayload | None = ...,
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


__all__ = [
    "Explicit",
    "ExplicitPayload",
]