from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class IpamPayload(TypedDict, total=False):
    """
    Type hints for system/ipam payload fields.
    
    Configure IP address management services.
    
    **Usage:**
        payload: IpamPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable IP address management services.
    server_type: NotRequired[Literal["fabric-root"]]  # Configure the type of IPAM server to use.
    automatic_conflict_resolution: NotRequired[Literal["disable", "enable"]]  # Enable/disable automatic conflict resolution.
    require_subnet_size_match: NotRequired[Literal["disable", "enable"]]  # Enable/disable reassignment of subnets to make requested and
    manage_lan_addresses: NotRequired[Literal["disable", "enable"]]  # Enable/disable default management of LAN interface addresses
    manage_lan_extension_addresses: NotRequired[Literal["disable", "enable"]]  # Enable/disable default management of FortiExtender LAN exten
    manage_ssid_addresses: NotRequired[Literal["disable", "enable"]]  # Enable/disable default management of FortiAP SSID addresses.
    pools: NotRequired[list[dict[str, Any]]]  # Configure IPAM pools.
    rules: NotRequired[list[dict[str, Any]]]  # Configure IPAM allocation rules.

# Nested classes for table field children

@final
class IpamPoolsObject:
    """Typed object for pools table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPAM pool name.
    name: str
    # Description.
    description: str
    # Configure IPAM pool subnet, Class A - Class B subnet.
    subnet: str
    # Configure pool exclude subnets.
    exclude: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class IpamRulesObject:
    """Typed object for rules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPAM rule name.
    name: str
    # Description.
    description: str
    # Configure serial number or wildcard of FortiGate to match.
    device: str
    # Configure name or wildcard of interface to match.
    interface: str
    # Configure role of interface to match.
    role: Literal["any", "lan", "wan", "dmz", "undefined"]
    # Configure name of IPAM pool to use.
    pool: str
    # Enable/disable DHCP server for matching IPAM interfaces.
    dhcp: Literal["enable", "disable"]
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class IpamResponse(TypedDict):
    """
    Type hints for system/ipam API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]
    server_type: Literal["fabric-root"]
    automatic_conflict_resolution: Literal["disable", "enable"]
    require_subnet_size_match: Literal["disable", "enable"]
    manage_lan_addresses: Literal["disable", "enable"]
    manage_lan_extension_addresses: Literal["disable", "enable"]
    manage_ssid_addresses: Literal["disable", "enable"]
    pools: list[dict[str, Any]]
    rules: list[dict[str, Any]]


@final
class IpamObject:
    """Typed FortiObject for system/ipam with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable IP address management services.
    status: Literal["enable", "disable"]
    # Configure the type of IPAM server to use.
    server_type: Literal["fabric-root"]
    # Enable/disable automatic conflict resolution.
    automatic_conflict_resolution: Literal["disable", "enable"]
    # Enable/disable reassignment of subnets to make requested and actual sizes match.
    require_subnet_size_match: Literal["disable", "enable"]
    # Enable/disable default management of LAN interface addresses.
    manage_lan_addresses: Literal["disable", "enable"]
    # Enable/disable default management of FortiExtender LAN extension interface addre
    manage_lan_extension_addresses: Literal["disable", "enable"]
    # Enable/disable default management of FortiAP SSID addresses.
    manage_ssid_addresses: Literal["disable", "enable"]
    # Configure IPAM pools.
    pools: list[IpamPoolsObject]  # Table field - list of typed objects
    # Configure IPAM allocation rules.
    rules: list[IpamRulesObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> IpamPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ipam:
    """
    Configure IP address management services.
    
    Path: system/ipam
    Category: cmdb
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
    ) -> IpamObject: ...
    
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
    ) -> IpamObject: ...
    
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
    ) -> IpamObject: ...
    
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
    ) -> IpamResponse: ...
    
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
    ) -> IpamResponse: ...
    
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
    ) -> IpamResponse: ...
    
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
    ) -> dict[str, Any]: ...
    
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
    ) -> IpamObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> IpamObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: IpamPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        server_type: Literal["fabric-root"] | None = ...,
        automatic_conflict_resolution: Literal["disable", "enable"] | None = ...,
        require_subnet_size_match: Literal["disable", "enable"] | None = ...,
        manage_lan_addresses: Literal["disable", "enable"] | None = ...,
        manage_lan_extension_addresses: Literal["disable", "enable"] | None = ...,
        manage_ssid_addresses: Literal["disable", "enable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        rules: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ipam",
    "IpamPayload",
    "IpamObject",
]