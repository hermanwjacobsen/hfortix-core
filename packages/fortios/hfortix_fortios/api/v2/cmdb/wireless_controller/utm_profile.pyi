from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class UtmProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/utm_profile payload fields.
    
    Configure UTM (Unified Threat Management) profile.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: antivirus-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.ips.sensor.SensorEndpoint` (via: ips-sensor)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: webfilter-profile)

    **Usage:**
        payload: UtmProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # UTM profile name.
    comment: NotRequired[str]  # Comment.
    utm_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable UTM logging.
    ips_sensor: NotRequired[str]  # IPS sensor name.
    application_list: NotRequired[str]  # Application control list name.
    antivirus_profile: NotRequired[str]  # AntiVirus profile name.
    webfilter_profile: NotRequired[str]  # WebFilter profile name.
    scan_botnet_connections: NotRequired[Literal["disable", "monitor", "block"]]  # Block or monitor connections to Botnet servers or disable Bo

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class UtmProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/utm_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    utm_log: Literal["enable", "disable"]
    ips_sensor: str
    application_list: str
    antivirus_profile: str
    webfilter_profile: str
    scan_botnet_connections: Literal["disable", "monitor", "block"]


@final
class UtmProfileObject:
    """Typed FortiObject for wireless_controller/utm_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # UTM profile name.
    name: str
    # Comment.
    comment: str
    # Enable/disable UTM logging.
    utm_log: Literal["enable", "disable"]
    # IPS sensor name.
    ips_sensor: str
    # Application control list name.
    application_list: str
    # AntiVirus profile name.
    antivirus_profile: str
    # WebFilter profile name.
    webfilter_profile: str
    # Block or monitor connections to Botnet servers or disable Botnet scanning.
    scan_botnet_connections: Literal["disable", "monitor", "block"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> UtmProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class UtmProfile:
    """
    Configure UTM (Unified Threat Management) profile.
    
    Path: wireless_controller/utm_profile
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
    ) -> UtmProfileObject: ...
    
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
    ) -> UtmProfileObject: ...
    
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
    ) -> list[UtmProfileObject]: ...
    
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
    ) -> UtmProfileResponse: ...
    
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
    ) -> UtmProfileResponse: ...
    
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
    ) -> list[UtmProfileResponse]: ...
    
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
    ) -> UtmProfileObject | list[UtmProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UtmProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> UtmProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
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
    ) -> UtmProfileObject: ...
    
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
        payload_dict: UtmProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
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
    "UtmProfile",
    "UtmProfilePayload",
    "UtmProfileObject",
]