from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class AutoConfigPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch-controller/auto_config_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: AutoConfigPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Auto-config policy name.
    qos_policy: NotRequired[str]  # Auto-Config QoS policy.
    storm_control_policy: NotRequired[str]  # Auto-Config storm control policy.
    poe_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable PoE status.
    igmp_flood_report: NotRequired[Literal["enable", "disable"]]  # Enable/disable IGMP flood report.
    igmp_flood_traffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable IGMP flood traffic.


class AutoConfigPolicy:
    """
    Policy definitions which can define the behavior on auto configured interfaces.
    
    Path: switch-controller/auto_config_policy
    Category: cmdb
    Primary Key: name
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
        payload_dict: AutoConfigPolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: AutoConfigPolicyPayload | None = ...,
        name: str | None = ...,
        qos_policy: str | None = ...,
        storm_control_policy: str | None = ...,
        poe_status: Literal["enable", "disable"] | None = ...,
        igmp_flood_report: Literal["enable", "disable"] | None = ...,
        igmp_flood_traffic: Literal["enable", "disable"] | None = ...,
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
        payload_dict: AutoConfigPolicyPayload | None = ...,
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