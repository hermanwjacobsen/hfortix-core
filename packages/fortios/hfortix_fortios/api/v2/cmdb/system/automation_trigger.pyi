from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AutomationTriggerPayload(TypedDict, total=False):
    """
    Type hints for system/automation_trigger payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AutomationTriggerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name.
    description: NotRequired[str]  # Description.
    trigger_type: NotRequired[Literal["event-based", "scheduled"]]  # Trigger type.
    event_type: NotRequired[Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"]]  # Event type.
    vdom: NotRequired[list[dict[str, Any]]]  # Virtual domain(s) that this trigger is valid for.
    license_type: NotRequired[Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"]]  # License type.
    report_type: NotRequired[Literal["posture", "coverage", "optimization", "any"]]  # Security Rating report.
    stitch_name: str  # Triggering stitch name.
    logid: NotRequired[list[dict[str, Any]]]  # Log IDs to trigger event.
    trigger_frequency: NotRequired[Literal["hourly", "daily", "weekly", "monthly", "once"]]  # Scheduled trigger frequency (default = daily).
    trigger_weekday: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]]  # Day of week for trigger.
    trigger_day: NotRequired[int]  # Day within a month to trigger.
    trigger_hour: NotRequired[int]  # Hour of the day on which to trigger (0 - 23, default = 1).
    trigger_minute: NotRequired[int]  # Minute of the hour on which to trigger (0 - 59, default = 0)
    trigger_datetime: NotRequired[str]  # Trigger date and time (YYYY-MM-DD HH:MM:SS).
    fields: NotRequired[list[dict[str, Any]]]  # Customized trigger field settings.
    faz_event_name: str  # FortiAnalyzer event handler name.
    faz_event_severity: NotRequired[str]  # FortiAnalyzer event severity.
    faz_event_tags: NotRequired[str]  # FortiAnalyzer event tags.
    serial: str  # Fabric connector serial number.
    fabric_event_name: str  # Fabric connector event handler name.
    fabric_event_severity: NotRequired[str]  # Fabric connector event severity.


class AutomationTrigger:
    """
    Trigger for automation stitches.
    
    Path: system/automation_trigger
    Category: cmdb
    Primary Key: name
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
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
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
        payload_dict: AutomationTriggerPayload | None = ...,
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


__all__ = [
    "AutomationTrigger",
    "AutomationTriggerPayload",
]