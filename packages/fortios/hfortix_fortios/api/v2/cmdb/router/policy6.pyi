from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class Policy6Payload(TypedDict, total=False):
    """
    Type hints for router/policy6 payload fields.
    
    Configure IPv6 routing policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: output-device)

    **Usage:**
        payload: Policy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    seq_num: NotRequired[int]  # Sequence number(1-65535).
    input_device: NotRequired[list[dict[str, Any]]]  # Incoming interface name.
    input_device_negate: NotRequired[Literal["enable", "disable"]]  # Enable/disable negation of input device match.
    src: NotRequired[list[dict[str, Any]]]  # Source IPv6 prefix.
    srcaddr: NotRequired[list[dict[str, Any]]]  # Source address name.
    src_negate: NotRequired[Literal["enable", "disable"]]  # Enable/disable negating source address match.
    dst: NotRequired[list[dict[str, Any]]]  # Destination IPv6 prefix.
    dstaddr: NotRequired[list[dict[str, Any]]]  # Destination address name.
    dst_negate: NotRequired[Literal["enable", "disable"]]  # Enable/disable negating destination address match.
    action: NotRequired[Literal["deny", "permit"]]  # Action of the policy route.
    protocol: NotRequired[int]  # Protocol number (0 - 255).
    start_port: NotRequired[int]  # Start destination port number (1 - 65535).
    end_port: NotRequired[int]  # End destination port number (1 - 65535).
    start_source_port: NotRequired[int]  # Start source port number (1 - 65535).
    end_source_port: NotRequired[int]  # End source port number (1 - 65535).
    gateway: NotRequired[str]  # IPv6 address of the gateway.
    output_device: NotRequired[str]  # Outgoing interface name.
    tos: NotRequired[str]  # Type of service bit pattern.
    tos_mask: NotRequired[str]  # Type of service evaluated bits.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this policy route.
    comments: NotRequired[str]  # Optional comments.
    internet_service_id: NotRequired[list[dict[str, Any]]]  # Destination Internet Service ID.
    internet_service_custom: NotRequired[list[dict[str, Any]]]  # Custom Destination Internet Service name.
    internet_service_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Destination Internet Service name.
    users: NotRequired[list[dict[str, Any]]]  # List of users.
    groups: NotRequired[list[dict[str, Any]]]  # List of user groups.

# Nested classes for table field children

@final
class Policy6InputdeviceObject:
    """Typed object for input-device table items.
    
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
class Policy6SrcObject:
    """Typed object for src table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 address prefix.
    addr6: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class Policy6SrcaddrObject:
    """Typed object for srcaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address/group name.
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
class Policy6DstObject:
    """Typed object for dst table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 address prefix.
    addr6: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class Policy6DstaddrObject:
    """Typed object for dstaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address/group name.
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
class Policy6InternetserviceidObject:
    """Typed object for internet-service-id table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Destination Internet Service ID.
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class Policy6InternetservicecustomObject:
    """Typed object for internet-service-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Destination Internet Service name.
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
class Policy6InternetservicefortiguardObject:
    """Typed object for internet-service-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Destination Internet Service name.
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
class Policy6UsersObject:
    """Typed object for users table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User name.
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
class Policy6GroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name.
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
class Policy6Response(TypedDict):
    """
    Type hints for router/policy6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    seq_num: int
    input_device: list[dict[str, Any]]
    input_device_negate: Literal["enable", "disable"]
    src: list[dict[str, Any]]
    srcaddr: list[dict[str, Any]]
    src_negate: Literal["enable", "disable"]
    dst: list[dict[str, Any]]
    dstaddr: list[dict[str, Any]]
    dst_negate: Literal["enable", "disable"]
    action: Literal["deny", "permit"]
    protocol: int
    start_port: int
    end_port: int
    start_source_port: int
    end_source_port: int
    gateway: str
    output_device: str
    tos: str
    tos_mask: str
    status: Literal["enable", "disable"]
    comments: str
    internet_service_id: list[dict[str, Any]]
    internet_service_custom: list[dict[str, Any]]
    internet_service_fortiguard: list[dict[str, Any]]
    users: list[dict[str, Any]]
    groups: list[dict[str, Any]]


@final
class Policy6Object:
    """Typed FortiObject for router/policy6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Sequence number(1-65535).
    seq_num: int
    # Incoming interface name.
    input_device: list[Policy6InputdeviceObject]  # Table field - list of typed objects
    # Enable/disable negation of input device match.
    input_device_negate: Literal["enable", "disable"]
    # Source IPv6 prefix.
    src: list[Policy6SrcObject]  # Table field - list of typed objects
    # Source address name.
    srcaddr: list[Policy6SrcaddrObject]  # Table field - list of typed objects
    # Enable/disable negating source address match.
    src_negate: Literal["enable", "disable"]
    # Destination IPv6 prefix.
    dst: list[Policy6DstObject]  # Table field - list of typed objects
    # Destination address name.
    dstaddr: list[Policy6DstaddrObject]  # Table field - list of typed objects
    # Enable/disable negating destination address match.
    dst_negate: Literal["enable", "disable"]
    # Action of the policy route.
    action: Literal["deny", "permit"]
    # Protocol number (0 - 255).
    protocol: int
    # Start destination port number (1 - 65535).
    start_port: int
    # End destination port number (1 - 65535).
    end_port: int
    # Start source port number (1 - 65535).
    start_source_port: int
    # End source port number (1 - 65535).
    end_source_port: int
    # IPv6 address of the gateway.
    gateway: str
    # Outgoing interface name.
    output_device: str
    # Type of service bit pattern.
    tos: str
    # Type of service evaluated bits.
    tos_mask: str
    # Enable/disable this policy route.
    status: Literal["enable", "disable"]
    # Optional comments.
    comments: str
    # Destination Internet Service ID.
    internet_service_id: list[Policy6InternetserviceidObject]  # Table field - list of typed objects
    # Custom Destination Internet Service name.
    internet_service_custom: list[Policy6InternetservicecustomObject]  # Table field - list of typed objects
    # FortiGuard Destination Internet Service name.
    internet_service_fortiguard: list[Policy6InternetservicefortiguardObject]  # Table field - list of typed objects
    # List of users.
    users: list[Policy6UsersObject]  # Table field - list of typed objects
    # List of user groups.
    groups: list[Policy6GroupsObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Policy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Policy6:
    """
    Configure IPv6 routing policies.
    
    Path: router/policy6
    Category: cmdb
    Primary Key: seq-num
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        seq_num: int,
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
    ) -> Policy6Object: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        seq_num: int,
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
    ) -> Policy6Object: ...
    
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
    ) -> list[Policy6Object]: ...
    
    @overload
    def get(
        self,
        seq_num: int | None = ...,
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
        seq_num: int,
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
    ) -> Policy6Response: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        seq_num: int,
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
    ) -> Policy6Response: ...
    
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
    ) -> list[Policy6Response]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        seq_num: int | None = ...,
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
        seq_num: int | None = ...,
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
    ) -> Policy6Object | list[Policy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Policy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Policy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> Policy6Object: ...
    
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        seq_num: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: Policy6Payload | None = ...,
        seq_num: int | None = ...,
        input_device: str | list[str] | list[dict[str, Any]] | None = ...,
        input_device_negate: Literal["enable", "disable"] | None = ...,
        src: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        src_negate: Literal["enable", "disable"] | None = ...,
        dst: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dst_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["deny", "permit"] | None = ...,
        protocol: int | None = ...,
        start_port: int | None = ...,
        end_port: int | None = ...,
        start_source_port: int | None = ...,
        end_source_port: int | None = ...,
        gateway: str | None = ...,
        output_device: str | None = ...,
        tos: str | None = ...,
        tos_mask: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        internet_service_id: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Policy6",
    "Policy6Payload",
    "Policy6Object",
]