from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class IkePayload(TypedDict, total=False):
    """
    Type hints for system/ike payload fields.
    
    Configure IKE global attributes.
    
    **Usage:**
        payload: IkePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    embryonic_limit: NotRequired[int]  # Maximum number of IPsec tunnels to negotiate simultaneously.
    dh_multiprocess: NotRequired[Literal["enable", "disable"]]  # Enable/disable multiprocess Diffie-Hellman daemon for IKE.
    dh_worker_count: NotRequired[int]  # Number of Diffie-Hellman workers to start.
    dh_mode: NotRequired[Literal["software", "hardware"]]  # Use software (CPU) or hardware (CPX) to perform Diffie-Hellm
    dh_keypair_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable Diffie-Hellman key pair cache.
    dh_keypair_count: NotRequired[int]  # Number of key pairs to pre-generate for each Diffie-Hellman
    dh_keypair_throttle: NotRequired[Literal["enable", "disable"]]  # Enable/disable Diffie-Hellman key pair cache CPU throttling.
    dh_group_1: NotRequired[str]  # Diffie-Hellman group 1 (MODP-768).
    dh_group_2: NotRequired[str]  # Diffie-Hellman group 2 (MODP-1024).
    dh_group_5: NotRequired[str]  # Diffie-Hellman group 5 (MODP-1536).
    dh_group_14: NotRequired[str]  # Diffie-Hellman group 14 (MODP-2048).
    dh_group_15: NotRequired[str]  # Diffie-Hellman group 15 (MODP-3072).
    dh_group_16: NotRequired[str]  # Diffie-Hellman group 16 (MODP-4096).
    dh_group_17: NotRequired[str]  # Diffie-Hellman group 17 (MODP-6144).
    dh_group_18: NotRequired[str]  # Diffie-Hellman group 18 (MODP-8192).
    dh_group_19: NotRequired[str]  # Diffie-Hellman group 19 (EC-P256).
    dh_group_20: NotRequired[str]  # Diffie-Hellman group 20 (EC-P384).
    dh_group_21: NotRequired[str]  # Diffie-Hellman group 21 (EC-P521).
    dh_group_27: NotRequired[str]  # Diffie-Hellman group 27 (EC-P224BP).
    dh_group_28: NotRequired[str]  # Diffie-Hellman group 28 (EC-P256BP).
    dh_group_29: NotRequired[str]  # Diffie-Hellman group 29 (EC-P384BP).
    dh_group_30: NotRequired[str]  # Diffie-Hellman group 30 (EC-P512BP).
    dh_group_31: NotRequired[str]  # Diffie-Hellman group 31 (EC-X25519).
    dh_group_32: NotRequired[str]  # Diffie-Hellman group 32 (EC-X448).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class IkeResponse(TypedDict):
    """
    Type hints for system/ike API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    embryonic_limit: int
    dh_multiprocess: Literal["enable", "disable"]
    dh_worker_count: int
    dh_mode: Literal["software", "hardware"]
    dh_keypair_cache: Literal["enable", "disable"]
    dh_keypair_count: int
    dh_keypair_throttle: Literal["enable", "disable"]
    dh_group_1: str
    dh_group_2: str
    dh_group_5: str
    dh_group_14: str
    dh_group_15: str
    dh_group_16: str
    dh_group_17: str
    dh_group_18: str
    dh_group_19: str
    dh_group_20: str
    dh_group_21: str
    dh_group_27: str
    dh_group_28: str
    dh_group_29: str
    dh_group_30: str
    dh_group_31: str
    dh_group_32: str


@final
class IkeObject:
    """Typed FortiObject for system/ike with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Maximum number of IPsec tunnels to negotiate simultaneously.
    embryonic_limit: int
    # Enable/disable multiprocess Diffie-Hellman daemon for IKE.
    dh_multiprocess: Literal["enable", "disable"]
    # Number of Diffie-Hellman workers to start.
    dh_worker_count: int
    # Use software (CPU) or hardware (CPX) to perform Diffie-Hellman calculations.
    dh_mode: Literal["software", "hardware"]
    # Enable/disable Diffie-Hellman key pair cache.
    dh_keypair_cache: Literal["enable", "disable"]
    # Number of key pairs to pre-generate for each Diffie-Hellman group (per-worker).
    dh_keypair_count: int
    # Enable/disable Diffie-Hellman key pair cache CPU throttling.
    dh_keypair_throttle: Literal["enable", "disable"]
    # Diffie-Hellman group 1 (MODP-768).
    dh_group_1: str
    # Diffie-Hellman group 2 (MODP-1024).
    dh_group_2: str
    # Diffie-Hellman group 5 (MODP-1536).
    dh_group_5: str
    # Diffie-Hellman group 14 (MODP-2048).
    dh_group_14: str
    # Diffie-Hellman group 15 (MODP-3072).
    dh_group_15: str
    # Diffie-Hellman group 16 (MODP-4096).
    dh_group_16: str
    # Diffie-Hellman group 17 (MODP-6144).
    dh_group_17: str
    # Diffie-Hellman group 18 (MODP-8192).
    dh_group_18: str
    # Diffie-Hellman group 19 (EC-P256).
    dh_group_19: str
    # Diffie-Hellman group 20 (EC-P384).
    dh_group_20: str
    # Diffie-Hellman group 21 (EC-P521).
    dh_group_21: str
    # Diffie-Hellman group 27 (EC-P224BP).
    dh_group_27: str
    # Diffie-Hellman group 28 (EC-P256BP).
    dh_group_28: str
    # Diffie-Hellman group 29 (EC-P384BP).
    dh_group_29: str
    # Diffie-Hellman group 30 (EC-P512BP).
    dh_group_30: str
    # Diffie-Hellman group 31 (EC-X25519).
    dh_group_31: str
    # Diffie-Hellman group 32 (EC-X448).
    dh_group_32: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> IkePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Ike:
    """
    Configure IKE global attributes.
    
    Path: system/ike
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeObject: ...
    
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
    ) -> IkeResponse: ...
    
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
    ) -> IkeResponse: ...
    
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
    ) -> IkeResponse: ...
    
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
    ) -> IkeObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> IkeObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
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
        payload_dict: IkePayload | None = ...,
        embryonic_limit: int | None = ...,
        dh_multiprocess: Literal["enable", "disable"] | None = ...,
        dh_worker_count: int | None = ...,
        dh_mode: Literal["software", "hardware"] | None = ...,
        dh_keypair_cache: Literal["enable", "disable"] | None = ...,
        dh_keypair_count: int | None = ...,
        dh_keypair_throttle: Literal["enable", "disable"] | None = ...,
        dh_group_1: str | None = ...,
        dh_group_2: str | None = ...,
        dh_group_5: str | None = ...,
        dh_group_14: str | None = ...,
        dh_group_15: str | None = ...,
        dh_group_16: str | None = ...,
        dh_group_17: str | None = ...,
        dh_group_18: str | None = ...,
        dh_group_19: str | None = ...,
        dh_group_20: str | None = ...,
        dh_group_21: str | None = ...,
        dh_group_27: str | None = ...,
        dh_group_28: str | None = ...,
        dh_group_29: str | None = ...,
        dh_group_30: str | None = ...,
        dh_group_31: str | None = ...,
        dh_group_32: str | None = ...,
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
    "Ike",
    "IkePayload",
    "IkeObject",
]