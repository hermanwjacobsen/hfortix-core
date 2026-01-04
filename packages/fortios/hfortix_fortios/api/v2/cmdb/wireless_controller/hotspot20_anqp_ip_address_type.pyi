from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class Hotspot20AnqpIpAddressTypePayload(TypedDict, total=False):
    """
    Type hints for wireless-controller/hotspot20_anqp_ip_address_type payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: Hotspot20AnqpIpAddressTypePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IP type name.
    ipv6_address_type: NotRequired[Literal["not-available", "available", "not-known"]]  # IPv6 address type.
    ipv4_address_type: NotRequired[Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"]]  # IPv4 address type.


class Hotspot20AnqpIpAddressType:
    """
    Configure IP address type availability.
    
    Path: wireless-controller/hotspot20_anqp_ip_address_type
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
        payload_dict: Hotspot20AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: Hotspot20AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
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
        payload_dict: Hotspot20AnqpIpAddressTypePayload | None = ...,
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