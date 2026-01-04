from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpsecManualkeyInterfacePayload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec_manualkey_interface payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpsecManualkeyInterfacePayload = {
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


class IpsecManualkeyInterface:
    """
    Configure IPsec manual keys.
    
    Path: vpn/ipsec_manualkey_interface
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: IpsecManualkeyInterfacePayload | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpsecManualkeyInterfacePayload | None = ...,
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
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: IpsecManualkeyInterfacePayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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