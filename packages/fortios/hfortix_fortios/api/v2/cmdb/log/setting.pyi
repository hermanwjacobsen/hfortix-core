from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/setting payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    long_live_session_stat: NotRequired[Literal["enable", "disable"]]  # Enable/disable long-live-session statistics logging.
    extended_utm_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended UTM logging.
    zone_name: NotRequired[Literal["enable", "disable"]]  # Enable/disable zone name logging.
    custom_log_fields: NotRequired[list[dict[str, Any]]]  # Custom fields to append to all log messages.
    anonymization_hash: NotRequired[str]  # User name anonymization hash salt.


class Setting:
    """
    Configure general log settings.
    
    Path: log/setting
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        payload_dict: SettingPayload | None = ...,
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