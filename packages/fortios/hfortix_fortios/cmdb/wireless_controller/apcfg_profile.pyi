from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ApcfgProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/apcfg_profile payload fields.
    
    Configure AP local configuration profiles.
    
    **Usage:**
        payload: ApcfgProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # AP local configuration profile name.
    ap_family: NotRequired[Literal["fap", "fap-u", "fap-c"]]  # FortiAP family type (default = fap).
    comment: NotRequired[str]  # Comment.
    ac_type: NotRequired[Literal["default", "specify", "apcfg"]]  # Validation controller type (default = default).
    ac_timer: NotRequired[int]  # Maximum waiting time for the AP to join the validation contr
    ac_ip: NotRequired[str]  # IP address of the validation controller that AP must be able
    ac_port: NotRequired[int]  # Port of the validation controller that AP must be able to jo
    command_list: NotRequired[list[dict[str, Any]]]  # AP local configuration command list.


class ApcfgProfileObject(FortiObject[ApcfgProfilePayload]):
    """Typed FortiObject for wireless_controller/apcfg_profile with IDE autocomplete support."""
    
    # AP local configuration profile name.
    name: str
    # FortiAP family type (default = fap).
    ap_family: Literal["fap", "fap-u", "fap-c"]
    # Comment.
    comment: str
    # Validation controller type (default = default).
    ac_type: Literal["default", "specify", "apcfg"]
    # Maximum waiting time for the AP to join the validation controller after applying
    ac_timer: int
    # IP address of the validation controller that AP must be able to join after apply
    ac_ip: str
    # Port of the validation controller that AP must be able to join after applying AP
    ac_port: int
    # AP local configuration command list.
    command_list: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ApcfgProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ApcfgProfile:
    """
    Configure AP local configuration profiles.
    
    Path: wireless_controller/apcfg_profile
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> list[ApcfgProfileObject]: ...
    
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
    ) -> ApcfgProfileObject | list[ApcfgProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ApcfgProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ApcfgProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ApcfgProfileObject: ...
    
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
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ApcfgProfile",
    "ApcfgProfilePayload",
    "ApcfgProfileObject",
]