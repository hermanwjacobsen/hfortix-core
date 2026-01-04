from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExtenderProfilePayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender_profile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExtenderProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiExtender profile name.
    id: NotRequired[int]  # ID.
    model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"]  # Model.
    extension: Literal["wan-extension", "lan-extension"]  # Extension option.
    allowaccess: NotRequired[Literal["ping", "telnet", "http", "https", "ssh", "snmp"]]  # Control management access to the managed extender. Separate 
    login_password_change: NotRequired[Literal["yes", "default", "no"]]  # Change or reset the administrator password of a managed exte
    login_password: str  # Set the managed extender's administrator password.
    enforce_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable/disable enforcement of bandwidth on LAN extension int
    bandwidth_limit: int  # FortiExtender LAN extension bandwidth limit (Mbps).
    cellular: str  # FortiExtender cellular configuration.
    wifi: NotRequired[str]  # FortiExtender Wi-Fi configuration.
    lan_extension: str  # FortiExtender LAN extension configuration.


class ExtenderProfile:
    """
    FortiExtender extender profile configuration.
    
    Path: extension_controller/extender_profile
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
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
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
        payload_dict: ExtenderProfilePayload | None = ...,
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