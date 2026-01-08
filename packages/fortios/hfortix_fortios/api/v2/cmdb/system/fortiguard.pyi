from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class FortiguardPayload(TypedDict, total=False):
    """
    Type hints for system/fortiguard payload fields.
    
    Configure FortiGuard services.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)

    **Usage:**
        payload: FortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    fortiguard_anycast: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of FortiGuard's Anycast network.
    fortiguard_anycast_source: NotRequired[Literal["fortinet", "aws", "debug"]]  # Configure which of Fortinet's servers to provide FortiGuard
    protocol: NotRequired[Literal["udp", "http", "https"]]  # Protocol used to communicate with the FortiGuard servers.
    port: NotRequired[Literal["8888", "53", "80", "443"]]  # Port used to communicate with the FortiGuard servers.
    load_balance_servers: NotRequired[int]  # Number of servers to alternate between as first FortiGuard o
    auto_join_forticloud: NotRequired[Literal["enable", "disable"]]  # Automatically connect to and login to FortiCloud.
    update_server_location: NotRequired[Literal["automatic", "usa", "eu"]]  # Location from which to receive FortiGuard updates.
    sandbox_region: NotRequired[str]  # FortiCloud Sandbox region.
    sandbox_inline_scan: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiCloud Sandbox inline-scan.
    update_ffdb: NotRequired[Literal["enable", "disable"]]  # Enable/disable Internet Service Database update.
    update_uwdb: NotRequired[Literal["enable", "disable"]]  # Enable/disable allowlist update.
    update_dldb: NotRequired[Literal["enable", "disable"]]  # Enable/disable DLP signature update.
    update_extdb: NotRequired[Literal["enable", "disable"]]  # Enable/disable external resource update.
    update_build_proxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable proxy dictionary rebuild.
    persistent_connection: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of persistent connection to receive updat
    vdom: NotRequired[str]  # FortiGuard Service virtual domain name.
    auto_firmware_upgrade: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic patch-level firmware upgrade from F
    auto_firmware_upgrade_day: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]]  # Allowed day(s) of the week to install an automatic patch-lev
    auto_firmware_upgrade_delay: NotRequired[int]  # Delay of day(s) before installing an automatic patch-level f
    auto_firmware_upgrade_start_hour: NotRequired[int]  # Start time in the designated time window for automatic patch
    auto_firmware_upgrade_end_hour: NotRequired[int]  # End time in the designated time window for automatic patch-l
    FDS_license_expiring_days: NotRequired[int]  # Threshold for number of days before FortiGuard license expir
    subscribe_update_notification: NotRequired[Literal["enable", "disable"]]  # Enable/disable subscription to receive update notification f
    antispam_force_off: NotRequired[Literal["enable", "disable"]]  # Enable/disable turning off the FortiGuard antispam service.
    antispam_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard antispam request caching. Uses a s
    antispam_cache_ttl: NotRequired[int]  # Time-to-live for antispam cache entries in seconds
    antispam_cache_mpermille: NotRequired[int]  # Maximum permille of FortiGate memory the antispam cache is a
    antispam_license: NotRequired[int]  # Interval of time between license checks for the FortiGuard a
    antispam_expiration: NotRequired[int]  # Expiration date of the FortiGuard antispam contract.
    antispam_timeout: int  # Antispam query time out (1 - 30 sec, default = 7).
    outbreak_prevention_force_off: NotRequired[Literal["enable", "disable"]]  # Turn off FortiGuard Virus Outbreak Prevention service.
    outbreak_prevention_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard Virus Outbreak Prevention cache.
    outbreak_prevention_cache_ttl: NotRequired[int]  # Time-to-live for FortiGuard Virus Outbreak Prevention cache
    outbreak_prevention_cache_mpermille: NotRequired[int]  # Maximum permille of memory FortiGuard Virus Outbreak Prevent
    outbreak_prevention_license: NotRequired[int]  # Interval of time between license checks for FortiGuard Virus
    outbreak_prevention_expiration: NotRequired[int]  # Expiration date of FortiGuard Virus Outbreak Prevention cont
    outbreak_prevention_timeout: int  # FortiGuard Virus Outbreak Prevention time out
    webfilter_force_off: NotRequired[Literal["enable", "disable"]]  # Enable/disable turning off the FortiGuard web filtering serv
    webfilter_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard web filter caching.
    webfilter_cache_ttl: NotRequired[int]  # Time-to-live for web filter cache entries in seconds
    webfilter_license: NotRequired[int]  # Interval of time between license checks for the FortiGuard w
    webfilter_expiration: NotRequired[int]  # Expiration date of the FortiGuard web filter contract.
    webfilter_timeout: int  # Web filter query time out (1 - 30 sec, default = 15).
    sdns_server_ip: NotRequired[list[dict[str, Any]]]  # IP address of the FortiGuard DNS rating server.
    sdns_server_port: NotRequired[int]  # Port to connect to on the FortiGuard DNS rating server.
    anycast_sdns_server_ip: NotRequired[str]  # IP address of the FortiGuard anycast DNS rating server.
    anycast_sdns_server_port: NotRequired[int]  # Port to connect to on the FortiGuard anycast DNS rating serv
    sdns_options: NotRequired[Literal["include-question-section"]]  # Customization options for the FortiGuard DNS service.
    source_ip: NotRequired[str]  # Source IPv4 address used to communicate with FortiGuard.
    source_ip6: NotRequired[str]  # Source IPv6 address used to communicate with FortiGuard.
    proxy_server_ip: NotRequired[str]  # Hostname or IPv4 address of the proxy server.
    proxy_server_port: NotRequired[int]  # Port used to communicate with the proxy server.
    proxy_username: NotRequired[str]  # Proxy user name.
    proxy_password: NotRequired[str]  # Proxy user password.
    ddns_server_ip: NotRequired[str]  # IP address of the FortiDDNS server.
    ddns_server_ip6: NotRequired[str]  # IPv6 address of the FortiDDNS server.
    ddns_server_port: NotRequired[int]  # Port used to communicate with FortiDDNS servers.
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class FortiguardResponse(TypedDict):
    """
    Type hints for system/fortiguard API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    fortiguard_anycast: Literal["enable", "disable"]
    fortiguard_anycast_source: Literal["fortinet", "aws", "debug"]
    protocol: Literal["udp", "http", "https"]
    port: Literal["8888", "53", "80", "443"]
    load_balance_servers: int
    auto_join_forticloud: Literal["enable", "disable"]
    update_server_location: Literal["automatic", "usa", "eu"]
    sandbox_region: str
    sandbox_inline_scan: Literal["enable", "disable"]
    update_ffdb: Literal["enable", "disable"]
    update_uwdb: Literal["enable", "disable"]
    update_dldb: Literal["enable", "disable"]
    update_extdb: Literal["enable", "disable"]
    update_build_proxy: Literal["enable", "disable"]
    persistent_connection: Literal["enable", "disable"]
    vdom: str
    auto_firmware_upgrade: Literal["enable", "disable"]
    auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    auto_firmware_upgrade_delay: int
    auto_firmware_upgrade_start_hour: int
    auto_firmware_upgrade_end_hour: int
    FDS_license_expiring_days: int
    subscribe_update_notification: Literal["enable", "disable"]
    antispam_force_off: Literal["enable", "disable"]
    antispam_cache: Literal["enable", "disable"]
    antispam_cache_ttl: int
    antispam_cache_mpermille: int
    antispam_license: int
    antispam_expiration: int
    antispam_timeout: int
    outbreak_prevention_force_off: Literal["enable", "disable"]
    outbreak_prevention_cache: Literal["enable", "disable"]
    outbreak_prevention_cache_ttl: int
    outbreak_prevention_cache_mpermille: int
    outbreak_prevention_license: int
    outbreak_prevention_expiration: int
    outbreak_prevention_timeout: int
    webfilter_force_off: Literal["enable", "disable"]
    webfilter_cache: Literal["enable", "disable"]
    webfilter_cache_ttl: int
    webfilter_license: int
    webfilter_expiration: int
    webfilter_timeout: int
    sdns_server_ip: list[dict[str, Any]]
    sdns_server_port: int
    anycast_sdns_server_ip: str
    anycast_sdns_server_port: int
    sdns_options: Literal["include-question-section"]
    source_ip: str
    source_ip6: str
    proxy_server_ip: str
    proxy_server_port: int
    proxy_username: str
    proxy_password: str
    ddns_server_ip: str
    ddns_server_ip6: str
    ddns_server_port: int
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int


