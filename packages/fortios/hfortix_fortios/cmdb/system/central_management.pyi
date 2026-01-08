from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class CentralManagementPayload(TypedDict, total=False):
    """
    Type hints for system/central_management payload fields.
    
    Configure central management.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: ca-cert)
        - :class:`~.certificate.local.LocalEndpoint` (via: local-cert)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: fortigate-cloud-sso-default-profile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: CentralManagementPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mode: NotRequired[Literal["normal", "backup"]]  # Central management mode.
    type: NotRequired[Literal["fortimanager", "fortiguard", "none"]]  # Central management type.
    fortigate_cloud_sso_default_profile: NotRequired[str]  # Override access profile. Permission is set to read-only with
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


class CentralManagementObject(FortiObject[CentralManagementPayload]):
    """Typed FortiObject for system/central_management with IDE autocomplete support."""
    
    # Central management mode.
    mode: Literal["normal", "backup"]
    # Central management type.
    type: Literal["fortimanager", "fortiguard", "none"]
    # Override access profile. Permission is set to read-only without a FortiGate Clou
    fortigate_cloud_sso_default_profile: str
    # Enable/disable allowing the central management server to restore the configurati
    schedule_config_restore: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to restore the scripts sto
    schedule_script_restore: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to push configuration chan
    allow_push_configuration: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to push firmware updates t
    allow_push_firmware: Literal["enable", "disable"]
    # Enable/disable remotely upgrading the firmware on this FortiGate from the centra
    allow_remote_firmware_upgrade: Literal["enable", "disable"]
    # Enable/disable allowing the central management server to remotely monitor this F
    allow_monitor: Literal["enable", "disable"]
    # Serial number.
    serial_number: str
    # IP address or FQDN of the FortiManager.
    fmg: str
    # IPv4 source address that this FortiGate uses when communicating with FortiManage
    fmg_source_ip: str
    # IPv6 source address that this FortiGate uses when communicating with FortiManage
    fmg_source_ip6: str
    # Certificate to be used by FGFM protocol.
    local_cert: str
    # CA certificate to be used by FGFM protocol.
    ca_cert: str
    # Virtual domain (VDOM) name to use when communicating with FortiManager.
    vdom: str
    # Additional severs that the FortiGate can use for updates (for AV, IPS, updates) 
    server_list: list[str]  # Auto-flattened from member_table
    # Port used to communicate with FortiManager that is acting as a FortiGuard update
    fmg_update_port: Literal["8890", "443"]
    # Enable/disable inclusion of HTTP header in update request.
    fmg_update_http_header: Literal["enable", "disable"]
    # Enable/disable inclusion of public FortiGuard servers in the override server lis
    include_default_servers: Literal["enable", "disable"]
    # Encryption strength for communications between the FortiGate and central managem
    enc_algorithm: Literal["default", "high", "low"]
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CentralManagementPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class CentralManagement:
    """
    Configure central management.
    
    Path: system/central_management
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> CentralManagementObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> CentralManagementObject: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> CentralManagementObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralManagementObject: ...
    
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
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
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        fmg_update_port: Literal["8890", "443"] | None = ...,
        fmg_update_http_header: Literal["enable", "disable"] | None = ...,
        include_default_servers: Literal["enable", "disable"] | None = ...,
        enc_algorithm: Literal["default", "high", "low"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "CentralManagementObject",
]