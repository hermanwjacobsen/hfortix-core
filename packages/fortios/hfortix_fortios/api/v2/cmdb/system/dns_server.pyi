from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class DnsServerPayload(TypedDict, total=False):
    """
    Type hints for system/dns_server payload fields.
    
    Configure DNS servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: name)

    **Usage:**
        payload: DnsServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # DNS server name.
    mode: NotRequired[Literal["recursive", "non-recursive", "forward-only", "resolver"]]  # DNS server mode.
    dnsfilter_profile: NotRequired[str]  # DNS filter profile.
    doh: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS over HTTPS/443 (default = disable).
    doh3: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS over QUIC/HTTP3/443 (default = disable).
    doq: NotRequired[Literal["enable", "disable"]]  # Enable/disable DNS over QUIC/853 (default = disable).

# Nested classes for table field children


# Response TypedDict for GET returns (all fields present in API response)
class DnsServerResponse(TypedDict):
    """
    Type hints for system/dns_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    mode: Literal["recursive", "non-recursive", "forward-only", "resolver"]
    dnsfilter_profile: str
    doh: Literal["enable", "disable"]
    doh3: Literal["enable", "disable"]
    doq: Literal["enable", "disable"]


@final
class DnsServerObject:
    """Typed FortiObject for system/dns_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # DNS server name.
    name: str
    # DNS server mode.
    mode: Literal["recursive", "non-recursive", "forward-only", "resolver"]
    # DNS filter profile.
    dnsfilter_profile: str
    # Enable/disable DNS over HTTPS/443 (default = disable).
    doh: Literal["enable", "disable"]
    # Enable/disable DNS over QUIC/HTTP3/443 (default = disable).
    doh3: Literal["enable", "disable"]
    # Enable/disable DNS over QUIC/853 (default = disable).
    doq: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> DnsServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class DnsServer:
    """
    Configure DNS servers.
    
    Path: system/dns_server
    Category: cmdb
    Primary Key: name
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
    ) -> DnsServerObject: ...
    
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
    ) -> DnsServerObject: ...
    
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
    ) -> list[DnsServerObject]: ...
    
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
    ) -> DnsServerResponse: ...
    
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
    ) -> DnsServerResponse: ...
    
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
    ) -> list[DnsServerResponse]: ...
    
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
    ) -> DnsServerObject | list[DnsServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DnsServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> DnsServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
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
    ) -> DnsServerObject: ...
    
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
        payload_dict: DnsServerPayload | None = ...,
        name: str | None = ...,
        mode: Literal["recursive", "non-recursive", "forward-only", "resolver"] | None = ...,
        dnsfilter_profile: str | None = ...,
        doh: Literal["enable", "disable"] | None = ...,
        doh3: Literal["enable", "disable"] | None = ...,
        doq: Literal["enable", "disable"] | None = ...,
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
    "DnsServer",
    "DnsServerPayload",
    "DnsServerObject",
]