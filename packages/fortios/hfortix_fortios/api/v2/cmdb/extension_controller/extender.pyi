from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ExtenderPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ExtenderPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # FortiExtender entry name.
    id: str  # FortiExtender serial number.
    authorized: Literal["discovered", "disable", "enable"]  # FortiExtender Administration (enable or disable).
    ext_name: NotRequired[str]  # FortiExtender name.
    description: NotRequired[str]  # Description.
    vdom: NotRequired[int]  # VDOM.
    device_id: NotRequired[int]  # Device ID.
    extension_type: Literal["wan-extension", "lan-extension"]  # Extension type for this FortiExtender.
    profile: NotRequired[str]  # FortiExtender profile configuration.
    override_allowaccess: NotRequired[Literal["enable", "disable"]]  # Enable to override the extender profile management access co
    allowaccess: NotRequired[Literal["ping", "telnet", "http", "https", "ssh", "snmp"]]  # Control management access to the managed extender. Separate 
    override_login_password_change: NotRequired[Literal["enable", "disable"]]  # Enable to override the extender profile login-password (admi
    login_password_change: NotRequired[Literal["yes", "default", "no"]]  # Change or reset the administrator password of a managed exte
    login_password: str  # Set the managed extender's administrator password.
    override_enforce_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable to override the extender profile enforce-bandwidth se
    enforce_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable/disable enforcement of bandwidth on LAN extension int
    bandwidth_limit: int  # FortiExtender LAN extension bandwidth limit (Mbps).
    wan_extension: NotRequired[str]  # FortiExtender wan extension configuration.
    firmware_provision_latest: NotRequired[Literal["disable", "once"]]  # Enable/disable one-time automatic provisioning of the latest


class Extender:
    """
    Extender controller configuration.
    
    Path: extension_controller/extender
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
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
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
        payload_dict: ExtenderPayload | None = ...,
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