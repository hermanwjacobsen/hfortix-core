from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

class CentralSnatMapSrcintfItem(TypedDict, total=False):
    """Type hints for srcintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapSrcintfItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Interface name. | MaxLen: 79


class CentralSnatMapDstintfItem(TypedDict, total=False):
    """Type hints for dstintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapDstintfItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Interface name. | MaxLen: 79


class CentralSnatMapOrigaddrItem(TypedDict, total=False):
    """Type hints for orig-addr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapOrigaddrItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Address name. | MaxLen: 79


class CentralSnatMapOrigaddr6Item(TypedDict, total=False):
    """Type hints for orig-addr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapOrigaddr6Item = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Address name. | MaxLen: 79


class CentralSnatMapDstaddrItem(TypedDict, total=False):
    """Type hints for dst-addr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapDstaddrItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Address name. | MaxLen: 79


class CentralSnatMapDstaddr6Item(TypedDict, total=False):
    """Type hints for dst-addr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapDstaddr6Item = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # Address name. | MaxLen: 79


class CentralSnatMapNatippoolItem(TypedDict, total=False):
    """Type hints for nat-ippool table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapNatippoolItem = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # IP pool name. | MaxLen: 79


class CentralSnatMapNatippool6Item(TypedDict, total=False):
    """Type hints for nat-ippool6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    Use this when building payloads for POST/PUT requests.
    
    **Available fields:**
        - name: str
    
    **Example:**
        entry: CentralSnatMapNatippool6Item = {
            "status": "enable",  # <- autocomplete shows all fields and validates Literal values
        }
    """
    
    name: str  # IPv6 pool name. | MaxLen: 79


# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CentralSnatMapPayload(TypedDict, total=False):
    """
    Type hints for firewall/central_snat_map payload fields.
    
    Configure IPv4 and IPv6 central SNAT policies.
    
    **Usage:**
        payload: CentralSnatMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: int  # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    status: Literal["enable", "disable"]  # Enable/disable the active status of this policy. | Default: enable
    type: Literal["ipv4", "ipv6"]  # IPv4/IPv6 source NAT. | Default: ipv4
    srcintf: list[CentralSnatMapSrcintfItem]  # Source interface name from available interfaces.
    dstintf: list[CentralSnatMapDstintfItem]  # Destination interface name from available interfac
    orig_addr: list[CentralSnatMapOrigaddrItem]  # IPv4 Original address.
    orig_addr6: list[CentralSnatMapOrigaddr6Item]  # IPv6 Original address.
    dst_addr: list[CentralSnatMapDstaddrItem]  # IPv4 Destination address.
    dst_addr6: list[CentralSnatMapDstaddr6Item]  # IPv6 Destination address.
    protocol: int  # Integer value for the protocol type (0 - 255). | Default: 0 | Min: 0 | Max: 255
    orig_port: str  # Original TCP port (1 to 65535, 0 means any port).
    nat: Literal["disable", "enable"]  # Enable/disable source NAT. | Default: enable
    nat46: Literal["enable", "disable"]  # Enable/disable NAT46. | Default: disable
    nat64: Literal["enable", "disable"]  # Enable/disable NAT64. | Default: disable
    nat_ippool: list[CentralSnatMapNatippoolItem]  # Name of the IP pools to be used to translate addre
    nat_ippool6: list[CentralSnatMapNatippool6Item]  # IPv6 pools to be used for source NAT.
    port_preserve: Literal["enable", "disable"]  # Enable/disable preservation of the original source | Default: enable
    port_random: Literal["enable", "disable"]  # Enable/disable random source port selection for so | Default: disable
    nat_port: str  # Translated port or port range
    dst_port: str  # Destination port or port range
    comments: str  # Comment. | MaxLen: 1023

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================

@final
class CentralSnatMapSrcintfObject:
    """Typed object for srcintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapDstintfObject:
    """Typed object for dstintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapOrigaddrObject:
    """Typed object for orig-addr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapOrigaddr6Object:
    """Typed object for orig-addr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapDstaddrObject:
    """Typed object for dst-addr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapDstaddr6Object:
    """Typed object for dst-addr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapNatippoolObject:
    """Typed object for nat-ippool table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP pool name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class CentralSnatMapNatippool6Object:
    """Typed object for nat-ippool6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 pool name. | MaxLen: 79
    name: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...




