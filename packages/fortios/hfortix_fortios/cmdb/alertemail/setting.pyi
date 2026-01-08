from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for alertemail/setting payload fields.
    
    Configure alert email settings.
    
    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    username: NotRequired[str]  # Name that appears in the From: field of alert emails (max. 6
    mailto1: NotRequired[str]  # Email address to send alert email to (usually a system admin
    mailto2: NotRequired[str]  # Optional second email address to send alert email to (max. 6
    mailto3: NotRequired[str]  # Optional third email address to send alert email to (max. 63
    filter_mode: NotRequired[Literal["category", "threshold"]]  # How to filter log messages that are sent to alert emails.
    email_interval: NotRequired[int]  # Interval between sending alert emails (1 - 99999 min, defaul
    IPS_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPS logs in alert email.
    firewall_authentication_failure_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable firewall authentication failure logs in alert
    HA_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable HA logs in alert email.
    IPsec_errors_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPsec error logs in alert email.
    FDS_update_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard update logs in alert email.
    PPP_errors_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable PPP error logs in alert email.
    sslvpn_authentication_errors_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable Agentless VPN authentication error logs in al
    antivirus_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable antivirus logs in alert email.
    webfilter_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable web filter logs in alert email.
    configuration_changes_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable configuration change logs in alert email.
    violation_traffic_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable violation traffic logs in alert email.
    admin_login_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable administrator login/logout logs in alert emai
    FDS_license_expiring_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard license expiration warnings in ale
    log_disk_usage_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable disk usage warnings in alert email.
    fortiguard_log_quota_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiCloud log quota warnings in alert email.
    amc_interface_bypass_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable Fortinet Advanced Mezzanine Card (AMC) interf
    FIPS_CC_errors: NotRequired[Literal["enable", "disable"]]  # Enable/disable FIPS and Common Criteria error logs in alert 
    FSSO_disconnect_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of FSSO collector agent disconnect.
    ssh_logs: NotRequired[Literal["enable", "disable"]]  # Enable/disable SSH logs in alert email.
    local_disk_usage: NotRequired[int]  # Disk usage percentage at which to send alert email (1 - 99 p
    emergency_interval: NotRequired[int]  # Emergency alert interval in minutes.
    alert_interval: NotRequired[int]  # Alert alert interval in minutes.
    critical_interval: NotRequired[int]  # Critical alert interval in minutes.
    error_interval: NotRequired[int]  # Error alert interval in minutes.
    warning_interval: NotRequired[int]  # Warning alert interval in minutes.
    notification_interval: NotRequired[int]  # Notification alert interval in minutes.
    information_interval: NotRequired[int]  # Information alert interval in minutes.
    debug_interval: NotRequired[int]  # Debug alert interval in minutes.
    severity: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log.


