from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class PppoeInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/pppoe_interface payload fields.
    
    Configure the PPPoE interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: device)

    **Usage:**
        payload: PppoeInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Name of the PPPoE interface.
    dial_on_demand: NotRequired[Literal["enable", "disable"]]  # Enable/disable dial on demand to dial the PPPoE interface wh
    ipv6: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv6 Control Protocol (IPv6CP).
    device: str  # Name for the physical interface.
    username: NotRequired[str]  # User name.
    password: NotRequired[str]  # Enter the password.
    pppoe_egress_cos: NotRequired[Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]]  # CoS in VLAN tag for outgoing PPPoE/PPP packets.
    auth_type: NotRequired[Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]]  # PPP authentication type to use.
    ipunnumbered: NotRequired[str]  # PPPoE unnumbered IP.
    pppoe_unnumbered_negotiate: NotRequired[Literal["enable", "disable"]]  # Enable/disable PPPoE unnumbered negotiation.
    idle_timeout: NotRequired[int]  # PPPoE auto disconnect after idle timeout (0-4294967295 sec).
    multilink: NotRequired[Literal["enable", "disable"]]  # Enable/disable PPP multilink support.
    mrru: NotRequired[int]  # PPP MRRU (296 - 65535, default = 1500).
    disc_retry_timeout: NotRequired[int]  # PPPoE discovery init timeout value in (0-4294967295 sec).
    padt_retry_timeout: NotRequired[int]  # PPPoE terminate timeout value in (0-4294967295 sec).
    service_name: NotRequired[str]  # PPPoE service name.
    ac_name: NotRequired[str]  # PPPoE AC name.
    lcp_echo_interval: NotRequired[int]  # Time in seconds between PPPoE Link Control Protocol (LCP) ec
    lcp_max_echo_fails: NotRequired[int]  # Maximum missed LCP echo messages before disconnect.


class PppoeInterfaceObject(FortiObject[PppoeInterfacePayload]):
    """Typed FortiObject for system/pppoe_interface with IDE autocomplete support."""
    
    # Name of the PPPoE interface.
    name: str
    # Enable/disable dial on demand to dial the PPPoE interface when packets are route
    dial_on_demand: Literal["enable", "disable"]
    # Enable/disable IPv6 Control Protocol (IPv6CP).
    ipv6: Literal["enable", "disable"]
    # Name for the physical interface.
    device: str
    # User name.
    username: str
    # Enter the password.
    password: str
    # CoS in VLAN tag for outgoing PPPoE/PPP packets.
    pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]
    # PPP authentication type to use.
    auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]
    # PPPoE unnumbered IP.
    ipunnumbered: str
    # Enable/disable PPPoE unnumbered negotiation.
    pppoe_unnumbered_negotiate: Literal["enable", "disable"]
    # PPPoE auto disconnect after idle timeout (0-4294967295 sec).
    idle_timeout: int
    # Enable/disable PPP multilink support.
    multilink: Literal["enable", "disable"]
    # PPP MRRU (296 - 65535, default = 1500).
    mrru: int
    # PPPoE discovery init timeout value in (0-4294967295 sec).
    disc_retry_timeout: int
    # PPPoE terminate timeout value in (0-4294967295 sec).
    padt_retry_timeout: int
    # PPPoE service name.
    service_name: str
    # PPPoE AC name.
    ac_name: str
    # Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.
    lcp_echo_interval: int
    # Maximum missed LCP echo messages before disconnect.
    lcp_max_echo_fails: int
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PppoeInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PppoeInterface:
    """
    Configure the PPPoE interfaces.
    
    Path: system/pppoe_interface
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> PppoeInterfaceObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[PppoeInterfaceObject]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        name: None = None,
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
    ) -> dict[str, Any]: ...
    
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
    ) -> PppoeInterfaceObject | list[PppoeInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PppoeInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PppoeInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
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
    ) -> PppoeInterfaceObject: ...
    
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
        payload_dict: PppoeInterfacePayload | None = ...,
        name: str | None = ...,
        dial_on_demand: Literal["enable", "disable"] | None = ...,
        ipv6: Literal["enable", "disable"] | None = ...,
        device: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        ipunnumbered: str | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
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
    "PppoeInterface",
    "PppoeInterfacePayload",
    "PppoeInterfaceObject",
]