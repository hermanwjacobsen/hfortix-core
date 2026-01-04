from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PtpPayload(TypedDict, total=False):
    """
    Type hints for system/ptp payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: PtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable setting the FortiGate system time by synchron
    mode: NotRequired[Literal["multicast", "hybrid"]]  # Multicast transmission or hybrid transmission.
    delay_mechanism: NotRequired[Literal["E2E", "P2P"]]  # End to end delay detection or peer to peer delay detection.
    request_interval: NotRequired[int]  # The delay request value is the logarithmic mean interval in 
    interface: str  # PTP client will reply through this interface.
    server_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiGate PTP server mode. Your FortiGate bec
    server_interface: NotRequired[list[dict[str, Any]]]  # FortiGate interface(s) with PTP server mode enabled. Devices


class Ptp:
    """
    Configure system PTP information.
    
    Path: system/ptp
    Category: cmdb
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
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: list[dict[str, Any]] | None = ...,
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
        payload_dict: PtpPayload | None = ...,
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