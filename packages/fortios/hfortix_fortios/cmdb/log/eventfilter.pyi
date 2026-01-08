from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class EventfilterPayload(TypedDict, total=False):
    """
    Type hints for log/eventfilter payload fields.
    
    Configure log event filters.
    
    **Usage:**
        payload: EventfilterPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    event: NotRequired[Literal["enable", "disable"]]  # Enable/disable event logging.
    system: NotRequired[Literal["enable", "disable"]]  # Enable/disable system event logging.
    vpn: NotRequired[Literal["enable", "disable"]]  # Enable/disable VPN event logging.
    user: NotRequired[Literal["enable", "disable"]]  # Enable/disable user authentication event logging.
    router: NotRequired[Literal["enable", "disable"]]  # Enable/disable router event logging.
    wireless_activity: NotRequired[Literal["enable", "disable"]]  # Enable/disable wireless event logging.
    wan_opt: NotRequired[Literal["enable", "disable"]]  # Enable/disable WAN optimization event logging.
    endpoint: NotRequired[Literal["enable", "disable"]]  # Enable/disable endpoint event logging.
    ha: NotRequired[Literal["enable", "disable"]]  # Enable/disable ha event logging.
    security_rating: NotRequired[Literal["enable", "disable"]]  # Enable/disable Security Rating result logging.
    fortiextender: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiExtender logging.
    connector: NotRequired[Literal["enable", "disable"]]  # Enable/disable SDN connector logging.
    sdwan: NotRequired[Literal["enable", "disable"]]  # Enable/disable SD-WAN logging.
    cifs: NotRequired[Literal["enable", "disable"]]  # Enable/disable CIFS logging.
    switch_controller: NotRequired[Literal["enable", "disable"]]  # Enable/disable Switch-Controller logging.
    rest_api: NotRequired[Literal["enable", "disable"]]  # Enable/disable REST API logging.
    web_svc: NotRequired[Literal["enable", "disable"]]  # Enable/disable web-svc performance logging.
    webproxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable web proxy event logging.


class EventfilterObject(FortiObject[EventfilterPayload]):
    """Typed FortiObject for log/eventfilter with IDE autocomplete support."""
    
    # Enable/disable event logging.
    event: Literal["enable", "disable"]
    # Enable/disable system event logging.
    system: Literal["enable", "disable"]
    # Enable/disable VPN event logging.
    vpn: Literal["enable", "disable"]
    # Enable/disable user authentication event logging.
    user: Literal["enable", "disable"]
    # Enable/disable router event logging.
    router: Literal["enable", "disable"]
    # Enable/disable wireless event logging.
    wireless_activity: Literal["enable", "disable"]
    # Enable/disable WAN optimization event logging.
    wan_opt: Literal["enable", "disable"]
    # Enable/disable endpoint event logging.
    endpoint: Literal["enable", "disable"]
    # Enable/disable ha event logging.
    ha: Literal["enable", "disable"]
    # Enable/disable Security Rating result logging.
    security_rating: Literal["enable", "disable"]
    # Enable/disable FortiExtender logging.
    fortiextender: Literal["enable", "disable"]
    # Enable/disable SDN connector logging.
    connector: Literal["enable", "disable"]
    # Enable/disable SD-WAN logging.
    sdwan: Literal["enable", "disable"]
    # Enable/disable CIFS logging.
    cifs: Literal["enable", "disable"]
    # Enable/disable Switch-Controller logging.
    switch_controller: Literal["enable", "disable"]
    # Enable/disable REST API logging.
    rest_api: Literal["enable", "disable"]
    # Enable/disable web-svc performance logging.
    web_svc: Literal["enable", "disable"]
    # Enable/disable web proxy event logging.
    webproxy: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> EventfilterPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Eventfilter:
    """
    Configure log event filters.
    
    Path: log/eventfilter
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
    ) -> EventfilterObject: ...
    
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
    ) -> EventfilterObject: ...
    
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
    ) -> EventfilterObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: EventfilterPayload | None = ...,
        event: Literal["enable", "disable"] | None = ...,
        system: Literal["enable", "disable"] | None = ...,
        vpn: Literal["enable", "disable"] | None = ...,
        user: Literal["enable", "disable"] | None = ...,
        router: Literal["enable", "disable"] | None = ...,
        wireless_activity: Literal["enable", "disable"] | None = ...,
        wan_opt: Literal["enable", "disable"] | None = ...,
        endpoint: Literal["enable", "disable"] | None = ...,
        ha: Literal["enable", "disable"] | None = ...,
        security_rating: Literal["enable", "disable"] | None = ...,
        fortiextender: Literal["enable", "disable"] | None = ...,
        connector: Literal["enable", "disable"] | None = ...,
        sdwan: Literal["enable", "disable"] | None = ...,
        cifs: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["enable", "disable"] | None = ...,
        rest_api: Literal["enable", "disable"] | None = ...,
        web_svc: Literal["enable", "disable"] | None = ...,
        webproxy: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> EventfilterObject: ...
    
    @overload
    def put(
        self,
        payload_dict: EventfilterPayload | None = ...,
        event: Literal["enable", "disable"] | None = ...,
        system: Literal["enable", "disable"] | None = ...,
        vpn: Literal["enable", "disable"] | None = ...,
        user: Literal["enable", "disable"] | None = ...,
        router: Literal["enable", "disable"] | None = ...,
        wireless_activity: Literal["enable", "disable"] | None = ...,
        wan_opt: Literal["enable", "disable"] | None = ...,
        endpoint: Literal["enable", "disable"] | None = ...,
        ha: Literal["enable", "disable"] | None = ...,
        security_rating: Literal["enable", "disable"] | None = ...,
        fortiextender: Literal["enable", "disable"] | None = ...,
        connector: Literal["enable", "disable"] | None = ...,
        sdwan: Literal["enable", "disable"] | None = ...,
        cifs: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["enable", "disable"] | None = ...,
        rest_api: Literal["enable", "disable"] | None = ...,
        web_svc: Literal["enable", "disable"] | None = ...,
        webproxy: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: EventfilterPayload | None = ...,
        event: Literal["enable", "disable"] | None = ...,
        system: Literal["enable", "disable"] | None = ...,
        vpn: Literal["enable", "disable"] | None = ...,
        user: Literal["enable", "disable"] | None = ...,
        router: Literal["enable", "disable"] | None = ...,
        wireless_activity: Literal["enable", "disable"] | None = ...,
        wan_opt: Literal["enable", "disable"] | None = ...,
        endpoint: Literal["enable", "disable"] | None = ...,
        ha: Literal["enable", "disable"] | None = ...,
        security_rating: Literal["enable", "disable"] | None = ...,
        fortiextender: Literal["enable", "disable"] | None = ...,
        connector: Literal["enable", "disable"] | None = ...,
        sdwan: Literal["enable", "disable"] | None = ...,
        cifs: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["enable", "disable"] | None = ...,
        rest_api: Literal["enable", "disable"] | None = ...,
        web_svc: Literal["enable", "disable"] | None = ...,
        webproxy: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: EventfilterPayload | None = ...,
        event: Literal["enable", "disable"] | None = ...,
        system: Literal["enable", "disable"] | None = ...,
        vpn: Literal["enable", "disable"] | None = ...,
        user: Literal["enable", "disable"] | None = ...,
        router: Literal["enable", "disable"] | None = ...,
        wireless_activity: Literal["enable", "disable"] | None = ...,
        wan_opt: Literal["enable", "disable"] | None = ...,
        endpoint: Literal["enable", "disable"] | None = ...,
        ha: Literal["enable", "disable"] | None = ...,
        security_rating: Literal["enable", "disable"] | None = ...,
        fortiextender: Literal["enable", "disable"] | None = ...,
        connector: Literal["enable", "disable"] | None = ...,
        sdwan: Literal["enable", "disable"] | None = ...,
        cifs: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["enable", "disable"] | None = ...,
        rest_api: Literal["enable", "disable"] | None = ...,
        web_svc: Literal["enable", "disable"] | None = ...,
        webproxy: Literal["enable", "disable"] | None = ...,
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
        payload_dict: EventfilterPayload | None = ...,
        event: Literal["enable", "disable"] | None = ...,
        system: Literal["enable", "disable"] | None = ...,
        vpn: Literal["enable", "disable"] | None = ...,
        user: Literal["enable", "disable"] | None = ...,
        router: Literal["enable", "disable"] | None = ...,
        wireless_activity: Literal["enable", "disable"] | None = ...,
        wan_opt: Literal["enable", "disable"] | None = ...,
        endpoint: Literal["enable", "disable"] | None = ...,
        ha: Literal["enable", "disable"] | None = ...,
        security_rating: Literal["enable", "disable"] | None = ...,
        fortiextender: Literal["enable", "disable"] | None = ...,
        connector: Literal["enable", "disable"] | None = ...,
        sdwan: Literal["enable", "disable"] | None = ...,
        cifs: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["enable", "disable"] | None = ...,
        rest_api: Literal["enable", "disable"] | None = ...,
        web_svc: Literal["enable", "disable"] | None = ...,
        webproxy: Literal["enable", "disable"] | None = ...,
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
    "Eventfilter",
    "EventfilterPayload",
    "EventfilterObject",
]