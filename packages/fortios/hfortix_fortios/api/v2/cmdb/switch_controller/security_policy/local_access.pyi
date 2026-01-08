from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class LocalAccessPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/security_policy/local_access payload fields.
    
    Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units.
    
    **Usage:**
        payload: LocalAccessPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Policy name.
    mgmt_allowaccess: NotRequired[Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]]  # Allowed access on the switch management interface.
    internal_allowaccess: NotRequired[Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]]  # Allowed access on the switch internal interface.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class LocalAccessResponse(TypedDict):
    """
    Type hints for switch_controller/security_policy/local_access API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]
    internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]


@final
class LocalAccessObject:
    """Typed FortiObject for switch_controller/security_policy/local_access with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy name.
    name: str
    # Allowed access on the switch management interface.
    mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]
    # Allowed access on the switch internal interface.
    internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> LocalAccessPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class LocalAccess:
    """
    Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units.
    
    Path: switch_controller/security_policy/local_access
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
    ) -> LocalAccessObject: ...
    
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
    ) -> LocalAccessObject: ...
    
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
    ) -> list[LocalAccessObject]: ...
    
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
    ) -> LocalAccessResponse: ...
    
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
    ) -> LocalAccessResponse: ...
    
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
    ) -> list[LocalAccessResponse]: ...
    
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
    ) -> LocalAccessObject | list[LocalAccessObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalAccessObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> LocalAccessObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
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
    ) -> LocalAccessObject: ...
    
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
        payload_dict: LocalAccessPayload | None = ...,
        name: str | None = ...,
        mgmt_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
        internal_allowaccess: Literal["https", "ping", "ssh", "snmp", "http", "telnet", "radius-acct"] | list[str] | None = ...,
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
    "LocalAccess",
    "LocalAccessPayload",
    "LocalAccessObject",
]