@final
class FortiguardObject:
    """Typed FortiObject for system/fortiguard with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable use of FortiGuard's Anycast network.
    fortiguard_anycast: Literal["enable", "disable"]
    # Configure which of Fortinet's servers to provide FortiGuard services in FortiGua
    fortiguard_anycast_source: Literal["fortinet", "aws", "debug"]
    # Protocol used to communicate with the FortiGuard servers.
    protocol: Literal["udp", "http", "https"]
    # Port used to communicate with the FortiGuard servers.
    port: Literal["8888", "53", "80", "443"]
    # Number of servers to alternate between as first FortiGuard option.
    load_balance_servers: int
    # Automatically connect to and login to FortiCloud.
    auto_join_forticloud: Literal["enable", "disable"]
    # Location from which to receive FortiGuard updates.
    update_server_location: Literal["automatic", "usa", "eu"]
    # FortiCloud Sandbox region.
    sandbox_region: str
    # Enable/disable FortiCloud Sandbox inline-scan.
    sandbox_inline_scan: Literal["enable", "disable"]
    # Enable/disable Internet Service Database update.
    update_ffdb: Literal["enable", "disable"]
    # Enable/disable allowlist update.
    update_uwdb: Literal["enable", "disable"]
    # Enable/disable DLP signature update.
    update_dldb: Literal["enable", "disable"]
    # Enable/disable external resource update.
    update_extdb: Literal["enable", "disable"]
    # Enable/disable proxy dictionary rebuild.
    update_build_proxy: Literal["enable", "disable"]
    # Enable/disable use of persistent connection to receive update notification from
    persistent_connection: Literal["enable", "disable"]
    # FortiGuard Service virtual domain name.
    vdom: str
    # Enable/disable automatic patch-level firmware upgrade from FortiGuard. The Forti
    auto_firmware_upgrade: Literal["enable", "disable"]
    # Allowed day(s) of the week to install an automatic patch-level firmware upgrade
    auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Delay of day(s) before installing an automatic patch-level firmware upgrade from
    auto_firmware_upgrade_delay: int
    # Start time in the designated time window for automatic patch-level firmware upgr
    auto_firmware_upgrade_start_hour: int
    # End time in the designated time window for automatic patch-level firmware upgrad
    auto_firmware_upgrade_end_hour: int
    # Threshold for number of days before FortiGuard license expiration to generate li
    FDS_license_expiring_days: int
    # Enable/disable subscription to receive update notification from FortiGuard.
    subscribe_update_notification: Literal["enable", "disable"]
    # Enable/disable turning off the FortiGuard antispam service.
    antispam_force_off: Literal["enable", "disable"]
    # Enable/disable FortiGuard antispam request caching. Uses a small amount of memor
    antispam_cache: Literal["enable", "disable"]
    # Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times re
    antispam_cache_ttl: int
    # Maximum permille of FortiGate memory the antispam cache is allowed to use
    antispam_cache_mpermille: int
    # Interval of time between license checks for the FortiGuard antispam contract.
    antispam_license: int
    # Expiration date of the FortiGuard antispam contract.
    antispam_expiration: int
    # Antispam query time out (1 - 30 sec, default = 7).
    antispam_timeout: int
    # Turn off FortiGuard Virus Outbreak Prevention service.
    outbreak_prevention_force_off: Literal["enable", "disable"]
    # Enable/disable FortiGuard Virus Outbreak Prevention cache.
    outbreak_prevention_cache: Literal["enable", "disable"]
    # Time-to-live for FortiGuard Virus Outbreak Prevention cache entries
    outbreak_prevention_cache_ttl: int
    # Maximum permille of memory FortiGuard Virus Outbreak Prevention cache can use
    outbreak_prevention_cache_mpermille: int
    # Interval of time between license checks for FortiGuard Virus Outbreak Prevention
    outbreak_prevention_license: int
    # Expiration date of FortiGuard Virus Outbreak Prevention contract.
    outbreak_prevention_expiration: int
    # FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7).
    outbreak_prevention_timeout: int
    # Enable/disable turning off the FortiGuard web filtering service.
    webfilter_force_off: Literal["enable", "disable"]
    # Enable/disable FortiGuard web filter caching.
    webfilter_cache: Literal["enable", "disable"]
    # Time-to-live for web filter cache entries in seconds (300 - 86400).
    webfilter_cache_ttl: int
    # Interval of time between license checks for the FortiGuard web filter contract.
    webfilter_license: int
    # Expiration date of the FortiGuard web filter contract.
    webfilter_expiration: int
    # Web filter query time out (1 - 30 sec, default = 15).
    webfilter_timeout: int
    # IP address of the FortiGuard DNS rating server.
    sdns_server_ip: list[dict[str, Any]]  # Multi-value field
    # Port to connect to on the FortiGuard DNS rating server.
    sdns_server_port: int
    # IP address of the FortiGuard anycast DNS rating server.
    anycast_sdns_server_ip: str
    # Port to connect to on the FortiGuard anycast DNS rating server.
    anycast_sdns_server_port: int
    # Customization options for the FortiGuard DNS service.
    sdns_options: Literal["include-question-section"]
    # Source IPv4 address used to communicate with FortiGuard.
    source_ip: str
    # Source IPv6 address used to communicate with FortiGuard.
    source_ip6: str
    # Hostname or IPv4 address of the proxy server.
    proxy_server_ip: str
    # Port used to communicate with the proxy server.
    proxy_server_port: int
    # Proxy user name.
    proxy_username: str
    # Proxy user password.
    proxy_password: str
    # IP address of the FortiDDNS server.
    ddns_server_ip: str
    # IPv6 address of the FortiDDNS server.
    ddns_server_ip6: str
    # Port used to communicate with FortiDDNS servers.
    ddns_server_port: int
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiguardPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Fortiguard:
    """
    Configure FortiGuard services.
    
    Path: system/fortiguard
    Category: cmdb
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardResponse: ...
    
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
    ) -> FortiguardResponse: ...
    
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
    ) -> FortiguardResponse: ...
    
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
    ) -> FortiguardObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> FortiguardObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
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
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
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
        payload_dict: FortiguardPayload | None = ...,
        fortiguard_anycast: Literal["enable", "disable"] | None = ...,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = ...,
        protocol: Literal["udp", "http", "https"] | None = ...,
        port: Literal["8888", "53", "80", "443"] | None = ...,
        load_balance_servers: int | None = ...,
        auto_join_forticloud: Literal["enable", "disable"] | None = ...,
        update_server_location: Literal["automatic", "usa", "eu"] | None = ...,
        sandbox_region: str | None = ...,
        sandbox_inline_scan: Literal["enable", "disable"] | None = ...,
        update_ffdb: Literal["enable", "disable"] | None = ...,
        update_uwdb: Literal["enable", "disable"] | None = ...,
        update_dldb: Literal["enable", "disable"] | None = ...,
        update_extdb: Literal["enable", "disable"] | None = ...,
        update_build_proxy: Literal["enable", "disable"] | None = ...,
        persistent_connection: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = ...,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list[str] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        auto_firmware_upgrade_end_hour: int | None = ...,
        FDS_license_expiring_days: int | None = ...,
        subscribe_update_notification: Literal["enable", "disable"] | None = ...,
        antispam_force_off: Literal["enable", "disable"] | None = ...,
        antispam_cache: Literal["enable", "disable"] | None = ...,
        antispam_cache_ttl: int | None = ...,
        antispam_cache_mpermille: int | None = ...,
        antispam_license: int | None = ...,
        antispam_expiration: int | None = ...,
        antispam_timeout: int | None = ...,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = ...,
        outbreak_prevention_cache_ttl: int | None = ...,
        outbreak_prevention_cache_mpermille: int | None = ...,
        outbreak_prevention_license: int | None = ...,
        outbreak_prevention_expiration: int | None = ...,
        outbreak_prevention_timeout: int | None = ...,
        webfilter_force_off: Literal["enable", "disable"] | None = ...,
        webfilter_cache: Literal["enable", "disable"] | None = ...,
        webfilter_cache_ttl: int | None = ...,
        webfilter_license: int | None = ...,
        webfilter_expiration: int | None = ...,
        webfilter_timeout: int | None = ...,
        sdns_server_ip: str | list[str] | None = ...,
        sdns_server_port: int | None = ...,
        anycast_sdns_server_ip: str | None = ...,
        anycast_sdns_server_port: int | None = ...,
        sdns_options: Literal["include-question-section"] | list[str] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        proxy_server_ip: str | None = ...,
        proxy_server_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        ddns_server_ip: str | None = ...,
        ddns_server_ip6: str | None = ...,
        ddns_server_port: int | None = ...,
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
    "Fortiguard",
    "FortiguardPayload",
    "FortiguardObject",
]