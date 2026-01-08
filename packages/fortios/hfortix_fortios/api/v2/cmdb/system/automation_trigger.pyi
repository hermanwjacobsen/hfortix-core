from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AutomationTriggerPayload(TypedDict, total=False):
    """
    Type hints for system/automation_trigger payload fields.
    
    Trigger for automation stitches.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.automation-stitch.AutomationStitchEndpoint` (via: stitch-name)

    **Usage:**
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

# Nested classes for table field children

@final
class AutomationTriggerVdomObject:
    """Typed object for vdom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual domain name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationTriggerLogidObject:
    """Typed object for logid table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Log ID.
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class AutomationTriggerFieldsObject:
    """Typed object for fields table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID.
    id: int
    # Name.
    name: str
    # Value.
    value: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class AutomationTriggerResponse(TypedDict):
    """
    Type hints for system/automation_trigger API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    description: str
    trigger_type: Literal["event-based", "scheduled"]
    event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"]
    vdom: list[dict[str, Any]]
    license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"]
    report_type: Literal["posture", "coverage", "optimization", "any"]
    stitch_name: str
    logid: list[dict[str, Any]]
    trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"]
    trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    trigger_day: int
    trigger_hour: int
    trigger_minute: int
    trigger_datetime: str
    fields: list[dict[str, Any]]
    faz_event_name: str
    faz_event_severity: str
    faz_event_tags: str
    serial: str
    fabric_event_name: str
    fabric_event_severity: str


@final
class AutomationTriggerObject:
    """Typed FortiObject for system/automation_trigger with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name.
    name: str
    # Description.
    description: str
    # Trigger type.
    trigger_type: Literal["event-based", "scheduled"]
    # Event type.
    event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"]
    # Virtual domain(s) that this trigger is valid for.
    vdom: list[AutomationTriggerVdomObject]  # Table field - list of typed objects
    # License type.
    license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"]
    # Security Rating report.
    report_type: Literal["posture", "coverage", "optimization", "any"]
    # Triggering stitch name.
    stitch_name: str
    # Log IDs to trigger event.
    logid: list[AutomationTriggerLogidObject]  # Table field - list of typed objects
    # Scheduled trigger frequency (default = daily).
    trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"]
    # Day of week for trigger.
    trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Day within a month to trigger.
    trigger_day: int
    # Hour of the day on which to trigger (0 - 23, default = 1).
    trigger_hour: int
    # Minute of the hour on which to trigger (0 - 59, default = 0).
    trigger_minute: int
    # Trigger date and time (YYYY-MM-DD HH:MM:SS).
    trigger_datetime: str
    # Customized trigger field settings.
    fields: list[AutomationTriggerFieldsObject]  # Table field - list of typed objects
    # FortiAnalyzer event handler name.
    faz_event_name: str
    # FortiAnalyzer event severity.
    faz_event_severity: str
    # FortiAnalyzer event tags.
    faz_event_tags: str
    # Fabric connector serial number.
    serial: str
    # Fabric connector event handler name.
    fabric_event_name: str
    # Fabric connector event severity.
    fabric_event_severity: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AutomationTriggerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AutomationTrigger:
    """
    Trigger for automation stitches.
    
    Path: system/automation_trigger
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> AutomationTriggerObject: ...
    
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
    ) -> list[AutomationTriggerObject]: ...
    
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
    ) -> AutomationTriggerResponse: ...
    
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
    ) -> AutomationTriggerResponse: ...
    
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
    ) -> list[AutomationTriggerResponse]: ...
    
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
    ) -> AutomationTriggerObject | list[AutomationTriggerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationTriggerObject: ...
    
    @overload
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AutomationTriggerObject: ...
    
    @overload
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
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
    ) -> AutomationTriggerObject: ...
    
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
        payload_dict: AutomationTriggerPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        trigger_type: Literal["event-based", "scheduled"] | None = ...,
        event_type: Literal["ioc", "event-log", "reboot", "low-memory", "high-cpu", "license-near-expiry", "local-cert-near-expiry", "ha-failover", "config-change", "security-rating-summary", "virus-ips-db-updated", "faz-event", "incoming-webhook", "fabric-event", "ips-logs", "anomaly-logs", "virus-logs", "ssh-logs", "webfilter-violation", "traffic-violation", "stitch"] | None = ...,
        license_type: Literal["forticare-support", "fortiguard-webfilter", "fortiguard-antispam", "fortiguard-antivirus", "fortiguard-ips", "fortiguard-management", "forticloud", "any"] | None = ...,
        report_type: Literal["posture", "coverage", "optimization", "any"] | None = ...,
        stitch_name: str | None = ...,
        logid: str | list[str] | list[dict[str, Any]] | None = ...,
        trigger_frequency: Literal["hourly", "daily", "weekly", "monthly", "once"] | None = ...,
        trigger_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        trigger_day: int | None = ...,
        trigger_hour: int | None = ...,
        trigger_minute: int | None = ...,
        trigger_datetime: str | None = ...,
        fields: str | list[str] | list[dict[str, Any]] | None = ...,
        faz_event_name: str | None = ...,
        faz_event_severity: str | None = ...,
        faz_event_tags: str | None = ...,
        serial: str | None = ...,
        fabric_event_name: str | None = ...,
        fabric_event_severity: str | None = ...,
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
    "AutomationTrigger",
    "AutomationTriggerPayload",
    "AutomationTriggerObject",
]