from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Ipv6TunnelPayload(TypedDict, total=False):
    """
    Type hints for system/ipv6_tunnel payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Ipv6TunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IPv6 tunnel name.
    source: NotRequired[str]  # Local IPv6 address of the tunnel.
    destination: str  # Remote IPv6 address of the tunnel.
    interface: NotRequired[str]  # Interface name.
    use_sdwan: NotRequired[Literal[{"description": "Disable use of SD-WAN to reach remote gateway", "help": "Disable use of SD-WAN to reach remote gateway.", "label": "Disable", "name": "disable"}, {"description": "Enable use of SD-WAN to reach remote gateway", "help": "Enable use of SD-WAN to reach remote gateway.", "label": "Enable", "name": "enable"}]]  # Enable/disable use of SD-WAN to reach remote gateway.
    auto_asic_offload: NotRequired[Literal[{"description": "Enable auto ASIC offloading", "help": "Enable auto ASIC offloading.", "label": "Enable", "name": "enable"}, {"description": "Disable ASIC offloading", "help": "Disable ASIC offloading.", "label": "Disable", "name": "disable"}]]  # Enable/disable tunnel ASIC offloading.


class Ipv6Tunnel:
    """
    Configure IPv6/IPv4 in IPv6 tunnel.
    
    Path: system/ipv6_tunnel
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
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal[{"description": "Disable use of SD-WAN to reach remote gateway", "help": "Disable use of SD-WAN to reach remote gateway.", "label": "Disable", "name": "disable"}, {"description": "Enable use of SD-WAN to reach remote gateway", "help": "Enable use of SD-WAN to reach remote gateway.", "label": "Enable", "name": "enable"}] | None = ...,
        auto_asic_offload: Literal[{"description": "Enable auto ASIC offloading", "help": "Enable auto ASIC offloading.", "label": "Enable", "name": "enable"}, {"description": "Disable ASIC offloading", "help": "Disable ASIC offloading.", "label": "Disable", "name": "disable"}] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Ipv6TunnelPayload | None = ...,
        name: str | None = ...,
        source: str | None = ...,
        destination: str | None = ...,
        interface: str | None = ...,
        use_sdwan: Literal[{"description": "Disable use of SD-WAN to reach remote gateway", "help": "Disable use of SD-WAN to reach remote gateway.", "label": "Disable", "name": "disable"}, {"description": "Enable use of SD-WAN to reach remote gateway", "help": "Enable use of SD-WAN to reach remote gateway.", "label": "Enable", "name": "enable"}] | None = ...,
        auto_asic_offload: Literal[{"description": "Enable auto ASIC offloading", "help": "Enable auto ASIC offloading.", "label": "Enable", "name": "enable"}, {"description": "Disable ASIC offloading", "help": "Disable ASIC offloading.", "label": "Disable", "name": "disable"}] | None = ...,
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
        payload_dict: Ipv6TunnelPayload | None = ...,
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
    "Ipv6Tunnel",
    "Ipv6TunnelPayload",
]