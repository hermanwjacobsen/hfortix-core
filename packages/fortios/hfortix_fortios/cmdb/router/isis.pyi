from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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


class IsisObject(FortiObject[IsisPayload]):
    """Typed FortiObject for router/isis with IDE autocomplete support."""
    
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
    isis_net: list[str]  # Auto-flattened from member_table
    # IS-IS interface configuration.
    isis_interface: list[str]  # Auto-flattened from member_table
    # IS-IS summary addresses.
    summary_address: list[str]  # Auto-flattened from member_table
    # IS-IS IPv6 summary address.
    summary_address6: list[str]  # Auto-flattened from member_table
    # IS-IS redistribute protocols.
    redistribute: list[str]  # Auto-flattened from member_table
    # IS-IS IPv6 redistribution for routing protocols.
    redistribute6: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> IsisPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Isis:
    """
    Configure IS-IS.
    
    Path: router/isis
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
    ) -> IsisObject: ...
    
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
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | list[dict[str, Any]] | None = ...,
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
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | list[dict[str, Any]] | None = ...,
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
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | list[dict[str, Any]] | None = ...,
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
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | list[dict[str, Any]] | None = ...,
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
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | list[dict[str, Any]] | None = ...,
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