from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class VdomSflowPayload(TypedDict, total=False):
    """
    Type hints for system/vdom_sflow payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: VdomSflowPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    vdom_sflow: NotRequired[Literal[{"description": "Enable sFlow for this VDOM", "help": "Enable sFlow for this VDOM.", "label": "Enable", "name": "enable"}, {"description": "Disable sFlow for this VDOM", "help": "Disable sFlow for this VDOM.", "label": "Disable", "name": "disable"}]]  # Enable/disable the sFlow configuration for the current VDOM.
    collectors: NotRequired[list[dict[str, Any]]]  # sFlow collectors.


class VdomSflow:
    """
    Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.
    
    Path: system/vdom_sflow
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
        payload_dict: VdomSflowPayload | None = ...,
        vdom_sflow: Literal[{"description": "Enable sFlow for this VDOM", "help": "Enable sFlow for this VDOM.", "label": "Enable", "name": "enable"}, {"description": "Disable sFlow for this VDOM", "help": "Disable sFlow for this VDOM.", "label": "Disable", "name": "disable"}] | None = ...,
        collectors: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: VdomSflowPayload | None = ...,
        vdom_sflow: Literal[{"description": "Enable sFlow for this VDOM", "help": "Enable sFlow for this VDOM.", "label": "Enable", "name": "enable"}, {"description": "Disable sFlow for this VDOM", "help": "Disable sFlow for this VDOM.", "label": "Disable", "name": "disable"}] | None = ...,
        collectors: list[dict[str, Any]] | None = ...,
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
        payload_dict: VdomSflowPayload | None = ...,
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
    "VdomSflow",
    "VdomSflowPayload",
]