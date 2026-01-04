from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GlobalSettingPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/global_setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GlobalSettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mac_aging_interval: NotRequired[int]  # Time after which an inactive MAC is aged out (10 - 1000000 s
    https_image_push: NotRequired[Literal["enable", "disable"]]  # Enable/disable image push to FortiSwitch using HTTPS.
    vlan_all_mode: NotRequired[Literal["all", "defined"]]  # VLAN configuration mode, user-defined-vlans or all-possible-
    vlan_optimization: NotRequired[Literal["prune", "configured", "none"]]  # FortiLink VLAN optimization.
    vlan_identity: NotRequired[Literal["description", "name"]]  # Identity of the VLAN. Commonly used for RADIUS Tunnel-Privat
    disable_discovery: NotRequired[list[dict[str, Any]]]  # Prevent this FortiSwitch from discovering.
    mac_retention_period: NotRequired[int]  # Time in hours after which an inactive MAC is removed from cl
    default_virtual_switch_vlan: NotRequired[str]  # Default VLAN for ports when added to the virtual-switch.
    dhcp_server_access_list: NotRequired[Literal["enable", "disable"]]  # Enable/disable DHCP snooping server access list.
    dhcp_option82_format: NotRequired[Literal["ascii", "legacy"]]  # DHCP option-82 format string.
    dhcp_option82_circuit_id: NotRequired[Literal["intfname", "vlan", "hostname", "mode", "description"]]  # List the parameters to be included to inform about client id
    dhcp_option82_remote_id: NotRequired[Literal["mac", "hostname", "ip"]]  # List the parameters to be included to inform about client id
    dhcp_snoop_client_req: NotRequired[Literal["drop-untrusted", "forward-untrusted"]]  # Client DHCP packet broadcast mode.
    dhcp_snoop_client_db_exp: NotRequired[int]  # Expiry time for DHCP snooping server database entries (300 -
    dhcp_snoop_db_per_port_learn_limit: NotRequired[int]  # Per Interface dhcp-server entries learn limit (0 - 1024, def
    log_mac_limit_violations: NotRequired[Literal["enable", "disable"]]  # Enable/disable logs for Learning Limit Violations.
    mac_violation_timer: NotRequired[int]  # Set timeout for Learning Limit Violations (0 = disabled).
    sn_dns_resolution: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS resolution of the FortiSwitch unit's IP a
    mac_event_logging: NotRequired[Literal["enable", "disable"]]  # Enable/disable MAC address event logging.
    bounce_quarantined_link: NotRequired[Literal["disable", "enable"]]  # Enable/disable bouncing (administratively bring the link dow
    quarantine_mode: NotRequired[Literal["by-vlan", "by-redirect"]]  # Quarantine mode.
    update_user_device: NotRequired[Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"]]  # Control which sources update the device user list.
    custom_command: NotRequired[list[dict[str, Any]]]  # List of custom commands to be pushed to all FortiSwitches in
    fips_enforce: NotRequired[Literal["disable", "enable"]]  # Enable/disable enforcement of FIPS on managed FortiSwitch de
    firmware_provision_on_authorization: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic provisioning of latest firmware on 
    switch_on_deauth: NotRequired[Literal["no-op", "factory-reset"]]  # No-operation/Factory-reset the managed FortiSwitch on deauth
    firewall_auth_user_hold_period: NotRequired[int]  # Time period in minutes to hold firewall authenticated MAC us


class GlobalSetting:
    """
    Configure FortiSwitch global settings.
    
    Path: switch_controller/global_setting
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
        payload_dict: GlobalSettingPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GlobalSettingPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
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
        payload_dict: GlobalSettingPayload | None = ...,
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