from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class FortiguardPayload(TypedDict, total=False):
    """
    Type hints for system/fortiguard payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    antispam_cache_ttl: NotRequired[int]  # Time-to-live for antispam cache entries in seconds (300 - 86
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
    outbreak_prevention_timeout: int  # FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, d
    webfilter_force_off: NotRequired[Literal["enable", "disable"]]  # Enable/disable turning off the FortiGuard web filtering serv
    webfilter_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGuard web filter caching.
    webfilter_cache_ttl: NotRequired[int]  # Time-to-live for web filter cache entries in seconds (300 - 
    webfilter_license: NotRequired[int]  # Interval of time between license checks for the FortiGuard w
    webfilter_expiration: NotRequired[int]  # Expiration date of the FortiGuard web filter contract.
    webfilter_timeout: int  # Web filter query time out (1 - 30 sec, default = 15).
    sdns_server_ip: NotRequired[str]  # IP address of the FortiGuard DNS rating server.
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


class Fortiguard:
    """
    Configure FortiGuard services.
    
    Path: system/fortiguard
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
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        auto_firmware_upgrade_delay: int | None = ...,
        auto_firmware_upgrade_start_hour: int | None = ...,
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
        payload_dict: FortiguardPayload | None = ...,
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