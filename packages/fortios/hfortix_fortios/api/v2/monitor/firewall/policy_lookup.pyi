from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PolicyLookupPayload(TypedDict, total=False):
    """
    Type hints for firewall/policy_lookup payload fields.
    
    Performs a policy lookup by creating a dummy packet and asking the kernel which policy would be hit.
    
    **Usage:**
        payload: PolicyLookupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ipv6: str  # ipv6
    srcintf: str  # srcintf
    sourceport: str  # sourceport
    sourceip: str  # sourceip
    protocol: str  # protocol
    dest: str  # dest
    destport: str  # destport
    icmptype: str  # icmptype
    icmpcode: str  # icmpcode
    policy_type: str  # policy_type
    auth_type: str  # auth_type
    user_group: str  # user_group
    server_name: str  # server_name
    user_db: str  # user_db
    group_attr_type: str  # group_attr_type

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class PolicyLookupResponse(TypedDict):
    """
    Type hints for firewall/policy_lookup API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ipv6: str
    srcintf: str
    sourceport: str
    sourceip: str
    protocol: str
    dest: str
    destport: str
    icmptype: str
    icmpcode: str
    policy_type: str
    auth_type: str
    user_group: str
    server_name: str
    user_db: str
    group_attr_type: str


@final
class PolicyLookupObject:
    """Typed FortiObject for firewall/policy_lookup with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ipv6
    ipv6: str
    # srcintf
    srcintf: str
    # sourceport
    sourceport: str
    # sourceip
    sourceip: str
    # protocol
    protocol: str
    # dest
    dest: str
    # destport
    destport: str
    # icmptype
    icmptype: str
    # icmpcode
    icmpcode: str
    # policy_type
    policy_type: str
    # auth_type
    auth_type: str
    # user_group
    user_group: str
    # server_name
    server_name: str
    # user_db
    user_db: str
    # group_attr_type
    group_attr_type: str
    
    # Common API response fields
    status: str
    http_status: int | None
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
    def to_dict(self) -> PolicyLookupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PolicyLookup:
    """
    Performs a policy lookup by creating a dummy packet and asking the kernel which policy would be hit.
    
    Path: firewall/policy_lookup
    Category: monitor
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # Service/Monitor endpoint with query parameters
    @overload
    def get(
        self,
        *,
        ipv6: str | None = ...,
        srcintf: str,
        sourceport: str | None = ...,
        sourceip: str,
        protocol: str,
        dest: str,
        destport: str | None = ...,
        icmptype: str | None = ...,
        icmpcode: str | None = ...,
        policy_type: Literal["*policy", "proxy"] | None = ...,
        auth_type: Literal["user", "group", "saml", "ldap"] | None = ...,
        user_group: str | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: Literal["*name", "id"] | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        vdom: str | bool | None = ...,
    ) -> PolicyLookupObject: ...
    
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
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
    ) -> PolicyLookupObject: ...
    
    # With mkey as keyword arg -> returns single object
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
    ) -> PolicyLookupObject: ...
    
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
    ) -> PolicyLookupObject: ...
    
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
    ) -> PolicyLookupObject: ...
    
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
    ) -> PolicyLookupObject: ...
    
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
    ) -> PolicyLookupObject: ...
    
    # Fallback overload for all other cases
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> PolicyLookupObject | dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: str | None = ...,
        srcintf: str | None = ...,
        sourceport: str | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: str | None = ...,
        icmptype: str | None = ...,
        icmpcode: str | None = ...,
        policy_type: str | None = ...,
        auth_type: str | None = ...,
        user_group: str | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PolicyLookupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: str | None = ...,
        srcintf: str | None = ...,
        sourceport: str | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: str | None = ...,
        icmptype: str | None = ...,
        icmpcode: str | None = ...,
        policy_type: str | None = ...,
        auth_type: str | None = ...,
        user_group: str | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: str | None = ...,
        srcintf: str | None = ...,
        sourceport: str | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: str | None = ...,
        icmptype: str | None = ...,
        icmpcode: str | None = ...,
        policy_type: str | None = ...,
        auth_type: str | None = ...,
        user_group: str | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: str | None = ...,
        srcintf: str | None = ...,
        sourceport: str | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: str | None = ...,
        icmptype: str | None = ...,
        icmpcode: str | None = ...,
        policy_type: str | None = ...,
        auth_type: str | None = ...,
        user_group: str | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PolicyLookupPayload | None = ...,
        ipv6: str | None = ...,
        srcintf: str | None = ...,
        sourceport: str | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: str | None = ...,
        icmptype: str | None = ...,
        icmpcode: str | None = ...,
        policy_type: str | None = ...,
        auth_type: str | None = ...,
        user_group: str | None = ...,
        server_name: str | None = ...,
        user_db: str | None = ...,
        group_attr_type: str | None = ...,
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
    "PolicyLookup",
    "PolicyLookupPayload",
    "PolicyLookupResponse",
    "PolicyLookupObject",
]