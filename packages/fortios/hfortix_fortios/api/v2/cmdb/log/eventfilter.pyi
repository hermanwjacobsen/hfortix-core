from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class EventfilterPayload(TypedDict, total=False):
    """
    Type hints for log/eventfilter payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    webproxy: NotRequired[Literal["enable", "disable"]]  # Enable/disable web proxy event logging.


class Eventfilter:
    """
    Configure log event filters.
    
    Path: log/eventfilter
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
        webproxy: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        webproxy: Literal["enable", "disable"] | None = ...,
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
        payload_dict: EventfilterPayload | None = ...,
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