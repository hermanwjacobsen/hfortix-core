from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/setting payload fields.
    
    Configure general log settings.
    
    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    resolve_ip: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding resolved domain names to traffic logs
    resolve_port: NotRequired[Literal["enable", "disable"]]  # Enable/disable adding resolved service names to traffic logs
    log_user_in_upper: NotRequired[Literal["enable", "disable"]]  # Enable/disable logs with user-in-upper.
    fwpolicy_implicit_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable implicit firewall policy logging.
    fwpolicy6_implicit_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable implicit firewall policy6 logging.
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended traffic logging.
    local_in_allow: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-in-allow logging.
    local_in_deny_unicast: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-in-deny-unicast logging.
    local_in_deny_broadcast: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-in-deny-broadcast logging.
    local_in_policy_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-in-policy logging.
    local_out: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-out logging.
    local_out_ioc_detection: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-out traffic IoC detection. Requires loc
    daemon_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable daemon logging.
    neighbor_event: NotRequired[Literal["enable", "disable"]]  # Enable/disable neighbor event logging.
    brief_traffic_format: NotRequired[Literal["enable", "disable"]]  # Enable/disable brief format traffic logging.
    user_anonymize: NotRequired[Literal["enable", "disable"]]  # Enable/disable anonymizing user names in log messages.
    expolicy_implicit_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable proxy firewall implicit policy logging.
    log_policy_comment: NotRequired[Literal["enable", "disable"]]  # Enable/disable inserting policy comments into traffic logs.
    faz_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable override FortiAnalyzer settings.
    syslog_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable override Syslog settings.
    rest_api_set: NotRequired[Literal["enable", "disable"]]  # Enable/disable REST API POST/PUT/DELETE request logging.
    rest_api_get: NotRequired[Literal["enable", "disable"]]  # Enable/disable REST API GET request logging.
    rest_api_performance: NotRequired[Literal["enable", "disable"]]  # Enable/disable REST API memory and performance stats in rest
    long_live_session_stat: NotRequired[Literal["enable", "disable"]]  # Enable/disable long-live-session statistics logging.
    extended_utm_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended UTM logging.
    zone_name: NotRequired[Literal["enable", "disable"]]  # Enable/disable zone name logging.
    web_svc_perf: NotRequired[Literal["enable", "disable"]]  # Enable/disable web-svc performance logging.
    custom_log_fields: NotRequired[list[dict[str, Any]]]  # Custom fields to append to all log messages.
    anonymization_hash: NotRequired[str]  # User name anonymization hash salt.

# Nested classes for table field children

@final
class SettingCustomlogfieldsObject:
    """Typed object for custom-log-fields table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom log field.
    field_id: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for log/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    resolve_ip: Literal["enable", "disable"]
    resolve_port: Literal["enable", "disable"]
    log_user_in_upper: Literal["enable", "disable"]
    fwpolicy_implicit_log: Literal["enable", "disable"]
    fwpolicy6_implicit_log: Literal["enable", "disable"]
    extended_log: Literal["enable", "disable"]
    local_in_allow: Literal["enable", "disable"]
    local_in_deny_unicast: Literal["enable", "disable"]
    local_in_deny_broadcast: Literal["enable", "disable"]
    local_in_policy_log: Literal["enable", "disable"]
    local_out: Literal["enable", "disable"]
    local_out_ioc_detection: Literal["enable", "disable"]
    daemon_log: Literal["enable", "disable"]
    neighbor_event: Literal["enable", "disable"]
    brief_traffic_format: Literal["enable", "disable"]
    user_anonymize: Literal["enable", "disable"]
    expolicy_implicit_log: Literal["enable", "disable"]
    log_policy_comment: Literal["enable", "disable"]
    faz_override: Literal["enable", "disable"]
    syslog_override: Literal["enable", "disable"]
    rest_api_set: Literal["enable", "disable"]
    rest_api_get: Literal["enable", "disable"]
    rest_api_performance: Literal["enable", "disable"]
    long_live_session_stat: Literal["enable", "disable"]
    extended_utm_log: Literal["enable", "disable"]
    zone_name: Literal["enable", "disable"]
    web_svc_perf: Literal["enable", "disable"]
    custom_log_fields: list[dict[str, Any]]
    anonymization_hash: str


@final
class SettingObject:
    """Typed FortiObject for log/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable adding resolved domain names to traffic logs if possible.
    resolve_ip: Literal["enable", "disable"]
    # Enable/disable adding resolved service names to traffic logs.
    resolve_port: Literal["enable", "disable"]
    # Enable/disable logs with user-in-upper.
    log_user_in_upper: Literal["enable", "disable"]
    # Enable/disable implicit firewall policy logging.
    fwpolicy_implicit_log: Literal["enable", "disable"]
    # Enable/disable implicit firewall policy6 logging.
    fwpolicy6_implicit_log: Literal["enable", "disable"]
    # Enable/disable extended traffic logging.
    extended_log: Literal["enable", "disable"]
    # Enable/disable local-in-allow logging.
    local_in_allow: Literal["enable", "disable"]
    # Enable/disable local-in-deny-unicast logging.
    local_in_deny_unicast: Literal["enable", "disable"]
    # Enable/disable local-in-deny-broadcast logging.
    local_in_deny_broadcast: Literal["enable", "disable"]
    # Enable/disable local-in-policy logging.
    local_in_policy_log: Literal["enable", "disable"]
    # Enable/disable local-out logging.
    local_out: Literal["enable", "disable"]
    # Enable/disable local-out traffic IoC detection. Requires local-out to be enabled
    local_out_ioc_detection: Literal["enable", "disable"]
    # Enable/disable daemon logging.
    daemon_log: Literal["enable", "disable"]
    # Enable/disable neighbor event logging.
    neighbor_event: Literal["enable", "disable"]
    # Enable/disable brief format traffic logging.
    brief_traffic_format: Literal["enable", "disable"]
    # Enable/disable anonymizing user names in log messages.
    user_anonymize: Literal["enable", "disable"]
    # Enable/disable proxy firewall implicit policy logging.
    expolicy_implicit_log: Literal["enable", "disable"]
    # Enable/disable inserting policy comments into traffic logs.
    log_policy_comment: Literal["enable", "disable"]
    # Enable/disable override FortiAnalyzer settings.
    faz_override: Literal["enable", "disable"]
    # Enable/disable override Syslog settings.
    syslog_override: Literal["enable", "disable"]
    # Enable/disable REST API POST/PUT/DELETE request logging.
    rest_api_set: Literal["enable", "disable"]
    # Enable/disable REST API GET request logging.
    rest_api_get: Literal["enable", "disable"]
    # Enable/disable REST API memory and performance stats in rest-api-get/set logs.
    rest_api_performance: Literal["enable", "disable"]
    # Enable/disable long-live-session statistics logging.
    long_live_session_stat: Literal["enable", "disable"]
    # Enable/disable extended UTM logging.
    extended_utm_log: Literal["enable", "disable"]
    # Enable/disable zone name logging.
    zone_name: Literal["enable", "disable"]
    # Enable/disable web-svc performance logging.
    web_svc_perf: Literal["enable", "disable"]
    # Custom fields to append to all log messages.
    custom_log_fields: list[SettingCustomlogfieldsObject]  # Table field - list of typed objects
    # User name anonymization hash salt.
    anonymization_hash: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Setting:
    """
    Configure general log settings.
    
    Path: log/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
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
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
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