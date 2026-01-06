from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class TrafficSnifferPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/traffic_sniffer payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: TrafficSnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mode: NotRequired[Literal[{"description": "Mirror traffic using a GRE tunnel", "help": "Mirror traffic using a GRE tunnel.", "label": "Erspan Auto", "name": "erspan-auto"}, {"description": "Mirror traffic on a layer2 VLAN", "help": "Mirror traffic on a layer2 VLAN.", "label": "Rspan", "name": "rspan"}, {"description": "Disable traffic mirroring (sniffer)", "help": "Disable traffic mirroring (sniffer).", "label": "None", "name": "none"}]]  # Configure traffic sniffer mode.
    erspan_ip: NotRequired[str]  # Configure ERSPAN collector IP address.
    target_mac: NotRequired[list[dict[str, Any]]]  # Sniffer MACs to filter.
    target_ip: NotRequired[list[dict[str, Any]]]  # Sniffer IPs to filter.
    target_port: NotRequired[list[dict[str, Any]]]  # Sniffer ports to filter.


class TrafficSniffer:
    """
    Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    
    Path: switch_controller/traffic_sniffer
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
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal[{"description": "Mirror traffic using a GRE tunnel", "help": "Mirror traffic using a GRE tunnel.", "label": "Erspan Auto", "name": "erspan-auto"}, {"description": "Mirror traffic on a layer2 VLAN", "help": "Mirror traffic on a layer2 VLAN.", "label": "Rspan", "name": "rspan"}, {"description": "Disable traffic mirroring (sniffer)", "help": "Disable traffic mirroring (sniffer).", "label": "None", "name": "none"}] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: list[dict[str, Any]] | None = ...,
        target_ip: list[dict[str, Any]] | None = ...,
        target_port: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal[{"description": "Mirror traffic using a GRE tunnel", "help": "Mirror traffic using a GRE tunnel.", "label": "Erspan Auto", "name": "erspan-auto"}, {"description": "Mirror traffic on a layer2 VLAN", "help": "Mirror traffic on a layer2 VLAN.", "label": "Rspan", "name": "rspan"}, {"description": "Disable traffic mirroring (sniffer)", "help": "Disable traffic mirroring (sniffer).", "label": "None", "name": "none"}] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: list[dict[str, Any]] | None = ...,
        target_ip: list[dict[str, Any]] | None = ...,
        target_port: list[dict[str, Any]] | None = ...,
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
        payload_dict: TrafficSnifferPayload | None = ...,
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
    "TrafficSniffer",
    "TrafficSnifferPayload",
]