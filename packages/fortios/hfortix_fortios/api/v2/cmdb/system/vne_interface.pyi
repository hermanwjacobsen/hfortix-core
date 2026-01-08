from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class VneInterfacePayload(TypedDict, total=False):
    """
    Type hints for system/vne_interface payload fields.
    
    Configure virtual network enabler tunnels.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: ssl-certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: VneInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # VNE tunnel name.
    interface: str  # Interface name.
    ssl_certificate: str  # Name of local certificate for SSL connections.
    bmr_hostname: str  # BMR hostname.
    auto_asic_offload: Literal["enable", "disable"]  # Enable/disable tunnel ASIC offloading.
    ipv4_address: NotRequired[str]  # Tunnel IPv4 address and netmask.
    br: str  # IPv6 address or FQDN of the border relay.
    update_url: str  # URL of provisioning server.
    mode: Literal["map-e", "fixed-ip", "ds-lite"]  # VNE tunnel mode.
    http_username: NotRequired[str]  # HTTP authentication user name.
    http_password: NotRequired[str]  # HTTP authentication password.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class VneInterfaceResponse(TypedDict):
    """
    Type hints for system/vne_interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    interface: str
    ssl_certificate: str
    bmr_hostname: str
    auto_asic_offload: Literal["enable", "disable"]
    ipv4_address: str
    br: str
    update_url: str
    mode: Literal["map-e", "fixed-ip", "ds-lite"]
    http_username: str
    http_password: str


@final
class VneInterfaceObject:
    """Typed FortiObject for system/vne_interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VNE tunnel name.
    name: str
    # Interface name.
    interface: str
    # Name of local certificate for SSL connections.
    ssl_certificate: str
    # BMR hostname.
    bmr_hostname: str
    # Enable/disable tunnel ASIC offloading.
    auto_asic_offload: Literal["enable", "disable"]
    # Tunnel IPv4 address and netmask.
    ipv4_address: str
    # IPv6 address or FQDN of the border relay.
    br: str
    # URL of provisioning server.
    update_url: str
    # VNE tunnel mode.
    mode: Literal["map-e", "fixed-ip", "ds-lite"]
    # HTTP authentication user name.
    http_username: str
    # HTTP authentication password.
    http_password: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> VneInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class VneInterface:
    """
    Configure virtual network enabler tunnels.
    
    Path: system/vne_interface
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
    ) -> VneInterfaceObject: ...
    
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
    ) -> VneInterfaceObject: ...
    
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
    ) -> list[VneInterfaceObject]: ...
    
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
    ) -> VneInterfaceResponse: ...
    
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
    ) -> VneInterfaceResponse: ...
    
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
    ) -> list[VneInterfaceResponse]: ...
    
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
    ) -> VneInterfaceObject | list[VneInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> VneInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
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
    ) -> VneInterfaceObject: ...
    
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
        payload_dict: VneInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ssl_certificate: str | None = ...,
        bmr_hostname: str | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        ipv4_address: str | None = ...,
        br: str | None = ...,
        update_url: str | None = ...,
        mode: Literal["map-e", "fixed-ip", "ds-lite"] | None = ...,
        http_username: str | None = ...,
        http_password: str | None = ...,
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
    "VneInterface",
    "VneInterfacePayload",
    "VneInterfaceObject",
]