class SettingObject(FortiObject[SettingPayload]):
    """Typed FortiObject for alertemail/setting with IDE autocomplete support."""
    
    # Name that appears in the From: field of alert emails (max. 63 characters).
    username: str
    # Email address to send alert email to (usually a system administrator) (max. 63 c
    mailto1: str
    # Optional second email address to send alert email to (max. 63 characters).
    mailto2: str
    # Optional third email address to send alert email to (max. 63 characters).
    mailto3: str
    # How to filter log messages that are sent to alert emails.
    filter_mode: Literal["category", "threshold"]
    # Interval between sending alert emails (1 - 99999 min, default = 5).
    email_interval: int
    # Enable/disable IPS logs in alert email.
    IPS_logs: Literal["enable", "disable"]
    # Enable/disable firewall authentication failure logs in alert email.
    firewall_authentication_failure_logs: Literal["enable", "disable"]
    # Enable/disable HA logs in alert email.
    HA_logs: Literal["enable", "disable"]
    # Enable/disable IPsec error logs in alert email.
    IPsec_errors_logs: Literal["enable", "disable"]
    # Enable/disable FortiGuard update logs in alert email.
    FDS_update_logs: Literal["enable", "disable"]
    # Enable/disable PPP error logs in alert email.
    PPP_errors_logs: Literal["enable", "disable"]
    # Enable/disable Agentless VPN authentication error logs in alert email.
    sslvpn_authentication_errors_logs: Literal["enable", "disable"]
    # Enable/disable antivirus logs in alert email.
    antivirus_logs: Literal["enable", "disable"]
    # Enable/disable web filter logs in alert email.
    webfilter_logs: Literal["enable", "disable"]
    # Enable/disable configuration change logs in alert email.
    configuration_changes_logs: Literal["enable", "disable"]
    # Enable/disable violation traffic logs in alert email.
    violation_traffic_logs: Literal["enable", "disable"]
    # Enable/disable administrator login/logout logs in alert email.
    admin_login_logs: Literal["enable", "disable"]
    # Enable/disable FortiGuard license expiration warnings in alert email.
    FDS_license_expiring_warning: Literal["enable", "disable"]
    # Enable/disable disk usage warnings in alert email.
    log_disk_usage_warning: Literal["enable", "disable"]
    # Enable/disable FortiCloud log quota warnings in alert email.
    fortiguard_log_quota_warning: Literal["enable", "disable"]
    # Enable/disable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs
    amc_interface_bypass_mode: Literal["enable", "disable"]
    # Enable/disable FIPS and Common Criteria error logs in alert email.
    FIPS_CC_errors: Literal["enable", "disable"]
    # Enable/disable logging of FSSO collector agent disconnect.
    FSSO_disconnect_logs: Literal["enable", "disable"]
    # Enable/disable SSH logs in alert email.
    ssh_logs: Literal["enable", "disable"]
    # Disk usage percentage at which to send alert email (1 - 99 percent, default = 75
    local_disk_usage: int
    # Emergency alert interval in minutes.
    emergency_interval: int
    # Alert alert interval in minutes.
    alert_interval: int
    # Critical alert interval in minutes.
    critical_interval: int
    # Error alert interval in minutes.
    error_interval: int
    # Warning alert interval in minutes.
    warning_interval: int
    # Notification alert interval in minutes.
    notification_interval: int
    # Information alert interval in minutes.
    information_interval: int
    # Debug alert interval in minutes.
    debug_interval: int
    # Lowest severity level to log.
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Setting:
    """
    Configure alert email settings.
    
    Path: alertemail/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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
        payload_dict: SettingPayload | None = ...,
        username: str | None = ...,
        mailto1: str | None = ...,
        mailto2: str | None = ...,
        mailto3: str | None = ...,
        filter_mode: Literal["category", "threshold"] | None = ...,
        email_interval: int | None = ...,
        IPS_logs: Literal["enable", "disable"] | None = ...,
        firewall_authentication_failure_logs: Literal["enable", "disable"] | None = ...,
        HA_logs: Literal["enable", "disable"] | None = ...,
        IPsec_errors_logs: Literal["enable", "disable"] | None = ...,
        FDS_update_logs: Literal["enable", "disable"] | None = ...,
        PPP_errors_logs: Literal["enable", "disable"] | None = ...,
        sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = ...,
        antivirus_logs: Literal["enable", "disable"] | None = ...,
        webfilter_logs: Literal["enable", "disable"] | None = ...,
        configuration_changes_logs: Literal["enable", "disable"] | None = ...,
        violation_traffic_logs: Literal["enable", "disable"] | None = ...,
        admin_login_logs: Literal["enable", "disable"] | None = ...,
        FDS_license_expiring_warning: Literal["enable", "disable"] | None = ...,
        log_disk_usage_warning: Literal["enable", "disable"] | None = ...,
        fortiguard_log_quota_warning: Literal["enable", "disable"] | None = ...,
        amc_interface_bypass_mode: Literal["enable", "disable"] | None = ...,
        FIPS_CC_errors: Literal["enable", "disable"] | None = ...,
        FSSO_disconnect_logs: Literal["enable", "disable"] | None = ...,
        ssh_logs: Literal["enable", "disable"] | None = ...,
        local_disk_usage: int | None = ...,
        emergency_interval: int | None = ...,
        alert_interval: int | None = ...,
        critical_interval: int | None = ...,
        error_interval: int | None = ...,
        warning_interval: int | None = ...,
        notification_interval: int | None = ...,
        information_interval: int | None = ...,
        debug_interval: int | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingObject",
]