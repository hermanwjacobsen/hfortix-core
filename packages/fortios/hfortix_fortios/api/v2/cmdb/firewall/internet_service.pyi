from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class InternetServicePayload(TypedDict, total=False):
    """
    Type hints for firewall/internet_service payload fields.
    
    Show Internet Service application.
    
    **Usage:**
        payload: InternetServicePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: NotRequired[int]  # Internet Service ID.
    name: NotRequired[str]  # Internet Service name.
    icon_id: NotRequired[int]  # Icon ID of Internet Service.
    direction: NotRequired[Literal["src", "dst", "both"]]  # How this service may be used in a firewall policy
    database: NotRequired[Literal["isdb", "irdb"]]  # Database name this Internet Service belongs to.
    ip_range_number: NotRequired[int]  # Number of IPv4 ranges.
    extra_ip_range_number: NotRequired[int]  # Extra number of IPv4 ranges.
    ip_number: NotRequired[int]  # Total number of IPv4 addresses.
    ip6_range_number: NotRequired[int]  # Number of IPv6 ranges.
    extra_ip6_range_number: NotRequired[int]  # Extra number of IPv6 ranges.
    singularity: NotRequired[int]  # Singular level of the Internet Service.
    obsolete: NotRequired[int]  # Indicates whether the Internet Service can be used.

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class InternetServiceResponse(TypedDict):
    """
    Type hints for firewall/internet_service API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int
    name: str
    icon_id: int
    direction: Literal["src", "dst", "both"]
    database: Literal["isdb", "irdb"]
    ip_range_number: int
    extra_ip_range_number: int
    ip_number: int
    ip6_range_number: int
    extra_ip6_range_number: int
    singularity: int
    obsolete: int


@final
class InternetServiceObject:
    """Typed FortiObject for firewall/internet_service with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Internet Service ID.
    id: int
    # Internet Service name.
    name: str
    # Icon ID of Internet Service.
    icon_id: int
    # How this service may be used in a firewall policy (source, destination or both).
    direction: Literal["src", "dst", "both"]
    # Database name this Internet Service belongs to.
    database: Literal["isdb", "irdb"]
    # Number of IPv4 ranges.
    ip_range_number: int
    # Extra number of IPv4 ranges.
    extra_ip_range_number: int
    # Total number of IPv4 addresses.
    ip_number: int
    # Number of IPv6 ranges.
    ip6_range_number: int
    # Extra number of IPv6 ranges.
    extra_ip6_range_number: int
    # Singular level of the Internet Service.
    singularity: int
    # Indicates whether the Internet Service can be used.
    obsolete: int
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> InternetServicePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class InternetService:
    """
    Show Internet Service application.
    
    Path: firewall/internet_service
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        id: int,
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
    ) -> InternetServiceObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> InternetServiceObject: ...
    
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
    ) -> list[InternetServiceObject]: ...
    
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int,
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
    ) -> InternetServiceResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
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
    ) -> InternetServiceResponse: ...
    
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
    ) -> list[InternetServiceResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
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
    ) -> InternetServiceObject | list[InternetServiceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InternetServiceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InternetServiceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> InternetServiceObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InternetServicePayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        icon_id: int | None = ...,
        direction: Literal["src", "dst", "both"] | None = ...,
        database: Literal["isdb", "irdb"] | None = ...,
        ip_range_number: int | None = ...,
        extra_ip_range_number: int | None = ...,
        ip_number: int | None = ...,
        ip6_range_number: int | None = ...,
        extra_ip6_range_number: int | None = ...,
        singularity: int | None = ...,
        obsolete: int | None = ...,
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
    "InternetService",
    "InternetServicePayload",
    "InternetServiceObject",
]