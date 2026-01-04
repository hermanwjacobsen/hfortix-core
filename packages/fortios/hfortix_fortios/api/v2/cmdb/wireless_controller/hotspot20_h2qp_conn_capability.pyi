from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Hotspot20H2qpConnCapabilityPayload(TypedDict, total=False):
    """
    Type hints for wireless-controller/hotspot20_h2qp_conn_capability payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Hotspot20H2qpConnCapabilityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Connection capability name.
    icmp_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set ICMP port service status.
    ftp_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set FTP port service status.
    ssh_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set SSH port service status.
    http_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set HTTP port service status.
    tls_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set TLS VPN (HTTPS) port service status.
    pptp_vpn_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set Point to Point Tunneling Protocol (PPTP) VPN port servic
    voip_tcp_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set VoIP TCP port service status.
    voip_udp_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set VoIP UDP port service status.
    ikev2_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set IKEv2 port service for IPsec VPN status.
    ikev2_xx_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN)
    esp_port: NotRequired[Literal["closed", "open", "unknown"]]  # Set ESP port service (used by IPsec VPNs) status.


class Hotspot20H2qpConnCapability:
    """
    Configure connection capability.
    
    Path: wireless-controller/hotspot20_h2qp_conn_capability
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
        payload_dict: Hotspot20H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Hotspot20H2qpConnCapabilityPayload | None = ...,
        name: str | None = ...,
        icmp_port: Literal["closed", "open", "unknown"] | None = ...,
        ftp_port: Literal["closed", "open", "unknown"] | None = ...,
        ssh_port: Literal["closed", "open", "unknown"] | None = ...,
        http_port: Literal["closed", "open", "unknown"] | None = ...,
        tls_port: Literal["closed", "open", "unknown"] | None = ...,
        pptp_vpn_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_tcp_port: Literal["closed", "open", "unknown"] | None = ...,
        voip_udp_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_port: Literal["closed", "open", "unknown"] | None = ...,
        ikev2_xx_port: Literal["closed", "open", "unknown"] | None = ...,
        esp_port: Literal["closed", "open", "unknown"] | None = ...,
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
        payload_dict: Hotspot20H2qpConnCapabilityPayload | None = ...,
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