from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CentralManagementPayload(TypedDict, total=False):
    """
    Type hints for system/central_management payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: CentralManagementPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mode: NotRequired[Literal["normal", "backup"]]  # Central management mode.
    type: NotRequired[Literal["fortimanager", "fortiguard", "none"]]  # Central management type.
    fortigate_cloud_sso_default_profile: NotRequired[str]  # Override access profile.
    schedule_config_restore: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing the central management server to res
    schedule_script_restore: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing the central management server to res
    allow_push_configuration: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing the central management server to pus
    allow_push_firmware: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing the central management server to pus
    allow_remote_firmware_upgrade: NotRequired[Literal["enable", "disable"]]  # Enable/disable remotely upgrading the firmware on this Forti
    allow_monitor: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowing the central management server to rem
    serial_number: NotRequired[str]  # Serial number.
    fmg: NotRequired[str]  # IP address or FQDN of the FortiManager.
    fmg_source_ip: NotRequired[str]  # IPv4 source address that this FortiGate uses when communicat
    fmg_source_ip6: NotRequired[str]  # IPv6 source address that this FortiGate uses when communicat
    local_cert: NotRequired[str]  # Certificate to be used by FGFM protocol.
    ca_cert: NotRequired[str]  # CA certificate to be used by FGFM protocol.
    vdom: NotRequired[str]  # Virtual domain (VDOM) name to use when communicating with Fo
    server_list: NotRequired[list[dict[str, Any]]]  # Additional severs that the FortiGate can use for updates (fo
    fmg_update_port: NotRequired[Literal["8890", "443"]]  # Port used to communicate with FortiManager that is acting as
    fmg_update_http_header: NotRequired[Literal["enable", "disable"]]  # Enable/disable inclusion of HTTP header in update request.
    include_default_servers: NotRequired[Literal["enable", "disable"]]  # Enable/disable inclusion of public FortiGuard servers in the
    enc_algorithm: NotRequired[Literal["default", "high", "low"]]  # Encryption strength for communications between the FortiGate
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.


class CentralManagement:
    """
    Configure central management.
    
    Path: system/central_management
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
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: CentralManagementPayload | None = ...,
        mode: Literal["normal", "backup"] | None = ...,
        type: Literal["fortimanager", "fortiguard", "none"] | None = ...,
        fortigate_cloud_sso_default_profile: str | None = ...,
        schedule_config_restore: Literal["enable", "disable"] | None = ...,
        schedule_script_restore: Literal["enable", "disable"] | None = ...,
        allow_push_configuration: Literal["enable", "disable"] | None = ...,
        allow_push_firmware: Literal["enable", "disable"] | None = ...,
        allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        allow_monitor: Literal["enable", "disable"] | None = ...,
        serial_number: str | None = ...,
        fmg: str | None = ...,
        fmg_source_ip: str | None = ...,
        fmg_source_ip6: str | None = ...,
        local_cert: str | None = ...,
        ca_cert: str | None = ...,
        server_list: list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
        payload_dict: CentralManagementPayload | None = ...,
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
    "CentralManagement",
    "CentralManagementPayload",
]