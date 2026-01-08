from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SensorPayload(TypedDict, total=False):
    """
    Type hints for ips/sensor payload fields.
    
    Configure IPS sensor.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: SensorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Sensor name.
    comment: NotRequired[str]  # Comment.
    replacemsg_group: NotRequired[str]  # Replacement message group.
    block_malicious_url: NotRequired[Literal["disable", "enable"]]  # Enable/disable malicious URL blocking.
    scan_botnet_connections: NotRequired[Literal["disable", "block", "monitor"]]  # Block or monitor connections to Botnet servers, or disable B
    extended_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable extended logging.
    entries: NotRequired[list[dict[str, Any]]]  # IPS sensor filter.

# Nested classes for table field children

@final
class SensorEntriesObject:
    """Typed object for entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Rule ID in IPS database (0 - 4294967295).
    id: int
    # Identifies the predefined or custom IPS signatures to add to the sensor.
    rule: str
    # Protect client or server traffic.
    location: str
    # Relative severity of the signature, from info to critical. Log messages generate
    severity: str
    # Protocols to be examined. Use all for every protocol and other for unlisted prot
    protocol: str
    # Operating systems to be protected. Use all for every operating system and other
    os: str
    # Operating systems to be protected. Use all for every application and other for u
    application: str
    # Signature default action filter.
    default_action: Literal["all", "pass", "block"]
    # Signature default status filter.
    default_status: Literal["all", "enable", "disable"]
    # List of CVE IDs of the signatures to add to the sensor.
    cve: str
    # List of signature vulnerability types to filter by.
    vuln_type: str
    # Filter by signature last modified date. Formats: before <date>, after <date>, be
    last_modified: str
    # Status of the signatures included in filter. Only those filters with a status to
    status: Literal["disable", "enable", "default"]
    # Enable/disable logging of signatures included in filter.
    log: Literal["disable", "enable"]
    # Enable/disable packet logging. Enable to save the packet that triggers the filte
    log_packet: Literal["disable", "enable"]
    # Enable/disable logging of attack context: URL buffer, header buffer, body buffer
    log_attack_context: Literal["disable", "enable"]
    # Action taken with traffic in which signatures are detected.
    action: Literal["pass", "block", "reset", "default"]
    # Count of the rate.
    rate_count: int
    # Duration (sec) of the rate.
    rate_duration: int
    # Rate limit mode.
    rate_mode: Literal["periodical", "continuous"]
    # Track the packet protocol field.
    rate_track: Literal["none", "src-ip", "dest-ip", "dhcp-client-mac", "dns-domain"]
    # Traffic from selected source or destination IP addresses is exempt from this sig
    exempt_ip: str
    # Quarantine method.
    quarantine: Literal["none", "attacker"]
    # Duration of quarantine.
    quarantine_expiry: str
    # Enable/disable quarantine logging.
    quarantine_log: Literal["disable", "enable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SensorResponse(TypedDict):
    """
    Type hints for ips/sensor API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    replacemsg_group: str
    block_malicious_url: Literal["disable", "enable"]
    scan_botnet_connections: Literal["disable", "block", "monitor"]
    extended_log: Literal["enable", "disable"]
    entries: list[dict[str, Any]]


@final
class SensorObject:
    """Typed FortiObject for ips/sensor with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Sensor name.
    name: str
    # Comment.
    comment: str
    # Replacement message group.
    replacemsg_group: str
    # Enable/disable malicious URL blocking.
    block_malicious_url: Literal["disable", "enable"]
    # Block or monitor connections to Botnet servers, or disable Botnet scanning.
    scan_botnet_connections: Literal["disable", "block", "monitor"]
    # Enable/disable extended logging.
    extended_log: Literal["enable", "disable"]
    # IPS sensor filter.
    entries: list[SensorEntriesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SensorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Sensor:
    """
    Configure IPS sensor.
    
    Path: ips/sensor
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
    ) -> SensorObject: ...
    
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
    ) -> SensorObject: ...
    
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
    ) -> list[SensorObject]: ...
    
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
    ) -> SensorResponse: ...
    
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
    ) -> SensorResponse: ...
    
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
    ) -> list[SensorResponse]: ...
    
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
    ) -> SensorObject | list[SensorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SensorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> SensorObject: ...
    
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
        payload_dict: SensorPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        block_malicious_url: Literal["disable", "enable"] | None = ...,
        scan_botnet_connections: Literal["disable", "block", "monitor"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Sensor",
    "SensorPayload",
    "SensorObject",
]