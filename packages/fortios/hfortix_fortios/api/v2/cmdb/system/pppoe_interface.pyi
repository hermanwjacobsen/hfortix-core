from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PppoeInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/pppoe_interface payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    disc_retry_timeout: NotRequired[int]  # PPPoE discovery init timeout value in (0-4294967295 sec).
    padt_retry_timeout: NotRequired[int]  # PPPoE terminate timeout value in (0-4294967295 sec).
    service_name: NotRequired[str]  # PPPoE service name.
    ac_name: NotRequired[str]  # PPPoE AC name.
    lcp_echo_interval: NotRequired[int]  # Time in seconds between PPPoE Link Control Protocol (LCP) ec
    lcp_max_echo_fails: NotRequired[int]  # Maximum missed LCP echo messages before disconnect.


class PppoeInterface:
    """
    Configure the PPPoE interfaces.
    
    Path: system/pppoe_interface
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
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
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
        payload_dict: PppoeInterfacePayload | None = ...,
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