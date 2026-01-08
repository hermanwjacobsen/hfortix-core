from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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
    lifetime: int  # NMMO HA registration request lifetime (180 - 65535 sec, defa
    reg_interval: int  # NMMO HA registration interval (5 - 300, default = 5).
    reg_retry: int  # Maximum number of NMMO HA registration retries (1 to 30, def
    n_mhae_spi: int  # NEMO authentication SPI (default: 256).
    n_mhae_key_type: Literal["ascii", "base64"]  # NEMO authentication key type (ASCII or base64).
    n_mhae_key: NotRequired[str]  # NEMO authentication key.
    hash_algorithm: Literal["hmac-md5"]  # Hash Algorithm (Keyed MD5).
    tunnel_mode: Literal["gre"]  # NEMO tunnel mode (GRE tunnel).
    network: NotRequired[list[dict[str, Any]]]  # NEMO network configuration.


class MobileTunnelObject(FortiObject[MobileTunnelPayload]):
    """Typed FortiObject for system/mobile_tunnel with IDE autocomplete support."""
    
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
    # Time before lifetime expiration to send NMMO HA re-registration (5 - 60, default
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
    network: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> MobileTunnelPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class MobileTunnel:
    """
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    Path: system/mobile_tunnel
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
    ) -> MobileTunnelObject: ...
    
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