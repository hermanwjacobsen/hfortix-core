from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class GenevePayload(TypedDict, total=False):
    """
    Type hints for system/geneve payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: GenevePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # GENEVE device or interface name. Must be an unique interface
    interface: str  # Outgoing interface for GENEVE encapsulated traffic.
    vni: int  # GENEVE network ID.
    type: Literal["ethernet", "ppp"]  # GENEVE type.
    ip_version: Literal["ipv4-unicast", "ipv6-unicast"]  # IP version to use for the GENEVE interface and so for commun
    remote_ip: str  # IPv4 address of the GENEVE interface on the device at the re
    remote_ip6: str  # IPv6 IP address of the GENEVE interface on the device at the
    dstport: NotRequired[int]  # GENEVE destination port (1 - 65535, default = 6081).


class Geneve:
    """
    Configure GENEVE devices.
    
    Path: system/geneve
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
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: GenevePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        type: Literal["ethernet", "ppp"] | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast"] | None = ...,
        remote_ip: str | None = ...,
        remote_ip6: str | None = ...,
        dstport: int | None = ...,
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
        payload_dict: GenevePayload | None = ...,
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