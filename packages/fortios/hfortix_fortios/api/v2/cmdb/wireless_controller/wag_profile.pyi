from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class WagProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wag_profile payload fields.
    
    Configure wireless access gateway (WAG) profiles used for tunnels on AP.
    
    **Usage:**
        payload: WagProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Tunnel profile name.
    comment: NotRequired[str]  # Comment.
    tunnel_type: NotRequired[Literal["l2tpv3", "gre"]]  # Tunnel type.
    wag_ip: NotRequired[str]  # IP Address of the wireless access gateway.
    wag_port: NotRequired[int]  # UDP port of the wireless access gateway.
    ping_interval: NotRequired[int]  # Interval between two tunnel monitoring echo packets
    ping_number: NotRequired[int]  # Number of the tunnel monitoring echo packets
    return_packet_timeout: NotRequired[int]  # Window of time for the return packets from the tunnel's remo
    dhcp_ip_addr: NotRequired[str]  # IP address of the monitoring DHCP request packet sent throug

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class WagProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/wag_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    comment: str
    tunnel_type: Literal["l2tpv3", "gre"]
    wag_ip: str
    wag_port: int
    ping_interval: int
    ping_number: int
    return_packet_timeout: int
    dhcp_ip_addr: str


@final
class WagProfileObject:
    """Typed FortiObject for wireless_controller/wag_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tunnel profile name.
    name: str
    # Comment.
    comment: str
    # Tunnel type.
    tunnel_type: Literal["l2tpv3", "gre"]
    # IP Address of the wireless access gateway.
    wag_ip: str
    # UDP port of the wireless access gateway.
    wag_port: int
    # Interval between two tunnel monitoring echo packets (1 - 65535 sec, default = 1)
    ping_interval: int
    # Number of the tunnel monitoring echo packets (1 - 65535, default = 5).
    ping_number: int
    # Window of time for the return packets from the tunnel's remote end
    return_packet_timeout: int
    # IP address of the monitoring DHCP request packet sent through the tunnel.
    dhcp_ip_addr: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> WagProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class WagProfile:
    """
    Configure wireless access gateway (WAG) profiles used for tunnels on AP.
    
    Path: wireless_controller/wag_profile
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
    ) -> WagProfileObject: ...
    
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
    ) -> WagProfileObject: ...
    
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
    ) -> list[WagProfileObject]: ...
    
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
    ) -> WagProfileResponse: ...
    
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
    ) -> WagProfileResponse: ...
    
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
    ) -> list[WagProfileResponse]: ...
    
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
    ) -> WagProfileObject | list[WagProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WagProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> WagProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
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
    ) -> WagProfileObject: ...
    
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
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
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
    "WagProfile",
    "WagProfilePayload",
    "WagProfileObject",
]