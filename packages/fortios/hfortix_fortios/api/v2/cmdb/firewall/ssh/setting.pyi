from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SettingPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssh/setting payload fields.
    
    SSH proxy settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.ssh.local-ca.LocalCaEndpoint` (via: caname, untrusted-caname)
        - :class:`~.firewall.ssh.local-key.LocalKeyEndpoint` (via: hostkey-dsa1024, hostkey-ecdsa256, hostkey-ecdsa384, +3 more)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    caname: NotRequired[str]  # CA certificate used by SSH Inspection.
    untrusted_caname: NotRequired[str]  # Untrusted CA certificate used by SSH Inspection.
    hostkey_rsa2048: NotRequired[str]  # RSA certificate used by SSH proxy.
    hostkey_dsa1024: NotRequired[str]  # DSA certificate used by SSH proxy.
    hostkey_ecdsa256: NotRequired[str]  # ECDSA nid256 certificate used by SSH proxy.
    hostkey_ecdsa384: NotRequired[str]  # ECDSA nid384 certificate used by SSH proxy.
    hostkey_ecdsa521: NotRequired[str]  # ECDSA nid384 certificate used by SSH proxy.
    hostkey_ed25519: NotRequired[str]  # ED25519 hostkey used by SSH proxy.
    host_trusted_checking: NotRequired[Literal["enable", "disable"]]  # Enable/disable host trusted checking.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for firewall/ssh/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    caname: str
    untrusted_caname: str
    hostkey_rsa2048: str
    hostkey_dsa1024: str
    hostkey_ecdsa256: str
    hostkey_ecdsa384: str
    hostkey_ecdsa521: str
    hostkey_ed25519: str
    host_trusted_checking: Literal["enable", "disable"]


@final
class SettingObject:
    """Typed FortiObject for firewall/ssh/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # CA certificate used by SSH Inspection.
    caname: str
    # Untrusted CA certificate used by SSH Inspection.
    untrusted_caname: str
    # RSA certificate used by SSH proxy.
    hostkey_rsa2048: str
    # DSA certificate used by SSH proxy.
    hostkey_dsa1024: str
    # ECDSA nid256 certificate used by SSH proxy.
    hostkey_ecdsa256: str
    # ECDSA nid384 certificate used by SSH proxy.
    hostkey_ecdsa384: str
    # ECDSA nid384 certificate used by SSH proxy.
    hostkey_ecdsa521: str
    # ED25519 hostkey used by SSH proxy.
    hostkey_ed25519: str
    # Enable/disable host trusted checking.
    host_trusted_checking: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Setting:
    """
    SSH proxy settings.
    
    Path: firewall/ssh/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingResponse: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingObject",
]