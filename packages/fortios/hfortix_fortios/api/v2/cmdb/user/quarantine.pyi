from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class QuarantinePayload(TypedDict, total=False):
    """
    Type hints for user/quarantine payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: QuarantinePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    quarantine: NotRequired[Literal["enable", "disable"]]  # Enable/disable quarantine.
    traffic_policy: NotRequired[str]  # Traffic policy for quarantined MACs.
    firewall_groups: NotRequired[str]  # Firewall address group which includes all quarantine MAC add
    targets: NotRequired[list[dict[str, Any]]]  # Quarantine entry to hold multiple MACs.


class Quarantine:
    """
    Configure quarantine support.
    
    Path: user/quarantine
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
        payload_dict: QuarantinePayload | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        traffic_policy: str | None = ...,
        firewall_groups: str | None = ...,
        targets: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        traffic_policy: str | None = ...,
        firewall_groups: str | None = ...,
        targets: list[dict[str, Any]] | None = ...,
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
        payload_dict: QuarantinePayload | None = ...,
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