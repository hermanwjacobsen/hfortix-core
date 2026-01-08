from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AccprofilePayload(TypedDict, total=False):
    """
    Type hints for system/accprofile payload fields.
    
    Configure access profiles for system administrators.
    
    **Usage:**
        payload: AccprofilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name.
    scope: NotRequired[Literal["vdom", "global"]]  # Scope of admin access: global or specific VDOM(s).
    comments: NotRequired[str]  # Comment.
    secfabgrp: NotRequired[Literal["none", "read", "read-write", "custom"]]  # Security Fabric.
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
    secfabgrp_permission: NotRequired[str]  # Custom Security Fabric permissions.
    admintimeout_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable overriding the global administrator idle time
    admintimeout: NotRequired[int]  # Administrator timeout for this access profile
    cli_diagnose: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run diagnostic commands.
    cli_get: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run get commands.
    cli_show: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run show commands.
    cli_exec: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run execute commands.
    cli_config: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to run config commands.
    system_execute_ssh: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to execute SSH commands.
    system_execute_telnet: NotRequired[Literal["enable", "disable"]]  # Enable/disable permission to execute TELNET commands.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class AccprofileResponse(TypedDict):
    """
    Type hints for system/accprofile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    scope: Literal["vdom", "global"]
    comments: str
    secfabgrp: Literal["none", "read", "read-write", "custom"]
    ftviewgrp: Literal["none", "read", "read-write"]
    authgrp: Literal["none", "read", "read-write"]
    sysgrp: Literal["none", "read", "read-write", "custom"]
    netgrp: Literal["none", "read", "read-write", "custom"]
    loggrp: Literal["none", "read", "read-write", "custom"]
    fwgrp: Literal["none", "read", "read-write", "custom"]
    vpngrp: Literal["none", "read", "read-write"]
    utmgrp: Literal["none", "read", "read-write", "custom"]
    wanoptgrp: Literal["none", "read", "read-write"]
    wifi: Literal["none", "read", "read-write"]
    netgrp_permission: str
    sysgrp_permission: str
    fwgrp_permission: str
    loggrp_permission: str
    utmgrp_permission: str
    secfabgrp_permission: str
    admintimeout_override: Literal["enable", "disable"]
    admintimeout: int
    cli_diagnose: Literal["enable", "disable"]
    cli_get: Literal["enable", "disable"]
    cli_show: Literal["enable", "disable"]
    cli_exec: Literal["enable", "disable"]
    cli_config: Literal["enable", "disable"]
    system_execute_ssh: Literal["enable", "disable"]
    system_execute_telnet: Literal["enable", "disable"]


@final
class AccprofileObject:
    """Typed FortiObject for system/accprofile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name.
    name: str
    # Scope of admin access: global or specific VDOM(s).
    scope: Literal["vdom", "global"]
    # Comment.
    comments: str
    # Security Fabric.
    secfabgrp: Literal["none", "read", "read-write", "custom"]
    # FortiView.
    ftviewgrp: Literal["none", "read", "read-write"]
    # Administrator access to Users and Devices.
    authgrp: Literal["none", "read", "read-write"]
    # System Configuration.
    sysgrp: Literal["none", "read", "read-write", "custom"]
    # Network Configuration.
    netgrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to Logging and Reporting including viewing log messages.
    loggrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to the Firewall configuration.
    fwgrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to IPsec, SSL, PPTP, and L2TP VPN.
    vpngrp: Literal["none", "read", "read-write"]
    # Administrator access to Security Profiles.
    utmgrp: Literal["none", "read", "read-write", "custom"]
    # Administrator access to WAN Opt & Cache.
    wanoptgrp: Literal["none", "read", "read-write"]
    # Administrator access to the WiFi controller and Switch controller.
    wifi: Literal["none", "read", "read-write"]
    # Custom network permission.
    netgrp_permission: str
    # Custom system permission.
    sysgrp_permission: str
    # Custom firewall permission.
    fwgrp_permission: str
    # Custom Log & Report permission.
    loggrp_permission: str
    # Custom Security Profile permissions.
    utmgrp_permission: str
    # Custom Security Fabric permissions.
    secfabgrp_permission: str
    # Enable/disable overriding the global administrator idle timeout.
    admintimeout_override: Literal["enable", "disable"]
    # Administrator timeout for this access profile
    admintimeout: int
    # Enable/disable permission to run diagnostic commands.
    cli_diagnose: Literal["enable", "disable"]
    # Enable/disable permission to run get commands.
    cli_get: Literal["enable", "disable"]
    # Enable/disable permission to run show commands.
    cli_show: Literal["enable", "disable"]
    # Enable/disable permission to run execute commands.
    cli_exec: Literal["enable", "disable"]
    # Enable/disable permission to run config commands.
    cli_config: Literal["enable", "disable"]
    # Enable/disable permission to execute SSH commands.
    system_execute_ssh: Literal["enable", "disable"]
    # Enable/disable permission to execute TELNET commands.
    system_execute_telnet: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AccprofilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Accprofile:
    """
    Configure access profiles for system administrators.
    
    Path: system/accprofile
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccprofileObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccprofileObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[AccprofileObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
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
    ) -> AccprofileResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
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
    ) -> AccprofileResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
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
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[AccprofileResponse]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
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
    ) -> AccprofileObject | list[AccprofileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccprofileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccprofileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AccprofileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AccprofilePayload | None = ...,
        name: str | None = ...,
        scope: Literal["vdom", "global"] | None = ...,
        comments: str | None = ...,
        secfabgrp: Literal["none", "read", "read-write", "custom"] | None = ...,
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
        secfabgrp_permission: str | None = ...,
        admintimeout_override: Literal["enable", "disable"] | None = ...,
        admintimeout: int | None = ...,
        cli_diagnose: Literal["enable", "disable"] | None = ...,
        cli_get: Literal["enable", "disable"] | None = ...,
        cli_show: Literal["enable", "disable"] | None = ...,
        cli_exec: Literal["enable", "disable"] | None = ...,
        cli_config: Literal["enable", "disable"] | None = ...,
        system_execute_ssh: Literal["enable", "disable"] | None = ...,
        system_execute_telnet: Literal["enable", "disable"] | None = ...,
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
    "Accprofile",
    "AccprofilePayload",
    "AccprofileObject",
]