from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GreTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/gre_tunnel payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GreTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Tunnel name.
    interface: NotRequired[str]  # Interface name.
    ip_version: NotRequired[Literal["4", "6"]]  # IP version to use for VPN interface.
    remote_gw6: str  # IPv6 address of the remote gateway.
    local_gw6: str  # IPv6 address of the local gateway.
    remote_gw: str  # IP address of the remote gateway.
    local_gw: str  # IP address of the local gateway.
    use_sdwan: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of SD-WAN to reach remote gateway.
    sequence_number_transmission: NotRequired[Literal["disable", "enable"]]  # Enable/disable including of sequence numbers in transmitted 
    sequence_number_reception: NotRequired[Literal["disable", "enable"]]  # Enable/disable validating sequence numbers in received GRE p
    checksum_transmission: NotRequired[Literal["disable", "enable"]]  # Enable/disable including checksums in transmitted GRE packet
    checksum_reception: NotRequired[Literal["disable", "enable"]]  # Enable/disable validating checksums in received GRE packets.
    key_outbound: NotRequired[int]  # Include this key in transmitted GRE packets (0 - 4294967295)
    key_inbound: NotRequired[int]  # Require received GRE packets contain this key (0 - 429496729
    dscp_copying: NotRequired[Literal["disable", "enable"]]  # Enable/disable DSCP copying.
    diffservcode: NotRequired[str]  # DiffServ setting to be applied to GRE tunnel outer IP header
    keepalive_interval: NotRequired[int]  # Keepalive message interval (0 - 32767, 0 = disabled).
    keepalive_failtimes: NotRequired[int]  # Number of consecutive unreturned keepalive messages before a


class GreTunnel:
    """
    Configure GRE tunnel.
    
    Path: system/gre_tunnel
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
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GreTunnelPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        remote_gw6: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        sequence_number_transmission: Literal["disable", "enable"] | None = ...,
        sequence_number_reception: Literal["disable", "enable"] | None = ...,
        checksum_transmission: Literal["disable", "enable"] | None = ...,
        checksum_reception: Literal["disable", "enable"] | None = ...,
        key_outbound: int | None = ...,
        key_inbound: int | None = ...,
        dscp_copying: Literal["disable", "enable"] | None = ...,
        diffservcode: str | None = ...,
        keepalive_interval: int | None = ...,
        keepalive_failtimes: int | None = ...,
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
        payload_dict: GreTunnelPayload | None = ...,
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