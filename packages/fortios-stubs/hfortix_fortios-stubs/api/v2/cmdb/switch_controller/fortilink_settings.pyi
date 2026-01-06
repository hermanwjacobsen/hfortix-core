from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FortilinkSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/fortilink_settings payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: FortilinkSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiLink settings name.
    fortilink: NotRequired[str]  # FortiLink interface to which this fortilink-setting belongs.
    inactive_timer: NotRequired[int]  # Time interval(minutes) to be included in the inactive device
    link_down_flush: NotRequired[Literal[{"description": "Disable clearing NAC and dynamic devices on a switch port when link down event happens", "help": "Disable clearing NAC and dynamic devices on a switch port when link down event happens.", "label": "Disable", "name": "disable"}, {"description": "Enable clearing NAC and dynamic devices on a switch port when link down event happens", "help": "Enable clearing NAC and dynamic devices on a switch port when link down event happens.", "label": "Enable", "name": "enable"}]]  # Clear NAC and dynamic devices on switch ports on link down e
    access_vlan_mode: NotRequired[Literal[{"description": "Backward compatible behavior", "help": "Backward compatible behavior.", "label": "Legacy", "name": "legacy"}, {"description": "When connection to FortiGate is lost, traffic on the VLAN may continue directly between end points", "help": "When connection to FortiGate is lost, traffic on the VLAN may continue directly between end points.", "label": "Fail Open", "name": "fail-open"}, {"description": "When connection to FortiGate is lost, traffic between endpoints on the VLAN is blocked", "help": "When connection to FortiGate is lost, traffic between endpoints on the VLAN is blocked.", "label": "Fail Close", "name": "fail-close"}]]  # Intra VLAN traffic behavior with loss of connection to the F
    nac_ports: NotRequired[str]  # NAC specific configuration.


class FortilinkSettings:
    """
    Configure integrated FortiLink settings for FortiSwitch.
    
    Path: switch_controller/fortilink_settings
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
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal[{"description": "Disable clearing NAC and dynamic devices on a switch port when link down event happens", "help": "Disable clearing NAC and dynamic devices on a switch port when link down event happens.", "label": "Disable", "name": "disable"}, {"description": "Enable clearing NAC and dynamic devices on a switch port when link down event happens", "help": "Enable clearing NAC and dynamic devices on a switch port when link down event happens.", "label": "Enable", "name": "enable"}] | None = ...,
        access_vlan_mode: Literal[{"description": "Backward compatible behavior", "help": "Backward compatible behavior.", "label": "Legacy", "name": "legacy"}, {"description": "When connection to FortiGate is lost, traffic on the VLAN may continue directly between end points", "help": "When connection to FortiGate is lost, traffic on the VLAN may continue directly between end points.", "label": "Fail Open", "name": "fail-open"}, {"description": "When connection to FortiGate is lost, traffic between endpoints on the VLAN is blocked", "help": "When connection to FortiGate is lost, traffic between endpoints on the VLAN is blocked.", "label": "Fail Close", "name": "fail-close"}] | None = ...,
        nac_ports: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: FortilinkSettingsPayload | None = ...,
        name: str | None = ...,
        fortilink: str | None = ...,
        inactive_timer: int | None = ...,
        link_down_flush: Literal[{"description": "Disable clearing NAC and dynamic devices on a switch port when link down event happens", "help": "Disable clearing NAC and dynamic devices on a switch port when link down event happens.", "label": "Disable", "name": "disable"}, {"description": "Enable clearing NAC and dynamic devices on a switch port when link down event happens", "help": "Enable clearing NAC and dynamic devices on a switch port when link down event happens.", "label": "Enable", "name": "enable"}] | None = ...,
        access_vlan_mode: Literal[{"description": "Backward compatible behavior", "help": "Backward compatible behavior.", "label": "Legacy", "name": "legacy"}, {"description": "When connection to FortiGate is lost, traffic on the VLAN may continue directly between end points", "help": "When connection to FortiGate is lost, traffic on the VLAN may continue directly between end points.", "label": "Fail Open", "name": "fail-open"}, {"description": "When connection to FortiGate is lost, traffic between endpoints on the VLAN is blocked", "help": "When connection to FortiGate is lost, traffic between endpoints on the VLAN is blocked.", "label": "Fail Close", "name": "fail-close"}] | None = ...,
        nac_ports: str | None = ...,
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
        payload_dict: FortilinkSettingsPayload | None = ...,
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
    "FortilinkSettings",
    "FortilinkSettingsPayload",
]