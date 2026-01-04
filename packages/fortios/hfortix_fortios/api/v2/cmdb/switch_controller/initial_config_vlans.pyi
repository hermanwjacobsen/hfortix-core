from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InitialConfigVlansPayload(TypedDict, total=False):
    """
    Type hints for switch-controller/initial_config_vlans payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InitialConfigVlansPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    optional_vlans: NotRequired[Literal["enable", "disable"]]  # Auto-generate pre-configured VLANs upon switch discovery.
    default_vlan: NotRequired[str]  # Default VLAN (native) assigned to all switch ports upon disc
    quarantine: NotRequired[str]  # VLAN for quarantined traffic.
    rspan: NotRequired[str]  # VLAN for RSPAN/ERSPAN mirrored traffic.
    voice: NotRequired[str]  # VLAN dedicated for voice devices.
    video: NotRequired[str]  # VLAN dedicated for video devices.
    nac: NotRequired[str]  # VLAN for NAC onboarding devices.
    nac_segment: NotRequired[str]  # VLAN for NAC segment primary interface.


class InitialConfigVlans:
    """
    Configure initial template for auto-generated VLAN interfaces.
    
    Path: switch-controller/initial_config_vlans
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
        payload_dict: InitialConfigVlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InitialConfigVlansPayload | None = ...,
        optional_vlans: Literal["enable", "disable"] | None = ...,
        default_vlan: str | None = ...,
        quarantine: str | None = ...,
        rspan: str | None = ...,
        voice: str | None = ...,
        video: str | None = ...,
        nac: str | None = ...,
        nac_segment: str | None = ...,
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
        payload_dict: InitialConfigVlansPayload | None = ...,
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