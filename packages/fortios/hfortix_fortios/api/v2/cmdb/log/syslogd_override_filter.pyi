from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class SyslogdOverrideFilterPayload(TypedDict, total=False):
    """
    Type hints for log/syslogd_override_filter payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: SyslogdOverrideFilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    severity: NotRequired[Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]]  # Lowest severity level to log.
    forward_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable forward traffic logging.
    local_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable local in or out traffic logging.
    multicast_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable multicast traffic logging.
    sniffer_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable sniffer traffic logging.
    ztna_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable ztna traffic logging.
    http_transaction: NotRequired[Literal["enable", "disable"]]  # Enable/disable log HTTP transaction messages.
    anomaly: NotRequired[Literal["enable", "disable"]]  # Enable/disable anomaly logging.
    voip: NotRequired[Literal["enable", "disable"]]  # Enable/disable VoIP logging.
    gtp: NotRequired[Literal["enable", "disable"]]  # Enable/disable GTP messages logging.
    forti_switch: NotRequired[Literal["enable", "disable"]]  # Enable/disable Forti-Switch logging.
    debug: NotRequired[Literal["enable", "disable"]]  # Enable/disable debug logging.
    free_style: NotRequired[list[dict[str, Any]]]  # Free style filters.


class SyslogdOverrideFilter:
    """
    Override filters for remote system server.
    
    Path: log/syslogd_override_filter
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
        payload_dict: SyslogdOverrideFilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: SyslogdOverrideFilterPayload | None = ...,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        forward_traffic: Literal["enable", "disable"] | None = ...,
        local_traffic: Literal["enable", "disable"] | None = ...,
        multicast_traffic: Literal["enable", "disable"] | None = ...,
        sniffer_traffic: Literal["enable", "disable"] | None = ...,
        ztna_traffic: Literal["enable", "disable"] | None = ...,
        http_transaction: Literal["enable", "disable"] | None = ...,
        anomaly: Literal["enable", "disable"] | None = ...,
        voip: Literal["enable", "disable"] | None = ...,
        gtp: Literal["enable", "disable"] | None = ...,
        forti_switch: Literal["enable", "disable"] | None = ...,
        debug: Literal["enable", "disable"] | None = ...,
        free_style: list[dict[str, Any]] | None = ...,
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
        payload_dict: SyslogdOverrideFilterPayload | None = ...,
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