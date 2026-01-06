from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class DosPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/DoS_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: DosPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID.
    status: NotRequired[Literal[{"description": "Enable this policy", "help": "Enable this policy.", "label": "Enable", "name": "enable"}, {"description": "Disable this policy", "help": "Disable this policy.", "label": "Disable", "name": "disable"}]]  # Enable/disable this policy.
    name: NotRequired[str]  # Policy name.
    comments: NotRequired[str]  # Comment.
    interface: str  # Incoming interface name from available interfaces.
    srcaddr: list[dict[str, Any]]  # Source address name from available addresses.
    dstaddr: list[dict[str, Any]]  # Destination address name from available addresses.
    service: list[dict[str, Any]]  # Service object from available options.
    anomaly: NotRequired[list[dict[str, Any]]]  # Anomaly name.


class DosPolicy:
    """
    Configure IPv4 DoS policies.
    
    Path: firewall/DoS_policy
    Category: cmdb
    Primary Key: policyid
    """
    
    def get(
        self,
        policyid: int | None = ...,
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
        payload_dict: DosPolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal[{"description": "Enable this policy", "help": "Enable this policy.", "label": "Enable", "name": "enable"}, {"description": "Disable this policy", "help": "Disable this policy.", "label": "Disable", "name": "disable"}] | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        interface: str | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        anomaly: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: DosPolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal[{"description": "Enable this policy", "help": "Enable this policy.", "label": "Enable", "name": "enable"}, {"description": "Disable this policy", "help": "Disable this policy.", "label": "Disable", "name": "disable"}] | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        interface: str | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        anomaly: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: DosPolicyPayload | None = ...,
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
    "DosPolicy",
    "DosPolicyPayload",
]