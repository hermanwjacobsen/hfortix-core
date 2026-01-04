from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SitTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/sit_tunnel payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SitTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Tunnel name.
    source: NotRequired[str]  # Source IP address of the tunnel.
    destination: str  # Destination IP address of the tunnel.
    ip6: NotRequired[str]  # IPv6 address of the tunnel.
    interface: NotRequired[str]  # Interface name.
    use_sdwan: NotRequired[Literal["disable", "enable"]]  # Enable/disable use of SD-WAN to reach remote gateway.
    auto_asic_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable tunnel ASIC offloading.


class SitTunnel:
    """
    Configure IPv6 tunnel over IPv4.
    
    Path: system/sit_tunnel
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
        payload_dict: SitTunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        ip6: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SitTunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        ip6: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal["disable", "enable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SitTunnelPayload | None = ...,
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