from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class AnqpIpAddressTypePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/anqp_ip_address_type payload fields.
    
    Configure IP address type availability.
    
    **Usage:**
        payload: AnqpIpAddressTypePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IP type name.
    ipv6_address_type: NotRequired[Literal["not-available", "available", "not-known"]]  # IPv6 address type.
    ipv4_address_type: NotRequired[Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"]]  # IPv4 address type.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class AnqpIpAddressTypeResponse(TypedDict):
    """
    Type hints for wireless_controller/hotspot20/anqp_ip_address_type API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    ipv6_address_type: Literal["not-available", "available", "not-known"]
    ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"]


@final
class AnqpIpAddressTypeObject:
    """Typed FortiObject for wireless_controller/hotspot20/anqp_ip_address_type with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IP type name.
    name: str
    # IPv6 address type.
    ipv6_address_type: Literal["not-available", "available", "not-known"]
    # IPv4 address type.
    ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> AnqpIpAddressTypePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class AnqpIpAddressType:
    """
    Configure IP address type availability.
    
    Path: wireless_controller/hotspot20/anqp_ip_address_type
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[AnqpIpAddressTypeObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[AnqpIpAddressTypeResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeObject | list[AnqpIpAddressTypeObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> AnqpIpAddressTypeObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AnqpIpAddressTypePayload | None = ...,
        name: str | None = ...,
        ipv6_address_type: Literal["not-available", "available", "not-known"] | None = ...,
        ipv4_address_type: Literal["not-available", "public", "port-restricted", "single-NATed-private", "double-NATed-private", "port-restricted-and-single-NATed", "port-restricted-and-double-NATed", "not-known"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
    "AnqpIpAddressType",
    "AnqpIpAddressTypePayload",
    "AnqpIpAddressTypeObject",
]