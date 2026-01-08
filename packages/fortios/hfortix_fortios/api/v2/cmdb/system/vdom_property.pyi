from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class VdomPropertyPayload(TypedDict, total=False):
    """
    Type hints for system/vdom_property payload fields.
    
    Configure VDOM property.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.vdom.VdomEndpoint` (via: name)

    **Usage:**
        payload: VdomPropertyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # VDOM name.
    description: NotRequired[str]  # Description.
    snmp_index: NotRequired[int]  # Permanent SNMP Index of the virtual domain (1 - 2147483647).
    session: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of sessions.
    ipsec_phase1: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of VPN IPsec phase 1 tunnels.
    ipsec_phase2: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of VPN IPsec phase 2 tunnels.
    ipsec_phase1_interface: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of VPN IPsec phase1 interface tunn
    ipsec_phase2_interface: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of VPN IPsec phase2 interface tunn
    dialup_tunnel: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of dial-up tunnels.
    firewall_policy: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall policies
    firewall_address: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall addresses
    firewall_addrgrp: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall address groups
    custom_service: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall custom services.
    service_group: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall service groups.
    onetime_schedule: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall one-time schedules..
    recurring_schedule: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of firewall recurring schedules.
    user: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of local users.
    user_group: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of user groups.
    sslvpn: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of Agentless VPNs.
    proxy: NotRequired[list[dict[str, Any]]]  # Maximum guaranteed number of concurrent proxy users.
    log_disk_quota: NotRequired[list[dict[str, Any]]]  # Log disk quota in megabytes (MB). Range depends on how much

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class VdomPropertyResponse(TypedDict):
    """
    Type hints for system/vdom_property API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    snmp_index: int
    session: list[dict[str, Any]]
    ipsec_phase1: list[dict[str, Any]]
    ipsec_phase2: list[dict[str, Any]]
    ipsec_phase1_interface: list[dict[str, Any]]
    ipsec_phase2_interface: list[dict[str, Any]]
    dialup_tunnel: list[dict[str, Any]]
    firewall_policy: list[dict[str, Any]]
    firewall_address: list[dict[str, Any]]
    firewall_addrgrp: list[dict[str, Any]]
    custom_service: list[dict[str, Any]]
    service_group: list[dict[str, Any]]
    onetime_schedule: list[dict[str, Any]]
    recurring_schedule: list[dict[str, Any]]
    user: list[dict[str, Any]]
    user_group: list[dict[str, Any]]
    sslvpn: list[dict[str, Any]]
    proxy: list[dict[str, Any]]
    log_disk_quota: list[dict[str, Any]]


@final
class VdomPropertyObject:
    """Typed FortiObject for system/vdom_property with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VDOM name.
    name: str
    # Description.
    description: str
    # Permanent SNMP Index of the virtual domain (1 - 2147483647).
    snmp_index: int
    # Maximum guaranteed number of sessions.
    session: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of VPN IPsec phase 1 tunnels.
    ipsec_phase1: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of VPN IPsec phase 2 tunnels.
    ipsec_phase2: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of VPN IPsec phase1 interface tunnels.
    ipsec_phase1_interface: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of VPN IPsec phase2 interface tunnels.
    ipsec_phase2_interface: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of dial-up tunnels.
    dialup_tunnel: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall policies
    firewall_policy: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall addresses (IPv4, IPv6, multicast).
    firewall_address: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall address groups (IPv4, IPv6).
    firewall_addrgrp: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall custom services.
    custom_service: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall service groups.
    service_group: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall one-time schedules..
    onetime_schedule: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of firewall recurring schedules.
    recurring_schedule: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of local users.
    user: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of user groups.
    user_group: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of Agentless VPNs.
    sslvpn: list[dict[str, Any]]  # Multi-value field
    # Maximum guaranteed number of concurrent proxy users.
    proxy: list[dict[str, Any]]  # Multi-value field
    # Log disk quota in megabytes (MB). Range depends on how much disk space is availa
    log_disk_quota: list[dict[str, Any]]  # Multi-value field
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VdomPropertyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class VdomProperty:
    """
    Configure VDOM property.
    
    Path: system/vdom_property
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> list[VdomPropertyObject]: ...
    
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
    ) -> VdomPropertyResponse: ...
    
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
    ) -> VdomPropertyResponse: ...
    
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
    ) -> list[VdomPropertyResponse]: ...
    
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
    ) -> VdomPropertyObject | list[VdomPropertyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VdomPropertyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VdomPropertyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
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
    ) -> VdomPropertyObject: ...
    
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
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
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
    "VdomProperty",
    "VdomPropertyPayload",
    "VdomPropertyObject",
]