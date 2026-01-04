from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpsecManualkeyPayload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec_manualkey payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpsecManualkeyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IPsec tunnel name.
    interface: str  # Name of the physical, aggregate, or VLAN interface.
    remote_gw: str  # Peer gateway.
    local_gw: NotRequired[str]  # Local gateway.
    authentication: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"]  # Authentication algorithm. Must be the same for both ends of 
    encryption: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"]  # Encryption algorithm. Must be the same for both ends of the 
    authkey: str  # Hexadecimal authentication key in 16-digit (8-byte) segments
    enckey: str  # Hexadecimal encryption key in 16-digit (8-byte) segments sep
    localspi: str  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns betw
    remotespi: str  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns bet
    npu_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable NPU offloading.


class IpsecManualkey:
    """
    Configure IPsec manual keys.
    
    Path: vpn/ipsec_manualkey
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
        payload_dict: IpsecManualkeyPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        authentication: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        encryption: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        authkey: str | None = ...,
        enckey: str | None = ...,
        localspi: str | None = ...,
        remotespi: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpsecManualkeyPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        authentication: Literal["null", "md5", "sha1", "sha256", "sha384", "sha512"] | None = ...,
        encryption: Literal["null", "des", "3des", "aes128", "aes192", "aes256", "aria128", "aria192", "aria256", "seed"] | None = ...,
        authkey: str | None = ...,
        enckey: str | None = ...,
        localspi: str | None = ...,
        remotespi: str | None = ...,
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
        payload_dict: IpsecManualkeyPayload | None = ...,
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