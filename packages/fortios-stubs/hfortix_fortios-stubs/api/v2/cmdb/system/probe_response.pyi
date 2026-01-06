from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class ProbeResponsePayload(TypedDict, total=False):
    """
    Type hints for system/probe_response payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: ProbeResponsePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    port: NotRequired[int]  # Port number to response.
    http_probe_value: NotRequired[str]  # Value to respond to the monitoring server.
    ttl_mode: NotRequired[Literal[{"description": "Reinitialize TTL", "help": "Reinitialize TTL.", "label": "Reinit", "name": "reinit"}, {"description": "Decrease TTL", "help": "Decrease TTL.", "label": "Decrease", "name": "decrease"}, {"description": "Retain TTL", "help": "Retain TTL.", "label": "Retain", "name": "retain"}]]  # Mode for TWAMP packet TTL modification.
    mode: NotRequired[Literal[{"description": "Disable probe", "help": "Disable probe.", "label": "None", "name": "none"}, {"description": "HTTP probe", "help": "HTTP probe.", "label": "Http Probe", "name": "http-probe"}, {"description": "Two way active measurement protocol", "help": "Two way active measurement protocol.", "label": "Twamp", "name": "twamp"}]]  # SLA response mode.
    security_mode: NotRequired[Literal[{"description": "Unauthenticated mode", "help": "Unauthenticated mode.", "label": "None", "name": "none"}, {"description": "Authenticated mode", "help": "Authenticated mode.", "label": "Authentication", "name": "authentication"}]]  # TWAMP responder security mode.
    password: NotRequired[str]  # TWAMP responder password in authentication mode.
    timeout: NotRequired[int]  # An inactivity timer for a twamp test session.


class ProbeResponse:
    """
    Configure system probe response.
    
    Path: system/probe_response
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
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal[{"description": "Reinitialize TTL", "help": "Reinitialize TTL.", "label": "Reinit", "name": "reinit"}, {"description": "Decrease TTL", "help": "Decrease TTL.", "label": "Decrease", "name": "decrease"}, {"description": "Retain TTL", "help": "Retain TTL.", "label": "Retain", "name": "retain"}] | None = ...,
        mode: Literal[{"description": "Disable probe", "help": "Disable probe.", "label": "None", "name": "none"}, {"description": "HTTP probe", "help": "HTTP probe.", "label": "Http Probe", "name": "http-probe"}, {"description": "Two way active measurement protocol", "help": "Two way active measurement protocol.", "label": "Twamp", "name": "twamp"}] | None = ...,
        security_mode: Literal[{"description": "Unauthenticated mode", "help": "Unauthenticated mode.", "label": "None", "name": "none"}, {"description": "Authenticated mode", "help": "Authenticated mode.", "label": "Authentication", "name": "authentication"}] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: ProbeResponsePayload | None = ...,
        port: int | None = ...,
        http_probe_value: str | None = ...,
        ttl_mode: Literal[{"description": "Reinitialize TTL", "help": "Reinitialize TTL.", "label": "Reinit", "name": "reinit"}, {"description": "Decrease TTL", "help": "Decrease TTL.", "label": "Decrease", "name": "decrease"}, {"description": "Retain TTL", "help": "Retain TTL.", "label": "Retain", "name": "retain"}] | None = ...,
        mode: Literal[{"description": "Disable probe", "help": "Disable probe.", "label": "None", "name": "none"}, {"description": "HTTP probe", "help": "HTTP probe.", "label": "Http Probe", "name": "http-probe"}, {"description": "Two way active measurement protocol", "help": "Two way active measurement protocol.", "label": "Twamp", "name": "twamp"}] | None = ...,
        security_mode: Literal[{"description": "Unauthenticated mode", "help": "Unauthenticated mode.", "label": "None", "name": "none"}, {"description": "Authenticated mode", "help": "Authenticated mode.", "label": "Authentication", "name": "authentication"}] | None = ...,
        password: str | None = ...,
        timeout: int | None = ...,
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
        payload_dict: ProbeResponsePayload | None = ...,
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
    "ProbeResponse",
    "ProbeResponsePayload",
]