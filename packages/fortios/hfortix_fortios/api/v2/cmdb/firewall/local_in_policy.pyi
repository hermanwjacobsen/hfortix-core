from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class LocalInPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/local_in_policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: LocalInPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # User defined local in policy ID.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    ha_mgmt_intf_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable dedicating the HA management interface only f
    intf: list[dict[str, Any]]  # Incoming interface name from available options.
    srcaddr: list[dict[str, Any]]  # Source address object from available options.
    srcaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr specifies what the source address must 
    dstaddr: list[dict[str, Any]]  # Destination address object from available options.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this l
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    internet_service_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service source name.
    dstaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr specifies what the destination address 
    action: NotRequired[Literal["accept", "deny"]]  # Action performed on traffic matching the policy (default = d
    service: list[dict[str, Any]]  # Service object from available options.
    service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled service specifies what the service must NOT be.
    internet_service_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service-src specifies what the service
    schedule: str  # Schedule object from available options.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this local-in policy.
    virtual_patch: NotRequired[Literal["enable", "disable"]]  # Enable/disable virtual patching.
    logtraffic: NotRequired[Literal["enable", "disable"]]  # Enable/disable local-in traffic logging.
    comments: NotRequired[str]  # Comment.


class LocalInPolicy:
    """
    Configure user defined IPv4 local-in policies.
    
    Path: firewall/local_in_policy
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
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: list[dict[str, Any]] | None = ...,
        internet_service_src_group: list[dict[str, Any]] | None = ...,
        internet_service_src_custom: list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: LocalInPolicyPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        ha_mgmt_intf_only: Literal["enable", "disable"] | None = ...,
        intf: list[dict[str, Any]] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: list[dict[str, Any]] | None = ...,
        internet_service_src_group: list[dict[str, Any]] | None = ...,
        internet_service_src_custom: list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        service: list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        virtual_patch: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
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
        payload_dict: LocalInPolicyPayload | None = ...,
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
    "LocalInPolicy",
    "LocalInPolicyPayload",
]