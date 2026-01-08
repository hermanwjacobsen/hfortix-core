from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class ManualkeyInterfacePayload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec/manualkey_interface payload fields.
    
    Configure IPsec manual keys.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: ManualkeyInterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IPsec tunnel name.
    interface: str  # Name of the physical, aggregate, or VLAN interface.
    ip_version: NotRequired[Literal["4", "6"]]  # IP version to use for VPN interface.
    addr_type: NotRequired[Literal["4", "6"]]  # IP version to use for IP packets.
    remote_gw: str  # IPv4 address of the remote gateway's external interface.
    remote_gw6: str  # Remote IPv6 address of VPN gateway.
    local_gw: NotRequired[str]  # IPv4 address of the local gateway's external interface.
    local_gw6: NotRequired[str]  # Local IPv6 address of VPN gateway.
    auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"]  # Authentication algorithm. Must be the same for both ends of 
    enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"]  # Encryption algorithm. Must be the same for both ends of the 
    auth_key: str  # Hexadecimal authentication key in 16-digit (8-byte) segments
    enc_key: str  # Hexadecimal encryption key in 16-digit (8-byte) segments sep
    local_spi: str  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns betw
    remote_spi: str  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns bet
    npu_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable offloading IPsec VPN manual key sessions to N


class ManualkeyInterfaceObject(FortiObject[ManualkeyInterfacePayload]):
    """Typed FortiObject for vpn/ipsec/manualkey_interface with IDE autocomplete support."""
    
    # IPsec tunnel name.
    name: str
    # Name of the physical, aggregate, or VLAN interface.
    interface: str
    # IP version to use for VPN interface.
    ip_version: Literal["4", "6"]
    # IP version to use for IP packets.
    addr_type: Literal["4", "6"]
    # IPv4 address of the remote gateway's external interface.
    remote_gw: str
    # Remote IPv6 address of VPN gateway.
    remote_gw6: str
    # IPv4 address of the local gateway's external interface.
    local_gw: str
    # Local IPv6 address of VPN gateway.
    local_gw6: str
    # Authentication algorithm. Must be the same for both ends of the tunnel.
    auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"]
    # Encryption algorithm. Must be the same for both ends of the tunnel.
    enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"]
    # Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphen
    auth_key: str
    # Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens.
    enc_key: str
    # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic stre
    local_spi: str
    # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic str
    remote_spi: str
    # Enable/disable offloading IPsec VPN manual key sessions to NPUs.
    npu_offload: Literal["enable", "disable"]
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ManualkeyInterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ManualkeyInterface:
    """
    Configure IPsec manual keys.
    
    Path: vpn/ipsec/manualkey_interface
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
    ) -> ManualkeyInterfaceObject: ...
    
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
    ) -> list[ManualkeyInterfaceObject]: ...
    
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
    ) -> ManualkeyInterfaceObject | list[ManualkeyInterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ManualkeyInterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> ManualkeyInterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
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
    ) -> ManualkeyInterfaceObject: ...
    
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
        payload_dict: ManualkeyInterfacePayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        addr_type: Literal["4", "6"] | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        auth_alg: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        auth_key: str | None = ...,
        enc_key: str | None = ...,
        local_spi: str | None = ...,
        remote_spi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
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
    "ManualkeyInterface",
    "ManualkeyInterfacePayload",
    "ManualkeyInterfaceObject",
]