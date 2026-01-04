from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class CentralSnatMapPayload(TypedDict, total=False):
    """
    Type hints for firewall/central_snat_map payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: CentralSnatMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the active status of this policy.
    type: NotRequired[Literal["ipv4", "ipv6"]]  # IPv4/IPv6 source NAT.
    srcintf: list[dict[str, Any]]  # Source interface name from available interfaces.
    dstintf: list[dict[str, Any]]  # Destination interface name from available interfaces.
    orig_addr: list[dict[str, Any]]  # IPv4 Original address.
    orig_addr6: list[dict[str, Any]]  # IPv6 Original address.
    dst_addr: list[dict[str, Any]]  # IPv4 Destination address.
    dst_addr6: list[dict[str, Any]]  # IPv6 Destination address.
    protocol: NotRequired[int]  # Integer value for the protocol type (0 - 255).
    orig_port: NotRequired[str]  # Original TCP port (1 to 65535, 0 means any port).
    nat: NotRequired[Literal["disable", "enable"]]  # Enable/disable source NAT.
    nat46: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46.
    nat64: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT64.
    nat_ippool: NotRequired[list[dict[str, Any]]]  # Name of the IP pools to be used to translate addresses from 
    nat_ippool6: NotRequired[list[dict[str, Any]]]  # IPv6 pools to be used for source NAT.
    port_preserve: NotRequired[Literal["enable", "disable"]]  # Enable/disable preservation of the original source port from
    port_random: NotRequired[Literal["enable", "disable"]]  # Enable/disable random source port selection for source NAT.
    nat_port: NotRequired[str]  # Translated port or port range (1 to 65535, 0 means any port)
    dst_port: NotRequired[str]  # Destination port or port range (1 to 65535, 0 means any port
    comments: NotRequired[str]  # Comment.


class CentralSnatMap:
    """
    Configure IPv4 and IPv6 central SNAT policies.
    
    Path: firewall/central_snat_map
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
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        orig_addr: list[dict[str, Any]] | None = ...,
        orig_addr6: list[dict[str, Any]] | None = ...,
        dst_addr: list[dict[str, Any]] | None = ...,
        dst_addr6: list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: list[dict[str, Any]] | None = ...,
        nat_ippool6: list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        orig_addr: list[dict[str, Any]] | None = ...,
        orig_addr6: list[dict[str, Any]] | None = ...,
        dst_addr: list[dict[str, Any]] | None = ...,
        dst_addr6: list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: list[dict[str, Any]] | None = ...,
        nat_ippool6: list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
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
        payload_dict: CentralSnatMapPayload | None = ...,
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
    "CentralSnatMap",
    "CentralSnatMapPayload",
]