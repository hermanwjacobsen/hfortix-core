from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class InterControllerPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/inter_controller payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: InterControllerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    inter_controller_mode: NotRequired[Literal["disable", "l2-roaming", "1+1"]]  # Configure inter-controller mode (disable, l2-roaming, 1+1, d
    l3_roaming: NotRequired[Literal["enable", "disable"]]  # Enable/disable layer 3 roaming (default = disable).
    inter_controller_key: NotRequired[str]  # Secret key for inter-controller communications.
    inter_controller_pri: NotRequired[Literal["primary", "secondary"]]  # Configure inter-controller's priority (primary or secondary,
    fast_failover_max: NotRequired[int]  # Maximum number of retransmissions for fast failover HA messa
    fast_failover_wait: NotRequired[int]  # Minimum wait time before an AP transitions from secondary co
    inter_controller_peer: NotRequired[list[dict[str, Any]]]  # Fast failover peer wireless controller list.


class InterController:
    """
    Configure inter wireless controller operation.
    
    Path: wireless_controller/inter_controller
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
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: list[dict[str, Any]] | None = ...,
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
        payload_dict: InterControllerPayload | None = ...,
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