from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AccprofilePayload(TypedDict, total=False):
    """
    Type hints for system/accprofile payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AccprofilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    scope: NotRequired[Literal["vdom", "global"]]  # Scope of admin access: global or specific VDOM(s).
    comments: NotRequired[str]  # Comment.
    secfabgrp: NotRequired[Literal["none", "read", "read-write"]]  # Security Fabric.
    ftviewgrp: NotRequired[Literal["none", "read", "read-write"]]  # FortiView.
    authgrp: NotRequired[Literal["none", "read", "read-write"]]  # Administrator access to Users and Devices.
    sysgrp: NotRequired[Literal["none", "read", "read-write", "custom"]]  # System Configuration.
    netgrp: NotRequired[Literal["none", "read", "read-write", "custom"]]  # Network Configuration.
    loggrp: NotRequired[Literal["none", "read", "read-write", "custom"]]  # Administrator access to Logging and Reporting including view
    fwgrp: NotRequired[Literal["none", "read", "read-write", "custom"]]  # Administrator access to the Firewall configuration.
    vpngrp: NotRequired[Literal["none", "read", "read-write"]]  # Administrator access to IPsec, SSL, PPTP, and L2TP VPN.
    utmgrp: NotRequired[Literal["none", "read", "read-write", "custom"]]  # Administrator access to Security Profiles.
    wanoptgrp: NotRequired[Literal["none", "read", "read-write"]]  # Administrator access to WAN Opt & Cache.
    wifi: NotRequired[Literal["none", "read", "read-write"]]  # Administrator access to the WiFi controller and Switch contr
    netgrp_permission: NotRequired[str]  # Custom network permission.
    sysgrp_permission: NotRequired[str]  # Custom system permission.
    fwgrp_permission: NotRequired[str]  # Custom firewall permission.
    loggrp_permission: NotRequired[str]  # Custom Log & Report permission.
    utmgrp_permission: NotRequired[str]  # Custom Security Profile permissions.
    admintimeout_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global administrator idle time
    admintimeout: NotRequired[int]  # Administrator timeout for this access profile (0 - 480 min, 
    cli_diagnose: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run diagnostic commands.
    cli_get: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run get commands.
    cli_show: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run show commands.
    cli_exec: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run execute commands.
    cli_config: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run config commands.
    system_execute_ssh: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to execute SSH commands.
    system_execute_telnet: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to execute TELNET commands.


class Accprofile:
    """
    Configure access profiles for system administrators.
    
    Path: system/accprofile
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
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write"] | None = ...,
        ftviewgrp: Literal["none", "read", "read-write"] | None = ...,
        authgrp: Literal["none", "read", "read-write"] | None = ...,
        sysgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        netgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        loggrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        fwgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        vpngrp: Literal["none", "read", "read-write"] | None = ...,
        utmgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
        wanoptgrp: Literal["none", "read", "read-write"] | None = ...,
        wifi: Literal["none", "read", "read-write"] | None = ...,
        netgrp_permission: str | None = ...,
        sysgrp_permission: str | None = ...,
        fwgrp_permission: str | None = ...,
        loggrp_permission: str | None = ...,
        utmgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
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
        payload_dict: AccprofilePayload | None = ...,
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