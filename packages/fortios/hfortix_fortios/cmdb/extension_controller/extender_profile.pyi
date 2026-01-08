from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ExtenderProfilePayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender_profile payload fields.
    
    FortiExtender extender profile configuration.
    
    **Usage:**
        payload: ExtenderProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # FortiExtender profile name.
    id: NotRequired[int]  # ID.
    model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"]  # Model.
    extension: Literal["wan-extension", "lan-extension"]  # Extension option.
    allowaccess: NotRequired[Literal["ping", "telnet", "http", "https", "ssh", "snmp"]]  # Control management access to the managed extender. Separate 
    login_password_change: NotRequired[Literal["yes", "default", "no"]]  # Change or reset the administrator password of a managed exte
    login_password: str  # Set the managed extender's administrator password.
    enforce_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable/disable enforcement of bandwidth on LAN extension int
    bandwidth_limit: int  # FortiExtender LAN extension bandwidth limit (Mbps).
    cellular: str  # FortiExtender cellular configuration.
    wifi: NotRequired[str]  # FortiExtender Wi-Fi configuration.
    lan_extension: str  # FortiExtender LAN extension configuration.


class ExtenderProfileObject(FortiObject[ExtenderProfilePayload]):
    """Typed FortiObject for extension_controller/extender_profile with IDE autocomplete support."""
    
    # FortiExtender profile name.
    name: str
    # ID.
    id: int
    # Model.
    model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"]
    # Extension option.
    extension: Literal["wan-extension", "lan-extension"]
    # Control management access to the managed extender. Separate entries with a space
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]
    # Change or reset the administrator password of a managed extender (yes, default, 
    login_password_change: Literal["yes", "default", "no"]
    # Set the managed extender's administrator password.
    login_password: str
    # Enable/disable enforcement of bandwidth on LAN extension interface.
    enforce_bandwidth: Literal["enable", "disable"]
    # FortiExtender LAN extension bandwidth limit (Mbps).
    bandwidth_limit: int
    # FortiExtender cellular configuration.
    cellular: str
    # FortiExtender Wi-Fi configuration.
    wifi: str
    # FortiExtender LAN extension configuration.
    lan_extension: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExtenderProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ExtenderProfile:
    """
    FortiExtender extender profile configuration.
    
    Path: extension_controller/extender_profile
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
    ) -> ExtenderProfileObject: ...
    
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
    ) -> list[ExtenderProfileObject]: ...
    
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
    ) -> ExtenderProfileObject | list[ExtenderProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
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
    ) -> ExtenderProfileObject: ...
    
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
        payload_dict: ExtenderProfilePayload | None = ...,
        name: str | None = ...,
        id: int | None = ...,
        model: Literal["FX201E", "FX211E", "FX200F", "FXA11F", "FXE11F", "FXA21F", "FXE21F", "FXA22F", "FXE22F", "FX212F", "FX311F", "FX312F", "FX511F", "FXR51G", "FXN51G", "FXW51G", "FVG21F", "FVA21F", "FVG22F", "FVA22F", "FX04DA", "FG", "BS10FW", "BS20GW", "BS20GN", "FVG51G", "FXE11G", "FX211G"] | None = ...,
        extension: Literal["wan-extension", "lan-extension"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        cellular: str | None = ...,
        wifi: str | None = ...,
        lan_extension: str | None = ...,
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
    "ExtenderProfile",
    "ExtenderProfilePayload",
    "ExtenderProfileObject",
]