# Response TypedDict for GET returns (all fields present in API response)
class CentralSnatMapResponse(TypedDict):
    """
    Type hints for firewall/central_snat_map API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int  # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    status: Literal["enable", "disable"]  # Enable/disable the active status of this policy. | Default: enable
    type: Literal["ipv4", "ipv6"]  # IPv4/IPv6 source NAT. | Default: ipv4
    srcintf: list[CentralSnatMapSrcintfItem]  # Source interface name from available interfaces.
    dstintf: list[CentralSnatMapDstintfItem]  # Destination interface name from available interfac
    orig_addr: list[CentralSnatMapOrigaddrItem]  # IPv4 Original address.
    orig_addr6: list[CentralSnatMapOrigaddr6Item]  # IPv6 Original address.
    dst_addr: list[CentralSnatMapDstaddrItem]  # IPv4 Destination address.
    dst_addr6: list[CentralSnatMapDstaddr6Item]  # IPv6 Destination address.
    protocol: int  # Integer value for the protocol type (0 - 255). | Default: 0 | Min: 0 | Max: 255
    orig_port: str  # Original TCP port (1 to 65535, 0 means any port).
    nat: Literal["disable", "enable"]  # Enable/disable source NAT. | Default: enable
    nat46: Literal["enable", "disable"]  # Enable/disable NAT46. | Default: disable
    nat64: Literal["enable", "disable"]  # Enable/disable NAT64. | Default: disable
    nat_ippool: list[CentralSnatMapNatippoolItem]  # Name of the IP pools to be used to translate addre
    nat_ippool6: list[CentralSnatMapNatippool6Item]  # IPv6 pools to be used for source NAT.
    port_preserve: Literal["enable", "disable"]  # Enable/disable preservation of the original source | Default: enable
    port_random: Literal["enable", "disable"]  # Enable/disable random source port selection for so | Default: disable
    nat_port: str  # Translated port or port range
    dst_port: str  # Destination port or port range
    comments: str  # Comment. | MaxLen: 1023


@final
class CentralSnatMapObject:
    """Typed FortiObject for firewall/central_snat_map with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy ID. | Default: 0 | Min: 0 | Max: 4294967295
    policyid: int
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Enable/disable the active status of this policy. | Default: enable
    status: Literal["enable", "disable"]
    # IPv4/IPv6 source NAT. | Default: ipv4
    type: Literal["ipv4", "ipv6"]
    # Source interface name from available interfaces.
    srcintf: list[CentralSnatMapSrcintfObject]
    # Destination interface name from available interfaces.
    dstintf: list[CentralSnatMapDstintfObject]
    # IPv4 Original address.
    orig_addr: list[CentralSnatMapOrigaddrObject]
    # IPv6 Original address.
    orig_addr6: list[CentralSnatMapOrigaddr6Object]
    # IPv4 Destination address.
    dst_addr: list[CentralSnatMapDstaddrObject]
    # IPv6 Destination address.
    dst_addr6: list[CentralSnatMapDstaddr6Object]
    # Integer value for the protocol type (0 - 255). | Default: 0 | Min: 0 | Max: 255
    protocol: int
    # Original TCP port (1 to 65535, 0 means any port).
    orig_port: str
    # Enable/disable source NAT. | Default: enable
    nat: Literal["disable", "enable"]
    # Enable/disable NAT46. | Default: disable
    nat46: Literal["enable", "disable"]
    # Enable/disable NAT64. | Default: disable
    nat64: Literal["enable", "disable"]
    # Name of the IP pools to be used to translate addresses from
    nat_ippool: list[CentralSnatMapNatippoolObject]
    # IPv6 pools to be used for source NAT.
    nat_ippool6: list[CentralSnatMapNatippool6Object]
    # Enable/disable preservation of the original source port from | Default: enable
    port_preserve: Literal["enable", "disable"]
    # Enable/disable random source port selection for source NAT. | Default: disable
    port_random: Literal["enable", "disable"]
    # Translated port or port range (1 to 65535, 0 means any port)
    nat_port: str
    # Destination port or port range
    dst_port: str
    # Comment. | MaxLen: 1023
    comments: str
    
    # Common API response fields
    status: str
    http_status: int | None
    http_status_code: int | None
    http_method: str | None
    http_response_time: float | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> str:
        """Get pretty-printed JSON string."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CentralSnatMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class CentralSnatMap:
    """
    Configure IPv4 and IPv6 central SNAT policies.
    
    Path: firewall/central_snat_map
    Category: cmdb
    Primary Key: policyid
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        policyid: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[CentralSnatMapObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    # With no mkey -> returns list of objects
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
    ) -> FortiObjectList[CentralSnatMapObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
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
    ) -> FortiObjectList[CentralSnatMapObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
    def get(
        self,
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject | list[CentralSnatMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[CentralSnatMapSrcintfItem] | None = ...,
        dstintf: str | list[str] | list[CentralSnatMapDstintfItem] | None = ...,
        orig_addr: str | list[str] | list[CentralSnatMapOrigaddrItem] | None = ...,
        orig_addr6: str | list[str] | list[CentralSnatMapOrigaddr6Item] | None = ...,
        dst_addr: str | list[str] | list[CentralSnatMapDstaddrItem] | None = ...,
        dst_addr6: str | list[str] | list[CentralSnatMapDstaddr6Item] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[CentralSnatMapNatippoolItem] | None = ...,
        nat_ippool6: str | list[str] | list[CentralSnatMapNatippool6Item] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "CentralSnatMap",
    "CentralSnatMapPayload",
    "CentralSnatMapResponse",
    "CentralSnatMapObject",
]