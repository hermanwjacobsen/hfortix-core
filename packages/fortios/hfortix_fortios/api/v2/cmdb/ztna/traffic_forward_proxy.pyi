from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class TrafficForwardProxyPayload(TypedDict, total=False):
    """
    Type hints for ztna/traffic_forward_proxy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: TrafficForwardProxyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # ZTNA proxy name.
    vip: NotRequired[str]  # Virtual IP name.
    host: NotRequired[str]  # Virtual or real host name.
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    log_blocked_traffic: NotRequired[Literal[{"description": "Do not log all traffic denied by this ZTNA web-proxy", "help": "Do not log all traffic denied by this ZTNA web-proxy.", "label": "Disable", "name": "disable"}, {"description": "Log all traffic denied by this ZTNA web-proxy", "help": "Log all traffic denied by this ZTNA web-proxy.", "label": "Enable", "name": "enable"}]]  # Enable/disable logging of blocked traffic.
    auth_portal: NotRequired[Literal[{"description": "Disable authentication portal", "help": "Disable authentication portal.", "label": "Disable", "name": "disable"}, {"description": "Enable authentication portal", "help": "Enable authentication portal.", "label": "Enable", "name": "enable"}]]  # Enable/disable authentication portal.
    auth_virtual_host: NotRequired[str]  # Virtual host for authentication portal.
    vip6: NotRequired[str]  # Virtual IPv6 name.


class TrafficForwardProxy:
    """
    Configure ZTNA traffic forward proxy.
    
    Path: ztna/traffic_forward_proxy
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
        payload_dict: TrafficForwardProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal[{"description": "Do not log all traffic denied by this ZTNA web-proxy", "help": "Do not log all traffic denied by this ZTNA web-proxy.", "label": "Disable", "name": "disable"}, {"description": "Log all traffic denied by this ZTNA web-proxy", "help": "Log all traffic denied by this ZTNA web-proxy.", "label": "Enable", "name": "enable"}] | None = ...,
        auth_portal: Literal[{"description": "Disable authentication portal", "help": "Disable authentication portal.", "label": "Disable", "name": "disable"}, {"description": "Enable authentication portal", "help": "Enable authentication portal.", "label": "Enable", "name": "enable"}] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: TrafficForwardProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal[{"description": "Do not log all traffic denied by this ZTNA web-proxy", "help": "Do not log all traffic denied by this ZTNA web-proxy.", "label": "Disable", "name": "disable"}, {"description": "Log all traffic denied by this ZTNA web-proxy", "help": "Log all traffic denied by this ZTNA web-proxy.", "label": "Enable", "name": "enable"}] | None = ...,
        auth_portal: Literal[{"description": "Disable authentication portal", "help": "Disable authentication portal.", "label": "Disable", "name": "disable"}, {"description": "Enable authentication portal", "help": "Enable authentication portal.", "label": "Enable", "name": "enable"}] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
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
        payload_dict: TrafficForwardProxyPayload | None = ...,
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
    "TrafficForwardProxy",
    "TrafficForwardProxyPayload",
]