from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class QosQosPolicyPayload(TypedDict, total=False):
    """
    Type hints for switch-controller/qos_qos_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: QosQosPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # QoS policy name.
    default_cos: int  # Default cos queue for untagged packets.
    trust_dot1p_map: NotRequired[str]  # QoS trust 802.1p map.
    trust_ip_dscp_map: NotRequired[str]  # QoS trust ip dscp map.
    queue_policy: NotRequired[str]  # QoS egress queue policy.


class QosQosPolicy:
    """
    Configure FortiSwitch QoS policy.
    
    Path: switch-controller/qos_qos_policy
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
        payload_dict: QosQosPolicyPayload | None = ...,
        name: str | None = ...,
        default_cos: int | None = ...,
        trust_dot1p_map: str | None = ...,
        trust_ip_dscp_map: str | None = ...,
        queue_policy: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: QosQosPolicyPayload | None = ...,
        name: str | None = ...,
        default_cos: int | None = ...,
        trust_dot1p_map: str | None = ...,
        trust_ip_dscp_map: str | None = ...,
        queue_policy: str | None = ...,
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
        payload_dict: QosQosPolicyPayload | None = ...,
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