from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IsisPayload(TypedDict, total=False):
    """
    Type hints for router/isis payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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


class Isis:
    """
    Configure IS-IS.
    
    Path: router/isis
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: IsisPayload | None = ...,
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