from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ResourceLimitsPayload(TypedDict, total=False):
    """
    Type hints for system/resource_limits payload fields.
    
    Configure resource limits.
    
    **Usage:**
        payload: ResourceLimitsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    session: NotRequired[int]  # Maximum number of sessions.
    ipsec_phase1: NotRequired[int]  # Maximum number of VPN IPsec phase1 tunnels.
    ipsec_phase2: NotRequired[int]  # Maximum number of VPN IPsec phase2 tunnels.
    ipsec_phase1_interface: NotRequired[int]  # Maximum number of VPN IPsec phase1 interface tunnels.
    ipsec_phase2_interface: NotRequired[int]  # Maximum number of VPN IPsec phase2 interface tunnels.
    dialup_tunnel: NotRequired[int]  # Maximum number of dial-up tunnels.
    firewall_policy: NotRequired[int]  # Maximum number of firewall policies
    firewall_address: NotRequired[int]  # Maximum number of firewall addresses (IPv4, IPv6, multicast)
    firewall_addrgrp: NotRequired[int]  # Maximum number of firewall address groups (IPv4, IPv6).
    custom_service: NotRequired[int]  # Maximum number of firewall custom services.
    service_group: NotRequired[int]  # Maximum number of firewall service groups.
    onetime_schedule: NotRequired[int]  # Maximum number of firewall one-time schedules.
    recurring_schedule: NotRequired[int]  # Maximum number of firewall recurring schedules.
    user: NotRequired[int]  # Maximum number of local users.
    user_group: NotRequired[int]  # Maximum number of user groups.
    sslvpn: NotRequired[int]  # Maximum number of Agentless VPN.
    proxy: NotRequired[int]  # Maximum number of concurrent proxy users.
    log_disk_quota: NotRequired[int]  # Log disk quota in megabytes (MB).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ResourceLimitsResponse(TypedDict):
    """
    Type hints for system/resource_limits API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    session: int
    ipsec_phase1: int
    ipsec_phase2: int
    ipsec_phase1_interface: int
    ipsec_phase2_interface: int
    dialup_tunnel: int
    firewall_policy: int
    firewall_address: int
    firewall_addrgrp: int
    custom_service: int
    service_group: int
    onetime_schedule: int
    recurring_schedule: int
    user: int
    user_group: int
    sslvpn: int
    proxy: int
    log_disk_quota: int


@final
class ResourceLimitsObject:
    """Typed FortiObject for system/resource_limits with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Maximum number of sessions.
    session: int
    # Maximum number of VPN IPsec phase1 tunnels.
    ipsec_phase1: int
    # Maximum number of VPN IPsec phase2 tunnels.
    ipsec_phase2: int
    # Maximum number of VPN IPsec phase1 interface tunnels.
    ipsec_phase1_interface: int
    # Maximum number of VPN IPsec phase2 interface tunnels.
    ipsec_phase2_interface: int
    # Maximum number of dial-up tunnels.
    dialup_tunnel: int
    # Maximum number of firewall policies
    firewall_policy: int
    # Maximum number of firewall addresses (IPv4, IPv6, multicast).
    firewall_address: int
    # Maximum number of firewall address groups (IPv4, IPv6).
    firewall_addrgrp: int
    # Maximum number of firewall custom services.
    custom_service: int
    # Maximum number of firewall service groups.
    service_group: int
    # Maximum number of firewall one-time schedules.
    onetime_schedule: int
    # Maximum number of firewall recurring schedules.
    recurring_schedule: int
    # Maximum number of local users.
    user: int
    # Maximum number of user groups.
    user_group: int
    # Maximum number of Agentless VPN.
    sslvpn: int
    # Maximum number of concurrent proxy users.
    proxy: int
    # Log disk quota in megabytes (MB).
    log_disk_quota: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ResourceLimitsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class ResourceLimits:
    """
    Configure resource limits.
    
    Path: system/resource_limits
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsResponse: ...
    
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
    ) -> ResourceLimitsResponse: ...
    
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
    ) -> ResourceLimitsResponse: ...
    
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
    ) -> ResourceLimitsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ResourceLimitsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
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
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
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
    "ResourceLimits",
    "ResourceLimitsPayload",
    "ResourceLimitsObject",
]