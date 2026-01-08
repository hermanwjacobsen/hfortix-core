from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class CentralSnatMapPayload(TypedDict, total=False):
    """
    Type hints for firewall/central_snat_map payload fields.
    
    Configure IPv4 and IPv6 central SNAT policies.
    
    **Usage:**
        payload: CentralSnatMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID.
    uuid: NotRequired[str]  # Universally Unique Identifier
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable the active status of this policy.
    type: NotRequired[Literal["ipv4", "ipv6"]]  # IPv4/IPv6 source NAT.
    srcintf: list[dict[str, Any]]  # Source interface name from available interfaces.
    dstintf: list[dict[str, Any]]  # Destination interface name from available interfaces.
    orig_addr: list[dict[str, Any]]  # IPv4 Original address.
    orig_addr6: list[dict[str, Any]]  # IPv6 Original address.
    dst_addr: list[dict[str, Any]]  # IPv4 Destination address.
    dst_addr6: list[dict[str, Any]]  # IPv6 Destination address.
    protocol: NotRequired[int]  # Integer value for the protocol type (0 - 255).
    orig_port: NotRequired[str]  # Original TCP port (1 to 65535, 0 means any port).
    nat: NotRequired[Literal["disable", "enable"]]  # Enable/disable source NAT.
    nat46: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46.
    nat64: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT64.
    nat_ippool: NotRequired[list[dict[str, Any]]]  # Name of the IP pools to be used to translate addresses from
    nat_ippool6: NotRequired[list[dict[str, Any]]]  # IPv6 pools to be used for source NAT.
    port_preserve: NotRequired[Literal["enable", "disable"]]  # Enable/disable preservation of the original source port from
    port_random: NotRequired[Literal["enable", "disable"]]  # Enable/disable random source port selection for source NAT.
    nat_port: NotRequired[str]  # Translated port or port range (1 to 65535, 0 means any port)
    dst_port: NotRequired[str]  # Destination port or port range
    comments: NotRequired[str]  # Comment.

# Nested classes for table field children

@final
class CentralSnatMapSrcintfObject:
    """Typed object for srcintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapDstintfObject:
    """Typed object for dstintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapOrigaddrObject:
    """Typed object for orig-addr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapOrigaddr6Object:
    """Typed object for orig-addr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapDstaddrObject:
    """Typed object for dst-addr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapDstaddr6Object:
    """Typed object for dst-addr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapNatippoolObject:
    """Typed object for nat-ippool table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP pool name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class CentralSnatMapNatippool6Object:
    """Typed object for nat-ippool6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 pool name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class CentralSnatMapResponse(TypedDict):
    """
    Type hints for firewall/central_snat_map API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    policyid: int
    uuid: str
    status: Literal["enable", "disable"]
    type: Literal["ipv4", "ipv6"]
    srcintf: list[dict[str, Any]]
    dstintf: list[dict[str, Any]]
    orig_addr: list[dict[str, Any]]
    orig_addr6: list[dict[str, Any]]
    dst_addr: list[dict[str, Any]]
    dst_addr6: list[dict[str, Any]]
    protocol: int
    orig_port: str
    nat: Literal["disable", "enable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
    nat_ippool: list[dict[str, Any]]
    nat_ippool6: list[dict[str, Any]]
    port_preserve: Literal["enable", "disable"]
    port_random: Literal["enable", "disable"]
    nat_port: str
    dst_port: str
    comments: str


@final
class CentralSnatMapObject:
    """Typed FortiObject for firewall/central_snat_map with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Policy ID.
    policyid: int
    # Universally Unique Identifier
    uuid: str
    # Enable/disable the active status of this policy.
    status: Literal["enable", "disable"]
    # IPv4/IPv6 source NAT.
    type: Literal["ipv4", "ipv6"]
    # Source interface name from available interfaces.
    srcintf: list[CentralSnatMapSrcintfObject]  # Table field - list of typed objects
    # Destination interface name from available interfaces.
    dstintf: list[CentralSnatMapDstintfObject]  # Table field - list of typed objects
    # IPv4 Original address.
    orig_addr: list[CentralSnatMapOrigaddrObject]  # Table field - list of typed objects
    # IPv6 Original address.
    orig_addr6: list[CentralSnatMapOrigaddr6Object]  # Table field - list of typed objects
    # IPv4 Destination address.
    dst_addr: list[CentralSnatMapDstaddrObject]  # Table field - list of typed objects
    # IPv6 Destination address.
    dst_addr6: list[CentralSnatMapDstaddr6Object]  # Table field - list of typed objects
    # Integer value for the protocol type (0 - 255).
    protocol: int
    # Original TCP port (1 to 65535, 0 means any port).
    orig_port: str
    # Enable/disable source NAT.
    nat: Literal["disable", "enable"]
    # Enable/disable NAT46.
    nat46: Literal["enable", "disable"]
    # Enable/disable NAT64.
    nat64: Literal["enable", "disable"]
    # Name of the IP pools to be used to translate addresses from available IP Pools.
    nat_ippool: list[CentralSnatMapNatippoolObject]  # Table field - list of typed objects
    # IPv6 pools to be used for source NAT.
    nat_ippool6: list[CentralSnatMapNatippool6Object]  # Table field - list of typed objects
    # Enable/disable preservation of the original source port from source NAT if it ha
    port_preserve: Literal["enable", "disable"]
    # Enable/disable random source port selection for source NAT.
    port_random: Literal["enable", "disable"]
    # Translated port or port range (1 to 65535, 0 means any port).
    nat_port: str
    # Destination port or port range (1 to 65535, 0 means any port).
    dst_port: str
    # Comment.
    comments: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> CentralSnatMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class CentralSnatMap:
    """
    Configure IPv4 and IPv6 central SNAT policies.
    
    Path: firewall/central_snat_map
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    # Single object (mkey/name provided as keyword arg)
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
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
    ) -> list[CentralSnatMapObject]: ...
    
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
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapResponse: ...
    
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
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapResponse: ...
    
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
    ) -> list[CentralSnatMapResponse]: ...
    
    # Default overload for dict mode
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
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
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
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject | list[CentralSnatMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: CentralSnatMapPayload | None = ...,
        policyid: int | None = ...,
        uuid: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        type: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> CentralSnatMapObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
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
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        orig_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_addr6: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: int | None = ...,
        orig_port: str | None = ...,
        nat: Literal["disable", "enable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat_ippool: str | list[str] | list[dict[str, Any]] | None = ...,
        nat_ippool6: str | list[str] | list[dict[str, Any]] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        nat_port: str | None = ...,
        dst_port: str | None = ...,
        comments: str | None = ...,
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
    "CentralSnatMap",
    "CentralSnatMapPayload",
    "CentralSnatMapObject",
]