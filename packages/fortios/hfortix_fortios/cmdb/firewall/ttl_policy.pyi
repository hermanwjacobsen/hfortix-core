from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class TtlPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/ttl_policy payload fields.
    
    Configure TTL policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.schedule.group.GroupEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.onetime.OnetimeEndpoint` (via: schedule)
        - :class:`~.firewall.schedule.recurring.RecurringEndpoint` (via: schedule)
        - :class:`~.system.interface.InterfaceEndpoint` (via: srcintf)
        - :class:`~.system.sdwan.zone.ZoneEndpoint` (via: srcintf)
        - :class:`~.system.zone.ZoneEndpoint` (via: srcintf)

    **Usage:**
        payload: TtlPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID.
    status: NotRequired[Literal["enable", "disable"]]  # Enable/disable this TTL policy.
    action: NotRequired[Literal["accept", "deny"]]  # Action to be performed on traffic matching this policy (defa
    srcintf: str  # Source interface name from available interfaces.
    srcaddr: list[dict[str, Any]]  # Source address object(s) from available options. Separate mu
    service: list[dict[str, Any]]  # Service object(s) from available options. Separate multiple 
    schedule: str  # Schedule object from available options.
    ttl: str  # Value/range to match against the packet's Time to Live value


class TtlPolicyObject(FortiObject[TtlPolicyPayload]):
    """Typed FortiObject for firewall/ttl_policy with IDE autocomplete support."""
    
    # ID.
    id: int
    # Enable/disable this TTL policy.
    status: Literal["enable", "disable"]
    # Action to be performed on traffic matching this policy (default = deny).
    action: Literal["accept", "deny"]
    # Source interface name from available interfaces.
    srcintf: str
    # Source address object(s) from available options. Separate multiple names with a 
    srcaddr: list[str]  # Auto-flattened from member_table
    # Service object(s) from available options. Separate multiple names with a space.
    service: list[str]  # Auto-flattened from member_table
    # Schedule object from available options.
    schedule: str
    # Value/range to match against the packet's Time to Live value (format: ttl[ - ttl
    ttl: str
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> TtlPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TtlPolicy:
    """
    Configure TTL policies.
    
    Path: firewall/ttl_policy
    Category: cmdb
    Primary Key: id
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> TtlPolicyObject: ...
    
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
    ) -> list[TtlPolicyObject]: ...
    
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
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        id: None = None,
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
    ) -> TtlPolicyObject | list[TtlPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TtlPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> TtlPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
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
    ) -> TtlPolicyObject: ...
    
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
        payload_dict: TtlPolicyPayload | None = ...,
        id: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        srcintf: str | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        schedule: str | None = ...,
        ttl: str | None = ...,
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
    "TtlPolicy",
    "TtlPolicyPayload",
    "TtlPolicyObject",
]