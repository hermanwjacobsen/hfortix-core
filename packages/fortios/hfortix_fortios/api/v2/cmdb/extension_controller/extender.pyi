from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class ExtenderPayload(TypedDict, total=False):
    """
    Type hints for extension_controller/extender payload fields.
    
    Extender controller configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.extension-controller.extender-profile.ExtenderProfileEndpoint` (via: profile)

    **Usage:**
        payload: ExtenderPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # FortiExtender entry name.
    id: str  # FortiExtender serial number.
    authorized: Literal["discovered", "disable", "enable"]  # FortiExtender Administration (enable or disable).
    ext_name: NotRequired[str]  # FortiExtender name.
    description: NotRequired[str]  # Description.
    vdom: NotRequired[int]  # VDOM.
    device_id: NotRequired[int]  # Device ID.
    extension_type: Literal["wan-extension", "lan-extension"]  # Extension type for this FortiExtender.
    profile: NotRequired[str]  # FortiExtender profile configuration.
    override_allowaccess: NotRequired[Literal["enable", "disable"]]  # Enable to override the extender profile management access co
    allowaccess: NotRequired[Literal["ping", "telnet", "http", "https", "ssh", "snmp"]]  # Control management access to the managed extender. Separate
    override_login_password_change: NotRequired[Literal["enable", "disable"]]  # Enable to override the extender profile login-password
    login_password_change: NotRequired[Literal["yes", "default", "no"]]  # Change or reset the administrator password of a managed exte
    login_password: str  # Set the managed extender's administrator password.
    override_enforce_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable to override the extender profile enforce-bandwidth se
    enforce_bandwidth: NotRequired[Literal["enable", "disable"]]  # Enable/disable enforcement of bandwidth on LAN extension int
    bandwidth_limit: int  # FortiExtender LAN extension bandwidth limit (Mbps).
    wan_extension: NotRequired[str]  # FortiExtender wan extension configuration.
    firmware_provision_latest: NotRequired[Literal["disable", "once"]]  # Enable/disable one-time automatic provisioning of the latest

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class ExtenderResponse(TypedDict):
    """
    Type hints for extension_controller/extender API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    id: str
    authorized: Literal["discovered", "disable", "enable"]
    ext_name: str
    description: str
    vdom: int
    device_id: int
    extension_type: Literal["wan-extension", "lan-extension"]
    profile: str
    override_allowaccess: Literal["enable", "disable"]
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]
    override_login_password_change: Literal["enable", "disable"]
    login_password_change: Literal["yes", "default", "no"]
    login_password: str
    override_enforce_bandwidth: Literal["enable", "disable"]
    enforce_bandwidth: Literal["enable", "disable"]
    bandwidth_limit: int
    wan_extension: str
    firmware_provision_latest: Literal["disable", "once"]


@final
class ExtenderObject:
    """Typed FortiObject for extension_controller/extender with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # FortiExtender entry name.
    name: str
    # FortiExtender serial number.
    id: str
    # FortiExtender Administration (enable or disable).
    authorized: Literal["discovered", "disable", "enable"]
    # FortiExtender name.
    ext_name: str
    # Description.
    description: str
    # VDOM.
    vdom: int
    # Device ID.
    device_id: int
    # Extension type for this FortiExtender.
    extension_type: Literal["wan-extension", "lan-extension"]
    # FortiExtender profile configuration.
    profile: str
    # Enable to override the extender profile management access configuration.
    override_allowaccess: Literal["enable", "disable"]
    # Control management access to the managed extender. Separate entries with a space
    allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"]
    # Enable to override the extender profile login-password (administrator password)
    override_login_password_change: Literal["enable", "disable"]
    # Change or reset the administrator password of a managed extender
    login_password_change: Literal["yes", "default", "no"]
    # Set the managed extender's administrator password.
    login_password: str
    # Enable to override the extender profile enforce-bandwidth setting.
    override_enforce_bandwidth: Literal["enable", "disable"]
    # Enable/disable enforcement of bandwidth on LAN extension interface.
    enforce_bandwidth: Literal["enable", "disable"]
    # FortiExtender LAN extension bandwidth limit (Mbps).
    bandwidth_limit: int
    # FortiExtender wan extension configuration.
    wan_extension: str
    # Enable/disable one-time automatic provisioning of the latest firmware version.
    firmware_provision_latest: Literal["disable", "once"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ExtenderPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Extender:
    """
    Extender controller configuration.
    
    Path: extension_controller/extender
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
    ) -> ExtenderObject: ...
    
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
    ) -> ExtenderObject: ...
    
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
    ) -> list[ExtenderObject]: ...
    
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
    ) -> ExtenderResponse: ...
    
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
    ) -> ExtenderResponse: ...
    
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
    ) -> list[ExtenderResponse]: ...
    
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
    ) -> ExtenderObject | list[ExtenderObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ExtenderObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
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
    ) -> ExtenderObject: ...
    
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
        payload_dict: ExtenderPayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        ext_name: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        extension_type: Literal["wan-extension", "lan-extension"] | None = ...,
        profile: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["ping", "telnet", "http", "https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_password_change: Literal["enable", "disable"] | None = ...,
        login_password_change: Literal["yes", "default", "no"] | None = ...,
        login_password: str | None = ...,
        override_enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        enforce_bandwidth: Literal["enable", "disable"] | None = ...,
        bandwidth_limit: int | None = ...,
        wan_extension: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
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
    "Extender",
    "ExtenderPayload",
    "ExtenderObject",
]