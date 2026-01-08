from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
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


class Policy6Object(FortiObject[Policy6Payload]):
    """Typed FortiObject for router/policy6 with IDE autocomplete support."""
    
    # Sequence number(1-65535).
    seq_num: int
    # Incoming interface name.
    input_device: list[str]  # Auto-flattened from member_table
    # Enable/disable negation of input device match.
    input_device_negate: Literal["enable", "disable"]
    # Source IPv6 prefix.
    src: list[str]  # Auto-flattened from member_table
    # Source address name.
    srcaddr: list[str]  # Auto-flattened from member_table
    # Enable/disable negating source address match.
    src_negate: Literal["enable", "disable"]
    # Destination IPv6 prefix.
    dst: list[str]  # Auto-flattened from member_table
    # Destination address name.
    dstaddr: list[str]  # Auto-flattened from member_table
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
    internet_service_id: list[str]  # Auto-flattened from member_table
    # Custom Destination Internet Service name.
    internet_service_custom: list[str]  # Auto-flattened from member_table
    # FortiGuard Destination Internet Service name.
    internet_service_fortiguard: list[str]  # Auto-flattened from member_table
    # List of users.
    users: list[str]  # Auto-flattened from member_table
    # List of user groups.
    groups: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> Policy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Policy6:
    """
    Configure IPv6 routing policies.
    
    Path: router/policy6
    Category: cmdb
    Primary Key: seq-num
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> Policy6Object: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        seq_num: None = None,
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