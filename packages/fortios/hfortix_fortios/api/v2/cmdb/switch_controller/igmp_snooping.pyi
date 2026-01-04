from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IgmpSnoopingPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/igmp_snooping payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IgmpSnoopingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    aging_time: NotRequired[int]  # Maximum number of seconds to retain a multicast snooping ent
    flood_unknown_multicast: NotRequired[Literal["enable", "disable"]]  # Enable/disable unknown multicast flooding.
    query_interval: NotRequired[int]  # Maximum time after which IGMP query will be sent (10 - 1200 


class IgmpSnooping:
    """
    Configure FortiSwitch IGMP snooping global settings.
    
    Path: switch_controller/igmp_snooping
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
        payload_dict: IgmpSnoopingPayload | None = ...,
        aging_time: int | None = ...,
        flood_unknown_multicast: Literal["enable", "disable"] | None = ...,
        query_interval: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IgmpSnoopingPayload | None = ...,
        aging_time: int | None = ...,
        flood_unknown_multicast: Literal["enable", "disable"] | None = ...,
        query_interval: int | None = ...,
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
        payload_dict: IgmpSnoopingPayload | None = ...,
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