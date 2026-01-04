from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class MulticastPolicy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/multicast_policy6 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: MulticastPolicy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Policy ID (0 - 4294967294).
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this policy.
    name: NotRequired[str]  # Policy name.
    srcintf: str  # IPv6 source interface name.
    dstintf: str  # IPv6 destination interface name.
    srcaddr: list[dict[str, Any]]  # IPv6 source address name.
    dstaddr: list[dict[str, Any]]  # IPv6 destination address name.
    action: NotRequired[Literal["accept", "deny"]]  # Accept or deny traffic matching the policy.
    protocol: NotRequired[int]  # Integer value for the protocol type as defined by IANA (0 - 
    start_port: NotRequired[int]  # Integer value for starting TCP/UDP/SCTP destination port in 
    end_port: NotRequired[int]  # Integer value for ending TCP/UDP/SCTP destination port in ra
    utm_status: NotRequired[Literal["enable", "disable"]]  # Enable to add an IPS security profile to the policy.
    ips_sensor: NotRequired[str]  # Name of an existing IPS sensor.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Enable or disable logging. Log all sessions or security prof
    auto_asic_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable offloading policy traffic for hardware accele
    comments: NotRequired[str]  # Comment.


class MulticastPolicy6:
    """
    Configure IPv6 multicast NAT policies.
    
    Path: firewall/multicast_policy6
    Category: cmdb
    Primary Key: id
    """
    
    def get(
        self,
        id: int | None = ...,
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
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
        id: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        srcintf: str | None = ...,
        dstintf: str | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: MulticastPolicy6Payload | None = ...,
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