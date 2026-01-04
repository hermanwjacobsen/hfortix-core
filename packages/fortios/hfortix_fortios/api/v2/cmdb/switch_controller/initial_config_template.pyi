from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InitialConfigTemplatePayload(TypedDict, total=False):
    """
    Type hints for switch-controller/initial_config_template payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InitialConfigTemplatePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Initial config template name.
    vlanid: int  # Unique VLAN ID.
    ip: NotRequired[str]  # Interface IPv4 address and subnet mask.
    allowaccess: NotRequired[Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm"]]  # Permitted types of management access to this interface.
    auto_ip: NotRequired[Literal["enable", "disable"]]  # Automatically allocate interface address and subnet block.
    dhcp_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable a DHCP server on this interface.


class InitialConfigTemplate:
    """
    Configure template for auto-generated VLANs.
    
    Path: switch-controller/initial_config_template
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
        payload_dict: InitialConfigTemplatePayload | None = ...,
        name: str | None = ...,
        vlanid: int | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm"] | None = ...,
        auto_ip: Literal["enable", "disable"] | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InitialConfigTemplatePayload | None = ...,
        name: str | None = ...,
        vlanid: int | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm"] | None = ...,
        auto_ip: Literal["enable", "disable"] | None = ...,
        dhcp_server: Literal["enable", "disable"] | None = ...,
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
        payload_dict: InitialConfigTemplatePayload | None = ...,
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