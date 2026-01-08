from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class LwProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/lw_profile payload fields.
    
    Configure LoRaWAN profile.
    
    **Usage:**
        payload: LwProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # LoRaWAN profile name.
    comment: NotRequired[str]  # Comment.
    lw_protocol: NotRequired[Literal["basics-station", "packet-forwarder"]]  # Configure LoRaWAN protocol (default = basics-station)
    cups_server: NotRequired[str]  # CUPS (Configuration and Update Server) domain name or IP add
    cups_server_port: NotRequired[int]  # CUPS Port value of LoRaWAN device.
    cups_api_key: NotRequired[str]  # CUPS API key of LoRaWAN device.
    tc_server: NotRequired[str]  # TC (Traffic Controller) domain name or IP address of LoRaWAN
    tc_server_port: NotRequired[int]  # TC Port value of LoRaWAN device.
    tc_api_key: NotRequired[str]  # TC API key of LoRaWAN device.


class LwProfileObject(FortiObject[LwProfilePayload]):
    """Typed FortiObject for wireless_controller/lw_profile with IDE autocomplete support."""
    
    # LoRaWAN profile name.
    name: str
    # Comment.
    comment: str
    # Configure LoRaWAN protocol (default = basics-station)
    lw_protocol: Literal["basics-station", "packet-forwarder"]
    # CUPS (Configuration and Update Server) domain name or IP address of LoRaWAN devi
    cups_server: str
    # CUPS Port value of LoRaWAN device.
    cups_server_port: int
    # CUPS API key of LoRaWAN device.
    cups_api_key: str
    # TC (Traffic Controller) domain name or IP address of LoRaWAN device.
    tc_server: str
    # TC Port value of LoRaWAN device.
    tc_server_port: int
    # TC API key of LoRaWAN device.
    tc_api_key: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LwProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LwProfile:
    """
    Configure LoRaWAN profile.
    
    Path: wireless_controller/lw_profile
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
    ) -> LwProfileObject: ...
    
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
    ) -> list[LwProfileObject]: ...
    
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
    ) -> LwProfileObject | list[LwProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LwProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LwProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
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
    ) -> LwProfileObject: ...
    
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
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
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
    "LwProfile",
    "LwProfilePayload",
    "LwProfileObject",
]