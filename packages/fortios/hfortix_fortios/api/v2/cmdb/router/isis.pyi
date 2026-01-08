from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class IsisPayload(TypedDict, total=False):
    """
    Type hints for router/isis payload fields.
    
    Configure IS-IS.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.access-list.AccessListEndpoint` (via: redistribute-l1-list, redistribute-l2-list)
        - :class:`~.router.access-list6.AccessList6Endpoint` (via: redistribute6-l1-list, redistribute6-l2-list)
        - :class:`~.router.key-chain.KeyChainEndpoint` (via: auth-keychain-l1, auth-keychain-l2)

    **Usage:**
        payload: IsisPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    is_type: NotRequired[Literal["level-1-2", "level-1", "level-2-only"]]  # IS type.
    adv_passive_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable IS-IS advertisement of passive interfaces onl
    adv_passive_only6: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv6 IS-IS advertisement of passive interface
    auth_mode_l1: NotRequired[Literal["password", "md5"]]  # Level 1 authentication mode.
    auth_mode_l2: NotRequired[Literal["password", "md5"]]  # Level 2 authentication mode.
    auth_password_l1: NotRequired[str]  # Authentication password for level 1 PDUs.
    auth_password_l2: NotRequired[str]  # Authentication password for level 2 PDUs.
    auth_keychain_l1: NotRequired[str]  # Authentication key-chain for level 1 PDUs.
    auth_keychain_l2: NotRequired[str]  # Authentication key-chain for level 2 PDUs.
    auth_sendonly_l1: NotRequired[Literal["enable", "disable"]]  # Enable/disable level 1 authentication send-only.
    auth_sendonly_l2: NotRequired[Literal["enable", "disable"]]  # Enable/disable level 2 authentication send-only.
    ignore_lsp_errors: NotRequired[Literal["enable", "disable"]]  # Enable/disable ignoring of LSP errors with bad checksums.
    lsp_gen_interval_l1: NotRequired[int]  # Minimum interval for level 1 LSP regenerating.
    lsp_gen_interval_l2: NotRequired[int]  # Minimum interval for level 2 LSP regenerating.
    lsp_refresh_interval: NotRequired[int]  # LSP refresh time in seconds.
    max_lsp_lifetime: NotRequired[int]  # Maximum LSP lifetime in seconds.
    spf_interval_exp_l1: NotRequired[str]  # Level 1 SPF calculation delay.
    spf_interval_exp_l2: NotRequired[str]  # Level 2 SPF calculation delay.
    dynamic_hostname: NotRequired[Literal["enable", "disable"]]  # Enable/disable dynamic hostname.
    adjacency_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable adjacency check.
    adjacency_check6: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv6 adjacency check.
    overload_bit: NotRequired[Literal["enable", "disable"]]  # Enable/disable signal other routers not to use us in SPF.
    overload_bit_suppress: NotRequired[Literal["external", "interlevel"]]  # Suppress overload-bit for the specific prefixes.
    overload_bit_on_startup: NotRequired[int]  # Overload-bit only temporarily after reboot.
    default_originate: NotRequired[Literal["enable", "disable"]]  # Enable/disable distribution of default route information.
    default_originate6: NotRequired[Literal["enable", "disable"]]  # Enable/disable distribution of default IPv6 route informatio
    metric_style: NotRequired[Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"]]  # Use old-style (ISO 10589) or new-style packet formats.
    redistribute_l1: NotRequired[Literal["enable", "disable"]]  # Enable/disable redistribution of level 1 routes into level 2
    redistribute_l1_list: NotRequired[str]  # Access-list for route redistribution from l1 to l2.
    redistribute_l2: NotRequired[Literal["enable", "disable"]]  # Enable/disable redistribution of level 2 routes into level 1
    redistribute_l2_list: NotRequired[str]  # Access-list for route redistribution from l2 to l1.
    redistribute6_l1: NotRequired[Literal["enable", "disable"]]  # Enable/disable redistribution of level 1 IPv6 routes into le
    redistribute6_l1_list: NotRequired[str]  # Access-list for IPv6 route redistribution from l1 to l2.
    redistribute6_l2: NotRequired[Literal["enable", "disable"]]  # Enable/disable redistribution of level 2 IPv6 routes into le
    redistribute6_l2_list: NotRequired[str]  # Access-list for IPv6 route redistribution from l2 to l1.
    isis_net: NotRequired[list[dict[str, Any]]]  # IS-IS net configuration.
    isis_interface: NotRequired[list[dict[str, Any]]]  # IS-IS interface configuration.
    summary_address: NotRequired[list[dict[str, Any]]]  # IS-IS summary addresses.
    summary_address6: NotRequired[list[dict[str, Any]]]  # IS-IS IPv6 summary address.
    redistribute: NotRequired[list[dict[str, Any]]]  # IS-IS redistribute protocols.
    redistribute6: NotRequired[list[dict[str, Any]]]  # IS-IS IPv6 redistribution for routing protocols.

# Nested classes for table field children

@final
class IsisIsisnetObject:
    """Typed object for isis-net table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ISIS network ID.
    id: int
    # IS-IS networks (format = xx.xxxx.  .xxxx.xx.).
    net: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class IsisIsisinterfaceObject:
    """Typed object for isis-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IS-IS interface name.
    name: str
    # Enable/disable interface for IS-IS.
    status: Literal["enable", "disable"]
    # Enable/disable IPv6 interface for IS-IS.
    status6: Literal["enable", "disable"]
    # IS-IS interface's network type.
    network_type: Literal["broadcast", "point-to-point", "loopback"]
    # IS-IS interface's circuit type.
    circuit_type: Literal["level-1-2", "level-1", "level-2"]
    # Level 1 CSNP interval.
    csnp_interval_l1: int
    # Level 2 CSNP interval.
    csnp_interval_l2: int
    # Level 1 hello interval.
    hello_interval_l1: int
    # Level 2 hello interval.
    hello_interval_l2: int
    # Level 1 multiplier for Hello holding time.
    hello_multiplier_l1: int
    # Level 2 multiplier for Hello holding time.
    hello_multiplier_l2: int
    # Enable/disable padding to IS-IS hello packets.
    hello_padding: Literal["enable", "disable"]
    # LSP transmission interval (milliseconds).
    lsp_interval: int
    # LSP retransmission interval (sec).
    lsp_retransmit_interval: int
    # Level 1 metric for interface.
    metric_l1: int
    # Level 2 metric for interface.
    metric_l2: int
    # Level 1 wide metric for interface.
    wide_metric_l1: int
    # Level 2 wide metric for interface.
    wide_metric_l2: int
    # Authentication password for level 1 PDUs.
    auth_password_l1: str
    # Authentication password for level 2 PDUs.
    auth_password_l2: str
    # Authentication key-chain for level 1 PDUs.
    auth_keychain_l1: str
    # Authentication key-chain for level 2 PDUs.
    auth_keychain_l2: str
    # Enable/disable authentication send-only for level 1 PDUs.
    auth_send_only_l1: Literal["enable", "disable"]
    # Enable/disable authentication send-only for level 2 PDUs.
    auth_send_only_l2: Literal["enable", "disable"]
    # Level 1 authentication mode.
    auth_mode_l1: Literal["md5", "password"]
    # Level 2 authentication mode.
    auth_mode_l2: Literal["md5", "password"]
    # Level 1 priority.
    priority_l1: int
    # Level 2 priority.
    priority_l2: int
    # Enable/disable IS-IS mesh group.
    mesh_group: Literal["enable", "disable"]
    # Mesh group ID <0-4294967295>, 0: mesh-group blocked.
    mesh_group_id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class IsisSummaryaddressObject:
    """Typed object for summary-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Summary address entry ID.
    id: int
    # Prefix.
    prefix: str
    # Level.
    level: Literal["level-1-2", "level-1", "level-2"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class IsisSummaryaddress6Object:
    """Typed object for summary-address6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Prefix entry ID.
    id: int
    # IPv6 prefix.
    prefix6: str
    # Level.
    level: Literal["level-1-2", "level-1", "level-2"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class IsisRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Protocol name.
    protocol: str
    # Status.
    status: Literal["enable", "disable"]
    # Metric.
    metric: int
    # Metric type.
    metric_type: Literal["external", "internal"]
    # Level.
    level: Literal["level-1-2", "level-1", "level-2"]
    # Route map name.
    routemap: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class IsisRedistribute6Object:
    """Typed object for redistribute6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Protocol name.
    protocol: str
    # Enable/disable redistribution.
    status: Literal["enable", "disable"]
    # Metric.
    metric: int
    # Metric type.
    metric_type: Literal["external", "internal"]
    # Level.
    level: Literal["level-1-2", "level-1", "level-2"]
    # Route map name.
    routemap: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class IsisResponse(TypedDict):
    """
    Type hints for router/isis API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    is_type: Literal["level-1-2", "level-1", "level-2-only"]
    adv_passive_only: Literal["enable", "disable"]
    adv_passive_only6: Literal["enable", "disable"]
    auth_mode_l1: Literal["password", "md5"]
    auth_mode_l2: Literal["password", "md5"]
    auth_password_l1: str
    auth_password_l2: str
    auth_keychain_l1: str
    auth_keychain_l2: str
    auth_sendonly_l1: Literal["enable", "disable"]
    auth_sendonly_l2: Literal["enable", "disable"]
    ignore_lsp_errors: Literal["enable", "disable"]
    lsp_gen_interval_l1: int
    lsp_gen_interval_l2: int
    lsp_refresh_interval: int
    max_lsp_lifetime: int
    spf_interval_exp_l1: str
    spf_interval_exp_l2: str
    dynamic_hostname: Literal["enable", "disable"]
    adjacency_check: Literal["enable", "disable"]
    adjacency_check6: Literal["enable", "disable"]
    overload_bit: Literal["enable", "disable"]
    overload_bit_suppress: Literal["external", "interlevel"]
    overload_bit_on_startup: int
    default_originate: Literal["enable", "disable"]
    default_originate6: Literal["enable", "disable"]
    metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"]
    redistribute_l1: Literal["enable", "disable"]
    redistribute_l1_list: str
    redistribute_l2: Literal["enable", "disable"]
    redistribute_l2_list: str
    redistribute6_l1: Literal["enable", "disable"]
    redistribute6_l1_list: str
    redistribute6_l2: Literal["enable", "disable"]
    redistribute6_l2_list: str
    isis_net: list[dict[str, Any]]
    isis_interface: list[dict[str, Any]]
    summary_address: list[dict[str, Any]]
    summary_address6: list[dict[str, Any]]
    redistribute: list[dict[str, Any]]
    redistribute6: list[dict[str, Any]]


@final
class IsisObject:
    """Typed FortiObject for router/isis with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IS type.
    is_type: Literal["level-1-2", "level-1", "level-2-only"]
    # Enable/disable IS-IS advertisement of passive interfaces only.
    adv_passive_only: Literal["enable", "disable"]
    # Enable/disable IPv6 IS-IS advertisement of passive interfaces only.
    adv_passive_only6: Literal["enable", "disable"]
    # Level 1 authentication mode.
    auth_mode_l1: Literal["password", "md5"]
    # Level 2 authentication mode.
    auth_mode_l2: Literal["password", "md5"]
    # Authentication password for level 1 PDUs.
    auth_password_l1: str
    # Authentication password for level 2 PDUs.
    auth_password_l2: str
    # Authentication key-chain for level 1 PDUs.
    auth_keychain_l1: str
    # Authentication key-chain for level 2 PDUs.
    auth_keychain_l2: str
    # Enable/disable level 1 authentication send-only.
    auth_sendonly_l1: Literal["enable", "disable"]
    # Enable/disable level 2 authentication send-only.
    auth_sendonly_l2: Literal["enable", "disable"]
    # Enable/disable ignoring of LSP errors with bad checksums.
    ignore_lsp_errors: Literal["enable", "disable"]
    # Minimum interval for level 1 LSP regenerating.
    lsp_gen_interval_l1: int
    # Minimum interval for level 2 LSP regenerating.
    lsp_gen_interval_l2: int
    # LSP refresh time in seconds.
    lsp_refresh_interval: int
    # Maximum LSP lifetime in seconds.
    max_lsp_lifetime: int
    # Level 1 SPF calculation delay.
    spf_interval_exp_l1: str
    # Level 2 SPF calculation delay.
    spf_interval_exp_l2: str
    # Enable/disable dynamic hostname.
    dynamic_hostname: Literal["enable", "disable"]
    # Enable/disable adjacency check.
    adjacency_check: Literal["enable", "disable"]
    # Enable/disable IPv6 adjacency check.
    adjacency_check6: Literal["enable", "disable"]
    # Enable/disable signal other routers not to use us in SPF.
    overload_bit: Literal["enable", "disable"]
    # Suppress overload-bit for the specific prefixes.
    overload_bit_suppress: Literal["external", "interlevel"]
    # Overload-bit only temporarily after reboot.
    overload_bit_on_startup: int
    # Enable/disable distribution of default route information.
    default_originate: Literal["enable", "disable"]
    # Enable/disable distribution of default IPv6 route information.
    default_originate6: Literal["enable", "disable"]
    # Use old-style (ISO 10589) or new-style packet formats.
    metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"]
    # Enable/disable redistribution of level 1 routes into level 2.
    redistribute_l1: Literal["enable", "disable"]
    # Access-list for route redistribution from l1 to l2.
    redistribute_l1_list: str
    # Enable/disable redistribution of level 2 routes into level 1.
    redistribute_l2: Literal["enable", "disable"]
    # Access-list for route redistribution from l2 to l1.
    redistribute_l2_list: str
    # Enable/disable redistribution of level 1 IPv6 routes into level 2.
    redistribute6_l1: Literal["enable", "disable"]
    # Access-list for IPv6 route redistribution from l1 to l2.
    redistribute6_l1_list: str
    # Enable/disable redistribution of level 2 IPv6 routes into level 1.
    redistribute6_l2: Literal["enable", "disable"]
    # Access-list for IPv6 route redistribution from l2 to l1.
    redistribute6_l2_list: str
    # IS-IS net configuration.
    isis_net: list[IsisIsisnetObject]  # Table field - list of typed objects
    # IS-IS interface configuration.
    isis_interface: list[IsisIsisinterfaceObject]  # Table field - list of typed objects
    # IS-IS summary addresses.
    summary_address: list[IsisSummaryaddressObject]  # Table field - list of typed objects
    # IS-IS IPv6 summary address.
    summary_address6: list[IsisSummaryaddress6Object]  # Table field - list of typed objects
    # IS-IS redistribute protocols.
    redistribute: list[IsisRedistributeObject]  # Table field - list of typed objects
    # IS-IS IPv6 redistribution for routing protocols.
    redistribute6: list[IsisRedistribute6Object]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> IsisPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Isis:
    """
    Configure IS-IS.
    
    Path: router/isis
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisResponse: ...
    
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
    ) -> IsisResponse: ...
    
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
    ) -> IsisResponse: ...
    
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
    ) -> IsisObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> IsisObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Isis",
    "IsisPayload",
    "IsisObject",
]