from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# ============================================================================
# Nested TypedDicts for table field children (dict mode)
# These MUST be defined before the Payload class to use them as type hints
# ============================================================================

# ============================================================================
# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
# ============================================================================
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
    ipv6: bool  # ipv6
    srcintf: str  # srcintf
    sourceport: int  # sourceport
    sourceip: str  # sourceip
    protocol: str  # protocol
    dest: str  # dest
    destport: int  # destport
    icmptype: int  # icmptype
    icmpcode: int  # icmpcode
    policy_type: str  # policy_type
    auth_type: str  # auth_type
    user_group: str  # user_group
    server_name: str  # server_name
    user_db: str  # user_db
    group_attr_type: str  # group_attr_type

# ============================================================================
# Nested classes for table field children (object mode - for API responses)
# ============================================================================



# Response TypedDict for GET returns (all fields present in API response)
class PolicyLookupResponse(TypedDict):
    """
    Type hints for firewall/policy_lookup API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    dstaddr: str
    dst_cate: int
    match: bool
    matched_policy_type: str
    policy_action: str
    policy_id: int
    proxy_policy_id: int
    remote_groups: str
    sec_default_action: str
    srcaddr: str
    success: bool
    urlf_entry_id: int
    user_group: str
    webfilter_action: str
    webfilter_category: int
    webfilter_profile: str
    error_code: str


@final
class PolicyLookupObject:
    """Typed FortiObject for firewall/policy_lookup with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # dstaddr
    dstaddr: str
    # dst_cate
    dst_cate: int
    # match
    match: bool
    # matched_policy_type
    matched_policy_type: str
    # policy_action
    policy_action: str
    # policy_id
    policy_id: int
    # proxy_policy_id
    proxy_policy_id: int
    # remote_groups
    remote_groups: str
    # sec_default_action
    sec_default_action: str
    # srcaddr
    srcaddr: str
    # success
    success: bool
    # urlf_entry_id
    urlf_entry_id: int
    # user_group
    user_group: str
    # webfilter_action
    webfilter_action: str
    # webfilter_category
    webfilter_category: int
    # webfilter_profile
    webfilter_profile: str
    # error_code
    error_code: str
    
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
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
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
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
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
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
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
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
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
        sourceport: int | None = ...,
        sourceip: str | None = ...,
        protocol: str | None = ...,
        dest: str | None = ...,
        destport: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
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