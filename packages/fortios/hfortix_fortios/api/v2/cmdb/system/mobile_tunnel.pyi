from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class MobileTunnelPayload(TypedDict, total=False):
    """
    Type hints for system/mobile_tunnel payload fields.
    
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: roaming-interface)

    **Usage:**
        payload: MobileTunnelPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # Tunnel name.
    status: NotRequired[Literal["disable", "enable"]]  # Enable/disable this mobile tunnel.
    roaming_interface: str  # Select the associated interface name from available options.
    home_agent: str  # IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).
    home_address: NotRequired[str]  # Home IP address (Format: xxx.xxx.xxx.xxx).
    renew_interval: int  # Time before lifetime expiration to send NMMO HA re-registrat
    lifetime: int  # NMMO HA registration request lifetime
    reg_interval: int  # NMMO HA registration interval (5 - 300, default = 5).
    reg_retry: int  # Maximum number of NMMO HA registration retries
    n_mhae_spi: int  # NEMO authentication SPI (default: 256).
    n_mhae_key_type: Literal["ascii", "base64"]  # NEMO authentication key type (ASCII or base64).
    n_mhae_key: NotRequired[str]  # NEMO authentication key.
    hash_algorithm: Literal["hmac-md5"]  # Hash Algorithm (Keyed MD5).
    tunnel_mode: Literal["gre"]  # NEMO tunnel mode (GRE tunnel).
    network: NotRequired[list[dict[str, Any]]]  # NEMO network configuration.

# Nested classes for table field children

@final
class MobileTunnelNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID.
    id: int
    # Select the associated interface name from available options.
    interface: str
    # Class IP and Netmask with correction
    prefix: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class MobileTunnelResponse(TypedDict):
    """
    Type hints for system/mobile_tunnel API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    status: Literal["disable", "enable"]
    roaming_interface: str
    home_agent: str
    home_address: str
    renew_interval: int
    lifetime: int
    reg_interval: int
    reg_retry: int
    n_mhae_spi: int
    n_mhae_key_type: Literal["ascii", "base64"]
    n_mhae_key: str
    hash_algorithm: Literal["hmac-md5"]
    tunnel_mode: Literal["gre"]
    network: list[dict[str, Any]]


@final
class MobileTunnelObject:
    """Typed FortiObject for system/mobile_tunnel with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tunnel name.
    name: str
    # Enable/disable this mobile tunnel.
    status: Literal["disable", "enable"]
    # Select the associated interface name from available options.
    roaming_interface: str
    # IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).
    home_agent: str
    # Home IP address (Format: xxx.xxx.xxx.xxx).
    home_address: str
    # Time before lifetime expiration to send NMMO HA re-registration
    renew_interval: int
    # NMMO HA registration request lifetime (180 - 65535 sec, default = 65535).
    lifetime: int
    # NMMO HA registration interval (5 - 300, default = 5).
    reg_interval: int
    # Maximum number of NMMO HA registration retries (1 to 30, default = 3).
    reg_retry: int
    # NEMO authentication SPI (default: 256).
    n_mhae_spi: int
    # NEMO authentication key type (ASCII or base64).
    n_mhae_key_type: Literal["ascii", "base64"]
    # NEMO authentication key.
    n_mhae_key: str
    # Hash Algorithm (Keyed MD5).
    hash_algorithm: Literal["hmac-md5"]
    # NEMO tunnel mode (GRE tunnel).
    tunnel_mode: Literal["gre"]
    # NEMO network configuration.
    network: list[MobileTunnelNetworkObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> MobileTunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class MobileTunnel:
    """
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    Path: system/mobile_tunnel
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> MobileTunnelObject: ...
    
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
    ) -> list[MobileTunnelObject]: ...
    
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
    ) -> MobileTunnelResponse: ...
    
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
    ) -> MobileTunnelResponse: ...
    
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
    ) -> list[MobileTunnelResponse]: ...
    
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
    ) -> MobileTunnelObject | list[MobileTunnelObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MobileTunnelObject: ...
    
    @overload
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> MobileTunnelObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> MobileTunnelObject: ...
    
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
        payload_dict: MobileTunnelPayload | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        roaming_interface: str | None = ...,
        home_agent: str | None = ...,
        home_address: str | None = ...,
        renew_interval: int | None = ...,
        lifetime: int | None = ...,
        reg_interval: int | None = ...,
        reg_retry: int | None = ...,
        n_mhae_spi: int | None = ...,
        n_mhae_key_type: Literal["ascii", "base64"] | None = ...,
        n_mhae_key: str | None = ...,
        hash_algorithm: Literal["hmac-md5"] | None = ...,
        tunnel_mode: Literal["gre"] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "MobileTunnel",
    "MobileTunnelPayload",
    "MobileTunnelObject",
]