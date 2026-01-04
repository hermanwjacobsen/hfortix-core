from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SwitchInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/switch_interface payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SwitchInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Interface name (name cannot be in use by any other interface
    vdom: str  # VDOM that the software switch belongs to.
    span_dest_port: NotRequired[str]  # SPAN destination port name. All traffic on the SPAN source p
    span_source_port: NotRequired[list[dict[str, Any]]]  # Physical interface name. Port spanning echoes all traffic on
    member: NotRequired[list[dict[str, Any]]]  # Names of the interfaces that belong to the virtual switch.
    type: NotRequired[Literal["switch", "hub"]]  # Type of switch based on functionality: switch for normal fun
    intra_switch_policy: NotRequired[Literal["implicit", "explicit"]]  # Allow any traffic between switch interfaces or require firew
    mac_ttl: NotRequired[int]  # Duration for which MAC addresses are held in the ARP table (
    span: NotRequired[Literal["disable", "enable"]]  # Enable/disable port spanning. Port spanning echoes traffic r
    span_direction: NotRequired[Literal["rx", "tx", "both"]]  # The direction in which the SPAN port operates, either: rx, t


class SwitchInterface:
    """
    Configure software switch interfaces by grouping physical and WiFi interfaces.
    
    Path: system/switch_interface
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
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: list[dict[str, Any]] | None = ...,
        member: list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SwitchInterfacePayload | None = ...,
        name: str | None = ...,
        span_dest_port: str | None = ...,
        span_source_port: list[dict[str, Any]] | None = ...,
        member: list[dict[str, Any]] | None = ...,
        type: Literal["switch", "hub"] | None = ...,
        intra_switch_policy: Literal["implicit", "explicit"] | None = ...,
        mac_ttl: int | None = ...,
        span: Literal["disable", "enable"] | None = ...,
        span_direction: Literal["rx", "tx", "both"] | None = ...,
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
        payload_dict: SwitchInterfacePayload | None = ...,
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