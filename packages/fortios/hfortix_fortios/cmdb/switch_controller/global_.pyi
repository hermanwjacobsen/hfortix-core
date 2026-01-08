from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/global_ payload fields.
    
    Configure FortiSwitch global settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: default-virtual-switch-vlan)

    **Usage:**
        payload: GlobalPayload = {
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


class GlobalObject(FortiObject[GlobalPayload]):
    """Typed FortiObject for switch_controller/global_ with IDE autocomplete support."""
    
    # Time after which an inactive MAC is aged out (10 - 1000000 sec, default = 300, 0
    mac_aging_interval: int
    # Enable/disable image push to FortiSwitch using HTTPS.
    https_image_push: Literal["enable", "disable"]
    # VLAN configuration mode, user-defined-vlans or all-possible-vlans.
    vlan_all_mode: Literal["all", "defined"]
    # FortiLink VLAN optimization.
    vlan_optimization: Literal["prune", "configured", "none"]
    # Identity of the VLAN. Commonly used for RADIUS Tunnel-Private-Group-Id.
    vlan_identity: Literal["description", "name"]
    # Prevent this FortiSwitch from discovering.
    disable_discovery: list[str]  # Auto-flattened from member_table
    # Time in hours after which an inactive MAC is removed from client DB (0 = aged ou
    mac_retention_period: int
    # Default VLAN for ports when added to the virtual-switch.
    default_virtual_switch_vlan: str
    # Enable/disable DHCP snooping server access list.
    dhcp_server_access_list: Literal["enable", "disable"]
    # DHCP option-82 format string.
    dhcp_option82_format: Literal["ascii", "legacy"]
    # List the parameters to be included to inform about client identification.
    dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"]
    # List the parameters to be included to inform about client identification.
    dhcp_option82_remote_id: Literal["mac", "hostname", "ip"]
    # Client DHCP packet broadcast mode.
    dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"]
    # Expiry time for DHCP snooping server database entries (300 - 259200 sec, default
    dhcp_snoop_client_db_exp: int
    # Per Interface dhcp-server entries learn limit (0 - 1024, default = 64).
    dhcp_snoop_db_per_port_learn_limit: int
    # Enable/disable logs for Learning Limit Violations.
    log_mac_limit_violations: Literal["enable", "disable"]
    # Set timeout for Learning Limit Violations (0 = disabled).
    mac_violation_timer: int
    # Enable/disable DNS resolution of the FortiSwitch unit's IP address with switch n
    sn_dns_resolution: Literal["enable", "disable"]
    # Enable/disable MAC address event logging.
    mac_event_logging: Literal["enable", "disable"]
    # Enable/disable bouncing (administratively bring the link down, up) of a switch p
    bounce_quarantined_link: Literal["disable", "enable"]
    # Quarantine mode.
    quarantine_mode: Literal["by-vlan", "by-redirect"]
    # Control which sources update the device user list.
    update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"]
    # List of custom commands to be pushed to all FortiSwitches in the VDOM.
    custom_command: list[str]  # Auto-flattened from member_table
    # Enable/disable enforcement of FIPS on managed FortiSwitch devices.
    fips_enforce: Literal["disable", "enable"]
    # Enable/disable automatic provisioning of latest firmware on authorization.
    firmware_provision_on_authorization: Literal["enable", "disable"]
    # No-operation/Factory-reset the managed FortiSwitch on deauthorization.
    switch_on_deauth: Literal["no-op", "factory-reset"]
    # Time period in minutes to hold firewall authenticated MAC users (5 - 1440, defau
    firewall_auth_user_hold_period: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure FortiSwitch global settings.
    
    Path: switch_controller/global_
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
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
        payload_dict: GlobalPayload | None = ...,
        mac_aging_interval: int | None = ...,
        https_image_push: Literal["enable", "disable"] | None = ...,
        vlan_all_mode: Literal["all", "defined"] | None = ...,
        vlan_optimization: Literal["prune", "configured", "none"] | None = ...,
        vlan_identity: Literal["description", "name"] | None = ...,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = ...,
        mac_retention_period: int | None = ...,
        default_virtual_switch_vlan: str | None = ...,
        dhcp_server_access_list: Literal["enable", "disable"] | None = ...,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = ...,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = ...,
        dhcp_snoop_client_db_exp: int | None = ...,
        dhcp_snoop_db_per_port_learn_limit: int | None = ...,
        log_mac_limit_violations: Literal["enable", "disable"] | None = ...,
        mac_violation_timer: int | None = ...,
        sn_dns_resolution: Literal["enable", "disable"] | None = ...,
        mac_event_logging: Literal["enable", "disable"] | None = ...,
        bounce_quarantined_link: Literal["disable", "enable"] | None = ...,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = ...,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        fips_enforce: Literal["disable", "enable"] | None = ...,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = ...,
        firewall_auth_user_hold_period: int | None = ...,
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
    "Global",
    "GlobalPayload",
    "GlobalObject",
]