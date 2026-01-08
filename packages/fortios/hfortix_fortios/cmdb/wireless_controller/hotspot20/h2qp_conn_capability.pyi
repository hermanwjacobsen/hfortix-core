from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class H2qpConnCapabilityPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/h2qp_conn_capability payload fields.
    
    Configure connection capability.
    
    **Usage:**
        payload: H2qpConnCapabilityPayload = {
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


class H2qpConnCapabilityObject(FortiObject[H2qpConnCapabilityPayload]):
    """Typed FortiObject for wireless_controller/hotspot20/h2qp_conn_capability with IDE autocomplete support."""
    
    # Connection capability name.
    name: str
    # Set ICMP port service status.
    icmp_port: Literal["closed", "open", "unknown"]
    # Set FTP port service status.
    ftp_port: Literal["closed", "open", "unknown"]
    # Set SSH port service status.
    ssh_port: Literal["closed", "open", "unknown"]
    # Set HTTP port service status.
    http_port: Literal["closed", "open", "unknown"]
    # Set TLS VPN (HTTPS) port service status.
    tls_port: Literal["closed", "open", "unknown"]
    # Set Point to Point Tunneling Protocol (PPTP) VPN port service status.
    pptp_vpn_port: Literal["closed", "open", "unknown"]
    # Set VoIP TCP port service status.
    voip_tcp_port: Literal["closed", "open", "unknown"]
    # Set VoIP UDP port service status.
    voip_udp_port: Literal["closed", "open", "unknown"]
    # Set IKEv2 port service for IPsec VPN status.
    ikev2_port: Literal["closed", "open", "unknown"]
    # Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status.
    ikev2_xx_port: Literal["closed", "open", "unknown"]
    # Set ESP port service (used by IPsec VPNs) status.
    esp_port: Literal["closed", "open", "unknown"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> H2qpConnCapabilityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class H2qpConnCapability:
    """
    Configure connection capability.
    
    Path: wireless_controller/hotspot20/h2qp_conn_capability
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
    ) -> H2qpConnCapabilityObject: ...
    
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
    ) -> list[H2qpConnCapabilityObject]: ...
    
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
    ) -> H2qpConnCapabilityObject | list[H2qpConnCapabilityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> H2qpConnCapabilityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> H2qpConnCapabilityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
    ) -> H2qpConnCapabilityObject: ...
    
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
        payload_dict: H2qpConnCapabilityPayload | None = ...,
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
    "H2qpConnCapability",
    "H2qpConnCapabilityPayload",
    "H2qpConnCapabilityObject",
]